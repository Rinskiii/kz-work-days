from datetime import date, timedelta

start = date(2025, 12, 15)
end = date(2026, 3, 10)

holidays: dict = {
    date(2025, 12, 16),
    date(2025, 12, 17),
    date(2026, 1, 1),
    date(2026, 1, 2),
    date(2026, 1, 7),
    date(2026, 3, 8),
}

work_days: int = 0
current: date = start

while current <= end:
    if current.weekday() < 5 and current not in holidays:
        work_days += 1
    current += timedelta(days=1)

print(work_days)