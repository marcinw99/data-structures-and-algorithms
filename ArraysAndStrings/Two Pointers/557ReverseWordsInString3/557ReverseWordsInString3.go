package main

import (
	"fmt"
	"unicode"
)

func reverseWords(s string) string {
	answer := make([]uint8, len(s))

	right := 0
	left := 0

	for right <= len(s)-1 {
		if unicode.IsSpace(rune(s[right])) || right == len(s)-1 {
			answer[right] = s[right]

			fmt.Println(left, right)
			for left < right-1 {
				answer[left] = s[right-left]
				left++
			}
			left++
		}

		right++
	}

	return string(answer)
}

func main() {
	//fmt.Println(reverseWords("Let's take LeetCode contest")) // s'teL ekat edoCteeL tsetnoc
	fmt.Println(reverseWords("Mr Ding")) // rM gniD
}
