# Coding With Kien

def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number+1):
        decimal = str(i).rjust(width)
        octal = oct(i)[2:].rjust(width)
        hexandecimal = hex(i)[2:].rjust(width)
        binary = bin(i)[2:].rjust(width)
        print(f"{decimal}   {octal}   {hexandecimal}   {binary}")

print_formatted(17)
