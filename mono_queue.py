from collections import deque

def streaming_max(nums, k):
    dq = deque()
    result = []

    for i in range(len(nums)):

        # Remove indices out of window
        if dq and dq[0] <= i - k:
            dq.popleft()

        # Remove smaller elements
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        # Record max
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(streaming_max(nums, k))