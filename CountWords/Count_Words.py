def count_words(words):
    answer = {}

    for word in words:
        if word in answer:
            answer[word] += 1
        else:
            answer[word] = 1

    return answer

print(count_words(["words", "are", "meaningful", "words", "words", "are"]))
