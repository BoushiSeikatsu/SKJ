import time
def cached(f):
    """
    Create a decorator that caches up to 3 function results, based on the same parameter values.

    When `f` is called with the same parameter values that are already in the cache, return the
    stored result associated with these parameter values. You can assume that `f` receives only
    positional arguments (you can ignore keyword arguments).

    When `f` is called with new parameter values, forget the oldest accessed result in the cache
    if the cache is already full.

    Example:
        @cached
        def fn(a, b):
            return a + b # imagine an expensive computation

        fn(1, 2) == 3 # computed
        fn(1, 2) == 3 # returned from cache, `a + b` is not executed
        fn(3, 4) == 7 # computed
        fn(3, 5) == 8 # computed
        fn(3, 6) == 9 # computed, (1, 2) was now forgotten
        fn(1, 2) == 3 # computed again, (3, 4) was now forgotten
    """
    queue = []
    def inner(*args, **kwargs):
        for i in range(0,len(queue)):
            if(queue[i][0] != args):
                if(queue[i][2] != 0):  
                    queue[i] = (queue[i][0],queue[i][1],queue[i][2]+1)
        for i in range(0,len(queue)):
            if(queue[i][0] == args):
                queue[i] = (queue[i][0],queue[i][1],1)
                return queue[i][1]                
        if(len(queue) != 3):#Isnt cached and queue isnt full
            queue.append((args,f(*args, **kwargs),0))
        else:#Isnt cached and queue is full
            indexToPop = 0
            highestNumber = 0
            for i in range(0,len(queue)):
                if(queue[i][2] > highestNumber):
                    indexToPop = i
                    highestNumber = queue[i][2]
            queue.pop(indexToPop)
            queue.append((args,f(*args, **kwargs),0))
        if(len(queue) == 0):#First call of function
            queue.append((args,f(*args, **kwargs),0))
        print(queue)
        return queue[-1][1]
        
    return inner
    pass
    pass

class GameOfLife:
    """
    Implement "Game of life" (https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).

    The game board will be represented with nested tuples, where '.'
    marks a dead cell and 'x' marks a live cell. Cells that are out of bounds of the board are
    assumed to be dead.

    Try some patterns from wikipedia + the provided tests to test the functionality.

    The GameOfLife objects should be immutable, i.e. the move method will return a new instance
    of GameOfLife.

    Example:
        game = GameOfLife((
            ('.', '.', '.'),
            ('.', 'x', '.'),
            ('.', 'x', '.'),
            ('.', 'x', '.'),
            ('.', '.', '.')
        ))
        game.alive()    # 3
        game.dead()     # 12
        x = game.move() # 'game' doesn't change
        # x.board:
        (
            ('.', '.', '.'),
            ('.', '.', '.'),
            ('x', 'x', 'x'),
            ('.', '.', '.'),
            ('.', '.', '.')
        )

        str(x)
        ...\n
        ...\n
        xxx\n
        ...\n
        ...\n
    """

    def __init__(self, board):
        """
        Create a constructor that receives the game board and stores it in an attribute called
        'board'.
        """
        self.board = board
        self.width = len(board[0])
        self.height = len(board)
        pass

    def move(self):
        """
        Simulate one iteration of the game and return a new instance of GameOfLife containing
        the new board state.
        """
        newBoard = []
        for i in range(0,self.height):
            newBoard.append([])
            for j in range(0,self.width):
                newBoard[i].append(self.board[i][j])
            newBoard[i] = list(newBoard[i])
        print(newBoard)
        for i in range(0, self.height):
            for j in range(0,self.width):
                isAlive = False
                countNeighbors = 0
                notOnTop = False
                notOnBottom = False
                if(self.board[i][j] == 'x'):
                    isAlive = True
                if(i != 0):
                    notOnTop = True
                    if(self.board[i-1][j] == 'x'):
                        countNeighbors += 1
                if(i != self.height - 1):
                    notOnBottom = True
                    if(self.board[i+1][j] == 'x'):
                        countNeighbors += 1
                if(j != 0):
                    if(notOnTop):
                        if(self.board[i-1][j-1] == 'x'):
                            countNeighbors += 1
                    if(notOnBottom):
                        if(self.board[i+1][j-1] == 'x'):
                            countNeighbors += 1
                    if(self.board[i][j-1] == 'x'):
                        countNeighbors += 1
                if(j != self.width - 1):
                    if(notOnTop):
                        if(self.board[i-1][j+1] == 'x'):
                            countNeighbors += 1
                    if(notOnBottom):
                        if(self.board[i+1][j+1] == 'x'):
                            countNeighbors += 1
                    if(self.board[i][j+1] == 'x'):
                        countNeighbors += 1
                if(isAlive):
                    if(countNeighbors < 2 or countNeighbors > 3):
                        newBoard[i][j] = '.'
                else:
                    if(countNeighbors == 3):
                        newBoard[i][j] = 'x'
        for i in range(0,self.height):
            newBoard[i] = tuple(newBoard[i])
        return GameOfLife(tuple(newBoard))
        pass

    def alive(self):
        """
        Return the number of cells that are alive.
        """
        count = 0
        for i in range(0,self.height):
            for j in range(0, self.width):
                if(self.board[i][j] == 'x'):
                    count += 1
        return count
        pass

    def dead(self):
        """
        Return the number of cells that are dead.
        """
        count = 0
        for i in range(0,self.height):
            for j in range(0, self.width):
                if(self.board[i][j] == '.'):
                    count += 1
        return count
        pass

    def __repr__(self):
        """
        Return a string that represents the state of the board in a single string (with newlines
        for each board row).
        """
        result = ""
        for i in range(0, self.height):
            for j in range(0, self.width):
                result = result + self.board[i][j]
            result = result + '\n'
        return result
        pass


def play_game(game, n):
    """
    You can use this function to render the game for n iterations
    """
    for i in range(n):
        print(game)
        game = game.move()
        time.sleep(0.25)  # sleep to see the output


# this code will only be executed if you run `python tasks.py`
# it will not be executed when tasks.py is imported
if __name__ == "__main__":
    play_game(GameOfLife((
        ('.', '.', '.'),
        ('.', 'x', '.'),
        ('.', 'x', '.'),
        ('.', 'x', '.'),
        ('.', '.', '.'),
    )), 10)