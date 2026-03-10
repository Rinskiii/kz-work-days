import numpy as np
import holidays
from datetime import datetime, date

kz_holidays: dict = holidays.KZ(years=[1991])

# for holiday in kz_holidays.items():
#     print(holiday)

kz_holidays_dates = [d.isoformat() for d in kz_holidays.keys()]

days = np.busday_count('2025-10-01', # Включительно
                        '2026-03-10', # Не включительно, поэтому +1 день
                        holidays=kz_holidays_dates)

print(days)