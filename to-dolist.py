import tkinter as tk
from tkinter import messagebox

def on_click():
    user_input=task_entry.get()
    if user_input.strip()!= "":
        existing_tasks = task_listbox.get(0, tk.END)
        if any(task.strip().lower() == user_input.strip().lower() for task in existing_tasks):
            messagebox.showwarning("Duplicate Task", "This task already exists.")
            return
        task_listbox.insert(tk.END,user_input)
        task_entry.delete(0, tk.END)    
    else:
        messagebox.showwarning("Empty Input", "Please enter a task before clicking Add.")
def delete_task():
    selected=task_listbox.curselection()
    if selected:
        task_listbox.delete(selected[0])
    else:
        messagebox.showwarning("Select Item","No tasks selected")

def task_complete():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        task_text = task_listbox.get(index)

        # Check if it's already marked
        if not task_text.startswith("✅"):
            updated_text = "✅ " + task_text
            task_listbox.delete(index)
            task_listbox.insert(index, updated_text)
        else:
            messagebox.showinfo("Already Done", "Task is already marked as completed.")
    else:
        messagebox.showwarning("No Selection", "Please select a task to mark as completed.")
    
def task_clear():
    if task_listbox.size()==0:
         messagebox.showwarning("Empty","No tasks present to delete")   
    else:  
        messagebox.showwarning("Confirm","Are you sure you want to delete tasks")
        task_listbox.delete(0,tk.END)
    

        
        
    
root = tk.Tk()
root.title("To-do List Application")
root.geometry("1080x720")
root.configure(bg="skyblue")

# Label first
label = tk.Label(root, text="Welcome to the application", font="TimesNewRoman")
label.pack(pady=10)

# Entry widget to accept task input
task_entry = tk.Entry(root)
task_entry.pack(pady=5)

#Button Creation
button=tk.Button(root,text="Add Task",command=on_click,bg="white")
button.pack(pady=5)

delete_button=tk.Button(root,text="Delete task",command=delete_task,bg="white")
delete_button.pack(pady=5)

completed_task=tk.Button(root,text="Mark Task as Complete",command=task_complete,bg="white")
completed_task.pack(pady=5)

clear_all_task=tk.Button(root,text="Clear the task",command=task_clear,bg="white")
clear_all_task.pack(pady=5)

#List Creation
task_listbox=tk.Listbox(root)
task_listbox.pack()

root.mainloop()
