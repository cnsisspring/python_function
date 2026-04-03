import random

def get_random_digit():
    return random.randint(0, 9)

def combine_digits(a, b):
    return a * 10 + b

def is_not_zero(num):
    return num != 0

def get_divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def get_divisor_count(divisors):
    return len(divisors)

def get_divisor_sum(divisors):
    return sum(divisors)

def get_second_largest_divisor(divisors):
    return sorted(divisors)[-2]

def print_answer_info(count, total, second):
    print(count)
    print(total)
    print(second)

def answer_loop(num, count, total, second):
    print_answer_info(count, total, second)
    while True:
        user = input()
        if user == "quit":
            return True
        guess = int(user)
        if guess == num:
            print("true")
            return True
        else:
            print("false")
            if guess < num:
                print("up")
            else:
                print("down")

def add_loop(num, divisor_sum):
    print(num)
    while True:
        user = input()
        if user == "quit":
            return True
        val = int(user)
        if val == divisor_sum:
            print("true")
            return True
        else:
            print("false")
            if val < divisor_sum:
                print("up")
            else:
                print("down")

def main():
    while True:
        a = get_random_digit()
        b = get_random_digit()
        num = combine_digits(a, b)
        if is_not_zero(num):
            break

    divisors = get_divisors(num)
    count = get_divisor_count(divisors)
    total = get_divisor_sum(divisors)
    second = get_second_largest_divisor(divisors)

    while True:
        mode = input("Add 혹은 Answer를 입력하세요 (종료: quit): ")

        if mode == "quit":
            break

        elif mode == "Answer":
            if answer_loop(num, count, total, second):
                break

        elif mode == "Add":
            if add_loop(num, total):
                break

        else:
            print("잘못된 입력입니다.")

if __name__ == "__main__":
    main()