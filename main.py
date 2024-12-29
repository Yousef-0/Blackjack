import random
#import tkinter

class Player:
    Players = []
    count = 0
    
    cards = []
    total = 0
    busted = False
    aces = 0
    
    def __init__(self, i, player_name):
        self.name = player_name
        self.cards = []
        self.total = 0
        self.stay = False
        self.busted = False
        self.split = False
        self.id = i
#        self.label = None
        Player.count += 1
        
    def add_card(self, card):
        self.cards.append(card)
        self.total += card_values[card]
#        self.label.config(text=self.name + ": " +str(self.cards))
        
    def split_cards(self):
        if self.cards[0] == self.cards[-1]:
            for i in range(len(Player.Players)):
                if Player.Players[i].id == self.id and Player.Players[i].name == self.name:
                    print("debug")
                    Player.Players.insert(i+1,(Player(self.id,self.name + '2')))
                    Player.Players[i+1].add_card(self.cards.pop())
            self.total = self.total/2
        else:
            print("you can't split silly")
    def qA(self):
        if 'A' in self.cards:
            self.cards.remove('A')
            self.cards.append('A_1')
            self.total -= 10
        else:
            self.busted = True
            self.stay = True

    def card_value(self): 
        self.total = 0
        for card in self.cards:
            self.total += card_values[card]
            
    def ace_converter(self):
        if 'A' in self.cards:
            self.cards.remove('A')
            self.cards.append('A_1')    


card_draws = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
              '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
              '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
              '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = list(card_draws)
random.shuffle(deck)
                
running_deck = {'2': 4, '3': 4, '4': 4, '5':4, '6': 4, '7': 4, '8': 4, '9': 4, '10': 4, 'J': 4, 'Q': 4, 'K': 4, 'A': 4} 

card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11, 'A_1': 1}        


number_of_players = int(input("Pppl plz "))

#window = thinter.Tk()

for i in range(number_of_players):
        Player.Players.append(Player(i, input("name plz ")))
        Player.Players[i].add_card(deck.pop())
        Player.Players[i].add_card(deck.pop())
#        Player.Players[i].label = tkinter.label(window,text= Player.Players[i].name + ": " +str(Player.Players[i].cards))
#        Player.Players[i].label.pack()        
        
Player.Players.append(Player(-1, "dealer"))
dealer = Player.Players[-1]
Player.Players[-1].add_card(deck.pop())
print(dealer.cards)
Player.Players[-1].add_card(deck.pop())
#Player.Players[-1].label = tkinter.label(window,text= Player.Players[i].name + ": " +str(Player.Players[i].cards))
#Player.Players[-1].label.pack()   

#frame = tkinter.Frame(window, borderwidth=4, relief=tkinter.GROOVE)
#buttondraw = tkinter.Button(frame,text="draw",command=click)
#buttonstay = tkinter.Button(frame,text="stay",command=click)
#buttonsplit = tkinter.Button(frame,text="split",command=click)
#buttondraw.pack()
#buttonstay.pack()
#buttonsplit.pack()

if dealer.total == 21:
    print(dealer.cards)
    print("U lose")

blackjack = False
i = 0
while i < len(Player.Players)-1:
    player = Player.Players[i]
    first_turn = True
    while player.stay == False:
        print(player.name + str(player.cards))
        if first_turn == True:
            action = input("Do you want to draw, split, or stay? ").strip().lower()
        else:
            action = input("Do you want to draw or stay? ").strip().lower()
        if action == "stay":
            player.stay = True
        elif action == "draw":
            player.add_card(deck.pop())
            if player.total > 21:
                player.qA()
            elif player.total == 21:
                player.stay = True
                blackjack = True
        elif action == "split" and first_turn == True:
            player.split_cards()
        first_turn = False
    print(player.cards)
    i += 1
    
while dealer.total < 17:
    dealer.add_card(deck.pop())
    if dealer.total > 21:
        dealer.qA()
    print(dealer.cards)
if dealer.busted == True:
    print("U win")
elif dealer.total == 21:
    print("U lose")
flag = False
for player in Player.Players:
    if player.busted == False:
        if player.total > dealer.total:
            print(player.name + " you won")
            flag = True
if not flag and dealer.busted == False:
    print("lose")

print(dealer.cards)
print(len(Player.Players))
    
#window.mainloop()
