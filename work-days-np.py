import numpy as np

from holidays_kz import holidays_91_26

holidays_91_26: list = [item for sublist in holidays_91_26 for item in sublist]


days = np.busday_count('2025-10-01', # Включительно
                        '2026-03-10', # Не включительно, поэтому +1 день
                        holidays=holidays_91_26)

print(days)

