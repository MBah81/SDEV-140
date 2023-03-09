import tkinter as tk
from tkinter import messagebox

class SchedulingApp:

    def __init__(self, master):
        self.master = master
        self.master.title("Scheduling App")

        # create the labels
        tk.Label(master, text="Task Name:").grid(row=0, sticky=tk.W)
        tk.Label(master, text="Task Date:").grid(row=1, sticky=tk.W)
        tk.Label(master, text="Task Time:").grid(row=2, sticky=tk.W)

        # create the entry boxes
        self.task_name_entry = tk.Entry(master)
        self.task_name_entry.grid(row=0, column=1)
        self.task_date_entry = tk.Entry(master)
        self.task_date_entry.grid(row=1, column=1)
        self.task_time_entry = tk.Entry(master)
        self.task_time_entry.grid(row=2, column=1)

        # create the buttons
        tk.Button(master, text="Add Task", command=self.add_task).grid(row=3, column=0)
        tk.Button(master, text="View Tasks", command=self.view_tasks).grid(row=3, column=1)
        tk.Button(master, text="Exit", command=self.exit_app).grid(row=3, column=2)

    # callback functions for the buttons
    def add_task(self):
        task_name = self.task_name_entry.get()
        task_date = self.task_date_entry.get()
        task_time = self.task_time_entry.get()

        if not all([task_name, task_date, task_time]):
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                task_datetime = datetime.datetime.strptime(f"{task_date} {task_time}", "%Y-%m-%d %H:%M")
                messagebox.showinfo("Success", f"Task '{task_name}' added for {task_datetime}")
            except ValueError:
                messagebox.showerror("Error", "Invalid date or time format")

    def view_tasks(self):
        messagebox.showinfo("View Tasks", "Not implemented yet")

    def exit_app(self):
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SchedulingApp(root)
    root.mainloop()


