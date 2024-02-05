package main

import "fmt"

// hash map + sliding window
func lengthOfLongestSubstring(s string) int {
	answer := 0

	letters := map[int32]bool{}

	left := 0
	for currentIndex, letter := range s {
		for letters[letter] {
			letters[int32(s[left])] = false
			left++
		}
		answer = max(answer, currentIndex-left+1)
		letters[letter] = true
	}

	return answer
}

func main() {
	fmt.Println(lengthOfLongestSubstring("abcabcbb")) // 3
	fmt.Println(lengthOfLongestSubstring("bbbbb"))    // 1
	fmt.Println(lengthOfLongestSubstring("pwwkew"))   // 3
	fmt.Println(lengthOfLongestSubstring("abcde"))    // 5
	fmt.Println(lengthOfLongestSubstring("aab"))      // 2
}
