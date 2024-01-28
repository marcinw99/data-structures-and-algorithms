package main

import "fmt"

type RichestCustomer struct {
	index  int
	wealth int
}

func maximumWealth(accounts [][]int) int {
	richestCustomer := RichestCustomer{}

	for accountIndex, accountBanks := range accounts {
		accountWealth := 0

		for _, v := range accountBanks {
			accountWealth += v
		}

		if accountWealth > richestCustomer.wealth {
			richestCustomer.index = accountIndex
			richestCustomer.wealth = accountWealth
		}
	}

	return richestCustomer.wealth
}

func main() {
	testData := [][]int{{1, 2, 3}, {3, 2, 1}}
	fmt.Println(maximumWealth(testData))
}

// time = O(n x m)
// space = O(1)
