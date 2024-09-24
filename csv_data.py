import csv
from datetime import datetime
from pathlib import Path
import matplotlib.pyplot as plt

path = Path('data/sitka_weather_07-2018_simple.csv')
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)

# 从文件中获取日期和最高气温/最低气温
highs, lows, dates = [], [], []
for row in reader:
    high = int(row[5])
    highs.append(high)
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    dates.append(current_date)
    low = int(row[6])
    lows.append(low)
# 根据最高温度绘制图形
fig, ax = plt.subplots(layout='constrained')
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图形的格式
ax.set_title("Daily high and low temperatures, July 2018", fontsize=12)
ax.set_xlabel('', fontsize=15)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=10)

plt.show()
