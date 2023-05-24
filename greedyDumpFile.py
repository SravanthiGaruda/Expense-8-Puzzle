from collections import deque 
import copy
import heapq

# matrixNode class is used to create node of the current state of 8 puzzle which consists of the following:
# Level - defines the depth of the node from the root node.
# zeroValIndex - Provides with the "0" value position
# matrix - node which consists of all the details.
# parentMatrix - parent state of the current state in 8 puzzle problem (for root node the parent matrix is null)
# currentMatrix - current state of the 8 puzzle problem 
# action - Action which is being performed to move the tile.
# changed_tile_val - Value of the tile which is being changed.
# cost_fn - h(n) 
class matrixNode:
    
    def __init__(self, level, zeroValIndex, matrix, parentMatrix, currentMatrix, action, changed_tile_val, cost_fn):
        self.level = level
        self.zeroValIndex = zeroValIndex
        self.matrix = matrix
        self.parentMatrix = parentMatrix
        self.currentMatrix = currentMatrix
        self.action = action
        self.changed_tile_val = changed_tile_val
        self.cost_fn = cost_fn
        # self.cost_gn = cost_gn
    
    # Used to sort the elements in fridge from greatest to lowest f(n) cost
    def __lt__(self, cost):  
        return self.cost_fn < cost.cost_fn 

class greedyMethodDumpFile():

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
    
    # Finds the index position of the values in tile
    def findIndex(self,val,matrix):

        for i in range(3):
            for j in range(3):
                if val == int(matrix[i][j]):
                    return [i,j]

    # Generates h(n) value - manhattan distance
    def generateCostFunction(self,current_matrix,goalState):

        manhattan_distance = 0
        for i in range(0,9):
            [x1,y1] = self.findIndex(i,current_matrix)
            [x2,y2] = self.findIndex(i,goalState)
            manhattan_distance += (abs(x1-x2)+abs(y1-y2))*i
        return manhattan_distance

    # Used to write the fringe values to the dump file
    def generateValOfHeap(self,heap,f):
        trav_heap = copy.deepcopy(heap)

        while trav_heap:
            matrix_node = heapq.heappop(trav_heap)
            f.write("\nState: ")
            f.write(str(matrix_node.currentMatrix))
            f.write(" Action: ")
            f.write(str(matrix_node.action))
            f.write(" F(n) = ")
            f.write(str(matrix_node.cost_fn))
            f.write(" G(n) = ")
            # f.write(str(matrix_node.cost_gn))
        return

    # Prints the steps once solution is found
    def printSolutionSteps(matrixRootNode):

        if matrixRootNode == "null":
            return

        greedyMethodDumpFile.printSolutionSteps(matrixRootNode.matrix)  
        if matrixRootNode.action != "Start":
            print(matrixRootNode.action)

    # Main code starts from here!
    def greedy(self, startState, goalState, zeroValIndex,f):

        f.write("Method Selected: greedy")
        f.write("\nRunning greedy")
        f.write("\n")
        heap = []
        closed_set = []
        cost_fn = self.generateCostFunction(startState,goalState) 
        rootMatrixNode = matrixNode(0, zeroValIndex, "null","null", startState, "Start","null",cost_fn)
        heapq.heappush(heap, rootMatrixNode)
        nodes_popped = 0
        nodes_expanded = len(closed_set)
        nodes_generated = 1
        max_fringe_size = 0

        # Checks the heap till it is empty
        while heap:
            temp_matrixNode = heapq.heappop(heap)
            zero_index = temp_matrixNode.zeroValIndex
            level = temp_matrixNode.level
            action = temp_matrixNode.action
            current_matrix = temp_matrixNode.currentMatrix
            parent_matrix = temp_matrixNode.parentMatrix
            cost_fn = temp_matrixNode.cost_fn
            nodes_popped += 1
            max_fringe_size = max(max_fringe_size, len(heap))

            f.write("\nGenerating successors to < state = ")
            f.write(str(current_matrix))
            f.write("\n")
            f.write(str(action))
            f.write(" F(n) = ")
            f.write(str(cost_fn))
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
                print("Solution Found at depth ", level," with cost of ", cost_fn)
                print("Steps: ")
                greedyMethodDumpFile.printSolutionSteps(temp_matrixNode)
                return 

            #check to make sure the current state is present in closed set or not if present will not generate successors.
            if current_matrix not in closed_set:
                closed_set.append(current_matrix)
                nodes_expanded = max(nodes_expanded,len(closed_set))

                #possible directions the tile can be moved 
                directions = [[0,1,"Left"],[0,-1,"Right"],[-1,0,"Down"],[1,0,"Up"]]
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
                        new_cost_fn = self.generateCostFunction(modified_matrix,goalState)
                        new_matrix_node = matrixNode(level+1,new_zero_index,temp_matrixNode,current_matrix,modified_matrix,new_action_val, changed_tile_val,new_cost_fn)
                        count += 1
                        generated_successors.append(modified_matrix)
                        heapq.heappush(heap, new_matrix_node)
                f.write("\n")
                f.write(str(count))
                f.write(" successors generated\n")
                f.write(" Generated Successors are : \n")
                f.write(str(generated_successors))
                f.write("Closed Set : ")
                f.write(str(closed_set))
                f.write("\nFringe : ")
                f.write(str(self.generateValOfHeap(heap,f)))
                nodes_generated += count
        print("Nodes Popped: ",nodes_popped)
        print("Nodes Expanded: ", nodes_expanded)
        print("Nodes Generated: ",nodes_generated)
        print("Max Fringe Size: ",max_fringe_size)
        return "No Output is possible"