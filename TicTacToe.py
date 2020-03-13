class Square:
    def __init__(self,X,Y,Symbol):
        self.X = X
        self.Y = Y
        self.Symbol = Symbol

    def set_symbol(self,Symbol):
        self.Symbol = Symbol

    def get_symbol(self):
        return self.Symbol


class Board:
    def __init__(self):
        pass

    def reset_board(self,row,col):
        self.row = row
        self.col = col
        self.array = [[j for j in range(self.col)] for i in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                self.array[i][j] = Square(i,j," ")

    def check(self,last_move):
        for i in range(self.col):
            if (i != 0 and self.array[last_move[0]][i].Symbol != " " and
                    self.array[last_move[0]][i].Symbol == self.array[last_move[0]][i - 1].Symbol):
                if (i == self.col - 1):
                    return True
            elif(i!=0):
                break
        for i in range(self.row):
            if (i != 0 and self.array[i][last_move[1]].Symbol != " " and
                    self.array[i][last_move[1]].Symbol == self.array[i-1][last_move[1]].Symbol):
                if (i == self.row - 1):
                    return True
            elif(i!=0):
                break
        if(last_move[0]==last_move[1]):
            for i in range(self.row):
                if (i != 0 and self.array[i][i].Symbol != " " and
                        self.array[i-1][i-1].Symbol == self.array[i][i].Symbol):
                    if (i == self.col - 1):
                        return True
                elif(i!=0):
                    break
        elif(last_move[0]+last_move[1]==self.col-1):
            i,j = 0,self.col-1
            while(i<self.row):
                if (i != 0 and self.array[i][j].Symbol != " " and
                        self.array[i][j].Symbol == self.array[i-1][j+1].Symbol):
                    if (i == self.row - 1):
                        return True
                elif(i!=0):
                    break
                i+=1
                j-=1
        return False


    def game_status(self):
        for i in range(self.row):
            for j in range(self.col):
                print("+---", end="")
            print("+")
            for j in range(self.col):
                print("|", self.array[i][j].Symbol, end=" ")
            print("|")
        for j in range(self.col):
            print("+---", end="")
        print("+")

def game_start():
    sq = int(input("Enter Square Board size: "))
    r,c = sq, sq
    board = Board()
    board.reset_board(r,c)
    board.game_status()
    i = 0
    prev = None
    while(i < r*c):
       x = int(input("Enter position X"))
       y = int(input("Enter position Y"))
       sym = input("Enter Symbol ")
       if(prev!=sym):
           prev = sym
       else:
           print("This is an opponent's move")
           continue
       if(x not in range(0,sq) or y not in range(0,sq) or (sym!="X" and sym!="O")):
           print("Invalid move")
           continue
       else:
           board.array[x][y].Symbol = sym
           board.game_status()
           if(board.check([x,y])):
               print(board.array[x][y].Symbol," wins")
               return
       i+=1
    print("No one wins")




if  __name__=="__main__":
    game_start()

