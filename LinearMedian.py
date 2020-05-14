import random

# Selecting the kth greatest number in an unordered list
# A fantastic O(n) implementation!
# For reference, see CLRS pp. 220


"""
Partition

Partition takes in a list of numbers and a pivot, around which it paritions the list into two halves,
those less than the pivot and those greater than the pivot.

To address repetition, it equally splits those equal to the pivot in two halves.

Then it returns both halves and the ranking of the pivot.
"""
def Partition(nums, pivot):
    low, high = [], []
    seen = 0    # if the pivot is seens
    for i in nums:
        if i < pivot:
            low.append(i)
        elif i > pivot:
            high.append(i)
        elif i == pivot:
            if seen == 0:   # the pivot itself is ignored
                pass
            elif seen % 2 == 0:  # the rest are split evenly
                high.append(i)
            else:
                low.append(i)
            seen += 1
    return len(low) + 1, low, high


"""
FindFiveMedian

Return the median of nums, whose length is less or equal than 5.
"""

def FindFiveMedian(nums):
    nums.sort()
    return nums[len(nums) // 2]


"""
FantasticSelect

Return the k-th greatest in num, an unordered list, in linear time.

See README for a brief description of the algorithm.
"""

def FantasticSelect(nums, k):
    #print(k)
    if len(nums) == 1:   # return the only number
        return nums[0]
    if k == 1:     # an optimization for k = 1
        return min(nums)
    # Compute the medians of five
    five_medians = []
    for i in range(0, len(nums), 5):
        five_medians.append(FindFiveMedian(nums[i:i + 5]))
    # Get median of medians
    med_of_medians = FantasticSelect(five_medians, (len(five_medians) + 1) // 2)
    # Partition and Recurse
    rank, low, high = Partition(nums, med_of_medians)
    if rank == k:
        return med_of_medians
    elif rank < k:
        return FantasticSelect(high, k - rank)
    else:
        return FantasticSelect(low, k)

# Demo

# Generate random numbers
a = []
for i in range(10**7):
    a.append(random.randint(-10**12, 10**12))
print("generation complete.")

print(FantasticSelect(a, 9000000))

#print(FantasticSelect(a, 100000))