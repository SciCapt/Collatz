def NumberTest(numberToTest):

    def repeatTest(list):   # Test for the values that indicate a repeating list
        endValue = False
        if len(list) >= 3:
            if abs(list[len(list)-1]) == 1:
                if abs(list[len(list)-2]) == 2:
                    endValue = True
            elif list[len(list)-1] == 0:
                if list[len(list)-1] == 0:
                    endValue = True
            elif list[len(list)-1] == -5:
                if list[len(list)-2] == -10:
                    endValue = True
            elif list[len(list)-1] == -17:
                if list[len(list)-2] == -34:
                    endValue = True
        return endValue

    # insert sacrifical number
    sacrifice = numberToTest

    # Form the following numbers based off of input (numberToTest)
    # and based off of the Collatz conjecture algorithm
    sacrifice = sacrifice//1
    fragments = [numberToTest]

    while repeatTest(fragments) != True:
        if sacrifice%2 > 0:                 # (if current value is odd)
            sacrifice = (sacrifice*3) + 1
            fragments.append(sacrifice)
        elif sacrifice%2 == 0:              # (if current value is even)
            sacrifice = sacrifice/2
            fragments.append(sacrifice)

    return fragments
