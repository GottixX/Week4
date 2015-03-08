def hash_them(keys, values):
    answer = {
        }

    index = 0
    
    for key in keys:
        if index < len(values):
            answer[key] = values[index]
        else:
            answer[key] = None

        index += 1

    return answer

