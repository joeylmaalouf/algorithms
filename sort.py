# IMPORT -----------------------------------------------------------------------
import random
import sys
import time
# ------------------------------------------------------------------------------


# BUBBLE -----------------------------------------------------------------------
def bubble(input):
    """ Repeatedly iterate through, "bubbling" the smaller values up towards
        the beginning of the list while the larger vales "sink" towards the end.
        Time complexity: best O(n^2), worst O(n^2), average O(n^2).
        Space complexity: O(1).
    """

    for i in range(len(input)):
        for j in range(len(input)-1, i, -1):
            if input[j] < input[j-1]:
                input[j-1], input[j] = input[j], input[j-1]
    return input
# ------------------------------------------------------------------------------


# HEAP -------------------------------------------------------------------------
def heap(input):
    """ Turn the list into a heap (a sorted binary tree), sorting them
        as they get inserted, then transform the heap back into a list.
        Time complexity: best O(n*log(n)), worst O(n*log(n)), average O(n*log(n)).
        Space complexity: O(1).
    """

    for start in range((len(input)-2)//2, -1, -1):
        _sift_down(input, start, len(input)-1)
    for end in range(len(input)-1, 0, -1):
        input[end], input[0] = input[0], input[end]
        _sift_down(input, 0, end-1)
    return input


def _sift_down(input, start, end):
    root = start
    while True:
        child = root*2+1
        if child > end:
            break
        if child+1 <= end and input[child] < input[child+1]:
            child += 1
        if input[root] < input[child]:
            input[root], input[child] = input[child], input[root]
            root = child
        else:
            break
# ------------------------------------------------------------------------------


# INSERTION --------------------------------------------------------------------
def insertion(input):
    """ For each value in the list, move it backwards until
        the only values before it are smaller than it.
        Time complexity: best O(n), worst O(n^2), average O(n^2).
        Space complexity: O(1).
    """

    for i in range(1, len(input)):
        j = i
        while j > 0 and input[j] < input[j-1]:
            input[j-1], input[j] = input[j], input[j-1]
            j -= 1
    return input
# ------------------------------------------------------------------------------


# MERGE ------------------------------------------------------------------------
def merge(input):
    """ Break the list into halves repeatedly until there are many groups
        of two or one, sort those, and put them back together sorted.
        Time complexity: best O(n*log(n)), worst O(n*log(n)), average O(n*log(n)).
        Space complexity: O(n).
    """

    # Split the list in two and recursively sort the two halves.
    if len(input) > 1:
        output = []
        middle = len(input)//2
        half1 = merge(input[:middle])
        half2 = merge(input[middle:])

        # Put the two halves back together until one runs out,
        # making sure to insert in order, even from different halves.
        i = j = 0  # half1 index, half2 index
        while i < len(half1) and j < len(half2):
            if half1[i] < half2[j]:
                output.append(half1[i])
                i += 1
            else:
                output.append(half2[j])
                j += 1

        # Since one of the halves ran out, we can just add in whatever's
        # left without having to worry about comparing the two.
        output.extend(half1[i:])
        output.extend(half2[j:])
        return output
    return input
# ------------------------------------------------------------------------------


# SELECTION --------------------------------------------------------------------
def selection(input):
    """ Like insertion sort, but only swaps the necessary values,
        rather than every value between the moving ones.
        Time complexity: best O(n^2), worst O(n^2), average O(n^2).
        Space complexity: O(1).
    """

    for i in range(len(input)):
        least = i
        for j in range(i+1, len(input)):
            if input[j] < input[least]:
                least = j
        input[i], input[least] = input[least], input[i]
    return input
# ------------------------------------------------------------------------------


# QUICK ------------------------------------------------------------------------
def quick(input):
    """ Like merge sort, it partitions the data and puts it back
        together again. However, merge sort sorts the data when putting
        it back together; quick sort sorts the data when partitioning it.
        Time complexity: best O(n*log(n)), worst O(n^2), average O(n*log(n)).
        Space complexity: O(n).
    """

    return _quick(input, 0, len(input)-1)


def _quick(input, start, end):
    if start < end:
        pivot = _partition(input, start, end)
        input = _quick(input, start, pivot-1)
        input = _quick(input, pivot+1, end)
    return input


def _partition(input, start, end):
    pivot = random.randint(start, end)
    input[pivot], input[end] = input[end], input[pivot]
    for i in range(start, end):
        if input[i] <= input[end]:
            input[i], input[start] = input[start], input[i]
            start += 1
    input[start], input[end] = input[end], input[start]
    return start
# ------------------------------------------------------------------------------


# UNIT TEST --------------------------------------------------------------------
def main(argv):
    my_list = [i for i in range(0, 10000)]
    functions = [bubble,
                 heap,
                 insertion,
                 merge,
                 selection,
                 quick]
    for fn in functions:
        random.shuffle(my_list)
        unsorted = my_list
        start = time.clock()
        my_list = fn(my_list)
        end = time.clock()
        if my_list == sorted(unsorted):
            print("{0}: {1:.8f} seconds".format(fn, end-start))


if __name__ == "__main__":
    main(sys.argv)
# ------------------------------------------------------------------------------
