for i in range(int(input())):
    N,K = list(map(int,input().split()))
    array = list(map(int,input().split()))
    first = list()
    second = list()
    array  = list()
    first.append(array[0:N+1])
    for a  in range(len(first)-1,-1,-1):
        array.append(first[a])
    second.append(array[N-1:])
    for b in range(len(second)-1,-1,-1):
        array.append(second[b])
    for a in range(len(array)):
        print(array[a])

        
    print()