/*
 * @lc app=leetcode id=1572 lang=csharp
 *
 * [1572] Matrix Diagonal Sum
 */

using Console;

// @lc code=start
public class Solution
{
	public int DiagonalSum(int[][] mat)
	{
		int sol = 0;
		for (int i = 0; i < mat.Length; i++)
			sol += mat[i][i] + mat[i][mat.Length - i - 1];

		if ((mat.Length % 2) == 1)
			sol -= mat[mat.Length / 2][mat.Length / 2];

		return sol;
	}
}
// @lc code=end
