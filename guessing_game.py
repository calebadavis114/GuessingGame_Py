class GuessingGame():
    def __init__(self,num):
        self.num = num
        self.solve = 'false'
    def guess(self, guess):
        if(guess == self.num):
            self.solve = 'true'
        elif(guess > self.num):
            print("lower")
        else:
            print("higher")
    def solved(self):
        if(self.solve == 'true'):
            print('Correct')
        else:
            print("False")
         

game = GuessingGame(10)
game.guess(6)
game.guess(11)
game.guess(55)
game.solved()