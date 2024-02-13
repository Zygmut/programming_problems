/*
 * @lc app=leetcode id=54 lang=csharp
 *
 * [54] Spiral Matrix
 */

using System.Collections.Generic;
// @lc code=start
public class Solution
{
	public IList<int> SpiralOrder(int[][] matrix)
	{
		int top = 0, right = matrix[0].Length - 1, bottom = matrix.Length - 1, left = 0;

		List<int> sol = new List<int>();

		while (true)
		{
			// Top side
			for (int i = left; i <= right; i++)
				sol.Add(matrix[top][i]);

			top++;

			if (top > bottom)
				break;

			// Right side
			for (int i = top; i <= bottom; i++)
				sol.Add(matrix[i][right]);

			right--;

			if (right < left)
				break;

			// Bottom side
			for (int i = right; i >= left; i--)
				sol.Add(matrix[bottom][i]);

			bottom--;

			if (bottom < top)
				break;

			// Left side
			for (int i = bottom; i >= top; i--)
				sol.Add(matrix[i][left]);

			left++;

			if (left > right)
				break;
		}

		return sol;
	}
}
// @lc code=end
