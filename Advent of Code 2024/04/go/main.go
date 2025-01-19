package main

import (
	"bufio"
	"fmt"
	_ "fmt"
	"os"
)

func Parse() [][]rune {
	scanner := bufio.NewScanner(os.Stdin)
	var out [][]rune

	for scanner.Scan() {
		out = append(out, []rune(scanner.Text()))
	}

	return out
}

func Letter(crossword [][]rune, x int, y int) rune {
	if x >= len(crossword) || x < 0 || y >= len(crossword[0]) || y < 0 {
		return ' '
	}

	return crossword[y][x]
}

func Find(crossword [][]rune, word string, x int, y int, dx int, dy int) bool {
	for idx, letter := range word {
		if Letter(crossword, x+idx*dx, y+idx*dy) != letter {
			return false
		}
	}

	return true
}

func Part1(crossword [][]rune) int {
	sol := 0
	directions := [][]int{{1, 0}, {1, 1}, {0, 1}, {-1, 1}, {-1, 0}, {-1, -1}, {0, -1}, {1, -1}}

	for y, line := range crossword {
		for x := range line {
			for _, direction := range directions {
				if Find(crossword, "XMAS", x, y, direction[0], direction[1]) {
					sol++
				}
			}
		}
	}

	return sol
}

func main() {
	crossword := Parse()

	fmt.Printf("Part 1: %d\n", Part1(crossword))
}
