import string
def has_all_alphabets(input_string):
    input_string = input_string.lower()
    return set(input_string) == set(string.ascii_lowercase)
n=int(input())
str=input()
if (n<26):
    print("NO")
else:
    if(has_all_alphabets(str)):
        print("YES")
    else:
        print("NO")
