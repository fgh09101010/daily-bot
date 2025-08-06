import requests
from scripts.api import call_chatgpt

def get_real_weather(location="Taipei"):
    try:
        url = f"https://wttr.in/{location}?format=Weather:+%C,+Temp:+%t,+Wind:+%w,+Humidity:+%h"
        response = requests.get(url)
        if response.status_code == 200:
            return f"📍 {location} 天氣：{response.text.strip()}"
        else:
            return "❌ 無法取得天氣資料"
    except Exception as e:
        return f"❌ 錯誤：{e}"
    

def get_weather_and_quote():
    weather = get_real_weather()
    quote = call_chatgpt("你是天氣專家。", f"以下是天氣\n{weather}")
    return f"{weather}\n> 「{quote}」"
