package main

import "fmt"

func countElements(arr []int) int {
	dict := map[int]bool{}
	counter := 0

	for _, v := range arr {
		dict[v] = true
	}

	for _, v := range arr {
		if dict[v+1] == true {
			counter++
		}
	}

	return counter
}

func main() {
	fmt.Println(countElements([]int{1, 2, 3}))                // 2
	fmt.Println(countElements([]int{1, 1, 3, 3, 5, 5, 7, 7})) // 0
}
