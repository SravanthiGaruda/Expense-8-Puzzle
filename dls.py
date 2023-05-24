from collections import deque 
import copy

# matrixNode class is used to create node of the current state of 8 puzzle which consists of the following:
# Level - defines the depth of the node from the root node.
# zeroValIndex - Provides with the "0" value position
# matrix - node which consists of all the details.
# parentMatrix - parent state of the current state in 8 puzzle problem (for root node the parent matrix is null)
# currentMatrix - current state of the 8 puzzle problem 
# action - Action which is being performed to move the tile.
# changed_tile_val - Value of the tile which is being changed.
# cost - g(n)
class matrixNode:
    
    def __init__(self, level, zeroValIndex, matrix,parentMatrix, currentMatrix, action, changed_tile_val, cost):
        self.level = level
        self.zeroValIndex = zeroValIndex
        self.matrix = matrix
        self.parentMatrix = parentMatrix
        self.currentMatrix = currentMatrix
        self.action = action
        self.changed_tile_val = changed_tile_val
        self.cost = cost

class depthLimitedSearch():

    # Function checks whether the tile can move in that direction or not. If it cannot move then returns False else True
    def directionIsSafe(self,checkIndex):
        if checkIndex[0] >=0 and checkIndex[0]<3 and checkIndex[1] >=0 and checkIndex[1]<3:
            return True
        return False

    #Generates modified matrix if the tile direction move is safe by swapping the values for the moved state.
    def generateMatrixWithMove(self,matrix,zero_index, new_zero_index):

        temp_matrix = matrix
        temp_matrix[zero_index[0]][zero_index[1]], temp_matrix[new_zero_index[0]][new_zero_index[1]] = temp_matrix[new_zero_index[0]][new_zero_index[1]], temp_matrix[zero_index[0]][zero_index[1]]
        return temp_matrix

    # Prints the steps once solution is found
    def printSolutionSteps(self,matrixRootNode):

        if matrixRootNode.matrix == "null":
            return

        self.printSolutionSteps(matrixRootNode.matrix)
        print(matrixRootNode.action)

    # Main code starts from here!
    def dls(self, startState, goalState, zeroValIndex,depth):
        queue = deque()
        rootMatrixNode = matrixNode(0, zeroValIndex,"null", "null", startState, "Start","null",0)
        queue.append(rootMatrixNode)
        nodes_popped = 0
        nodes_expanded = 0
        nodes_generated = 1
        max_fringe_size = 1
        level = 0
        
        # Checks the queue till it is empty
        while queue:
            max_fringe_size = max(max_fringe_size, len(queue))
            temp_matrixNode = queue.pop()
            zero_index = temp_matrixNode.zeroValIndex
            level = temp_matrixNode.level
            current_matrix = temp_matrixNode.currentMatrix
            cost = temp_matrixNode.cost
            changed_tile_val = temp_matrixNode.changed_tile_val
            nodes_popped += 1
            

            # checks where the current state is equal to goal state or not.
            if goalState == current_matrix:
                print("Nodes Popped: ",nodes_popped)
                print("Nodes Expanded: ", nodes_expanded)
                print("Nodes Generated: ",nodes_generated)
                print("Max Fringe Size: ",max_fringe_size)
                print("Solution Found at depth ", level," with cost of ", cost)
                print("Steps: ")
                self.printSolutionSteps(temp_matrixNode)
                return 

            #Checking if the current state level is equal to the depth specified
            if int(level) == int(depth):
                continue

            #possible directions the tile can be moved 
            directions = [[0,1,"Left"],[1,0,"Up"],[0,-1,"Right"],[-1,0,"Down"]]
            count = 0
            for i in range(len(directions)):
                new_zero_index = []
                new_zero_index.append(zero_index[0] + directions[i][0])
                new_zero_index.append(zero_index[1] + directions[i][1])
                new_zero_index.append(directions[i][2])

                #Checking if the direction is safe or not
                if self.directionIsSafe(new_zero_index):
                        
                    modified_matrix = copy.deepcopy(current_matrix)
                    modified_matrix = self.generateMatrixWithMove(modified_matrix,zero_index,new_zero_index)
                    changed_tile_val = current_matrix[new_zero_index[0]][new_zero_index[1]]
                    new_action_val = "Move " + changed_tile_val + " " +new_zero_index[2]
                    new_cost = cost + int(changed_tile_val)
                    new_matrix_node = matrixNode(level+1,new_zero_index,temp_matrixNode,current_matrix,modified_matrix,new_action_val, changed_tile_val,new_cost)
                    count += 1
                    queue.append(new_matrix_node)
            if count>0:
                nodes_expanded +=1
            nodes_generated += count
        print("Nodes Popped: ",nodes_popped)
        print("Nodes Expanded: ", nodes_expanded)
        print("Nodes Generated: ",nodes_generated)
        print("Max Fringe Size: ",max_fringe_size)
        return "No Output is possible"