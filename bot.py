import requests, time, os
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
def get_gold_price():
    try:
        r = requests.get("https://api.gold-api.com/price/XAU", timeout=10).json()
        return float(r.get("price", 0))
    except:
        return 0
def send(msg):
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": CHAT_ID, "text": msg})
    except:
        pass
send("✅ بوت الذهب اشتغل!")
while True:
    try:
        p = get_gold_price()
        if p:
            send(f"💰 الذهب: ${p}")
        time.sleep(3600)
    except:
        time.sleep(60)
