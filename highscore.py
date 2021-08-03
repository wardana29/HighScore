class GameEntry:
    total_player = 0
    
    def __init__(self, name, score,timeq): 
        self.name = name
        self.score = score
        self.time = timeq

        GameEntry.total_player += 1

    def set_name(self, name):
        self.name = name
        
    def get_name(self):
        return self.name
    
    def set_score(self, score):
        self.score = score
        
    def get_score(self):
        return self.score
    
    def set_time(self,timeq):
        self.time = timeq
        
    def get_time(self):
        return self.time

    def getTotal():
        return GameEntry.total_player



class ScoreBoard:
    def __init__(self,capacity):
        self.capacity = capacity
        self.board = [None] * self.capacity
        self.n = 0

    def getCapacity(self):
        return self.capacity

    def sumEntries(self):
        return self.n

    def addItem(self, game_entry):
        score = game_entry.get_score()

        good = len(self.board) > self.n or score > self.board[self.capacity -1].get_score()

        if good:
            if self.n < self.capacity:
                self.n += 1 

                j = self.n - 1

                while j > 0 and self.board[j-1].get_score() < score:
                    self.board[j] = self.board[j-1]
                    j -= 1

                self.board[j] = game_entry
                print(f"Entri {score} ditambahkan")


    def listEntries(self):
        for i in range (0, self.n):
            print(i+1,":", getattr(self.board[i], 'name'), getattr(self.board[i], 'score'))

board = ScoreBoard(10)
player1 = GameEntry("Lily", 89, 4)
player2 = GameEntry("Rama", 89, 4)
player3 = GameEntry("Karmila", 79, 4)

score_board.addItem(player1)
score_board.addItem(player2)
score_board.addItem(player3)

active = True

while active:
    print("")
    start = input("Opsi: \n 1 = Tambah Entry Baru \n 2 = Tampilkan List ScoreBoard \n 3 = Keluar \n")
    print("")
    if start == '2':
        board.listEntries()
    elif start == '1':
        name = input("Masukkan nama pemain ")
        skor = int(input("Masukkan skor "))
        waktu = int(input("Masukkan waktu "))

        in_score = GameEntry(name, skor, waktu)
        set_board = board.addItem(in_score)

        print(f"Entri baru ditambahkan: {in_score.get_name()} {in_score.get_score()} {in_score.get_time()}")
    else:
        break








lily_score = GameEntry("Lily", 89, 4)
lily_score2 = GameEntry("Lily", 89, 4)
lily_score3 = GameEntry("Lily", 79, 4)

score_board = ScoreBoard(2)
score_board.addItem(lily_score)
score_board.addItem(lily_score2)
score_board.addItem(lily_score3)
                    
print(lily_score.get_score())