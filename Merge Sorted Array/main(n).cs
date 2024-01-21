public class Solution {
    public void Merge(int[] nums1, int m, int[] nums2, int n)
			{
		int endIndex = nums1.Length - 1;
		int nums1Iter = m - 1;
		int nums2Iter = n - 1;
		while (nums2Iter >= 0)
		{
			if (nums1Iter >= 0 && nums1[nums1Iter] > nums2[nums2Iter])
			{
				nums1[endIndex--] = nums1[nums1Iter--];
			} else
			{
				nums1[endIndex--] = nums2[nums2Iter--];
			}
		}
	}
}