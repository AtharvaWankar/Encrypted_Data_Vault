import tkinter as tk
from tkinter import messagebox, simpledialog
import hashlib


data_entries = []

def hash_data(data):
    hashed_data = hashlib.sha256(data.encode()).hexdigest()
    return hashed_data

def save_data(name, email, address):
    hashed_name = hash_data(name)
    hashed_email = hash_data(email)
    hashed_address = hash_data(address)
    
    data = {
        'Name': hashed_name,
        'Email': hashed_email,
        'Address': hashed_address,
        'Original': {
            'Name': name,
            'Email': email,
            'Address': address
        }
    }
    data_entries.append(data)
    update_display()
    
    
    with open('data.txt', 'w') as file:
        for entry in data_entries:
            file.write(f"Name: {entry['Name']}, Email: {entry['Email']}, Address: {entry['Address']}\n")
    
    messagebox.showinfo("Success", "Data saved securely.")

def delete_data(index):
    if index < len(data_entries):
        del data_entries[index]
        update_display()
        
        # Update data.txt after deletion
        with open('data.txt', 'w') as file:
            for entry in data_entries:
                file.write(f"Name: {entry['Name']}, Email: {entry['Email']}, Address: {entry['Address']}\n")

def show_original_data(index):
    if index < len(data_entries):
        original_data = data_entries[index]['Original']
        messagebox.showinfo("Original Data", f"Name: {original_data['Name']}\nEmail: {original_data['Email']}\nAddress: {original_data['Address']}")

def update_display():
    # Clear previous entries
    for widget in data_frame.winfo_children():
        widget.destroy()
    
    
    for i, data in enumerate(data_entries):
        label = tk.Label(data_frame, text=f"Name: {data['Name']}, Email: {data['Email']}, Address: {data['Address']}")
        label.pack()

        
        button_frame = tk.Frame(data_frame)
        button_frame.pack()

       
        view_button = tk.Button(button_frame, text="View Original", command=lambda idx=i: show_original_data(idx))
        view_button.pack(side=tk.LEFT, padx=5)

        
        delete_button = tk.Button(button_frame, text="Delete", command=lambda idx=i: delete_data(idx))
        delete_button.pack(side=tk.LEFT, padx=5)

def submit():
    name = entry_name.get()
    email = entry_email.get()
    address = entry_address.get()
    
    save_data(name, email, address)


root = tk.Tk()
root.title("Secure Data Entry")
root.geometry("600x400")

label_name = tk.Label(root, text="Name:")
label_name.pack()

entry_name = tk.Entry(root)
entry_name.pack()

label_email = tk.Label(root, text="Email:")
label_email.pack()

entry_email = tk.Entry(root)
entry_email.pack()

label_address = tk.Label(root, text="Address:")
label_address.pack()

entry_address = tk.Entry(root)
entry_address.pack()

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()


data_frame = tk.Frame(root)
data_frame.pack(pady=20)

root.mainloop()
