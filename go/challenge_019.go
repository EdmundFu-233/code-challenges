package main

import "fmt"

func process019(x int) int {
	return x * 2
}

func main() {
	for i := 1; i <= 5; i++ {
		fmt.Printf("process(%d) = %d\n", i, process019(i))
	}
}
