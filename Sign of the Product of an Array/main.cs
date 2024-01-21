public class Solution
{
	readonly int POSITIVE = 1;
	readonly int NEGATIVE = -1;
	private int signFunc(int number) =>  number == 0 ? 0 : (number < 0 ? NEGATIVE : POSITIVE);
    public int ArraySign(int[] nums) => nums.Aggregate(POSITIVE, (acc, next) => acc*=signFunc(next));
}