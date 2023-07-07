import streamlit as st
import pandas as pd
import json
import requests
st.title('【提案デモ】API経由で送料取得のPythonプログラム')

def get_tenki(i):
    API_TOKEN = "9b309f634e720af3da701050cdf006d6"

    if __name__ == "__main__":
        # i=1
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/forecast",
            params={
                ## 緯度・軽度を指定する場合
                "lat": str(data["緯度"][i]),
                "lon": str(data["経度"][i]),
                "appid": API_TOKEN,
                "units": "metric",
                "lang": "ja",
            },
        )
        json_data =json.loads(response.text)
        df2 = pd.json_normalize(json_data)
        df1 = pd.json_normalize(json_data,record_path='list')
        filtered_df = df1[df1['dt_txt'].str.contains('12:00:00|18:00:00')]
        df5 = pd.DataFrame({
            '店舗名': df2['city.name'],
            '緯度': df2['city.coord.lat'],
            '経度': df2['city.coord.lon'],
            '昼時間帯の天気': filtered_df.iloc[0]['weather'][0]['description'],
            '昼時間帯の降水量': filtered_df.iloc[0]['rain.3h'],
            '夜時間帯の天気': filtered_df.iloc[1]['weather'][0]['description'],
            '夜時間帯の降水量': filtered_df.iloc[1]['rain.3h']
        })
        st.write(df5)
st.write('登録済みpandasのデータフレーム形式データ')
data = {
    "店舗名": ["札幌", "仙台", "東京", "大阪"],
    "緯度": [43.0621, 38.2688, 35.6895, 34.6937],
    "経度": [141.3544, 140.8721, 139.6917, 135.5023]
}
df = pd.DataFrame(data)
df
st.write('ボタンを押すと今日の天気予報をAPI（openwheathermap）で取得し、データフレーム形式に変換します')
button1 = st.button('札幌店')
button2 = st.button('仙台店')
button3 = st.button('東京店')
button4 = st.button('大阪店')

if button1:
    i=0
    get_tenki(i)
elif button2:
    i=1
    get_tenki(i)
elif button3:
    i=2
    get_tenki(i)
elif button4:
    i=3
    get_tenki(i)

