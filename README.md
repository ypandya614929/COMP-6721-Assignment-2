# COMP-6721-Assignment-2
COMP-6721-Assignment-2

## To setup virtualenv if not already
    
    virtualenv -p python3.6 env
    source env/bin/activate
    pip install -r requirements.txt


### Assignment-2 Commands
    - python autograder.py -q q1
    - python autograder.py -q q2
    - python autograder.py -q q3
    - python autograder.py -q q4
    - python autograder.py -q q5
    - python autograder.py -q q7
    - python autograder.py -q q8

	- python autograder.py


#### Note
    There is one terminal/cmd output file 'autograder_out.txt' which shows the grading and 
    result of test cases.


### Game Play Commands
    
#### Question:1
    python pacman.py -l tinyMaze -p SearchAgent
    python pacman.py -l mediumMaze -p SearchAgent
    python pacman.py -l bigMaze -z .5 -p SearchAgent

#### Question:2
    python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
    python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5

#### Question:3
    python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
    python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
    python pacman.py -l mediumScaryMaze -p StayWestSearchAgent

#### Question:4
    python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic

#### Question:5
    python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
    python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem

#### Question:7
    python pacman.py -l testSearch -p AStarFoodSearchAgent
    python pacman.py -l trickySearch -p AStarFoodSearchAgent

#### Question:8
    python pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5