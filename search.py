# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    Algorithm Logic
    ---------------
    Insert root state into states stack, iterate thorough stack till it becomes empty or goal state is reached,
    extract top most state of the stack, check if the current state is goal state or not,
    return list of actions if the current state is a goal state, otherwise, insert current state
    into list of visited states. For current state iterate through all its successors and check
    if next state of successor state is visited or not, if not visited then, add action of current state
    into list of actions, add current successor state into states stack and repeat the flow.
    return list of actions if stack is empty or goal state is not found.
    """

    states = util.Stack()  # DFS states
    visited_states = set()  # To maintain visited states
    actions = []   # To return actions from which goal state is arrived
    states.push((problem.getStartState(), []))
    while not states.isEmpty():
        current_state, current_state_actions = states.pop()
        if problem.isGoalState(current_state):
            actions = current_state_actions
            break
        if current_state not in visited_states:
            visited_states.add(current_state)
            for successor in problem.getSuccessors(current_state):
                successor_state, successor_action, successor_cost = successor
                if successor_state not in visited_states:
                    successor_combined_actions = current_state_actions + [successor_action]
                    states.push((successor_state, successor_combined_actions))
    return actions


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first.

    Algorithm Logic
    ---------------
    Insert root state into states queue, iterate thorough queue till it becomes empty or goal state is reached,
    extract top most state of the queue, check if the current state is goal state or not,
    return list of actions if the current state is a goal state, otherwise, insert current state
    into list of visited states. For current state iterate through all its successors and check
    if next state of successor state is visited or not, if not visited then, add action of current state
    into list of actions, add current successor state into states queue and repeat the flow.
    return list of actions if queue is empty or goal state is not found.
    """

    states = util.Queue()  # BFS states
    visited_states = set()  # To maintain visited states
    actions = []  # To return actions from which goal state is arrived
    states.push((problem.getStartState(), []))
    while not states.isEmpty():
        current_state, current_state_actions = states.pop()
        if problem.isGoalState(current_state):
            actions = current_state_actions
            break
        if current_state not in visited_states:
            visited_states.add(current_state)
            for successor in problem.getSuccessors(current_state):
                successor_state, successor_action, successor_cost = successor
                if successor_state not in visited_states:
                    successor_combined_actions = current_state_actions + [successor_action]
                    states.push((successor_state, successor_combined_actions))
    return actions


def uniformCostSearch(problem):
    """Search the node of least total cost first.

    Algorithm Logic
    ---------------
    Insert root state into states PriorityQueue, iterate thorough PriorityQueue till it becomes empty or goal state
    is reached, extract top most state of the PriorityQueue, check if the current state is goal state or not,
    return list of actions if the current state is a goal state, otherwise, insert current state
    into list of visited states. For current state iterate through all its successors and check
    if next state of successor state is visited or not, if not visited then, add action of current state
    into list of actions, calculate priority value based on the current state cost and successor cost, add current
    successor state into states PriorityQueue and repeat the flow.
    return list of actions if PriorityQueue is empty or goal state is not found.
    """

    states = util.PriorityQueue()  # UCS states
    visited_states = set()  # To maintain visited states
    actions = []  # To return actions from which goal state is arrived
    start_state = (problem.getStartState(), [], 0)
    states.push(start_state, 0)
    while not states.isEmpty():
        current_state, current_state_actions, current_state_cost = states.pop()
        if problem.isGoalState(current_state):
            actions = current_state_actions
            break
        if current_state not in visited_states:
            visited_states.add(current_state)
            for successor in problem.getSuccessors(current_state):
                successor_state, successor_action, successor_cost = successor
                if successor_state not in visited_states:
                    priority_val = current_state_cost + successor_cost
                    successor_combined_actions = current_state_actions + [successor_action]
                    new_state = (successor_state, successor_combined_actions, priority_val)
                    states.update(new_state, priority_val)
    return actions


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first.

    Algorithm Logic
    ---------------
    Insert root state into states PriorityQueue, iterate thorough PriorityQueue till it becomes empty or goal state
    is reached, extract top most state of the PriorityQueue, check if the current state is goal state or not,
    return list of actions if the current state is a goal state, otherwise, insert current state
    into list of visited states. For current state iterate through all its successors and check
    if next state of successor state is visited or not, if not visited then, add action of current state
    into list of actions, calculate heuristic value based on the current state cost, successor cost and based on
    heuristic function's value depending on successor's state and problem, add current successor state into
    states PriorityQueue and repeat the flow.
    return list of actions if PriorityQueue is empty or goal state is not found.
    """

    states = util.PriorityQueue()  # UCS states
    visited_states = set()  # To maintain visited states
    actions = []  # To return actions from which goal state is arrived
    start_state = (problem.getStartState(), [], 0)
    states.push(start_state, 0)
    while not states.isEmpty():
        current_state, current_state_actions, current_state_cost = states.pop()
        if problem.isGoalState(current_state):
            actions = current_state_actions
            break
        if current_state not in visited_states:
            visited_states.add(current_state)
            for successor in problem.getSuccessors(current_state):
                successor_state, successor_action, successor_cost = successor
                if successor_state not in visited_states:
                    new_state_cost = current_state_cost + successor_cost
                    heuristic_val = new_state_cost + heuristic(successor_state, problem)
                    successor_combined_actions = current_state_actions + [successor_action]
                    new_state = (successor_state, successor_combined_actions, new_state_cost)
                    states.update(new_state, heuristic_val)
    return actions


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
