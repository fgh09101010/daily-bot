import dotenv
import os
import requests
# 嘗試讀取本地 .env 檔案（本地開發用）
dotenv.load_dotenv()

# 優先使用環境變數（GitHub Actions 設定 Secrets）
API_KEY = os.getenv("API_KEY")

def call_chatgpt(system,text):

    # ✅ 使用你申請到的 URL 和 API KEY
    url = 'https://free.v36.cm/v1/chat/completions'
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json',
    }

    # 要送出的訊息內容
    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": text}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        content = result['choices'][0]['message']['content']
        return content
    
    except requests.exceptions.RequestException as e:
        return f"{str(e)}"
    

