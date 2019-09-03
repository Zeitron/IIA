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
        state, 'direcao' is the action required to get there, and 'stepCost' is
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

    from util import Stack

    print("Determino o ponto inicial:", problem.getStartState())
    print("Estou no objetivo?", problem.isGoalState(problem.getStartState()))
    print("Quais sao os \"vizinhos\":", problem.getSuccessors
    (problem.getStartState()))

    atual = problem.getStartState()
    anterior = None
    percorrido = [(atual)]
    """*************************************************************************

        Define a variavel no e seta valores da posicao atual, posicao anterior,
    direcao e se ja percorreu o caminho

    *************************************************************************"""
    no = []
    no.append({'posicao atual': atual, 'posicao anterior': None, 'direcao': None,
     'percorrido?': False})

    stack = Stack()
    stack.push(atual)

    """************************************************************************

            Le a posicao do no atual e adiciona o no na lista de nos, posterior-
        mente ele retira eles da lista de nos e marca que ja percorreu esse no

    *************************************************************************"""

    while not stack.isEmpty():
        atual = stack.pop()
        percorrido.append((atual))

        lista_no = []
        for node in no:
            if node['posicao atual'] == atual:
                lista_no.append(node)

        if len(lista_no) > 1:
            for node in lista_no:
                if node['posicao anterior'] == anterior:
                    node['percorrido?'] = True
        else:
            lista_no[0]['percorrido?'] = True

        anterior = atual
    """************************************************************************

            Caso ele tenha chegado no objetivo ele para de procurar o caminho

    *************************************************************************"""
        if problem.isGoalState(atual):
            break

        successors = problem.getSuccessors(atual)
        for successor in successors:
            if successor[0] not in percorrido:
                no.append({'posicao atual': successor[0],
                 'posicao anterior': atual, 'direcao': successor[1],
                 'percorrido?': False})
                stack.push(successor[0])
    menor_caminho = []
    caminho = no[-1]
    """*************************************************************************

            O caminho é feito a partir do no final ate o no inicial

    *************************************************************************"""
    while caminho:
        if not caminho['posicao anterior']:
            break
        menor_caminho.insert(0, caminho['direcao'])
        caminho = next((item for item in no if item['posicao atual'] ==
        caminho['posicao anterior'] and item['percorrido?'] ), None)

    return menor_caminho


def aStarSearch(problem, heuristic=nullHeuristic):

    from util import PriorityQueue

    print("Determino o ponto inicial:", problem.getStartState())
    print("Estou no objetivo?", problem.isGoalState(problem.getStartState()))
    print("Quais sao os \"vizinhos\":", problem.getSuccessors
    (problem.getStartState()))

    atual = problem.getStartState()
    percorrido = []

    """*************************************************************************

            Define a variavel no e seta os valores de no-anterior, ação e percu-
        so para nulo, tal como o custo.

    *************************************************************************"""

    no = []
    no.append({'posicao atual': atual, 'posicao anterior': None, 'direcao': None,
    'percorrido?': False, custo: 0})

    stack = PriorityQueue()
    stack.push(atual,0)


    """*************************************************************************

            O caminho é o ponto atual do no usado para achar o destino final

    *************************************************************************"""

    caminho = None

    while not stack.isEmpty():
        atual = stack.pop()
        if atual in percorrido:
            continue

        percorrido.append(atual)

        potentialNodes = []
        for node in no:
            if node['posicao atual'] == atual:
                potentialNodes.append(node)

    """*************************************************************************

            Com base nas atividades ministradas em aula o algoritmo A* sempre
        viaja para o No de menor custo, o que caso depende da heuristica usada.

    *************************************************************************"""


        if len(potentialNodes) > 1:
            smallNode = potentialNodes[0]
            for node in potentialNodes:
                if smallNode[custo] > node[custo]:
                    smallNode = node
            currNode = smallNode
        else:
            currNode = potentialNodes[0]

        currNode['percorrido?'] = True

    """*************************************************************************

            Quebra o laço caso tenha chegado ao objetivo, e entao comeca a calcu-
        lar o "melhor" custo para o trajeto.

    *************************************************************************"""

        if problem.isGoalState(atual):
            caminho = currNode
            break

    """*************************************************************************

            Trexo que é calculado custo para chegar somado ao custo da Heuristica

    *************************************************************************"""
        successors = problem.getSuccessors(atual)
        for successor in successors:
            if successor[0] not in percorrido:
                costSoFar = successor[2] + currNode[custo]
                costPlusHeuristic = costSoFar + heuristic(successor[0],problem)
                no.append({'posicao atual': successor[0],
                'posicao anterior': atual, 'direcao': successor[1],
                'percorrido?': False, custo: costSoFar })
                stack.push(successor[0],costPlusHeuristic)

    path = []
    while caminho:
        if not caminho['posicao anterior']:
            break
        path.insert(0, caminho['direcao'])
        potentialPath = []
        for node in no:
            if node['posicao atual'] == caminho['posicao anterior']
            and node['percorrido?']:
                potentialPath.append(node)

        if len(potentialPath) > 1:
            caminho = potentialPath[0]
            for path in potentialPath:
                if caminho[custo] > path[custo]:
                    caminho = path
        else:
            caminho = potentialPath[0]

    return path


# Abbreviations
"""*************************************************************************

        As abreviações não utilizadas foram comentadas

*************************************************************************"""

"bfs = breadthFirstSearch"
dfs = depthFirstSearch
astar = aStarSearch
"ucs = uniformCostSearch"
