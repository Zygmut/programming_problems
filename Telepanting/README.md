# Telepanting

An ant moves on the real line with constant speed of **1** unit per second. It starts at **0** and always moves to the right (so its position increases by **1** each second).

There are **n** portals, the **i**-th of which is located at position $x_i$ and teleports to position $y_i < x_i$. Each portal can be either _active_ or _inactive_. The initial state of the **i**-th portal is determined by $s_i$: if $s_i=0$ then the **i**-th portal is initially _inactive_, if $s_i=1$ then the **i**-th portal is initially _active_. When the ant travels through a portal (i.e., when its position coincides with the position of a portal):

if the portal is _inactive_, it becomes _active_ (in this case the path of the ant is not affected);
if the portal is _active_, it becomes _inactive_ and the ant is instantly teleported to the position $y_i$, where it keeps on moving as normal.

How long (from the instant it starts moving) does it take for the ant to reach the position $x_n+1$? It can be shown that this happens in a finite amount of time. Since the answer may be very large, compute it modulo **998244353**.

## Input

The first line contains the integer n (1≤n≤2⋅ $10^5$ ) — the number of portals.

The **i**-th of the next n lines contains three integers $x_i$, $y_i$ and $s_i$ (1≤ $y_i$ < $x_i$ ≤ $10^9$ , $s_i$ ∈{0,1}) — the position of the **i**-th portal, the position where the ant is teleported when it travels through the **i**-th portal (if it is active), and the initial state of the **i**-th portal.

The positions of the portals are strictly increasing, that is $x_1$ < $x_2$ <⋯< $x_n$ . It is guaranteed that the 2n integers $x_1$ , $x_2$ ,…, $x_n$ , $y_1$ , $y_2$ ,…, $y_n$ are all distinct.

## Output

Output the amount of time elapsed, in seconds, from the instant the ant starts moving to the instant it reaches the position $x_n+1$. Since the answer may be very large, output it modulo **998244353**.

## Examples

### Example 1

```txt
Input:
1
454971987 406874902 1

Output:
503069073
```

### Example 2

```txt
Input:
4
3 2 0
6 5 1
7 4 0
8 1 1

Output:
23
```

### Example 3

```txt
Input:
5
243385510 42245605 0
644426565 574769163 0
708622105 208990040 0
786625660 616437691 0
899754846 382774619 0

Output:
899754847
```

### Example 4

```txt
Input:
5
200000000 100000000 1
600000000 400000000 0
800000000 300000000 0
900000000 700000000 1
1000000000 500000000 0

Output:
3511295
```
