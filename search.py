# IMPORT -----------------------------------------------------------------------
import random
import sys
import time
# ------------------------------------------------------------------------------


# BINARY -----------------------------------------------------------------------
def binary(valuelist, searchval):
    """ Search valuelist for searchval, narrowing
    the region of interest by half with every probe.
    Does require the list to be sorted.
    Time complexity: best O(log(n)), worst O(log(n)), average O(log(n)).
    Space complexity: O(1).
    """

    # Create the bounds; lower is inclusive, upper is exclusive.
    lower, upper = 0, len(valuelist)

    # Loop until we return a value.
    while True:
        # If the ROI is empty, we couldn't find the value.
        if lower == upper:
            return -1

        # Check the middle value.
        middle = (lower+upper)//2
        midval = valuelist[middle]
        if midval == searchval:
            return middle             # We found it.
        elif midval > searchval:
            upper = middle            # Probed too high, search the lower half.
        else:
            lower = middle+1          # Probed too low, search the upper half.
# ------------------------------------------------------------------------------


# LINEAR -----------------------------------------------------------------------
def linear(valuelist, searchval):
    """ Search valuelist for searchval,
    checking every index in order.
    Does not require the list to be sorted.
    Time complexity: best O(1), worst O(n), average O(n/2).
    Space complexity: O(1).
    """

    # Iterate through the list, probing repeatedly until we find it.
    for i, val in enumerate(valuelist):
        if val == searchval:
            return i
    return -1
# ------------------------------------------------------------------------------


# UNIT TEST --------------------------------------------------------------------
def main(argv):
    my_list = [x*x for x in range(0, 10000)]
    test_ind = random.randint(0, len(my_list)-1)
    test_val = my_list[test_ind]
    functions = [binary, linear]
    for fn in functions:
        start = time.clock()
        index = fn(my_list, test_val)
        end = time.clock()
        if index == test_ind:
            print("{0}: {1:.8f} seconds".format(fn, end-start))


if __name__ == "__main__":
    main(sys.argv)
# ------------------------------------------------------------------------------
