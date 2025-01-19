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

func Parse() ([][]int, error) {
	var reports [][]int

	// Parse Lists into two
	scanner := bufio.NewScanner(os.Stdin)

	// Parse Lists into two
	line := 0
	for scanner.Scan() {
		var levels = strings.Fields(scanner.Text())
		reports = append(reports, make([]int, len(levels)))

		for lvl_idx, level := range levels {
			value, err := strconv.Atoi(level)

			if err != nil {
				return nil, errors.New(fmt.Sprintf("Unable to convert %s into a number", level))
			}

			reports[line][lvl_idx] = value
		}

		line += 1
	}

	return reports, nil
}

func isSafe(report []int) bool {
	var isAscending bool = true

	for idx := 1; idx < len(report); idx++ {

		diff := float64(report[idx] - report[idx-1])

		// Save ascending or descending state
		if idx == 1 && diff < 0 {
			isAscending = false
		}

		if math.Abs(diff) < 1 || math.Abs(diff) > 3 || diff >= 0 != isAscending {
			return false
		}
	}

	return true

}
func Part1(reports [][]int) int {
	var safeReports int = 0
	for _, report := range reports {
		if isSafe(report) {
			safeReports += 1
		}
	}

	return safeReports
}

func Part2(reports [][]int) int {
	var safeReports int = 0
	for _, report := range reports {
		if isSafe(report) {
			safeReports += 1
			continue
		}

		for idx := range report {
			copy := slices.Clone(report)

			subset := slices.Delete(copy, idx, idx+1)

			if isSafe(subset) {
				safeReports += 1
				break
			}
		}

	}

	return safeReports
}

func main() {

	reports, err := Parse()

	if err != nil {
		panic(err)
	}

	fmt.Printf("Part 1: %d\n", Part1(reports))
	fmt.Printf("Part 2: %d\n", Part2(reports))
}
