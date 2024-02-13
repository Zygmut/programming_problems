public class Solution
{

	public bool isVowel(char character) =>
		('a' == character)
		|| ('e' == character)
		|| ('i' == character)
		|| ('o' == character)
		|| ('u' == character);

	public int MaxVowels(string s, int k)
	{
		int vowel_count = 0;
		int max_vowels = 0;
		for (int i = 0; i < k; i++)
		{
			if (isVowel(s[i]))
			{
				vowel_count++;
			}
		}

		max_vowels = vowel_count;

		for (int i = k; i < s.Length; i++)
		{
			if (isVowel(s[i])) vowel_count++;
			if (isVowel(s[i - k])) vowel_count--;
			max_vowels = Math.Max(max_vowels, vowel_count);
			if (max_vowels == k)
			{
				return max_vowels;
			}
		}
		return max_vowels;

	}
}
