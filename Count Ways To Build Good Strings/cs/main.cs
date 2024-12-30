/*
 * @lc app=leetcode id=2466 lang=csharp
 *
 * [2466] Count Ways To Build Good Strings
 */

using System.Collections.Generic;
// @lc code=start
public class Solution
{
	public const int mod = 1000000007;
	public int CountGoodStrings(int low, int high, int zero, int one)
	{
		int[] memo = new int[high + 1];
		memo[0] = 1;

		for (int i = 1; i <= high; i++)
		{
			if (i - zero >= 0)
				memo[i] += memo[i - zero];

			if (i - one >= 0)
				memo[i] += memo[i - one];

			memo[i] %= mod;
		}

		int result = 0;
		for (int i = low; i <= high; i++)
			result = (result + memo[i]) % mod;

		return result;
	}

}
// @lc code=end
