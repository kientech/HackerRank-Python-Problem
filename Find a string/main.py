# Coding With Kien
# HackerRank Solutions

def count_substring(string, sub_string):
    counting = 0
    while sub_string in string:
        cha = string.find(sub_string)
        string = string[cha+1:]
        counting += 1
    return counting
    

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)