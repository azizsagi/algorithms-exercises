package main

import "fmt"

type S struct {
	m string
}

func f() *S {
	return &S{"foo"}
}

func main() {

	v := 15 % 4

	switch v {
	case 3:
		fmt.Println(100)

	}
}
