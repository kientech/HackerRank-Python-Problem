if __name__ == '__main__':
    N = int(input()) # Integer Number
    L = []
    for i in range(N):
        user_func = input().split()
        # insert 0 5 --> ["insert", "0", "5"]
        command = user_func[0]
        
        if command == 'append':
            L.append(int(user_func[1]))
        elif command == 'insert':
            L.insert(int(user_func[1]), int(user_func[2]))
        elif command == 'remove':
            L.remove(int(user_func[1]))
        elif command == 'print':
            print(L)
        elif command == 'sort':
            L.sort()
        elif command == 'pop':
            L.pop()
        elif command == 'reverse':
            L.reverse()