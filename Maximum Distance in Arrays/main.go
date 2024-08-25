func maxDistance(arrays [][]int) int {
	minVal := arrays[0][0]
	maxVal := arrays[0][len(arrays[0]) - 1]
	maxDistance := 0

	for _, arr := range arrays[1:]{
		maxDistance = max(maxDistance, max(maxVal - arr[0], arr[len(arr) - 1] - minVal))
		maxVal = max(maxVal, arr[len(arr) - 1])
		minVal = min(minVal, arr[0])
	}

	return maxDistance
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
