def reverse(str):
    reverse_string=""
    for char in str:
        reverse_string = char+reverse_string
    return reverse_string

str=input("Enter the String")
print(reverse(str))
