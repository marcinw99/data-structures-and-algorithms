package main

import "fmt"

func canConstruct(ransomNote string, magazine string) bool {
	requiredLetters := map[int32]int{}
	foundLettersCount := 0

	for _, v := range ransomNote {
		if _, ok := requiredLetters[v]; ok {
			requiredLetters[v]++
		} else {
			requiredLetters[v] = 1
		}
	}

	for _, v := range magazine {
		if _, ok := requiredLetters[v]; ok && requiredLetters[v] > 0 {
			requiredLetters[v]--
			foundLettersCount++
		}

		if foundLettersCount == len(ransomNote) {
			return true
		}
	}

	return false
}

// space = O(n)
// time = O(n+m)

func canConstructBestFromLC(ransomNote string, magazine string) bool {
	array := [26]int{} // 26 due to only 26 letters of the alphabet required

	for i := 0; i < len(magazine); i++ {
		array[magazine[i]-'a']++ // this is based on ASCII values and increments by letter
	}

	for i := 0; i < len(ransomNote); i++ {
		array[ransomNote[i]-'a']--

		if array[ransomNote[i]-'a'] < 0 {
			return false
		}
	}

	return true
}

// mine would perform better if the magazine were to be a longer string

func main() {
	//fmt.Println(canConstructBestFromLC("aab", "baa"))
	//fmt.Println(canConstructBestFromLC("aab", "baa"))
	fmt.Println(canConstructBestFromLC("aab", "abc"))
}
