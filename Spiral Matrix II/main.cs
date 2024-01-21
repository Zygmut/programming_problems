/*
 * @lc app=leetcode id=59 lang=csharp
 *
 * [59] Spiral Matrix II
 */

// @lc code=start
public class Solution
{
	public int[][] GenerateMatrix(int n)
	{
		int left = 0, top = 0, right = n - 1, bottom = n - 1;
		int[][] sol = new int[n][];

		for (int i = 0; i < sol.Length; i++)
			sol[i] = new int[n];

		int counter = 1;
		while (left <= right || top <= bottom)
		{
			// Top side
			for (int i = left; i <= right; i++)
				sol[top][i] = counter++;

			top++;

			// Right side
			for (int i = top; i <= bottom; i++)
				sol[i][right] = counter++;

			right--;

			// Bottom side
			for (int i = right; i >= left; i--)
				sol[bottom][i] = counter++;

			bottom--;

			// Left side
			for (int i = bottom; i >= top; i--)
				sol[i][left] = counter++;

			left++;
		}

		return sol;

	}
}
// @lc code=end

