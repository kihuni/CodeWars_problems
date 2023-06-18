def to_weird_case(string):
    words = string.split(" ") # ['hello', 'world']
    result = []
    print(words)

    for word in words:
        chars = list(word)
        print(chars)
        weird_case_word = [char.upper() if index % 2 == 0 else char.lower() for index, char in enumerate(chars)]
        result.append("".join(weird_case_word))

    return " ".join(result)
print(to_weird_case("hello world"))