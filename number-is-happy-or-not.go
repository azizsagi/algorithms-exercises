package main

import (
	"fmt"
	"math"
	"slices"
	"strconv"
	"strings"
)

func main() {

	fmt.Print("welcome")
	isHappy(19)
}

func isHappy(num int) bool {

	seen := []int{}

	for !slices.Contains(seen, num) {
		seen = append(seen, num)
		sum := 0
		a := strconv.Itoa(num)
		res := strings.Split(a, "")

		for _, element := range res {
			n, err := strconv.ParseFloat(element)
			sum = sum + int(math.Pow(n, 2))
		}

		if sum == 1 {
			return true
		}

	}

	return false
}
