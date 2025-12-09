import requests

def instant_rug_check(token_address: str):
    url = f"https://api.dexscreener.com/latest/dex/tokens/{token_address}"
    data = requests.get(url).json().get("pairs", [{}])[0]

    if not data:
        print("Токен не найден или ещё нет пары")
        return

    token = data["baseToken"]
    liq = data["liquidity"]["usd"]
    mc = data.get("fdv", 0)
    lp_burned = "burned" in data.get("labels", [])
    honeypot = data.get("honeypot", False)

    print(f"BASE RUG-CHECK → {token['symbol']}\n"
          f"MC: ${mc:,.0f} | Liq: ${liq:,.0f}\n"
          f"LP Burned: {'YES' if lp_burned else 'NO'}\n"
          f"Honeypot: {'YES — НЕ ПОКУПАЙ!' if honeypot else 'No'}\n"
          f"https://dexscreener.com/base/{data['pairAddress']}\n"
          f"{'SAFE' if (lp_burned and not honeypot and liq > 5000) else 'RISKY AS HELL'}")

if __name__ == "__main__":
    addr = input("Base token address: ").strip()
    instant_rug_check(addr)
