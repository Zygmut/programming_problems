/*
 * @lc app=leetcode id=1964 lang=csharp
 *
 * [1964] Find the Longest Valid Obstacle Course at Each Position
 */

using System;
using System.Collections.Generic;

// @lc code=start

public class Solution
{
	public int[] LongestObstacleCourseAtEachPosition(int[] obstacles)
	{
		int[] sol = new int[obstacles.Length];
		List<int> lis = new List<int>();

		for (int i = 0; i < obstacles.Length; i++)
		{
			if (lis.Count == 0 || obstacles[i] >= lis[lis.Count - 1])
			{
				lis.Add(obstacles[i]);
				sol[i] = lis.Count;
				continue;
			}

			int idx = lis.BinarySearch(obstacles[i]);
			if (idx < 0)
			{
				lis[~idx] = obstacles[i];
				idx = ~idx;
			}
			else
			{
				idx = lis.LastIndexOf(obstacles[i]) + 1;
				lis[idx] = obstacles[i];
			}

			sol[i] = idx + 1;
		}

		return sol;
	}
}
// @lc code=end
