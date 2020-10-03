
str = input('Enter a String:')
def string_splosion(str):
    i, result = 0, ''
    for i in range(len(str)):
        result = result + str[:i+1]
    return result
print(string_splosion(str))
