import requests
import datetime
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = "709769371"
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def get_market_summary():
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)

    return f"""📈 [{yesterday} 마켓 요약]

🇰🇷 코스피: 2,640.45 (+0.7%)
🇺🇸 나스닥: 15,601.45 (-0.4%)
🪙 비트코인: $63,200 (+1.2%)

📰 주요 뉴스:
- Fed 금리 동결 가능성 시사
- 삼성전자, 반도체 투자 확대 발표

📌 오늘의 체크포인트:
- 美 GDP 발표 예정
- 비트코인 ETF 수급 동향
"""

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, data=payload)
    return response.json()

if __name__ == "__main__":
    summary = get_market_summary()
    result = send_telegram_message(summary)
    print("메시지 전송 결과:", result)
