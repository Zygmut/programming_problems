package main

func lexicalOrder(n int) []int {
	res := []int{}

	queue := []int{1, 2, 3, 4, 5, 6, 7, 8, 9}

	for len(queue) > 0 {
		val := queue[0]
		queue = queue[1:]

		if val > n {
			continue
		}

		res = append(res, val)

		val *= 10

		newValues := []int{}

		for a := range 10 {
			newValues = append(newValues, val+a)
		}

		queue = append(newValues, queue...)
	}

	return res
}

func lexicalOrderStack(n int) []int {
	res := []int{}

	stack := []int{9, 8, 7, 6, 5, 4, 3, 2, 1}

	for len(stack) > 0 {
		val := stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		if val > n {
			continue
		}

		res = append(res, val)

		val *= 10
		for a := range 9 {
			stack = append(stack, val+9-a)
		}

		stack = append(stack, val)
	}

	return res
}

func lexicalOrderStackPreAlloc(n int) []int {
	res := make([]int, 0, n)

	stack := []int{9, 8, 7, 6, 5, 4, 3, 2, 1}

	for len(stack) > 0 {
		val := stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		if val > n {
			continue
		}

		res = append(res, val)

		val *= 10
		for a := range 9 {
			stack = append(stack, val+9-a)
		}

		stack = append(stack, val)
	}

	return res
}

func lexicalOrderDynStackPreAlloc(n int) []int {
	res := make([]int, 0, n)

	stack := []int{1}

	for len(stack) > 0 {
		val := stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		if val > n {
			continue
		}

		res = append(res, val)

		if val%10 != 9 {
			stack = append(stack, val+1)
		}

		stack = append(stack, val*10)
	}

	return res
}
