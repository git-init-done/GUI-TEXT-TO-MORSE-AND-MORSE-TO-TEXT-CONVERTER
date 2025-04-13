import tkinter as tk

class Morse:
    def __init__(self, s: str):
        self.input = s
        self.morsehashmap = {
            'A': ".-", 'B': "-...", 'C': "-.-.", 'D': "-..", 'E': ".", 'F': "..-.", 
            'G': "--.", 'H': "....", 'I': "..", 'J': ".---", 'K': "-.-", 'L': ".-..", 
            'M': "--", 'N': "-.", 'O': "---", 'P': ".--.", 'Q': "--.-", 'R': ".-.", 
            'S': "...", 'T': "-", 'U': "..-", 'V': "...-", 'W': ".--", 'X': "-..-", 
            'Y': "-.--", 'Z': "--..",
            '0': "-----", '1': ".----", '2': "..---", '3': "...--", '4': "....-", 
            '5': ".....", '6': "-....", '7': "--...", '8': "---..", '9': "----.",
            '?': "..--..", '!': "-.-.--", '.': ".-.-.-", ',': "--..--", ';': "-.-.-.",
            ':': "---...", '+': ".-.-.", '-': "-....-", '/': "-..-.", '=': "-...-",
            ' ': "/"
        }
        self.output = "" 
        
    def input_to_morse(self) -> str:
        for i in self.input:
            self.x = i.upper()
            if self.x not in self.morsehashmap:
                return "Unsupported characters! First unsupported character encountered: '"+self.x+"'"
            self.output += self.morsehashmap[self.x]
            self.output += " "
        return self.output

class Text:
    def __init__(self, s: str):
        self.input = s
        self.texthashmap = {
            ".-": 'A', "-...": 'B', "-.-.": 'C', "-..": 'D', ".": 'E', "..-.": 'F', 
            "--.": 'G', "....": 'H', "..": 'I', ".---": 'J', "-.-": 'K', ".-..": 'L', 
            "--": 'M', "-.": 'N', "---": 'O', ".--.": 'P', "--.-": 'Q', ".-.": 'R', 
            "...": 'S', "-": 'T', "..-": 'U', "...-": 'V', ".--": 'W', "-..-": 'X', 
            "-.--": 'Y', "--..": 'Z',
            "-----": '0', ".----": '1', "..---": '2', "...--": '3', "....-": '4', 
            ".....": '5', "-....": '6', "--...": '7', "---..": '8', "----.": '9',
            "..--..": '?', "-.-.--": '!', ".-.-.-": '.', "--..--": ',', "-.-.-.": ';',
            "---...": ':', ".-.-.": '+', "-....-": '-', "-..-.": '/', "-...-": '=',
            "/": ' '
        }
        self.output = ""
        
    def input_to_text(self) -> str:
        self.split = self.input.split()
        for i in self.split:
            if(i in self.texthashmap):
                self.output += self.texthashmap[i]
            else:
                return "Invalid Input!"
        return self.output
        
def create_window():
    
    #Text to Morse
    
    window = tk.Tk()
    window.title("Text <---> Morse")
    window.geometry("1920x1080")

    start1_label = tk.Label(window, text = "TEXT TO MORSE CONVERTER (Please Note that / represents a space in the ouput)", bg = "red", justify = "center")
    start1_label.grid(row = 0, column = 0)
    input_label = tk.Label(window, text="PLEASE ENTER YOUR INPUT: ", bg="yellow")
    input_label.grid(row=1, column=0)

    global entry
    entry = tk.Entry(window, width=50)
    entry.grid(row=1, column=1)

    morse_text = tk.Text(window, height=10, width=70, wrap=tk.WORD, font=("Helvetica", 16))
    morse_text.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

    def convert_to_morse():
        input_ = entry.get()
        a = Morse(input_)
        morse_text.delete(1.0, tk.END)
        morse_text.insert(tk.END, a.input_to_morse())

    entry_button = tk.Button(window, text="Submit", command=convert_to_morse)
    entry_button.grid(row=1, column=2)

    def clear_1():
        entry.delete(0, tk.END)
        morse_text.delete(1.0, tk.END)

    clear_button = tk.Button(window, text="Clear", command=clear_1)
    clear_button.grid(row = 3, column = 5, padx = 2, pady = 2)
    
    #Morse to Text
    
    random_label = tk.Label(window, text = "\n\n\n")
    random_label.grid(row = 13, column = 0)
    start2_label = tk.Label(window, text = "MORSE TO TEXT CONVERTER (Please Use Spaces Between Letters and use only . and - based input)", bg = "red", justify = "left")
    start2_label.grid(row = 14, column = 0)
    input2_label = tk.Label(window, text="PLEASE ENTER YOUR INPUT: ", bg="yellow")
    input2_label.grid(row = 15, column = 0)
    
    global entry2
    entry2 = tk.Entry(window, width=50)
    entry2.grid(row = 15, column = 1)

    text_text = tk.Text(window, height=10, width=70, wrap=tk.WORD, font=("Helvetica", 16))
    text_text.grid(row = 16, column = 0, columnspan = 3, padx = 10, pady = 10)

    def convert_to_text():
        input2_ = entry2.get()
        b = Text(input2_)
        text_text.delete(1.0, tk.END)
        text_text.insert(tk.END, b.input_to_text())

    entry2_button = tk.Button(window, text="Submit", command=convert_to_text)
    entry2_button.grid(row=15, column=2)

    def clear_2():
        entry2.delete(0, tk.END)
        text_text.delete(1.0, tk.END)

    clear2_button = tk.Button(window, text="Clear", command=clear_2)
    clear2_button.grid(row = 16, column = 5, padx = 2, pady = 2)

    window.mainloop()

create_window()