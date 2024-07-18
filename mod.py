import tkinter as tk



def mod():
    usernumber = float(userinput_number.get())
    usernumber2 = float(userinput_number2.get())
    result_label.config(text="หารได้ = %f" %(usernumber / usernumber2))
    result_label2.config(text="หารเอาเศษได้ = %.1f" %(usernumber % usernumber2))
             
def on_entry_click(event):
    if userinput_number.get() == "ตัวตั้ง":
        userinput_number.delete(0, "end")
def on_entry_click2(event):
    if userinput_number2.get() == "ตัวหาร":
        userinput_number2.delete(0, "end") 

root = tk.Tk()
root.title("เครื่องคำนวณหารเอาเศษ")
root.geometry('400x400')
root.option_add("*Font", "consolas 20")
userinput_number_label = tk.Label(root, text="เครื่องคำนวณหารเอาเศษ by tartah")
userinput_number_label.pack()

userinput_number = tk.Entry(root,textvariable=tk.StringVar())
userinput_number.insert(0, "ตัวตั้ง")
userinput_number.bind("<FocusIn>", on_entry_click)
userinput_number.pack()

userinput_number2 = tk.Entry(root,textvariable=tk.StringVar())
userinput_number2.insert(0, "ตัวหาร")
userinput_number2.bind("<FocusIn>", on_entry_click2)
userinput_number2.pack()

calculate_button = tk.Button(root, text="Calculate", command=mod,bg="green",fg="white") 
calculate_button.pack(side="bottom", pady=20)

result_label2 = tk.Label(root, text="")
result_label2.pack(side="bottom")

result_label = tk.Label(root, text="")
result_label.pack(side="bottom")




root.mainloop()
