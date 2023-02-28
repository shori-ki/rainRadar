# -*- coding: utf-8 -*-

import folium

# 地図生成
folium_map = folium.Map(location=[35.010341, 135.768714], zoom_start=10)

#降雨レイヤ追加
folium.TileLayer(opacity=1,overlay=True,tiles="https://tile.openweathermap.org/map/precipitation_new/{z}/{x}/{y}.png?appid=hogehoge",attr="OpenWethermap").add_to(folium_map)
#雲レイヤ追加
folium.TileLayer(opacity=1,overlay=True,tiles="https://tile.openweathermap.org/map/clouds_new/{z}/{x}/{y}.png?appid=hogehoge",attr="OpenWethermap").add_to(folium_map)
# 地図保存
folium_map.save("aa.html")

