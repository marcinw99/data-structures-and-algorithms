package main

import "fmt"

func merge(nums1 []int, m int, nums2 []int, n int) {
	var removedNumsCache []int
	cacheSize := 0
	nums2Pointer := 0

	if n == 0 {
		return
	}

	for i := 0; i < m+n; i++ {
		isInFreeSpace := i >= m
		if (isInFreeSpace || (nums2[nums2Pointer] < nums1[i])) && (cacheSize == 0 || nums2[nums2Pointer] < removedNumsCache[0]) {
			if i <= m-1 {
				removedNumsCache = append(removedNumsCache, nums1[i])
				cacheSize++
			}
			nums1[i] = nums2[nums2Pointer]
			nums2Pointer++
		} else if cacheSize > 0 && (isInFreeSpace || removedNumsCache[0] < nums1[i]) && removedNumsCache[0] < nums2[nums2Pointer] {
			if i <= m-1 {
				removedNumsCache = append(removedNumsCache, nums1[i])
				cacheSize++
			}
			nums1[i] = removedNumsCache[0]
			removedNumsCache = removedNumsCache[1:]
			cacheSize--
		}
	}
}

func mergeTwoPointers(nums1 []int, m int, nums2 []int, n int) {
	nums1Pointer := m - 1
	nums2Pointer := n - 1

	// iterate backwards
	for i := m + n - 1; i >= 0; i-- {

		// if nums2 are exhausted, we have the rest of nums1 in proper order
		if nums2Pointer < 0 {
			return
		}

		// if nums1 are exhausted, we know the rest of nums2 will be less than the least of nums1
		if nums1Pointer < 0 {
			nums1[i] = nums2[nums2Pointer]
			nums2Pointer--
		} else {
			// main copying
			if nums2[nums2Pointer] > nums1[nums1Pointer] {
				nums1[i] = nums2[nums2Pointer]
				nums2Pointer--
			} else {
				nums1[i] = nums1[nums1Pointer]
				nums1Pointer--
			}
		}
	}
}

func main() {
	testData1 := []int{1, 2, 3, 0, 0, 0}
	mergeTwoPointers(testData1, 3, []int{2, 5, 6}, 3)
	fmt.Println(testData1) // 1, 2, 2, 3, 5, 6

	testData2 := []int{1}
	mergeTwoPointers(testData2, 1, []int{}, 0)
	fmt.Println(testData2) // 1

	testData3 := []int{0}
	mergeTwoPointers(testData3, 0, []int{1}, 1)
	fmt.Println(testData3) // 1
}
