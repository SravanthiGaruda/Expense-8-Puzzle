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

class iterativeDeepeningSearchDumpFile():

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
    
    # Used to write the fringe values to the dump file
    def generateValOfQueue(self,queue,f):
        trav_queue = copy.deepcopy(queue)

        while trav_queue:
            matrix_node = trav_queue.popleft()
            f.write("\nState: ")
            f.write(str(matrix_node.currentMatrix))
            f.write(" Action: ")
            f.write(str(matrix_node.action))
            f.write(" cost = ")
            f.write(str(matrix_node.cost))
            f.write(" Level = ")
            f.write(str(matrix_node.level))
        return

    # Main code starts from here!
    def ids(self, startState, goalState, zeroValIndex,depth,f):
        f.write("\nMethod Selected: ids\n")
        f.write("Running ids\n")
        f.write("Checking solution for depth = ")
        f.write(str(depth))
        f.write("\n")
        queue = deque()
        rootMatrixNode = matrixNode(0, zeroValIndex,"null", "null", startState, "Start","null",0)
        queue.append(rootMatrixNode)
        nodes_popped = 0
        nodes_expanded = 0
        nodes_generated = 1
        max_fringe_size = 0
        level = 0

        # Checks the queue till it is empty
        while queue:

            temp_matrixNode = queue.pop()
            zero_index = temp_matrixNode.zeroValIndex
            level = temp_matrixNode.level
            current_matrix = temp_matrixNode.currentMatrix
            cost = temp_matrixNode.cost
            action = temp_matrixNode.action
            parent_matrix = temp_matrixNode.parentMatrix
            changed_tile_val = temp_matrixNode.changed_tile_val
            nodes_popped += 1
            max_fringe_size = max(max_fringe_size, len(queue))
            
            f.write("\nGenerating successors to < state = ")
            f.write(str(current_matrix))
            f.write("\n")
            f.write(str(action))
            f.write("\ncost = ")
            f.write(str(cost))
            f.write("\nd = ")
            f.write(str(level))
            f.write("\nParent = Pointer to ")
            f.write(str(parent_matrix))

            # checks where the current state is equal to goal state or not.
            if goalState == current_matrix:
                f.write("\nNodes Popped: ")
                f.write(str(nodes_popped))
                f.write("\nNodes Expanded: ")
                f.write(str(nodes_expanded))
                f.write("\nNodes Generated: ")
                f.write(str(nodes_generated))
                f.write("\nMax Fringe Size: ")
                f.write(str(max_fringe_size))
                print("Nodes Popped: ",nodes_popped)
                print("Nodes Expanded: ", nodes_expanded)
                print("Nodes Generated: ",nodes_generated)
                print("Max Fringe Size: ",max_fringe_size)
                print("Solution Found at depth ", level," with cost of ", cost)
                print("Steps: ")
                self.printSolutionSteps(temp_matrixNode)
                return 


            if int(level) < int(depth):

                #possible directions the tile can be moved 
                directions = [[-1,0,"Down"],[1,0,"Up"],[0,-1,"Right"],[0,1,"Left"]]
                count = 0
                generated_successors = []
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
                        generated_successors.append(modified_matrix)
                        queue.append(new_matrix_node)
                f.write("\n")
                f.write(str(count))
                f.write(" successors generated\n")
                f.write(" Generated Successors are : \n")
                f.write(str(generated_successors))
                f.write("\nFringe : ")
                f.write(str(self.generateValOfQueue(queue,f)))
                if count > 0:
                    nodes_expanded +=1
                nodes_generated += count
        print("Nodes Popped: ",nodes_popped)
        print("Nodes Expanded: ", nodes_expanded)
        print("Nodes Generated: ",nodes_generated)
        print("Max Fringe Size: ",max_fringe_size)
        return "No Output is possible"