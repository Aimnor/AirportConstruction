# Problem
The tropical island nation of Piconesia is famous for its beautiful beaches, lush vegetation, cocoa and coffee
plantations, and wonderful weather all year round. This paradise is being considered as a future location for
the World Finals of the ACM International Collegiate Programming Contest (or at the very least a vacation
spot for the executive council). There is only one small problem: the island is really hard to reach.
Currently, the fastest way to reach the island takes three days from the nearest airport, and uses a combination
of fishing boat, oil tanker, kayak, and submarine. To make attending the ICPC World Finals slightly easier
and to jump-start the island’s tourism business, Piconesia is planning to build its first airport.
Since longer landing strips can accommodate larger airplanes, Piconesia has decided to build the longest
possible landing strip on their island. Unfortunately, they have been unable to determine where this landing
strip should be located. Maybe you can help?
For this problem we model the boundary of Piconesia as a polygon. Given this polygon, you need to compute
the length of the longest landing strip (i.e., straight line segment) that can be built on the island. The landing
strip must not intersect the sea, but it may touch or run along the boundary of the island. Figure A.1 shows
an example corresponding to the first sample input.

## Input
The input starts with a line containing an integer n (3 < n < 200) specifying the number of vertices of the
polygon. This is followed by n lines, each containing two integers x and y (|x|, |y| < $10^6$ ) that give the
coordinates (x, y) of the vertices of the polygon in counter-clockwise order. The polygon is simple, i.e., its
vertices are distinct and no two edges of the polygon intersect or touch, except that consecutive edges touch
at their common vertex. In addition, no two consecutive edges are collinear.

## Output
Display the length of the longest straight line segment that fits inside the polygon, with an absolute or relative
error of at most $10^{-6}$.
|Sample Input 1|Sample Output 1|
|---|---|
|7 0 20 40 0 40 20 70 50 50 70 30 50 0 50|76.157731059|

|Sample Input 2|Sample Output 2|
|---|---|
|3 0 2017 -2017 -2017 2017 0| 4510.149110617|

# Solution

This problem, simply put, is to find the longest line inside a polygon

I started by analyzing the problems with drawings. I thought about line equations, angles and other analytical geometric stuffs.

After a very quick research on internet I came across this repository:
https://github.com/BradleyWood/Longest-Line-In-Polygon

Witch was build to solve this problem (some files are called "airport" ...)

He came with this postulate:

The longest line inside a polygon must pass through at least two vertices but not necessarily end on a vertex. This rule simplifies runway construction since if we have found a valid line between two vertices we can extend the line on both sides until it intersects with an edge.

I try to found more literature on the subject and specifically something that contradict this postulate and came across none.

## Naive Implementation
So I started first to implement a naive implementation (see naiveImplementation.py) that doesn't take in account the fact that the polygon can have "holes", and with this I had the correct expected outputs for the examples (see test.py).

In order to do that, I simply test every segment build with a combination of two vertices and return the longest. To be more efficient I plot the figure, you can see some in the output directory (in blue the polygon, red all the segments and green the longest one)

After I build an example that doesn't work with this code (see input2 in test.py or outputs/NaiveExampleInput2.png)

To make it work create an virtual environnement, install matplotlib & run test.py (or run it directly on a env with python3 & matplotlib)

For Linux:
``` bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python test.py
```

## Implementation
My plan is so far to use the naive implementation as a base and:
- Detect if the segment is going out of the polygon
- Prolongate the segment if its possible to have the maximum length of this line

For both of those feature we need to calculate the intersection between the current segment and every other vertices in the polygon.

In a plane, every line can be represent by the equation ax + b = y.

So:
1. I calculate the equation of each vertices: $a_{v}$ $x$ + $b_{v}$ = $y$ with:
    - $a_{v}$ = ($y_{r}$ - $y_{l}$) / ($x_{r}$ - $x_{l}$)
    - $b_{v}$ = $y_{l}$ - $a_{v}$ $x_{l}$

2. For each candidate (those from the naive algorithm) I calculate their line equation: $a_{current}$ $x$ + $b_{current}$ = $y$

3.
    1. If $a_{v}$ = $a_{current}$ then either the line are parallel, either they are coincident and we can ignore this case (continue)
    2. If not we calculate the intersection point. If it is in the vertice, then we calculate this length and keep it, it will be our reference and for a candidate we must find the minimum (the first intersection with the polygon)

This is my state of mind after roughly 2/3 hours of search

For me, the must important method that I currently didn't have time to think about but is most needed is:
 *How to know if I can continue my segment ?* or *How to know if I am still in the polygon ?*

Indeed If I have this method I can use it in 3.2 in order to avoid a wrong extension.
I have some leads, I found this wikipedia page that explains this problem: https://en.wikipedia.org/wiki/Point_in_polygon

But mainly I found a python lib that seems to have all the correct functions to solve this problem:
https://shapely.readthedocs.io/en/stable/

Especially the "within" method:
https://shapely.readthedocs.io/en/latest/reference/shapely.within.html?highlight=within#shapely.within

# Précisions
Pour cette partie j'utilise le français pour la rédaction car je suis quand même plus à l'aise dans cette langue. Je pourrais faire l'exercice de l'écrire en anglais mais cela me demanderait plus de temps.

Je pense avoir passé un peu plus de 3h afin d'avoir un état de réflexion assez "satisfaisant" pour moi. C'est à dire avoir pris le temps de m'approprier l'exercice (reformulation du problème, tracé de figure d'exemple) et trouvé une façon propre de résoudre l'exercice + la rédaction de cette solution. Je n'ai également pas passé 3h d'affilée à le faire, j'aime bien réfléchir à un problème et par exemple aller faire autre chose afin de réfléchir en "tâche de fond" sur le problème.

Ce qui m'a conduit à avoir des réflexions annexes sur le problème:
Cet énoncé est une simplification d'un problème plus complexe. Dans le cas d'une construction d'aéroport il faut prendre en compte la topologie c'est à dire par exemple :
- sortir les x plus grands tracés pour que des géomaîtres étudient des alternatives ?
- pouvoir penser à étendre l'aéroport sur la mer plutôt que de forer à travers une montagne ? (c'est à dire avoir une surface 3d avec le niveau de la mer à la place d'un simple polygone)

Ce n'est qu'un exemple de paramètre parmi bien d'autres bien sûr.