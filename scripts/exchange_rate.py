import requests
from bs4 import BeautifulSoup
from .common import HEADERS

def get_usd_to_twd():
    url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
    try:
        res = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(res.text, "html.parser")
        rows = soup.select("table.table tbody tr")
        for row in rows:
            currency = row.select_one("td.currency div.visible-phone")
            if currency and "美金" in currency.text:
                cash_buy = row.select_one("td[data-table='本行現金買入']").text.strip()
                return f"💱 美元兌台幣現金買入價：{cash_buy}"
        return "💱 無法取得美元匯率。"
    except Exception as e:
        return f"💱 錯誤：{e}"
