from models.player import Player

def game(player1, player2):
    if player1.choice == player2.choice: 
        return f'{None} wins'
    elif player1.choice == "rock": 
        if player2.choice == "scissors":
            return f'{player1.name} wins by playing {player1.choice}'
        else: 
            return f'{player2.name} wins by playing {player2.choice}'
    elif player1.choice == "scissors": 
        if player2.choice == "paper":
            return f'{player1.name} wins by playing {player1.choice}'
        else: 
            return f'{player2.name} wins by playing {player2.choice}'
    elif player1.choice == "paper": 
        if player2.choice == "rock":
            return f'{player1.name} wins by playing {player1.choice}'
        else:
            return f'{player2.name} wins by playing {player2.choice}'

    

