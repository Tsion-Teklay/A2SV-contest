def process_string(input_string):
    vowels = "AEIOUYaeiouy"
    result = []
 
    for char in input_string:
        if char in vowels:
            continue
        else:
            result.append(".")
            if char.isupper():
                char = char.lower()
            result.append(char)
 
    return ''.join(result)
