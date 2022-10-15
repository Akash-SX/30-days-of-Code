if __name__ == '__main__':
    n = int(input().strip())
    string=''

    arr = list(map(int, input().rstrip().split()))
    for i in arr[::-1]:
        string+=str(i)+' '
    print(string)
