package main

import (
	"fmt"
	"time"
)

func main() {
	i := 1
	start := time.Now()

	for i < 1000000000 {
		i++
	}

	fmt.Print(time.Since(start).Seconds())

}
