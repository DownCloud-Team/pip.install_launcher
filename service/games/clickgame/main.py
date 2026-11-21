print("Importing Module...")
import customtkinter as ctk
import time

time.sleep(int("2"))

clicks = int("0")

def click():
    
    global clicks
    
    print("Ein klick wurde übernommen")
    
    clicks = clicks + int("1")
    
    game_title.configure(text=f"Klicks:[{clicks}]")

print("Setting up...")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

time.sleep(int("2"))

print("Create: [Window]")

game = ctk.CTk()
game.title("Click Game")

print("Create: [Game Title]")

game_title = ctk.CTkButton(game, text="Klicks:[Keine]")
game_title.pack(pady=20)

print("Create: [Game Button]")

game_click = ctk.CTkButton(game, text="+1 Klick", command=click)
game_click.pack(pady=20)

time.sleep(int("1"))

game.mainloop()
