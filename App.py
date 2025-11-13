import tkinter as tk

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '{', '}', '[', ']', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/','~','`']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']



def varifier():
    global entry
    entry = pass_entry.get()
    if not any(char in symbols for char in entry) and not any(char in numbers for char in entry):
        weakpw = tk.Label(window, text="*weak password. You should add numbers or characters", bg="lightblue", fg="red")
        weakpw.grid(row=1, column=4, padx=1, pady=10)
    
    elif any (char in symbols for char in entry) and not any(char in numbers for char in entry):
        medpw = tk.Label(window, text="*Medium password. You should add numbers", bg="lightblue", fg="red")
        medpw.grid(row=1, column=4, padx=1, pady=10)
    
    elif any(char in numbers for char in entry) and not any(char in symbols for char in entry):
        medpw2 = tk.Label(window, text="*Medium password. You should add Symbols", bg="lightblue", fg="red")
        medpw2.grid(row=1, column=4, padx=1, pady=10)

    else:
        strongpw = tk.Label(window, text="*Strong Password", bg="lightblue", fg="green")
        strongpw.grid(row=1, column=4, padx=1, pady=10)



def passcheck():
    pass_button.destroy()
    #password entry
    global pass_entry 
    pass_entry= tk.Entry(window)
    pass_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
    #enter button
    enter = tk.Button(window, text = "Enter", bg = "white", fg ="black", command = varifier)
    enter.grid(row=1, column=2, columnspan=2, padx=1, pady=10)
    back_button = tk.Button(window, text="<-- Back", bg="Red", fg="white", width= 20, command= window.destroy)
    back_button .grid(row=3, column=0, padx = 10, pady=10)




#Main window
window = tk.Tk()
window.title("The Cove")
window.geometry("400x400")
window.configure(bg="lightblue")  # Light blue background
title =  tk.Label (window, text="The Cove", bg="lightblue", fg="black", font=("Arial", 23))
title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

#interaction
pass_button = tk.Button(window, text="Password Checker", bg="white", fg="black" , width= 20, command= passcheck)
pass_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)



window.mainloop()
