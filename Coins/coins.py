def calculate_coins(sum):
    result = {}
    coins = [100, 50, 20, 10, 5, 2, 1]

    sum = round(sum * 100)

    for coin in coins:
        times = sum // coin

        result[coin] = times

        sum -= times * coin
    return result

print(calculate_coins(8.94))
print(calculate_coins(0.53))
