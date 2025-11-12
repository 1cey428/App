import tkinter as tk

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '{', '}', '[', ']', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/','~','`']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']



def varifier():
    global entry
    entry = pass_entry.get()
    if not any(char in symbols for char in entry) and not any(char in numbers for char in entry):
        print("weak password")
        print("You should add some symbols or numbers")
    elif any (char in symbols for char in entry) and not any(char in numbers for char in entry):
        print("medium password")
        print("You should add some numbers")
    elif any(char in numbers for char in entry) and not any(char in symbols for char in entry):
        print("medium password")
        print("You should add some Symbols")
    else:
        print("strong password")



def passcheck():
    pass_button.destroy()
    #password entry
    global pass_entry 
    pass_entry= tk.Entry(window)
    pass_entry.grid(row=0, column=0, padx=5, pady=10)
    #enter button
    enter = tk.Button(window, text = "Enter", bg = "white", fg ="black", command = varifier)
    enter.grid(row=0, column=1, padx=5, pady=10)

    


#Main window
window = tk.Tk()
window.title("The Cove")
window.geometry("400x400")
window.configure(bg="lightblue")  # Light blue background

#interaction
pass_button = tk.Button(window, text="Password Checker", bg="white", fg="black" , command= passcheck)
pass_button.grid(row = 0, column= 6, padx=5, pady=10)

window.mainloop()
