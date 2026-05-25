# two sum practice for muscle memory
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i
    return ()

# repeat
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        difference = target - num
        if difference in seen:
            return (seen[difference], i)
        seen[num] = i
    return ()


def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        difference = target - num
        if difference in seen:
            return (seen[difference], i)
        seen[num] = i
    return ()

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        difference = target - num
        if difference in seen:
            return (seen[difference], i)
        seen[num] = i
    return ()

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        difference = target - num
        if difference in seen:
            return (seen[difference], i)
        seen[num] = i
    return ()
