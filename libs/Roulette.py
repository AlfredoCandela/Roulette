import random

class Roulette:
    def __init__(self, balance):

        self.money = balance
        red_numbers = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}
        black_numbers = {2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35}

        self.first_row = {1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34}
        self.second_row = {2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35}
        self.third_row = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36}

        self.first_dozen = set(range(1,13))
        self.second_dozen = set(range(13,25))
        self.third_dozen = set(range(25,37))

        self.first_half = set(range(1,19))
        self.second_half = set(range(19,37))

        self.cells = []
        for number in range(37):
            cell = {"number": number, "even": number % 2 == 0, "high": number >= 19}
            if number in red_numbers:
                cell["colour"] = "red"
            elif number in black_numbers:
                cell["colour"] = "black"
            else:
                cell["colour"] = "green"

            self.cells.append(cell)

        self.current_cell = self.cells[0]

    def spin(self):
        self.current_cell = self.cells[random.randint(0, 36)]

    def straight(self, selected_number, bet):
        self.spin()
        if self.current_cell["number"] == selected_number:
            balance = bet * 35
            message = f"You have bet on {selected_number} and you won {balance} €"
        else:
            balance = -bet
            message = f"You have bet on {selected_number} and you lost {bet} €"
        self.money += balance

        return message
    
    def colour(self, selected_colour, bet):
        self.spin()
        if self.current_cell["colour"] == selected_colour:
            balance = bet
            message = f"You have bet on {selected_colour} and you won {balance} €"
        else:
            balance = -bet
            message = f"You have bet on {selected_colour} and you lost {bet} €"
        self.money += balance
        return message
    
    def half(self, half, bet):
        self.spin()
        if half == 1:
            winner_half = self.first_half
        else:
            winner_half = self.second_half

        if self.current_cell["number"] in winner_half:
            balance = bet*2
            message = f"You have bet on half {half} and you won {balance} €"
        else:
            balance = -bet
            message = f"You have bet on half {half} and you lost {bet} €"

        self.money += balance
        return message

    def dozen(self, dozen, bet):
        self.spin()
        if dozen == 1:
            winner_dozen = self.first_dozen
        elif dozen == 2:
            winner_dozen = self.second_dozen
        else:
            winner_dozen = self.third_dozen

        if self.current_cell["number"] in winner_dozen:
            balance = bet*2
            message = f"You have bet on dozen {dozen} and you won {balance} €"
        else:
            balance = -bet
            message = f"You have bet on dozen {dozen} and you lost {bet} €"

        self.money += balance
        return message

    def row(self, row, bet):
        self.spin()
        if row == 1:
            winner_row = self.first_row
        elif row == 2:
            winner_row = self.second_row
        else:
            winner_row = self.third_row

        if self.current_cell["number"] in winner_row:
            balance = bet*2
            message = f"You have bet on row {row} and you won {balance} €"
        else:
            balance = -bet
            message = f"You have bet on row {row} and you lost {bet} €"

        self.money += balance
        return message

    def even_odd(self, is_even, bet):
        self.spin()
        if self.current_cell["number"] == 0:
            balance = -bet
            win = False
        elif self.current_cell["even"] == is_even:
            balance = bet
            win = True
        else:
            balance = -bet
            win = False
        self.money += balance

        if is_even:
            even_odd_bet = "even"
        else:
            even_odd_bet = "odd"

        if win == True:
            message = f"You have bet on {even_odd_bet} and you won {balance} €"
        else:
            message = f"You have bet on {even_odd_bet} and you lost {bet} €"

        return message
    

