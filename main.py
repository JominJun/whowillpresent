import time, math

def makeAddPresenter(arr):
    if len(arr) and arr[-1] // 10: # 비어있는 배열이 아니고 두 자리수 숫자라면
        return [i for i in range(1, 36) if i % 10 == (int(str(arr[-1])[0]) + int(str(arr[-1])[1])) % 10]
    return [] # 한 자리수 숫자거나 비어있다면

def makeMulPresenter(arr):
    if len(arr) and arr[-1] // 10:
        return [i for i in range(1, 36) if i % 10 == ((int(str(arr[-1])[0])) * int(str(arr[-1])[1])) % 10]
    return []

def makeReversePresenter(arr):
    if len(arr) and arr[-1] // 10:
        return [i for i in range(1, 36) if i % 10 == int(str(arr[-1])[1] + str(arr[-1])[0]) % 10]
    return []


day = int(time.strftime("%d", time.localtime(time.time())))
std_presenter = sorted([i for i in range(1, 36) if i%10 == day%10], key=lambda k: k-day if k-day >= 0 else math.inf)
plus_presenter = makeAddPresenter(std_presenter)
mul_presenter = makeMulPresenter(std_presenter)
reverse_presenter = makeReversePresenter(std_presenter)

result = {
    "Origin": std_presenter,
    "Tree 1": { # 덧셈
        "Tree 1": plus_presenter,
        "Tree 1-1": makeAddPresenter(plus_presenter),    # 덧셈
        "Tree 1-2": makeMulPresenter(plus_presenter),    # 곱셈
        "Tree 1-3": makeReversePresenter(plus_presenter) # 전환
    },
    "Tree 2": { # 곱셈
        "Tree 2": mul_presenter,
        "Tree 2-1": makeAddPresenter(mul_presenter),    # 덧셈
        "Tree 2-2": makeMulPresenter(mul_presenter),    # 곱셈
        "Tree 2-3": makeReversePresenter(mul_presenter) # 전환
    },
    "Tree 3": { # 전환
        "Tree 3": reverse_presenter,
        "Tree 3-1": makeAddPresenter(reverse_presenter),    # 덧셈
        "Tree 3-2": makeMulPresenter(reverse_presenter),    # 곱셈
        "Tree 3-3": makeReversePresenter(reverse_presenter) # 전환
    }
}

def getInfoByNum(num):
    ourClass = [...] # 비밀이에요 ><
    return ourClass[num-1]
