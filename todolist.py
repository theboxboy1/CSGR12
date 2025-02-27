import tkinter
import tkinter.messagebox
import pickle
from PIL import Image, ImageTk  # Import PIL for better image support

root = tkinter.Tk()
root.title("To-Do List by Zakariya, Lukas, Edward, Alex")

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")

def load_tasks():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Cannot find tasks.dat.")

def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))

# Create GUI
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

button_add_task = tkinter.Button(root, text="Add task", width=48, command=add_task)
button_add_task.pack()

button_delete_task = tkinter.Button(root, text="Delete task", width=48, command=delete_task)
button_delete_task.pack()

button_load_tasks = tkinter.Button(root, text="Load tasks", width=48, command=load_tasks)
button_load_tasks.pack()

button_save_tasks = tkinter.Button(root, text="Save tasks", width=48, command=save_tasks)
button_save_tasks.pack()

# Add Ad Spot 1 (ad.png)
try:
    ad_image = Image.open(r"C:\Users\zyahm\Downloads\ad.png")  # Path to the first image
    ad_image = ad_image.resize((300, 100))  # Resize for better fit
    ad_photo = ImageTk.PhotoImage(ad_image)

    ad_label = tkinter.Label(root, image=ad_photo)
    ad_label.image = ad_photo  # Keep a reference to avoid garbage collection
    ad_label.pack(pady=10)  # Adds spacing below
except:
    ad_label = tkinter.Label(root, text="Ad Space 1", font=("Arial", 14, "bold"), bg="gray", width=40, height=5)
    ad_label.pack(pady=10)

# Add Ad Spot 2 (boyboy.png)
try:
    boyboy_image = Image.open(r"C:\Users\zyahm\Downloads\boyboy.png")  # Path to the second image
    boyboy_image = boyboy_image.resize((300, 100))  # Resize for better fit
    boyboy_photo = ImageTk.PhotoImage(boyboy_image)

    boyboy_label = tkinter.Label(root, image=boyboy_photo)
    boyboy_label.image = boyboy_photo  
    boyboy_label.pack(pady=10)  # Adds spacing below
except:
    boyboy_label = tkinter.Label(root, text="Ad Space 2", font=("Arial", 14, "bold"), bg="gray", width=40, height=5)
    boyboy_label.pack(pady=10)

root.mainloop()
