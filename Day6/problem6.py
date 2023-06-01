def to_jaden_case(string):
    words = string.split()
    capitalized_words = [word.capitalize() for word in words]
    converted_string = " ".join(capitalized_words)
    return converted_string

quote = "How can mirrors be real if our eyes aren't real"
print(to_jaden_case(quote))