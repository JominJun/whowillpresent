import time

day = int(time.strftime("%d", time.localtime(time.time())))
std_presenter = list() # 날짜로 인해 선택된 자
total_presenter = list()
add_presenter = list() # 덧셈으로 인해 선택된 자
add_add_presenter = list()
add_mul_presenter = list()
add_con_presenter = list()
mul_presenter = list() # 곱셈으로 인해 선택된 자
mul_add_presenter = list()
mul_mul_presenter = list()
mul_con_presenter = list()
con_presenter = list() # 숫자 반전으로 인해 선택된 자
con_add_presenter = list()
con_mul_presenter = list()
con_con_presenter = list()

def condition(inp):
    return inp<=35

def returnCMAX(inp):
    return 3 if int(str(inp)[-1]) >= 6 else 4

def fillList(arr, inp):
    for i in range(returnCMAX(inp)):
        k = 30 if inp + i * 10 >= 35 else 0
        arr.append(inp + i * 10 - k)
    return arr

def maker(type, arr):
    k = -1 if int(arr[-1]) >= 10 else -2
    break_list = list(str(arr[k]))

    if(type == "add"):
        return int(break_list[0]) + int(break_list[1])
    elif(type == "mul"):
        return int(break_list[0]) * int(break_list[1])
    elif(type == "con"):
        if(break_list[1] == break_list[0]):
            break_list = list(str(arr[k-1]))
        return int(break_list[1]+break_list[0])

print("날짜")
print(fillList(std_presenter,day), end="\n\n")

print("날짜->덧셈")
print(fillList(add_presenter, maker("add", fillList(std_presenter, day))))
print("날짜->덧셈->덧셈")
print(fillList(add_add_presenter, maker("add", fillList(add_presenter, maker("add", fillList(std_presenter, day))))))
print("날짜->덧셈->곱셈")
print(fillList(add_mul_presenter, maker("mul", fillList(add_presenter, maker("add", fillList(std_presenter, day))))))
print("날짜->덧셈->전환")
print(fillList(add_con_presenter, maker("con", fillList(add_presenter, maker("add", fillList(std_presenter, day))))), end="\n\n")

print("날짜->곱셈")
print(fillList(mul_presenter, maker("mul", fillList(std_presenter, day))))
print("날짜->곱셈->덧셈")
print(fillList(mul_add_presenter, maker("add", fillList(add_presenter, maker("mul", fillList(std_presenter, day))))))
print("날짜->곱셈-곱셈")
print(fillList(mul_mul_presenter, maker("mul", fillList(add_presenter, maker("mul", fillList(std_presenter, day))))))
print("날짜->곱셈->전환")
print(fillList(mul_con_presenter, maker("con", fillList(add_presenter, maker("mul", fillList(std_presenter, day))))), end="\n\n")

print("날짜->전환")
print(fillList(con_presenter, maker("con", fillList(std_presenter, day))))
print("날짜->전환->덧셈")
print(fillList(con_add_presenter, maker("add", fillList(add_presenter, maker("con", fillList(std_presenter, day))))))
print("날짜->전환->곱셈")
print(fillList(con_mul_presenter, maker("mul", fillList(add_presenter, maker("con", fillList(std_presenter, day))))))
print("날짜->전환->전환")
print(fillList(con_con_presenter, maker("con", fillList(add_presenter, maker("con", fillList(std_presenter, day))))))

total_presenter = std_presenter + add_presenter + add_add_presenter + add_mul_presenter + add_con_presenter + mul_presenter + mul_add_presenter + mul_mul_presenter + mul_con_presenter + con_presenter + con_add_presenter + con_mul_presenter + con_con_presenter
total_presenter = list(set(total_presenter))
total_presenter = list(filter(condition, total_presenter))

print("=====[오늘 해야할 사람(최종)]=====")
print(total_presenter)