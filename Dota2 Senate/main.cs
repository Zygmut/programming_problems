public class Solution
{
	public string PredictPartyVictory(string senate)
	{

		int acumulator = 0;
		Queue<int> radiantSenate = new Queue<int>();
		Queue<int> direSenate = new Queue<int>();
		foreach (char senator in senate)
		{
			if (senator == 'R')
			{
				radiantSenate.Enqueue(acumulator++);
			}
			else
			{
				direSenate.Enqueue(acumulator++);
			}
		}

		while (radiantSenate.Count != 0 && direSenate.Count != 0)
		{
			int radiantSenatorPosition = radiantSenate.Dequeue();
			int direSenatorPosition = direSenate.Dequeue();
			if (radiantSenatorPosition < direSenatorPosition)
			{
				radiantSenate.Enqueue(acumulator++);
			}
			else
			{
				direSenate.Enqueue(acumulator++);
			}
		}

		return radiantSenate.Count != 0 ? "Radiant" : "Dire";
	}

}