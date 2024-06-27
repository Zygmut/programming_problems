public class Solution
{
	public IList<IList<int>> FindDifference(int[] nums1, int[] nums2) =>
		new[] {
			nums1.Except(nums2).ToList(),
			nums2.Except(nums1).ToList(),
		};
}
