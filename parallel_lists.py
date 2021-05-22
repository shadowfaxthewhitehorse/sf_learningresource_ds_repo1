# parallel lists
  
x = [1, 2, 3, 4, 5, 6]
y = ['a', 'b', 'c', 'd', 'e', 'f']


print(x[0])
print(y[0])

def number_alpha():
    alpha = list('abcdefghijklmnopqrstuvwxyz')

    alpha2 = []
    num2 = []

    for num, let in enumerate(alpha, 1):
        alpha2.append(let)
        num2.append(num)

    dict = {}

    for num, let in enumerate(alpha, 1):
        dict[let] = num

    return alpha2, num2, dict

aleph, nem, dict = number_alpha()

print(aleph)
print(nem)
print(dict)

# print(tuple(number_alpha()))
