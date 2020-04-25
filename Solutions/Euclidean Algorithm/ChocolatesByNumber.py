def solution(chocolates, num):
    eaten = []
    toEat = 0
    eaten.append(toEat)
    while True:
        toEat = (toEat + num) % chocolates
        if toEat not in eaten:
            eaten.append(toEat)
        else:
            break

    return len(eaten)

print(solution(10, 4))
