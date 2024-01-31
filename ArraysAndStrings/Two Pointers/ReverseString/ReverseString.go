package main

import "fmt"

func reverseString(s []byte) {
	inputLength := len(s)

	var leftSideCharacter byte

	for i := 0; i < inputLength/2; i++ {
		leftSideCharacter = s[i]

		s[i] = s[inputLength-i-1]
		s[inputLength-i-1] = leftSideCharacter
	}
}

func reverseStringTwoPointers(s []byte) {
	leftPointer := 0
	rightPointer := len(s) - 1
	var leftCharacterCache byte

	for leftPointer < rightPointer {
		leftCharacterCache = s[leftPointer]

		s[leftPointer] = s[rightPointer]
		s[rightPointer] = leftCharacterCache
		leftPointer++
		rightPointer--
	}
}

func main() {
	testData := []byte("abcdef")

	reverseString(testData)
	reverseStringTwoPointers(testData)

	fmt.Println(string(testData))
}
