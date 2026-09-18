def convert_currency(amount_rub, rate):
    return amount_rub / rate

print("--- Простой конвертер валют ---")

# Примерные фиксированные курсы валют для тренировки
rates = {
    "usd": 90.0,
    "eur": 98.0,
    "cny": 12.5
}

try:
    rubles = float(input("Введи сумму в рублях (₽): "))
    print("\nРезультат конвертации:")
    for currency, rate in rates.items():
        converted = convert_currency(rubles, rate)
        print(f"- {converted:.2f} {currency.upper()} (по курсу {rate})")
        
except ValueError:
    print("Ошибка: пожалуйста, вводи только числа!")