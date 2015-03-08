def count_zero_pairs(numbers):
    count = 0
    n = len(numbers)

    for i_index in range(0, n):
        for j_index in range(i_index, n):
            i = numbers[i_index]
            j = numbers[j_index]

            if i + j == 0:
                count += 1

    return count
print(count_zero_pairs([0, 2, -2, 5, 10]))
