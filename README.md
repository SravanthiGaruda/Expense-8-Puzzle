# Expense-8-Puzzle

Structure of Code
1. expense_8_puzzle.py
    - expense_8_puzzle file is the main file which is used to run the algorithms.
    - expense_8_puzzle file reads inputs from command line and calls its respective algorithm which needs to be executed depending on the methodName and DumpFlag value.
    - The start.txt and goal.txt files are converted into a matrix format using "readFile" function.
    - "Expense8PuzzleWithoutDumpFile" function is used to call the algorithm files which does not create a dumpFile.
    - "Expense8PuzzleWithDumpFile" function is used to call the algorithm files which creates a dumpFile as well.
    - DumpFile is created in the following format :
        - "{'trace-'}{current_date}{'-'}{current_time}.txt"
        - example : trace-2023-02-26-13:55:14.541841.txt
    - DumpFile generally consists of the following details :
        - Command Line Arguments given
        - Method Name which is Selected
        - Current Node for which successors are being generated.
        - Cost of Node
        - Depth of Node
        - Parent of the Node
        - Number of successors generated for Node
        - Closed Set
        - Fringe 
2. Below file names are used to run their respective algorithm without creating a dump file when "Expense8PuzzleWithoutDumpFile" method is called.
    - aStar.py runs a Star algorithm
    - breadthFirstSearch.py runs Breadth first search algorithm
    - dfs.py runs Depth first search" algorithm
    - dls.py runs Depth limited search algorithm
    - greedy.py runs Greedy algorithm
    - ids.py runs iterative deepening search algorithm
    - ucs.py runs Uniform cost search algorithm

3. Below file names are used to run their respective algorithm with creating a dump file when "Expense8PuzzleWithDumpFile" method is called.
    - aStarDumpFile.py runs a* algorithm
    - bfsDumpFile.py runs Breadth first search algorithm
    - dfsDumpFile.py runs Depth first search" algorithm
    - dlsDumpFile.py runs Depth limited search algorithm
    - greedyDumpFile.py runs Greedy algorithm
    - idsDumpFile.py runs iterative deepening search algorithm
    - ucsDumpFile.py runs Uniform cost search algorithm
4. If the output says "No solution is possible" it means that the 8 puzzle problem start state and goal state are unsolvable.

How to Use
1. Make sure to include start.txt and goal.txt file in the same folder if not present or edit them.
2. To create DumpFile using algorithm use the below commands:
    - python3 expense_8_puzzle.py start.txt goal.txt ucs true
    - In order to run a* algorithm in command line try to use any of the below two commands to avoid error:
        1. python3 expense_8_puzzle.py start.txt goal.txt a\* true
        2. python3 expense_8_puzzle.py start.txt goal.txt "a*" true
4. To directly run the code without creating a Dump File use the below commands:
    - python3 expense_8_puzzle.py start.txt goal.txt ucs
    - python3 expense_8_puzzle.py start.txt goal.txt ucs False
    - In order to run a* algorithm in command line try to use any of the below two commands to avoid error:
        1. python3 expense_8_puzzle.py start.txt goal.txt a\* 
        2. python3 expense_8_puzzle.py start.txt goal.txt "a*"
5. Use python in place of python3 in the command if not running. 
6. If the code is being executed on MAC then use python3 or else use python for windows.

Note: dfs, dls, ucs programs may take time to run depending on the inputs provided.

