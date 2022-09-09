# The Number of Weak Characters in the Game

You are playing a game that contains multiple characters, and each of the characters has **two** main properties: **attack** and **defense**. You are given a 2D integer array ```properties``` where ```properties[i]``` = [ $\text{attack}_i$, $\text{defense}_i$ ] represents the properties of the $\text{i}^{th}$ character in the game.

A character is said to be **weak** if any other character has **both** attack and defense levels **strictly greater** than this character's attack and defense levels. More formally, a character i is said to be **weak** if there exists another character ```j``` where $\text{attack}_j > \text{attack}_i$ and $\text{defense}_j > \text{defense}_i$ .

_Return the number of **weak** characters._

## Examples

### Example 1

```txt
Input: properties = [[5,5],[6,3],[3,6]]
Output: 0
Explanation: No character has strictly greater attack and defense than the other.
```

### Example 2

```txt
Input: properties = [[2,2],[3,3]]
Output: 1
Explanation: The first character is weak because the second character has a strictly greater attack and defense.
```

### Example 3

```txt
Input: properties = [[1,5],[10,4],[4,3]]
Output: 1
Explanation: The third character is weak because the second character has a strictly greater attack and defense.
```

## Constraints

- 2 <= ```properties.length``` <= $10^5$
- ```properties[i].length``` == 2
- 1 <= $\text{attack}_i$ , $\text{defense}_i$ <= $10^5$
