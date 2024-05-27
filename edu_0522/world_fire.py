from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt
import plotly.express as px

path = Path("eq_data/MODIS_C6_1_Russia_Asia_24h.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
print(header_row)
# latitude,longitude,brightness,scan,track,acq_date,acq_time,satellite,confidence,version,bright_t31,frp,daynight
# Extract dates, and high and low temperatures.
mags, lons, lats, fire_title, titles = [], [], [], [], []
for row in reader:
    current_date = datetime.strptime(row[5], "%Y-%m-%d")
    try:
        lat = float(row[0])
        lon = float(row[1])
        mag = float(row[2])
        fire_title = str(row[5])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        lats.append(lat)
        lons.append(lon)
        mags.append(mag)
        titles.append(fire_title)

title = "MODIS_C6_1_Russia_Asia_24h"
fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    size=mags,
    title=title,
    color=mags,
    color_continuous_scale="Viridis",
    labels={"color": "Magnitude"},
    projection="natural earth",
    hover_name=titles,
)
fig.show()

plt.show()
