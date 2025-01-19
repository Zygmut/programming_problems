package main

import (
	"bufio"
	"fmt"
	_ "fmt"
	"os"
	"regexp"
	"strconv"
)

func Parse() string {
	scanner := bufio.NewScanner(os.Stdin)
	var out string
	for scanner.Scan() {
		out += scanner.Text()
	}

	return out
}
func Part1(memory string) int {
	regex := regexp.MustCompile(`mul\((\d+),(\d+)\)`)

	result := 0

	for _, match := range regex.FindAllStringSubmatch(memory, -1) {

		a, err := strconv.Atoi(match[1])
		if err != nil {
			panic(fmt.Sprintf("Unable to convert %s into a number", match[1]))
		}

		b, err := strconv.Atoi(match[2])
		if err != nil {
			panic(fmt.Sprintf("Unable to convert %s into a number", match[2]))
		}

		result += a * b
	}

	return result
}

func Part2(memory string) int {
	regex := regexp.MustCompile(`mul\((\d+),(\d+)\)|do(?:n't)?\(\)`)

	enabled := true
	result := 0

	for _, match := range regex.FindAllStringSubmatch(memory, -1) {

		if match[0][0] == 'd' {
			enabled = match[0][len(match[0])-3] != 't'
			continue
		}

		if enabled {
			a, err := strconv.Atoi(match[1])
			if err != nil {
				panic(fmt.Sprintf("Unable to convert %s into a number", match[1]))
			}

			b, err := strconv.Atoi(match[2])
			if err != nil {
				panic(fmt.Sprintf("Unable to convert %s into a number", match[2]))
			}

			result += a * b
		}
	}

	return result
}

func main() {
	memory := Parse()

	fmt.Printf("Part 1: %d\n", Part1(memory))
	fmt.Printf("Part 2: %d\n", Part2(memory))
}
