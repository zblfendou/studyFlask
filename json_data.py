import json
from datetime import datetime
from pathlib import Path

import pandas as pd
import plotly.express as px

path = Path('data/earthquakes1970-2014.json')
contents = path.read_text('utf-8')

all_eq_data = json.loads(contents)
# # 将文件内容转化成更加易读的版本
# p = Path('data/earthquakes1970-2014-formated.json')
# dumps = json.dumps(all_data, indent=4)
# p.write_text(dumps)
# 查看数据集中所有的地震
all_eq_dicts = all_eq_data['features']
mags, titles, longs, lats, dates = [], [], [], [],[]
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['Magnitude']
    title = eq_dict['properties']['Source']
    long = eq_dict['properties']['Longitude']
    lat = eq_dict['properties']['Latitude']
    date = eq_dict['properties']['DateTime']
    mags.append(mag)
    titles.append(title)
    longs.append(long)
    lats.append(lat)
    dates.append(datetime.strptime(str(date)[0:len(date)-3],'%Y/%m/%d %H:%M:%S'))

data = pd.DataFrame(data=zip(mags, titles, longs, lats,dates), columns=['震级', '位置', '经度', '纬度','日期'])

fig = px.scatter(data, x='经度', y='纬度', labels={'x': '经度', 'y': '维度'}, size='震级',
                 range_x=[-200, 200], range_y=[-90, 90], title='全球地震数据', hover_name=titles,
                 size_max=10,color='震级', color_continuous_scale='plasma',hover_data=['日期'])

fig.show()
