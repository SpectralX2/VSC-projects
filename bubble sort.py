import random

def create_list():
    nums = []
    for i in range(10):
        nums.append(random.randint(-1000, 1000))
    return nums
def swap(lst, i1, i2):
    temp = lst[i2]
    lst[i2] = lst[i1]
    lst[i1] = temp

def bubble_list(lst):
    for i in range(1, len(lst)):
        j = i - 1
        while j >= 0:
            if lst[j + 1] < lst[j]:
                swap(lst, j+1, j)
            j -= 1

def main():
     rlist = create_list()
     print("Original List:", rlist)
     bubble_list(rlist)
     print("Sorted List:", rlist)
main()