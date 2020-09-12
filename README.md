# 누가 발표할까?
과학(물리)쌤이 누구를 발표시키실지 구해주는 프로그램

# 과학쌤의 발표 공식
ex) 2020.09.02

1) 날짜를 기준으로 부른다 => 2번
2) 일의 자리 숫자가 같은 걸 부른다 => 12, 22, 32
3) 마지막으로 부른 번호를 뒤집거나 각 자리수를 곱하거나 더한다. (예외적으로 시계를 보거나 오프라인 수업에서는 교탁에 있는 분필의 바코드 숫자를 볼 수도 있다)
4) 다시 일의 자리 숫자가 같은 걸 부른다
5) 3)으로 가서 무한반복

# 안내
* getInfoByNum은 개인정보보호를 위하여 코드에 기재하지 않았으며 구조는 다음과 같습니다.<br>
<pre><code>def getInfoByNum(num):
    ourClass = [
        {
            "id": 1,
            "name": "이름",
            ...
        },
        {...},
        ...
    ]
    return ourClass[num-1]
</code></pre>

# 사용
[KakaoScheduleAlarm](https://github.com/JominJun/KakaoScheduleAlarm)

# 예외
예외는 언제나 존재합니다
