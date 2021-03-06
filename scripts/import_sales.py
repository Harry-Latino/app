"""Script to import sales"""


def run():
    # Python
    import csv
    from datetime import datetime

    # Models
    from apps.sales.models import Sale
    from apps.profiles.models import Profile
    from apps.products.models import Product
    from apps.authentication.models import User

    # Django
    from django.conf import settings
    from django.db.models.signals import post_save

    SCRIPTS_DIR = settings.BASE_DIR / "scripts"
    path = SCRIPTS_DIR / "transacciones.csv"
    with open(path) as read_file:
        csv_reader = csv.reader(read_file, delimiter=";")
        line = 0
        # ['numero', 'fecha', 'referencia', 'forum_id',', 'vendedor']
        for row in csv_reader:
            try:
                raw_date = row[1].split("-")
                date = datetime(int(raw_date[0]), int(raw_date[1]), int(raw_date[2]))
                product = Product.objects.get(reference=row[2])
                profile = Profile.objects.get(forum_user_id=row[3])
                if User.objects.filter(pk=row[4]).exists():
                    user = User.objects.get(pk=row[4])
                else:
                    user = User.objects.first()
                pk = int(row[0])
                # user = User.objects.get(pk=1)
                data = {
                    "date": date,
                    "product": product,
                    "profile": profile,
                    "buyer": user,
                }
                sale, created = Sale.objects.get_or_create(pk=pk, defaults=data)
                if not created:
                    sale.buyer = user
                    sale.save()
            except Exception as e:
                print(e)
                print(f"{row[4]}: {row[0]}")


run()
