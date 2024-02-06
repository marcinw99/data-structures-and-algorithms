package main

import "fmt"

/**
 * Definition for singly-linked list.
 */

type ListNode struct {
	Val  int
	Next *ListNode
}

func deleteDuplicates(head *ListNode) *ListNode {
	dummy := head
	slow := dummy
	fast := dummy

	for fast != nil && fast.Next != nil {
		for slow.Val == fast.Val && fast.Next != nil {
			fast = fast.Next
		}
		if slow.Val == fast.Val { // end of the list
			slow.Next = nil
		} else {
			slow.Next = fast
			slow = fast
		}
	}

	return dummy
}

// simpler
func deleteDuplicatesSimpler(head *ListNode) *ListNode {
	dummy := head
	current := dummy

	for current != nil && current.Next != nil {
		if current.Next.Val == current.Val {
			current.Next = current.Next.Next
		} else {
			current = current.Next
		}
	}

	return dummy
}

func printLinkedListValues(head *ListNode) {
	dummy := head
	fmt.Println(dummy.Val)

	for dummy.Next != nil {
		dummy = dummy.Next
		fmt.Println(dummy.Val)
	}
}

func main() {
	test1Node1 := ListNode{1, nil}
	test1Node2 := ListNode{1, nil}
	test1Node3 := ListNode{2, nil}
	test1Node1.Next = &test1Node2
	test1Node2.Next = &test1Node3

	test2Node1 := ListNode{1, nil}
	test2Node2 := ListNode{1, nil}
	test2Node3 := ListNode{2, nil}
	test2Node4 := ListNode{3, nil}
	test2Node5 := ListNode{3, nil}
	test2Node6 := ListNode{3, nil}
	test2Node1.Next = &test2Node2
	test2Node2.Next = &test2Node3
	test2Node3.Next = &test2Node4
	test2Node4.Next = &test2Node5
	test2Node5.Next = &test2Node6

	//fmt.Println("test1")
	//printLinkedListValues(&test1Head)
	//fmt.Println("test2")
	//printLinkedListValues(&test2Head)

	output1 := deleteDuplicatesSimpler(&test1Node1) // 0,1,2
	fmt.Println("test1")
	printLinkedListValues(output1)

	output2 := deleteDuplicatesSimpler(&test2Node1) // 0,1,2,3
	fmt.Println("test2")
	printLinkedListValues(output2)
}
