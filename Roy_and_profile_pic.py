L=int(input())
N=int(input())
for i in range(N):
    W,H = list(map(int,input().split(' ')))
    if W<L or H<L:
        print("UPLOAD ANOTHER")
    elif W==H or (W==L and H==L):
        print("ACCEPTED") 
    else:
        print("CROP IT")
