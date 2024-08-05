import tkinter as tk
from tkinter import *
from tkinter import font
import RandWords
from random import shuffle

from tkinter import messagebox


def close_window():
    master.destroy()

def openInfoTab():

    def close_infotab():
        infoT.destroy()

    infoT = tk.Tk()
    infoT.title("Game Instructions")
    infoT.geometry("490x410")
    infoT.resizable(False, False)
    infoT.configure(bg="light gray")

    file_path = "C:/Users/anany/Documents/Ananya Adivi Documents/Instructions of Word Scramble.txt"

    text_widget = tk.Text(infoT, wrap="word", width=40, height=20)
    text_widget.pack(pady=10)

    with open(file_path, 'r') as file:
        content = file.read()
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END, content)

    exit = tk.Button(infoT,
                     text="LET'S PLAY!",
                     bg="#ffffff",
                     activebackground="#F57AB8",
                     command=close_infotab,
                     font=25)

    exit.pack(pady=10, padx =10,side = BOTTOM)


def openNew():
    newWindow = tk.Tk()
    newWindow.title("Guessing Game")
    newWindow.geometry("400x450")
    newWindow.resizable(False, False)
    newWindow.configure(bg="light green")
    global rand_word
    global hint_count
    global score
    score = 0


    def display_word():
        global rand_word
        Guess_entry.delete(0, END)
        ans_label.config(text = "")
        hint_label.config(text = "")

        rand_word = RandWords.choose_random()
        break_rand_word = list(rand_word)
        shuffle(break_rand_word)
        WordDisp.config(text=break_rand_word)

    def answer():
        global score

        if Guess_entry.get() == "":
            messagebox.showinfo("Error", "please enter your guess!")

        elif Guess_entry.get() == rand_word:
            messagebox.showinfo("Correct!", "Good Job, you got it correct! \nMove on to your next word!")
            score += 7
            score_label.config(text=str(score))
        else:
            messagebox.showinfo("Uh-Oh!", "Looks like you got it incorrect, try using the hint!")
            score -= 1
            score_label.config(text=str(score))

    def get_hint():
        global rand_word
        global score


        if rand_word in RandWords.animals:
            hint_label.config(text = "The word is a type of animal")
            score -=1
            score_label.config(text = str(score))

        elif rand_word in RandWords.fruits:
            hint_label.config(text = "The word is a type of fruit")
            score -= 1
            score_label.config(text=str(score))

        else:
            hint_label.config(text = "The word is a type of stationary item")
            score -= 1
            score_label.config(text=str(score))

    ShowWord = tk.Label(newWindow,
                        text="Click the button below to go to the next word! ",
                        anchor="center",
                        bg="light green",
                        font = font5,
                        height=4)

    GuessWord = tk.Label(newWindow,
                         text="Guess the Word!",
                         anchor="center",
                         bg="light green",
                         font=font5,
                         height=3)

    WordDisp = tk.Label(newWindow,
                        anchor="center",
                        bg="#4CBB6B",
                        font = font_size_newWin,
                        )

    ans_label = tk.Label(newWindow,
                         text = "",
                         anchor = "center",
                         bg = "light green",
                         font =  font_size_newWin)

    hint_label = tk.Label(newWindow,
                          text = "",
                          anchor="center",
                          bg = "light green",
                          font = font_size_newWin)

    score_name = tk.Label(newWindow,
                          text = "Score Count",
                          bg = "#eff47c",
                          font = font_size_newWin)

    score_label = tk.Label(newWindow,
                           text = "     ",
                           bg = "#eff47c",
                           font = font_size_newWin)

    disp_Bttn = tk.Button(newWindow,
                          text="NEXT WORD",
                          bg="#ffffff",
                          activebackground="#6CE832",
                          command = display_word,
                          font = 15)

    submit_bttn = tk.Button(newWindow,
                            text = "Submit",
                            bg = "#ffffff",
                            activebackground="#6CE832",
                            font = 14,
                            command=answer)

    hint_bttn = tk.Button(newWindow,
                          text = "Hint",
                          bg = "#ffffff",
                          activebackground="#6CE832",
                          font = 12,
                          command = get_hint)



    Guess_entry = tk.Entry(newWindow,
                           font=entry_font,
                           justify="center")




    score_name.pack(padx=15, side=TOP, anchor = "w")
    score_label.pack(padx=15, side=TOP, anchor = "w")
    GuessWord.pack()
    WordDisp.pack(pady=10)
    Guess_entry.pack()
    submit_bttn.pack(pady=10)
    ans_label.pack(pady=7)
    hint_bttn.pack()
    hint_label.pack()
    ShowWord.pack()
    disp_Bttn.pack()



    display_word()




# -- Home Page  -- #

master = tk.Tk()
master.geometry("300x280")
master.title("Home Page")
master.resizable(False, False)
master.configure(bg="light pink")

# --- Font characteristics --- #
label_font = font.Font(weight="bold", size=16)
font_size_subtitle = font.Font(size=12)
font_size_newWin = font.Font(size=12)
entry_font = font.Font(size=15)
font5 = font.Font(size=25)
# --- Font characteristics --- #

MainLabel = tk.Label(master,
                     text="WELCOME TO THE HOME PAGE!",
                     wraplength=200,
                     anchor="center",
                     bg="light pink",
                     font=label_font,
                     height=4)

Subtitle = tk.Label(master,
                    text="Click 'START' to play the game!",
                    anchor="center",
                    bg="#f16bb2",
                    font=font_size_subtitle)

StartBtn = tk.Button(master,
                     text="START",
                     command=openNew,
                     bg="#9cf36e",
                     activebackground="#F57AB8")

InstrBtn = tk.Button(master,
                     text = "INSTRUCTIONS",
                     command=openInfoTab,
                     bg = "light yellow",
                     activebackground="#F57AB8")

ExitBtn = tk.Button(master,
                    text="EXIT",
                    bg="#ffffff",
                    activebackground="#F57AB8",
                    command=close_window)


MainLabel.pack(padx=25, pady=5)
Subtitle.pack(padx=5, pady=5)
StartBtn.pack(padx=5, pady=5)
InstrBtn.pack(padx=5, pady=5)
ExitBtn.pack(padx=5, pady=5)

master.mainloop()
