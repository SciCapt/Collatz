from matplotlib import pyplot as plt
import math as m

# Calculate the pattern for the first {end} numbers
nonConvergedValues = []
start = 0; end = 1000
for i in range(start, end):
    num = i
    bounces = [num]

    # Collatz section
    while num > 1:

        # powerTwoCheck = m.log(num, 2)
        # if powerTwoCheck == powerTwoCheck//1:
        #     # is a values that will converge (multiple of 2)
        #     nonConvergedValues.append(len(bounces))
        #     break

        if num%2 == 0:
            num /= 2
            bounces.append(num)
        else:
            num *= 3
            num += 1
            bounces.append(num)

    nonConvergedValues.append(len(bounces))

# Plotting
plt.plot([*range(len(nonConvergedValues))], nonConvergedValues, "+")
plt.xlabel("Value Tested")
plt.ylabel("Iterations until reaching a multiple of two")
plt.title("Numbers Tested in Collatz vs. Itr. Until Reaching a Power of 2")
plt.show()