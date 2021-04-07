def sorting(a,n):
    numberOfSwaps = 0
    for i in range(n):
        for j in range(n-1):
            if a[j] > a[j+1]:
                temp1, temp2 = a[j], a[j+1]
                a[j], a[j+1] = temp2, temp1
                numberOfSwaps += 1
        
        if(numberOfSwaps == 0):
            break
    print("Array is sorted in",numberOfSwaps,"swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[n-1])


if __name__ == '__main__':
    n = int(input())
    s = list(map(int, input().rstrip().split()))
    sorting(s,n);