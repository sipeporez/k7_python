from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

path = Path("edu_0527/연습문제/data/sit,dv,sf.csv")
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)

# Extract dates and rainfall.
temp_list = [
    "USW00023272",
    "USC00503605",
    "USC00505519",
    "USR0000CHNM",
    "USC00042319",
    "USW00053139",
    "USW00025379",
    "USW00025333",
]
dates, highs, lows = [],[],[]
for i in range(len(temp_list)):
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            high = float(row[4])
            low = float(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
        if temp_list[i] != row[0]:
            break

# Plot the rainfall.
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(dates, highs, color="red", alpha=0.5)
ax.plot(dates, lows, color="blue", alpha=0.5)
# ax.scatter(dates, highs, color="red")

# Format plot.
ax.set_title("Sitka Daily Railfall", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Railfall", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
