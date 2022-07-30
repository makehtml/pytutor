def capitalize_second_letter(word):
    empty = []
    for ind, j in enumerate(word):  # possible use of range func
        if ind % 2 != 0:
            empty.append(word[ind].upper())
        else:
            empty.append(word[ind])
    return ''.join(empty)

def adjusting_to_language(text):
    new_text, empty = text.lower().split(), []
    for word in new_text:
        empty.append(capitalize_second_letter(word))
    return ' '.join(empty)

