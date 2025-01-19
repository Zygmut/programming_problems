package main

import (
	"bufio"
	"errors"
	"fmt"
	"math"
	"os"
	"slices"
	"strconv"
	"strings"
)

func Parse() ([]int, []int, error) {
	var ids1, ids2 []int

	scanner := bufio.NewScanner(os.Stdin)

	// Parse Lists into two
	for scanner.Scan() {
		var ids = strings.Fields(scanner.Text())

		id1, err := strconv.Atoi(ids[0])

		if err != nil {
			return nil, nil, errors.New(fmt.Sprintf("Could not parse element %s into integer", ids[0]))
		}

		id2, err := strconv.Atoi(ids[1])

		if err != nil {
			return nil, nil, errors.New(fmt.Sprintf("Could not parse element %s into integer", ids[1]))
		}

		ids1 = append(ids1, id1)
		ids2 = append(ids2, id2)
	}

	return ids1, ids2, nil
}

func Part1(first []int, second []int) int {
	slices.Sort(first)
	slices.Sort(second)

	var sum int = 0

	for idx := range first {
		sum += int(math.Abs(float64(first[idx] - second[idx])))
	}

	return sum
}

func Part2(first []int, second []int) int {
	var sum = 0

	slices.Sort(first)

	for _, number := range second {
		if Search(first, number) {
			sum += number
		}
	}

	return sum
}

func Search(array []int, search int) bool {
	found := false
	low := 0
	high := len(array) - 1
	for low <= high {
		mid := (low + high) / 2
		if array[mid] == search {
			found = true
			break
		}
		if array[mid] > search {
			high = mid - 1
		} else {
			low = mid + 1
		}
	}
	return found
}

func main() {

	first, second, err := Parse()

	if err != nil {
		panic(err)
	}

	fmt.Printf("Part 1: %d\n", Part1(first, second))

	fmt.Printf("Part 2: %d\n", Part2(first, second))
}
