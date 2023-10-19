import random

def my_name():
    print("my name is TomSawyer")

def who():
    print("who a u?")

def lotto():
    # 로또번호를 저장할 리스트 생성
    numbers = []

    # 1~45 사이의 숫자 중 중복되지 않는 6개의 숫자를 추첨
    while len(numbers) < 6:
        number = random.randint(1, 45)
        if number not in numbers:
            numbers.append(number)

    # 추첨된 로또번호를 오름차순 정렬하여 반환
    numbers.sort()
    return numbers
