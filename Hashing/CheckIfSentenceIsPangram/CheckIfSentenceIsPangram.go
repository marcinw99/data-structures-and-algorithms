package main

import "fmt"

func checkIfPangram(sentence string) bool {
	dict := map[int32]bool{}

	for _, v := range sentence {
		dict[v] = true
		if len(dict) == 26 {
			return true
		}
	}

	return false
}

func main() {
	fmt.Println(checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
	fmt.Println(checkIfPangram("leetcode"))
}
