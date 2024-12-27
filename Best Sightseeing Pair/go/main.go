package main

func maxScoreSightseeingPair(values []int) int {
	maxScore := 0
	candidate := values[0]

	for idx := 1; idx < len(values); idx++ {
		maxScore = max(maxScore, candidate+values[idx]-idx)
		candidate = max(candidate, values[idx]-idx)
	}

	return maxScore
}
