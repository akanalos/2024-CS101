x=int(input())
for i in range(x):
    n=input()
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(min(sum(a)+min(b)*len(a),sum(b)+min(a)*len(b)))