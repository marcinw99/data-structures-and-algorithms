package main

import (
	"fmt"
	"slices"
)

// mine
func findWinnersHashMap(matches [][]int) [][]int {
	playersLosses := map[int]int{}

	for _, match := range matches {
		winner, loser := match[0], match[1]

		playersLosses[loser] = (playersLosses[loser] | 0) + 1
		playersLosses[winner] = playersLosses[winner] | 0 // could also be just = playersLosses[winner] due to Go rules
	}

	noLossesPlayers := []int{}
	oneLossPlayers := []int{}

	for player, lossesCount := range playersLosses {
		if lossesCount == 0 {
			noLossesPlayers = append(noLossesPlayers, player)
		} else if lossesCount == 1 {
			oneLossPlayers = append(oneLossPlayers, player)
		}
	}

	slices.Sort(noLossesPlayers)
	slices.Sort(oneLossPlayers)

	return [][]int{noLossesPlayers, oneLossPlayers}
}

// T = O(n log n) S = O(n)

func findWinnersHashSet(matches [][]int) [][]int {
	noLossesPlayers := map[int]bool{}
	oneLossPlayers := map[int]bool{}
	multipleLossesPlayers := map[int]bool{}

	for _, match := range matches {
		winner, loser := match[0], match[1]

		if noLossesPlayers[loser] {
			delete(noLossesPlayers, loser)
			oneLossPlayers[loser] = true
		} else if oneLossPlayers[loser] {
			delete(oneLossPlayers, loser)
			multipleLossesPlayers[loser] = true
		} else if !multipleLossesPlayers[loser] {
			oneLossPlayers[loser] = true
		}

		if !multipleLossesPlayers[winner] && !oneLossPlayers[winner] {
			noLossesPlayers[winner] = true
		}
	}

	answer := [][]int{{}, {}}

	for player := range noLossesPlayers {
		answer[0] = append(answer[0], player)
	}
	for player := range oneLossPlayers {
		answer[1] = append(answer[1], player)
	}

	slices.Sort(answer[0])
	slices.Sort(answer[1])

	return answer
}

func findWinnersHashMapAndHashSet(matches [][]int) [][]int {
	seen := map[int]bool{}
	playersLosses := map[int]int{}

	for _, match := range matches {
		winner := match[0]
		loser := match[1]
		seen[winner] = true
		seen[loser] = true
		if _, ok := playersLosses[loser]; ok {
			playersLosses[loser]++
		} else {
			playersLosses[loser] = 1
		}
	}

	answer := make([][]int, 2)

	for player := range seen {
		lossesCount := playersLosses[player]
		if lossesCount == 0 {
			answer[0] = append(answer[0], player)
		} else if lossesCount == 1 {
			answer[1] = append(answer[1], player)
		}
	}

	slices.Sort(answer[0])
	slices.Sort(answer[1])

	return answer
}

// https://en.wikipedia.org/wiki/Counting_sort
func findWinnersCountingSort(matches [][]int) [][]int {
	const maxPlayers = 100001
	lossesCount := make([]int, maxPlayers)
	for i := range lossesCount { // this would have been a lot cleaner in Python
		lossesCount[i] = -1
	}
	answer := [][]int{{}, {}}

	for _, match := range matches {
		winner, loser := match[0], match[1]
		if lossesCount[winner] == -1 {
			lossesCount[winner] = 0
		}
		if lossesCount[loser] == -1 {
			lossesCount[loser] = 1
		} else {
			lossesCount[loser] += 1
		}
	}

	for i := 0; i < maxPlayers; i++ {
		if lossesCount[i] == 0 {
			answer[0] = append(answer[0], i)
		} else if lossesCount[i] == 1 {
			answer[1] = append(answer[1], i)
		}
	}

	return answer
}

// n = matches length k = losses count length
// T = O(n+k), S = O(k)

func main() {
	testData := [][]int{{1, 3}, {2, 3}, {3, 6}, {5, 6}, {5, 7}, {4, 5}, {4, 8}, {4, 9}, {10, 4}, {10, 9}}
	fmt.Println(findWinnersCountingSort(testData)) // {{1,2,10}, {4,5,7,8}}
}
