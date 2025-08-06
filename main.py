from datetime import datetime
from scripts.weather_and_quote import get_weather_and_quote
from scripts.life_tip import get_life_tip
from scripts.fun_fact import get_fun_fact


today = datetime.now().strftime("%Y-%m-%d")

with open("README.md", "w", encoding="utf-8") as f:
    f.write(f"# 🌅 Daily Digest for {today}\n\n")
    f.write("## 🌤️ 今日天氣小語\n")
    f.write(get_weather_and_quote() + "\n\n")
    f.write("## 💬 人生建議\n")
    f.write(get_life_tip() + "\n\n")
    f.write("## 🧠 冷知識一則\n")
    f.write(get_fun_fact() + "\n")

print(f"README.md 已更新，包含 {today} 的每日摘要。")

