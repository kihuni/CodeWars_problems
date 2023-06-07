import re

def break_camel_case(s):
    # Use regular expression to insert a space before any uppercase letter
    result = re.sub(r'([A-Z])', r' \1', s)
    return result

# Example usage

text = "camelCaseString"

result = break_camel_case(text)
print(result) # camel Case String