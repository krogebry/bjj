#!/usr/bin/env python3

import time
from datetime import date

pans_2023 = date(2023, 3, 22)
pans_2024 = date(2024, 3, 22)

today = date.today()

delta = (pans_2024 - today)

months = int(delta.days / 30) - 1

days = months * 30

print(f"Num months: {months} / {days} / {delta.days}")


