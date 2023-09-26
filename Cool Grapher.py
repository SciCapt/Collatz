from matplotlib import pyplot as plt
import numpy as np

# Basic parameters
## Calculate for the range [0, values-1]
values = 1000
maxes = []

# Setup graph stuff
fig, ax = plt.subplots(2)
fig.suptitle(f"Graphs of 0-{values-1} and the unique maximums found")

# Calculate the pattern for the first {values} numbers
for i in range(values):
    num = i
    bounces = [num]

    # Collatz section
    while num > 1:
        if num%2 == 0:
            num /= 2
            bounces.append(num)
        else:
            num *= 3
            num += 1
            bounces.append(num)

    # Note the different repeating maximums
    maxes.append(max(bounces))

    # Add the new patten plotted onto the graph
    ax[0].plot([*range(len(bounces))], bounces)
    if i%(values/10) == 0:
        plt.pause(0.001)

# Maximum values
uniqueMaxes, c = np.unique(np.array(maxes), return_counts=True)
ax[1].plot(uniqueMaxes, c, "g+")
plt.show()
