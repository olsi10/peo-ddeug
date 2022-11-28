# 게임 체크 여부
def gameTF(a):
    if a == 1:
        print("게임 플레이 여부 -> 참")
        return 1
    else: # value.get() == 0:
        print("게임 플레이 여부 -> 거짓")
        return 0

# 게임 창 실행
def gameOpen():
    if num == 1:
        print("참@!@!")
    else:
        print("거짓!!!!")


num = int(input("1"))
gameTF(num)
gameOpen()