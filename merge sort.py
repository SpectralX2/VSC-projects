import random

def create_list():
    nums = []
    for i in range(10):
        nums.append(random.randint(-1000, 1000))
    return nums

def merge(original, left, right):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            original[k] = left[i]
            i += 1
        else:
            original[k] = right[j]
            j += 1
        k += 1

        while i < len(left):
            original[k] = left[i]
            i += 1
            k += 1
    #if j < len(right) then there are still elements in right that have not been sorted into theoriginal.
        while j < len(right):
            original[k] = right[j]
            j += 1
            k += 1
    #splits the list into 2 halves, then splits each half in half. Continue until only 1 elementremains in each half list.
def split(alist):
    if(len(alist) > 1):
        #find middle of list.
        middle = len(alist) // 2
        left = alist[:middle]
        right = alist[middle:]
        #split apart the halves
        split(left)
        split(right)
        #merge the halves back together
        merge(alist, left, right)
def merge_sort(a):
    split(a)
def main():
    rlist = create_list()
    print("Original List", rlist)
    merge_sort(rlist)
    print("Merge Sort", rlist)
    print(rlist)
main()