# steps:

# Define the function accum with a single parameter, string.
# Initialize an empty list called result to store the intermediate strings.
# Iterate over each character in the string parameter using the enumerate function to get the index and character.
# Create a new string for each character, where the character is repeated index + 1 times.
# Convert the new string to lowercase using the lower() method.
# Append the modified string to the result list.
# Finally, join all the strings in the result list using hyphens ("-") as the separator and return the result.


def accum(string):
    result = []
    for index, char in enumerate(string):
        string_result = char * (index + 1)
        result.append(string_result.lower())
    return "-".join(result)

print(accum("abcd")) #a-bb-ccc-dddd