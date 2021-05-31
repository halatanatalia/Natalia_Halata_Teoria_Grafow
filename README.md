# Graph Theory - Ford Fulkerson's algorithm and solved tasks for an example graph

1. "Natalia_Hałata_TG_część_analityczna.pdf" - file containig first part of the project
2. "main.py" and "example.json" - files containig second part of the project. 

## Requirements

To properly use the algorithm, you must use a JSON file, in a format like this:   

  s - start of an edge - number
  e - end of an edge - number
  w - weight of an edge - number
```
[
  [s1, e1, w1],
  [s2, e2, w2],
       ...
       ...
       ...
  [sn, en, wn],
  [source, sink]
]
```
Source and sink numbers must be smaller than the amount of vertices(as we start with 0 and finish with v - 1).
Example of the correct JSON file is included as "example.json" and the algorithm may tested on it.

## Results

The result is a number of maximum flow in the given graph from source to sink.  

## Use of the Ford Fulkerson's algorithm:

1. In telecommunication - used by shipping companies, airlines and cities in infrastructure planning
2. In finance - analyze and solve problems that may occur in financial contagion, finding projects whose total profit would be as large as possible.
3. In bussiness - used for appropriate distribution of the tasks, members or teams
4. Baseball Elimination Problem - figuring out which teams are eliminated based on the fixtures remaining. While this may seem trivial, this problem is much more complex than it looks on the surface.
Some problems were solved were solved by this algorithm, but within the time, the Goldberg and Tarjan's algorithm, Dinitz's algorithm etc. replace it. 

### Source
https://digitalcommons.georgiasouthern.edu/cgi/viewcontent.cgi?article=2720&context=etd
http://www.jistm.com/PDF/JISTM-2017-04-06-02.pdf
https://en.wikipedia.org/wiki/Ford–Fulkerson_algorithm
https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/
