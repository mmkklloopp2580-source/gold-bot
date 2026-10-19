import os, time, requests
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
def get_gold_price():
    try:
        r = requests.get("https://api.gold-api.com/price/XAU", timeout=10)
        return float(r.json().get("price", 0))
    except:
        return 0
def send(msg):
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": CHAT_ID, "text": msg}, timeout=10)
    except:
        pass
send("✔️ بوت الذهب اشتغل!")
while True:
    price = get_gold_price()
    if price > 0:
        send(f"💰 سعر الذهب: ${price:.2f} للاونصة")
    time.sleep(3600)
