from django.core.management.base import BaseCommand
from kruzky.models import Veduci, Kruzok


class Command(BaseCommand):
    help = "Import dat zo suboru"

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        veduci_dict = {}

        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()

                # VEDUCI
                if line.startswith("Veduci:"):
                    data = line.replace("Veduci:", "").strip()
                    meno, email = [x.strip() for x in data.split(",")]

                    veduci, created = Veduci.objects.get_or_create(
                        email=email,
                        defaults={"meno": meno}
                    )

                    veduci_dict[meno] = veduci

                # KRUZOK
                elif line.startswith("Kruzok:"):
                    data = line.replace("Kruzok:", "").strip()
                    nazov, den, miestnost, meno_veduceho = [x.strip() for x in data.split(",")]

                    veduci = veduci_dict.get(meno_veduceho)

                    if veduci:
                        Kruzok.objects.create(
                            nazov=nazov,
                            den=den,
                            miestnost=miestnost,
                            veduci=veduci
                        )
                    else:
                        self.stdout.write(self.style.WARNING(
                            f"Vedúci {meno_veduceho} neexistuje!"
                        ))

        self.stdout.write(self.style.SUCCESS("Import hotový!"))