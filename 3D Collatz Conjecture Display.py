from mpl_toolkits import mplot3d
from matplotlib import pyplot as plt
from EnchancedNumberTester import NumberTest

## Input Range
firstTest = int(input('First Test Number in Range: '))
lastTest = int(input('Last Test Number in Range: '))

## Making y, x, z Scatter Lists
YL = []
XL = []
ZL = []
z = 0
for test in range (firstTest, lastTest+1):
    bounceList = NumberTest(test)
    for bY in range(len(bounceList)):
        YL.append(bounceList[bY])

    bounceLength = [*range(len(bounceList))]
    for bX in range(len(bounceList)):
        XL.append(bounceLength[bX])

    for bZ in range(len(bounceList)):
        ZL.append(z)
    z = z + 1

## Final 3D Plotting
ax = plt.axes(projection='3d')
ax.scatter3D(XL, YL, ZL)
ax.set_xlabel('Bounce Indices')     # X Values
ax.set_ylabel('Bounce Value')       # Y Values
ax.set_zlabel('Starting Number')    # Z Values
ax.view_init(50, 160)
plt.show()
