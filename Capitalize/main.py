# Coding With Kien

def solve(s):
    words = s.split()
    for i in words:
        s = s.replace(i, i.capitalize())
    return s

if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
