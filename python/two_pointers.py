def two_sum(nums, target):
    l, r = 0, len(nums) - 1
    while l < r:
        s = nums[l] + nums[r]
        if s == target: return [l, r]
        elif s < target: l += 1
        else: r -= 1
    return []

def three_sum(nums):
    nums.sort()
    result = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]: continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == 0:
                result.append([nums[i], nums[l], nums[r]])
                l += 1; r -= 1
                while l < r and nums[l] == nums[l - 1]: l += 1
            elif s < 0: l += 1
            else: r -= 1
    return result

def max_area(height):
    l, r = 0, len(height) - 1
    max_water = 0
    while l < r:
        water = min(height[l], height[r]) * (r - l)
        max_water = max(max_water, water)
        if height[l] < height[r]: l += 1
        else: r -= 1
    return max_water

if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))
    print(three_sum([-1, 0, 1, 2, -1, -4]))
    print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
