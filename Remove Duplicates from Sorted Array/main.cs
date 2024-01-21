public class Solution
{
	public int RemoveDuplicates(int[] nums)
	{
		int count = 1;
		foreach (int num in nums)
		{
			if (nums[count - 1] != num)
			{
				nums[count++] = num;
			}
		}
		return count;
	}
}