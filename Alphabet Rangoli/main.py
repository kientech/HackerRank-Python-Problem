# Coding With Kien 
import string
def print_rangoli(size):
    design = string.ascii_lowercase
    L = []
    for i in range(number):
        string_ = "-".join(design[i:number])
        L.append((string_[::-1] + string_[1:]).center(4*number-3, "-"))
    print('\n'.join(L[:0:-1] + L))

if __name__ == '__main__':
    number = int(input())
    print_rangoli(number)