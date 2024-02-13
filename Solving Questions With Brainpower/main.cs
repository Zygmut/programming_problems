/*
 * @lc app=leetcode id=2140 lang=csharp
 *
 * [2140] Solving Questions With Brainpower
 */

using System;
// @lc code=start
public class Solution
{
	public long MostPoints(int[][] questions)
	{
		const int n = questions.Length;
		long[] memo = new long[n + 1];

		for (int i = n - 1; i >= 0; i--)
		{
			memo[i] = Math.Max(memo[i + 1], questions[i][0] + memo[Math.Min(n , 1 + i + questions[i][1])]);
		}

		return memo[0];
	}
}
// @lc code=end
