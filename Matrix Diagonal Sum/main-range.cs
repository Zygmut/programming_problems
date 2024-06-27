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
		int range = 0, sol = mat.Sum(x => x[range] + x[^++range]);
		return (mat.Length % 2) == 0 ? sol : sol -= mat[mat.Length / 2][mat.Length / 2];
	}
}
// @lc code=end
