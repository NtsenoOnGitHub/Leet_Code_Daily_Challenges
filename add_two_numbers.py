def add_two_numbers(l1: list[int], l2: list[int]) -> list[int]:
    buildstring  = ''
    for index, num in enumerate(l1):
        buildstring += str(num)
    
    num1 = int(buildstring)
    buildstring = ''

    for index, num in enumerate(l2):
        buildstring += str(num)
    
    num2 = int(buildstring)

    if num1 + num2 == 0:
        return [0]

    results = str(num1 + num2)
    lst = []

    for i in range(1, len(results)+1):
        lst.append(int(results[-(i)]))

    return lst


print(add_two_numbers([0], [0]))