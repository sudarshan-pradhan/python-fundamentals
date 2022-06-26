
price = 300

if price >= 300:
    price = price - (price * 0.3)
elif price >= 200 and price < 300:
    price = price - (price * 0.2)
elif price >= 100 and price < 200:
    price = price - (price * 0.1)
elif price < 100:
    price = price - (price * 0.05)

print(price)