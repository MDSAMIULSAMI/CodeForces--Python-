def min_animals(legs):
    cows = legs // 4
    remaining_legs = legs % 4
    chickens = remaining_legs > 0
    return cows + chickens


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(min_animals(n))
