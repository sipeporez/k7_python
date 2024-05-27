from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

path = Path("edu_0527/연습문제/data/sitka.csv")
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)

# Extract dates and rainfall.
dates, highs = [], []
for row in reader:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    high = float(row[3])
    dates.append(current_date)
    highs.append(high)

# Plot the rainfall.
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(dates, highs, color="red")
# ax.scatter(dates, highs, color="red")

# Format plot.
ax.set_title("Sitka Daily Railfall", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Railfall", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
