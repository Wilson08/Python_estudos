class RegularCard
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

queen_of_hearts_R = RegularCard('Q','Hearts')
print(queen_of_hearts_R.rank)
print(queen_of_hearts_R)