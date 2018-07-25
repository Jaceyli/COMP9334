import math
import matplotlib.pyplot as plt

# k is state number
# n is waiting slots
# r is ρ = λ/μ = 15/3

r = 5


def calculate_expression(k):
    # when k <= 4
    if k <= 4:
        p0 = sum([(1 / math.factorial(i)) * r ** i for i in range(0, k + 1)]) ** -1
        pk = p0 * (1 / math.factorial(k)) * r ** k
        all_p = [(1 / math.factorial(i))*p0 * r ** i for i in range(0, k + 1)]
        return p0, pk, all_p
    # when k > 4
    if k > 4:

        sum_basic = sum([(1 / math.factorial(i)) * r ** i for i in range(0, 4 + 1)])
        p0 = (sum([(1 / (24 * 4 ** (i - 4)) * r ** i) for i in range(5, k + 1)]) + sum_basic) ** -1
        pk = p0 * (1 / (24 * 4 ** (k - 4))) * r ** k

        all_p = [(1 / math.factorial(i)) * p0 * r ** i for i in range(0, 4 + 1)]
        for i in range(5, k + 1):
            all_p.append(p0 * (1 / (24 * 4 ** (i - 4))) * r ** i)
        return p0, pk, all_p


print("-----------------(d i)---------------")
print("waiting slots: 2, p0:",calculate_expression(6)[0], ", pk:",calculate_expression(6)[1])

print("\n\n-----------------(d ii)---------------")
# print(calculate_expression(6)[2])
N = sum([i * calculate_expression(6)[2][i] for i in range(0, 7)])
X = (1 - calculate_expression(6)[1]) * 15
R = N / X * (60*60)
S = (60*60)/3
print("Response time:", R, "\nWaiting time:", R - S)

print("\n\n-----------------(e)---------------")
W =[5, 10, 15, 20]
for i in W:
    print("waiting slots:",i + 2, ", p0:",calculate_expression(i + 6)[0], ", pk:",calculate_expression(i+6)[1])

print("\n\n-----------------(f)---------------")
# draw the plot chart
L = [i for i in range(1, 50)]

L_draw_x = []
L_draw_y = []
for i in L:
    if i > 4:
        print("waiting slots:", i - 4, ", p0:", calculate_expression(i + 6)[0], ", pk:", calculate_expression(i + 6)[1])
        L_draw_x.append(i - 4)
        L_draw_y.append(calculate_expression(i)[1])
plt.plot(L_draw_x, L_draw_y, "", linewidth=1)
plt.xlabel("Waiting slots")
plt.ylabel("Blocking probability")
plt.show()