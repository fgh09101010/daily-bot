import requests
from bs4 import BeautifulSoup
from .common import HEADERS

def get_github_trending():
    url = "https://github.com/trending"
    try:
        res = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(res.text, "html.parser")
        repos = soup.select("article.Box-row")[:3]
        trending = []
        for repo in repos:
            name = repo.h2.a.get_text(strip=True).replace("\n", "").replace(" ", "")
            desc_tag = repo.p
            desc = desc_tag.get_text(strip=True) if desc_tag else "無描述"
            trending.append(f"- [{name}](https://github.com/{name}): {desc}")
        return "🔥 GitHub Trending 今日熱門：\n" + "\n".join(trending)
    except Exception as e:
        return f"🔥 錯誤：{e}"
