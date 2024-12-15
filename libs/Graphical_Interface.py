import customtkinter as ctk
from libs.Roulette import Roulette
from PIL import Image

class Graphical_Interface(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.margins = 10
        self.title("Alf's Roulette, the very best roulette of the world, I promise")
        self.geometry("1400x800")
        ctk.set_appearance_mode("Dark")

        self.bet = 0
        self.roulette = Roulette(30)
        self.big_font=("default",20)

        self.button_id = 0
        self.selected_button_id = None
        self.select_bet_buttons = []

        self.money_frame = ctk.CTkFrame(self, corner_radius=10)
        self.money_frame.grid(row=0, column=0, pady=self.margins)
        self.fill_money_frame()

        self.bets_frame = ctk.CTkFrame(self, corner_radius=10, fg_color="transparent")
        self.bets_frame.grid(row=1, column=1, rowspan=2)
        self.fill_bets_frame()

        raw_image = ctk.CTkImage(light_image=Image.open('libs/roulette.png'),
                                 dark_image=Image.open('libs/roulette.png'),
                                 size=(500,500))
        
        image_in_GUI = ctk.CTkLabel(self, text="", image=raw_image)
        image_in_GUI.grid(row=2, column=0, padx=self.margins, pady=self.margins)

        self.create_bet_button()
        self.set_message()
        self.create_show_result_cell()
    
    def create_show_result_cell(self):
        self.result_cell = ctk.CTkButton(self, text=self.roulette.current_cell["number"],
                               width=150, height=150,
                               fg_color=self.roulette.current_cell["colour"],
                               font=("default", 90), state="enabled", corner_radius=10)
        self.result_cell.grid(row=3,column=0)

    def set_message(self):
        self.message =ctk.CTkLabel(self, text="Bet something.", font=("default",30))
        self.message.grid(row=0,column=1)
        

    def create_bet_button(self):
        self.bet_button = ctk.CTkButton(self, text="Choose a bet", command= self.spin_roulette,
                               width=200, height=100, fg_color="black", font=("default",30),
                               state="disabled")
        self.bet_button.grid(row=3, column=1, padx=self.margins, pady=self.margins)

    def create_select_button(self, frame, text, width, height, font, bet_choice,
                             bet_game, fg_color=None):
        
        button = ctk.CTkButton(frame, text=text,
                               command=lambda id=self.button_id: self.select_bet(id),
                               width=width, fg_color=fg_color, font=font, height=height)
        button.initial_colour = button._fg_color
        button.bet_game = bet_game
        button.bet_choice = bet_choice
        self.select_bet_buttons.append(button)
        self.button_id += 1
        return button

    def fill_bets_frame(self):
        buttons_height = 55

        button = self.create_select_button(frame=self.bets_frame, text="0", width=55,
                                           fg_color="green", font=self.big_font,
                                           height=buttons_height, bet_game=self.roulette.straight,
                                           bet_choice=0)
        button.grid(row=0, column=0, pady=2, padx=2, rowspan=3, sticky="ns")

        cell_number = 1
        for column in range(1,13):
            for row in range(3):
                colour = self.roulette.cells[cell_number]["colour"]
                button = self.create_select_button(frame=self.bets_frame, text=cell_number, width=55,
                                                   fg_color=colour, font=self.big_font, 
                                                   height=buttons_height,
                                                   bet_game=self.roulette.straight,
                                                   bet_choice=cell_number)
                button.grid(row=row, column=column, pady=2, padx=2)  

                cell_number += 1
        
        for row in range(3):
            button = self.create_select_button(frame=self.bets_frame,
                                            text=f"Row {row+1}", width=100, font=self.big_font,
                                            height=buttons_height, bet_game=self.roulette.row,
                                            bet_choice=row+1)
            button.grid(row=row, column=13, pady=2, padx=2)

        for dozen in range(3):
            button = self.create_select_button(frame=self.bets_frame,
                                            text=f"Dozen {dozen+1}", width=232, font=self.big_font,
                                            height=buttons_height, bet_game=self.roulette.dozen,
                                            bet_choice=dozen+1)
            button.grid(row=3, column=dozen*4+1, pady=2, columnspan=4)
        

        self.bets_frame.grid_rowconfigure(4, minsize=10)

        button = self.create_select_button(frame=self.bets_frame, text="Half 1 (from 1 to 18)", width=232,
                                           font=self.big_font, height=buttons_height,
                                           bet_game=self.roulette.half, bet_choice=1)
        button.grid(row=5, column=1, pady=5, columnspan=4)
        button = self.create_select_button(frame=self.bets_frame, text="Half 2 (from 19 to 36)", width=232,
                                           font=self.big_font, height=buttons_height,
                                           bet_game=self.roulette.half, bet_choice=2)
        button.grid(row=6, column=1, pady=5, columnspan=4)

        button = self.create_select_button(frame=self.bets_frame, text="RED", width=232,
                                           font=self.big_font, fg_color="red",
                                           height=buttons_height,
                                           bet_game=self.roulette.colour, bet_choice="red")
        button.grid(row=5, column=5, pady=5, columnspan=4)
        button = self.create_select_button(frame=self.bets_frame, text="BLACK", width=232,
                                           font=self.big_font, fg_color="black",
                                           height=buttons_height,
                                           bet_game=self.roulette.colour, bet_choice="black")
        button.grid(row=6, column=5, pady=5, columnspan=4)

        button = self.create_select_button(frame=self.bets_frame, text="EVEN", width=232,
                                           font=self.big_font, height=buttons_height,
                                           bet_game=self.roulette.even_odd, bet_choice=True)
        button.grid(row=5, column=9, pady=5, columnspan=4)
        button = self.create_select_button(frame=self.bets_frame, text="ODD", width=232,
                                           font=self.big_font, height=buttons_height,
                                           bet_game=self.roulette.even_odd, bet_choice=False)
        button.grid(row=6, column=9, pady=5, columnspan=4)

    def spin_roulette(self):

        game = self.select_bet_buttons[self.selected_button_id].bet_game
        choice = self.select_bet_buttons[self.selected_button_id].bet_choice
        message = game(choice,self.bet)

        if self.bet > self.roulette.money:
            self.bet = self.roulette.money
            self.bet_text.configure(text=f"Bet: {self.bet} €")

        self.wallet_text.configure(text=f"Wallet: {self.roulette.money} €")
        self.result_cell.configure(text=self.roulette.current_cell["number"],
                                   fg_color=self.roulette.current_cell["colour"])
        
        self.message.configure(text=message)

        if self.roulette.money == 0:
            self.message.configure(text="You lost everything. Stop gambling!")
            self.bet_button.configure(state="enabled", fg_color="gray",
                                      text_color="black", text= ":(", width=350)

    def select_bet(self, button_id):
        if self.bet_button._state == "disabled":
            self.bet_button.configure(state="normal", fg_color="gold",
                                      text_color="black", text= "GAMBLING TIME!",
                                      hover_color="gold4", width=350)

        self.unmark_previous_button()
        self.selected_button_id = button_id
        self.mark_selected_button()

    def unmark_previous_button(self):
        if self.selected_button_id == None:
            return
        button_from_id = self.select_bet_buttons[self.selected_button_id]
        button_from_id.configure(fg_color=button_from_id.initial_colour)

    def mark_selected_button(self):
        self.select_bet_buttons[self.selected_button_id].configure(fg_color="gray", hover_color="gray")
            
    def fill_money_frame(self):
        self.wallet_text = ctk.CTkLabel(master=self.money_frame, text=f"Wallet: {self.roulette.money} €", font=self.big_font)
        self.wallet_text.grid(row=0, column=0, padx=self.margins, pady=self.margins)

        self.bet_selector_frame = ctk.CTkFrame(self.money_frame, corner_radius=10,
                                               fg_color="transparent")
        self.bet_selector_frame.grid(row=0,column=1)

        self.bet_text = ctk.CTkLabel(master=self.bet_selector_frame, text=f"Bet: {self.bet} €",
                                     font=self.big_font)
        self.bet_text.grid(row=0, column=0, padx=self.margins, pady=self.margins, rowspan=2)

        increase_button = ctk.CTkButton(self.bet_selector_frame, text="▲", 
                                        command=self.increase_bet, font=self.big_font)
        increase_button.grid(row=0, column=1, pady=5, padx=5)

        decrease_button = ctk.CTkButton(self.bet_selector_frame, text="▼",
                                        command=self.decrease_bet, font=self.big_font)
        decrease_button.grid(row=1, column=1, pady=5, padx=5)

    def increase_bet(self):
        if self.bet < self.roulette.money:
            self.bet += 1
            self.bet_text.configure(text=f"Bet: {self.bet} €")

    def decrease_bet(self):
        if self.bet > 0:
            self.bet -= 1
            self.bet_text.configure(text=f"Bet: {self.bet} €")


app = Graphical_Interface()
app.mainloop()
