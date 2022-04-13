import random
from imaginarydate import ImaginaryTestingDate
from imaginarydate.nakarina import IronThroneDate, OsabunDate


# ----------------------------------------------------------------------------------------------------------------------
def print_hi(name):
    print(f"Testings for {name}")

    # testing...
    ImaginaryTestingDate().tests()
    IronThroneDate().tests()
    OsabunDate().tests()
    print()

    # correspondances
    # Le jour utilisé comme référence est le Fán 1/1/0 du Système du Trône de Fer.
    # Il correspond au Année 0 Mois 9 Jour 1 du Système d'Osabuñ.
    for i in range(5):
        if i == 0:
            prefix = "[Reference date] "
            d1 = IronThroneDate(day=1, month=1, year=0)
        else:
            prefix = ""
            d1 = IronThroneDate(day=random.randint(1, 32), month=random.randint(1, 23), year=random.randint(1, 1929))
        d2 = OsabunDate().from_datestamp(d1.datestamp, datestamp_offset=OsabunDate(month=9).datestamp)
        print(f"{prefix}date {d1} from {d1.name} <=> {d2} from {d2.name}")

    # date 08/13/4014 from Iron Throne <=> 10/07/19230 from Osabuñ
    d1 = IronThroneDate(day=8, month=13, year=4014)
    d2 = OsabunDate().from_date(d1, date_offset=OsabunDate(month=9))
    print(f"date {d1} from {d1.name} <=> {d2} from {d2.name}")


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    print_hi('ImaginaryDate')
