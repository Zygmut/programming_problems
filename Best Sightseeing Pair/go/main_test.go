package main

import (
	"testing"
)

type TestCase struct {
	Input    []int
	Expected int
}

var testCases = []TestCase{
	{[]int{8, 1, 5, 2, 6}, 11},
	{[]int{1, 2}, 2},
}

func Test(t *testing.T) {
	for _, testCase := range testCases {
		if got := maxScoreSightseeingPair(testCase.Input); got != testCase.Expected {
			t.Errorf("Assertion error. Got %d but expected %d", got, testCase.Expected)
		}
	}
}
