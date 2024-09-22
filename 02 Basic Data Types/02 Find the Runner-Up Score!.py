if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr=list(arr)
    arr_max = max(arr)

    while arr_max in arr:
        arr.remove(arr_max)
    
    print(max(arr))
