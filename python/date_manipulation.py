import datetime
import time

oneday = datetime.date(2023, 7, 14)
print(f"{oneday:%Y_%m_%d}")
print("{:%Y_%m_%d}".format(oneday))

print(time.strftime("%Y%m%d_%H%M%S%z", time.localtime()))  # it works in Odoo
print(time.strftime("%Y%m%d_%H%M%S%z"))