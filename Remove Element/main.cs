public class Solution
{
	public int RemoveElement(int[] nums, int val)
	{
		int count = 0;
		foreach (int num in nums)
		{
			if (num != val)
			{
				nums[count++] = num;
			}
		}
		return count;
	}
}