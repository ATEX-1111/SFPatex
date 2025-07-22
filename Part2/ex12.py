def check_string(str1, str2, str3):
    result1 = "Found it!" if "The" in str1 else "Nope."
    result2 = "Found it!" if "The" in str2 else "Nope."
    result3 = "Found it!" if "The" in str3 else "Nope."

    return result1, result2, result3

str1 = 'The'
str2 = 'Thumbs up'
str3 = 'Theatre can be boring'

r1, r2, r3 = check_string(str1, str2, str3)
print(r1)
print(r2)
print(r3)