def count_zero_neighbours(numbers):
    index = 0
    answer = 0
    
    for number in numbers:
        if index < len(numbers) - 1:
            bour = numbers[index + 1]

            if number + bour == 0:
                answer += 1
        index += 1

    return answer

print(count_zero_neighbours([1, 2, -2, 0, 0, 5, -5]))
