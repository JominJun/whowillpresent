import time, math

day = int(time.strftime("%d", time.localtime(time.time())))
std_presenter = sorted([i for i in range(1, 36) if i%10 == day%10], key=lambda k: k-day if k-day >= 0 else math.inf)
plus_presenter = [i for i in range(1, 36) if i%10 == (int(str(std_presenter[-1])[0])+int(str(std_presenter[-1])[1]))%10]
mul_presenter = [i for i in range(1, 36) if i%10 == (int(str(std_presenter[-1])[0])*int(str(std_presenter[-1])[1]))%10]
reverse_presenter =[i for i in range(1, 36) if i%10 == (int(str(std_presenter[-1])[1]+str(std_presenter[-1])[0]))%10]

result = {
    "Origin": std_presenter,
    "Tree 1": { # 덧셈
        "Tree 1": plus_presenter,
        "Tree 1-1": [i for i in range(1, 36) if i%10 == (int(str(plus_presenter[-1])[0])+int(str(plus_presenter[-1])[1]))%10], # 덧셈
        "Tree 1-2": [i for i in range(1, 36) if i%10 == (int(str(plus_presenter[-1])[0])*int(str(plus_presenter[-1])[1]))%10], # 곱셈
        "Tree 1-3": [i for i in range(1, 36) if i%10 == (int(str(plus_presenter[-1])[1]+str(plus_presenter[-1])[0]))%10]       # 전환
    },
    "Tree 2": { # 곱셈
        "Tree 2": mul_presenter,
        "Tree 2-1": [i for i in range(1, 36) if i%10 == (int(str(mul_presenter[-1])[0])+int(str(mul_presenter[-1])[1]))%10], # 덧셈
        "Tree 2-2": [i for i in range(1, 36) if i%10 == (int(str(mul_presenter[-1])[0])*int(str(mul_presenter[-1])[1]))%10], # 곱셈
        "Tree 2-3": [i for i in range(1, 36) if i%10 == (int(str(mul_presenter[-1])[1]+str(mul_presenter[-1])[0]))%10]       # 전환
    },
    "Tree 3": { # 전환
        "Tree 3": reverse_presenter,
        "Tree 3-1": [i for i in range(1, 36) if i%10 == (int(str(reverse_presenter[-1])[0])+int(str(reverse_presenter[-1])[1]))%10], # 덧셈
        "Tree 3-2": [i for i in range(1, 36) if i%10 == (int(str(reverse_presenter[-1])[0])*int(str(reverse_presenter[-1])[1]))%10], # 곱셈
        "Tree 3-3": [i for i in range(1, 36) if i%10 == (int(str(reverse_presenter[-1])[1]+str(reverse_presenter[-1])[0]))%10]       # 전환
    }
}

def getInfoByNum(num):
    ourClass = [...] # 비밀이에요 ><
    return ourClass[num-1]
