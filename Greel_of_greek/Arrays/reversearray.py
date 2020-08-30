def reverse(array,n,k):
    i=0
    while(i<n):
        left = i
        right = min(k-i-1,n-1)
if __name__ == "__main__":
    for _ in range(int(input())):
        size,position = list(map,int,input().split())
        array = list(map(int,input().split())
        reverse(array,size,position)

        





















# #code
# for _ in range(int(input())):
#     N     = int(input())
#     array = list(map(int,input().split()))
#     array= array[::-1]
#     for i in range(len(array)):
#         print(array[i],end=' ')
# print()