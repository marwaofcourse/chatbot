
# Crypto Advisor Bot

crypto_data = {
    "Bitcoin": {
        "price_trend": "rising",
        "energy_efficiency": "poor",
        "project_viability": "strong"
    },
    "Ethereum": {
        "price_trend": "rising",
        "energy_efficiency": "moderate",
        "project_viability": "strong"
    },
    "Dogecoin": {
        "price_trend": "falling",
        "energy_efficiency": "good",
        "project_viability": "weak"
    },
    "Cardano": {
        "price_trend": "stable",
        "energy_efficiency": "good",
        "project_viability": "strong"
    }
}

def crypto_chatbot():
    print("💬 Hi! I'm your Crypto Advisor Bot.")
    print("I can help you analyze cryptocurrencies based on profitability and sustainability.")
    print("Available coins: Bitcoin, Ethereum, Dogecoin, Cardano")

    while True:
        user_input = input("👉 Enter the name of a cryptocurrency (or type 'exit' to quit): ").strip().title()

        if user_input.lower() == 'exit':
            print("👋 Thanks for using Crypto Advisor Bot. Happy investing!")
            break

        if user_input not in crypto_data:
            print("❌ Sorry, I don't have data for that coin.")
            continue

        coin = crypto_data[user_input]
        trend = coin['price_trend']
        efficiency = coin['energy_efficiency']
        viability = coin['project_viability']

        print(f"\n📊 Analysis for {user_input}:")
        print(f"- Price Trend: {trend}")
        print(f"- Energy Efficiency: {efficiency}")
        print(f"- Project Viability: {viability}")

        if trend == "rising" and (efficiency == "good" or efficiency == "moderate") and viability == "strong":
            print("✅ Advice: Strong investment opportunity. Consider investing.")
        elif trend == "rising" and viability == "moderate":
            print("⚠️ Advice: Moderate potential. Invest with caution.")
        elif trend == "falling" or viability == "weak":
            print("❌ Advice: Not a good investment currently.")
        elif efficiency == "poor":
            print("⚠️ Advice: Environmental concerns. Consider sustainability before investing.")
        else:
            print("ℹ️ Advice: Monitor performance and sustainability metrics over time.")

        print("\n")

# Run the bot
if __name__ == "__main__":
    crypto_chatbot()
