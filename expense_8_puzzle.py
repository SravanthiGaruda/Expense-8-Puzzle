import sys
import datetime
from bfsDumpFile import *
from breadthFirstSearch import *
from aStar import *
from aStarDumpFile import *
from dfs import *
from dfsDumpFile import *
from greedy import *
from greedyDumpFile import *
from ucs import *
from ucsDumpFile import *
from dls import *
from dlsDumpFile import *
from ids import *
from idsDumpFile import *

def main(args):
    len_of_arguments = len(args)
    depth = ""

    # Taking another input from user if dls method name is provided
    if args[2] == "dls":
        print("Specify Required Depth Limited = ")
        depth = input()

    #Checking the arguments provided by the user
    if len_of_arguments == 3 or (len_of_arguments == 4 and args[3].lower() == "false"):
        Expense8PuzzleWithoutDumpFile(args[0],args[1],args[2],depth)
    else:
        #generating date and time 
        current_date_time = datetime.datetime.now()
        #extracting date 
        current_date = current_date_time.date()
        #extracting time
        current_time = current_date_time.time()
        #creating a dump file
        f = open(f"{'trace-'}{current_date}{'-'}{current_time}.txt", "x")
        f.write("Command Line Arguments: ")
        f.write(args[0])
        f.write(" ")
        f.write(args[1]) 
        f.write(" ")
        f.write(args[2])
        f.write(" True\n")
        Expense8PuzzleWithDumpFile(args[0],args[1],args[2],depth,f)

# Function used to read start and goal state
def readFile(file):
    file = open(file,'r')
    startMatrix = []
    for line in file.readlines():
        line = line.strip()
        line = line.split()
        for val in line:
            if val == "END":
                break
            startMatrix.append(val)
    startState = []
    i = 0
    while i < len(startMatrix):
        col = []
        for j in range(3):
            col.append(startMatrix[i+j])
        startState.append(col)
        i +=3
    return startState

# Function used to create search zero index in matrix
def searchZeroInMatrix(startState):
    for i in range(3):
        for j in range(3):
            if startState[i][j] == "0":
                return [i,j]

def Expense8PuzzleWithoutDumpFile(startState,goalState,methodType,depth):
    startState = readFile(startState)
    goalState = readFile(goalState)
    methodName = methodType
    zeroValIndex = searchZeroInMatrix(startState)

    if methodName == "bfs":
        bfs_sol = breadthFirstSearch()
        bfs_final_val = bfs_sol.bfs(startState, goalState, zeroValIndex)
        print(bfs_final_val)
    elif methodName == "ucs":
        ucs_sol = ucsMethod()
        ucs_final_val = ucs_sol.ucs(startState, goalState, zeroValIndex)
        print(ucs_final_val)
    elif methodName == "dfs":
        dfs_sol = depthFirstSearch()
        dfs_final_val = dfs_sol.dfs(startState, goalState, zeroValIndex)
        print(dfs_final_val)
    elif methodName == "dls":
        dls_sol = depthLimitedSearch()
        dls_final_val = dls_sol.dls(startState,goalState,zeroValIndex,depth)
        print(dls_final_val)
    elif methodName == "greedy":
        greedy_sol = greedyMethod()
        greedy_final_val = greedy_sol.greedy(startState, goalState, zeroValIndex)
        print(greedy_final_val)
    elif methodName == "a*":
        aStar_sol = aStarMethod()
        aStar_final_val = aStar_sol.aStar(startState, goalState, zeroValIndex)
        print(aStar_final_val)
    elif methodName == "ids":
        ids_sol = iterativeDeepeningSearch()
        depth = 0
        val = ids_sol.ids(startState, goalState, zeroValIndex,depth)
        if val == "No Output is possible":
            temp_Val = "No Output is possible"
            while val == temp_Val:
                depth = depth + 1
                temp_Val = ids_sol.ids(startState, goalState, zeroValIndex, depth)

def Expense8PuzzleWithDumpFile(startState,goalState,methodType,depth,f):
    startState = readFile(startState)
    goalState = readFile(goalState)
    methodName = methodType
    zeroValIndex = searchZeroInMatrix(startState)
    if methodName == "bfs":
        bfs_sol = breadthFirstSearchWithDumpFile()
        bfs_final_val = bfs_sol.bfs(startState,goalState,zeroValIndex,f)
        print(bfs_final_val)
    elif methodName == "ucs":
        ucs_sol = ucsMethodDumpFile()
        ucs_final_val = ucs_sol.ucs(startState, goalState, zeroValIndex,f)
        print(ucs_final_val)
    elif methodName == "dfs":
        dfs_sol = depthFirstSearchWithDumpFile()
        dfs_final_val = dfs_sol.dfs(startState, goalState, zeroValIndex, f)
        print(dfs_final_val)
    elif methodName == "dls":
        dls_sol = depthLimitedSearchDumpFile()
        dls_final_val = dls_sol.dls(startState,goalState,zeroValIndex,depth,f)
        print(dls_final_val)
    elif methodName == "greedy":
        greedy_sol = greedyMethodDumpFile()
        greedy_final_val = greedy_sol.greedy(startState, goalState, zeroValIndex, f)
        print(greedy_final_val)
    elif methodName == "a*":
        aStar_sol = aStarMethodDumpFile()
        aStar_final_val = aStar_sol.aStar(startState, goalState, zeroValIndex,f)
        print(aStar_final_val)
    elif methodName == "ids":
        ids_sol = iterativeDeepeningSearchDumpFile()
        depth = 0
        val = ids_sol.ids(startState, goalState, zeroValIndex,depth, f)
        if val == "No Output is possible":
            temp_Val = "No Output is possible"
            while val == temp_Val:
                depth = depth + 1
                temp_Val = ids_sol.ids(startState, goalState, zeroValIndex, depth, f)


main(sys.argv[1:])

