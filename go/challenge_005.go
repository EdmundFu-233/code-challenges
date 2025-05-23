package main

import "fmt"

func process005(x int) int {
	return x * 2
}

func main() {
	for i := 1; i <= 5; i++ {
		fmt.Printf("process(%d) = %d\n", i, process005(i))
	}
}
