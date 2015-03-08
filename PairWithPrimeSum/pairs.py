def prime_pair(numbers):
    prime_pair = True
    index = 0

    while index < len(numbers) - 1:
        check = numbers[index]
        for number in numbers:
            sum = number + check
            for int in range(1, sum - 1):
                if sum % int == 0:
                    prime_pair = False
                else:
                    prime_pair = True

                    if prime_pair == True:
                        return prime_pair
        index += 1

    return prime_pair
