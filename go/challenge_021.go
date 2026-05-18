package main

import "fmt"

// maxSlidingWindow returns the maximum element in each sliding window of size k.
func maxSlidingWindow(nums []int, k int) []int {
	if len(nums) == 0 || k <= 0 {
		return nil
	}
	result := make([]int, 0, len(nums)-k+1)
	// deque stores indices with decreasing values
	deque := make([]int, 0)
	for i, v := range nums {
		// Remove indices outside current window
		for len(deque) > 0 && deque[0] < i-k+1 {
			deque = deque[1:]
		}
		// Remove smaller values from back
		for len(deque) > 0 && nums[deque[len(deque)-1]] < v {
			deque = deque[:len(deque)-1]
		}
		deque = append(deque, i)
		// First window complete
		if i >= k-1 {
			result = append(result, nums[deque[0]])
		}
	}
	return result
}

func main() {
	testCases := []struct {
		nums []int
		k    int
		want []int
	}{
		{[]int{1, 3, -1, -3, 5, 3, 6, 7}, 3, []int{3, 3, 5, 5, 6, 7}},
		{[]int{1}, 1, []int{1}},
		{[]int{9, 8, 7, 6, 5}, 2, []int{9, 8, 7, 6}},
		{[]int{}, 3, nil},
	}
	for i, tc := range testCases {
		got := maxSlidingWindow(tc.nums, tc.k)
		ok := len(got) == len(tc.want)
		if ok {
			for j := range got {
				if got[j] != tc.want[j] {
					ok = false
					break
				}
			}
		}
		if ok {
			fmt.Printf("Challenge 021 test %d PASSED\n", i+1)
		} else {
			fmt.Printf("Challenge 021 test %d FAILED: got %v, want %v\n", i+1, got, tc.want)
		}
	}
}
