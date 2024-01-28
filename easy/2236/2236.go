package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func checkTree(root *TreeNode) bool {
	return root.Val == (root.Left.Val + root.Right.Val)
}

func main() {

	testValue := TreeNode{
		Val: 12,
		Left: &TreeNode{
			Val:   5,
			Left:  nil,
			Right: nil,
		},
		Right: &TreeNode{
			Val:   7,
			Left:  nil,
			Right: nil,
		},
	}

	fmt.Println(checkTree(&testValue))

	defer fmt.Println("world!")
	fmt.Println("Hello")
}
