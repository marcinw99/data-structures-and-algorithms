package main

import "fmt"

func numJewelsInStones(jewels string, stones string) int {
	answer := 0

	jewelsDict := map[int32]bool{}

	for _, jewel := range jewels {
		jewelsDict[jewel] = true
	}

	for _, stone := range stones {
		if jewelsDict[stone] {
			answer++
		}
	}

	return answer
}

func main() {
	fmt.Println(numJewelsInStones("aA", "aAAbbbb")) // 3
	fmt.Println(numJewelsInStones("z", "ZZ"))       // 0
}
