package main

import (
	"fmt"
	"math"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

// optimised for space complexity
func middleNodeSpace(head *ListNode) *ListNode {
	currentNode := head
	listLength := 1

	for currentNode.Next != nil {
		currentNode = currentNode.Next
		listLength++
	}

	currentNode = head

	for i := 1; i < listLength/2; i++ {
		currentNode = currentNode.Next
		listLength++
	}

	return currentNode
}

// time = O(1.5n)
// space = O(1)

// optimised for time complexity
func middleNodeTime(head *ListNode) *ListNode {
	var knownNodes = map[int]*ListNode{}

	currentNode := head

	for currentNode != nil {
		knownNodes[currentNode.Val] = currentNode
		currentNode = currentNode.Next
	}

	nodesCount := len(knownNodes)

	middleNodeIndex := int(math.Ceil(float64(nodesCount) / 2))

	// if there are 2 middle nodes, return the second one
	if nodesCount%2 == 0 {
		middleNodeIndex++
	}

	return knownNodes[middleNodeIndex]
}

// time = O(n)
// space = O(n)

func middleNode(head *ListNode) *ListNode {
	currentNode := head
	middleNode := head

	// this logic is so shit, but it's also amazingly fast
	previouslyIncremented := true
	for currentNode != nil {
		currentNode = currentNode.Next
		if previouslyIncremented {
			previouslyIncremented = false
		} else {
			middleNode = middleNode.Next
			previouslyIncremented = true
		}
	}

	return middleNode
}

// time = O(n)
// space = O(1)

func middleNodeBest(head *ListNode) *ListNode {
	currentNode := head
	middleNode := head

	for currentNode != nil && currentNode.Next != nil {
		middleNode = middleNode.Next
		currentNode = currentNode.Next.Next
	}

	return middleNode
}

func main() {
	testData := &ListNode{
		Val:  1,
		Next: nil,
	}

	currentNode := testData
	for i := 2; i <= 5; i++ {
		currentNode.Next = &ListNode{
			Val:  i,
			Next: nil,
		}
		currentNode = currentNode.Next
	}

	fmt.Println(middleNodeBest(testData))
}
