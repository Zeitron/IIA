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


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0



"Primeiro trabalho de IIA - UnB"
"Paulo Mauricio Costa Lopes, 18/0112520"
"Gabriel de Sousa Vieira,    16/0006350"

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
    """
    "*** YOUR CODE HERE ***"

    from util import Stack

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    current = problem.getStartState()
    previous = None
    explored = [(current)]

    "Define a variavel no e seta valores de anterior ação e percuso"
    no = []
    no.append({'Current': current, 'Previous': None, 'Action': None, 'Traveled': False})

    stack = Stack()
    stack.push(current)

    while not stack.isEmpty():
        current = stack.pop()
        explored.append((current))

        currNode = []
        for node in no:
            if node['Current'] == current:
                currNode.append(node)

        if len(currNode) > 1:
            for node in currNode:
                if node['Previous'] == previous:
                    node['Traveled'] = True
        else:
            currNode[0]['Traveled'] = True

        previous = current
        "caso ele tenha chegado no objetivo ele para de procurar o caminho"
        if problem.isGoalState(current):
            break

        successors = problem.getSuccessors(current)
        for successor in successors:
            if successor[0] not in explored:
                no.append({'Current': successor[0], 'Previous': current, 'Action': successor[1], 'Traveled': False})
                stack.push(successor[0])
    path = []
    caminho = no[-1]
    """
    Path tracing from the goal/end node to the starting node using previous
    """
    while caminho:
        """print ("caminho = ", caminho)"""
        if not caminho['Previous']:
            break
        path.insert(0, caminho['Action'])
        caminho = next((item for item in no if item['Current'] == caminho['Previous'] and item['Traveled'] ), None)

    return path


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"


    from util import PriorityQueue

    current = problem.getStartState()
    explored = []

    "Define a variavel no e seta os valores de no-anterior, ação e percuso para nulo, tal como o custo"

    no = []
    no.append({'Current': current, 'Previous': None, 'Action': None, 'Traveled': False, 'Cost': 0})

    stack = PriorityQueue()
    stack.push(current,0)

    """
    caminho is the current node used in path tracing
    """
    caminho = None

    while not stack.isEmpty():
        current = stack.pop()
        if current in explored:
            continue

        explored.append(current)

        potentialNodes = []
        for node in no:
            if node['Current'] == current:
                potentialNodes.append(node)

        """
        Com base nas atividades ministradas em aula o algoritmo A* sempre
        viaja para o No de menor custo
        """

        if len(potentialNodes) > 1:
            smallNode = potentialNodes[0]
            for node in potentialNodes:
                if smallNode['Cost'] > node['Cost']:
                    smallNode = node
            currNode = smallNode
        else:
            currNode = potentialNodes[0]

        currNode['Traveled'] = True

        " Caso o no atual seja o no de objetivo ele para o caminho"

        if problem.isGoalState(current):
            caminho = currNode
            break

        successors = problem.getSuccessors(current)
        for successor in successors:
            if successor[0] not in explored:
                costSoFar = successor[2] + currNode['Cost']
                costPlusHeuristic = costSoFar + heuristic(successor[0],problem)
                no.append({'Current': successor[0], 'Previous': current, 'Action': successor[1],
                 'Traveled': False, 'Cost': costSoFar })
                stack.push(successor[0],costPlusHeuristic)

    """
    Path tracing from the goal/end node to the starting node using previous
    """
    path = []
    while caminho:
        if not caminho['Previous']:
            break
        path.insert(0, caminho['Action'])
        potentialPath = []
        for node in no:
            if node['Current'] == caminho['Previous'] and node['Traveled']:
                potentialPath.append(node)

        if len(potentialPath) > 1:
            caminho = potentialPath[0]
            for path in potentialPath:
                if caminho['Cost'] > path['Cost']:
                    caminho = path
        else:
            caminho = potentialPath[0]

    return path


# Abbreviations
"bfs = breadthFirstSearch"
dfs = depthFirstSearch
astar = aStarSearch
"ucs = uniformCostSearch"
