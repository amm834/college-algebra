# n1/d1 = n2/d2


n1 = 10
d1 = 30

n2 = 10
d2 = 0

if n2 == 0:
    answer = n1 * d2 / d1
    print("n2 = ", answer)

if d2 == 0:
    answer = n2 * d1 / n1
    print("d2 = ", answer)
