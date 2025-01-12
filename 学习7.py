def match_example(num):
    match num:
        case 1:
            print("匹配到值为1")
        case 2:
            print("匹配到值为2")
        case _:
            print("匹配到其他值")
a=int(input())
match_example(a)
for x in range(2,6):
  print(x)
else:
  print("Finally finished!")