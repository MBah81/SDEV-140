import tkinter as tk
from tkinter import messagebox
import datetime


class SchedulingApp:
    def __init__(self, master):
        try:
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

            # create an empty list to store the tasks
            self.tasks = []

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during initialization: {str(e)}")

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
                task = {"name": task_name, "datetime": task_datetime}
                self.tasks.append(task)  # add the task to the list
                messagebox.showinfo("Success", f"Task '{task_name}' added for {task_datetime}")
            except ValueError:
                messagebox.showerror("Error",
                                     "Invalid date or time format. Please enter date in yyyy-mm-dd format and time in hh:mm format")

    def view_tasks(self):
        # create a new window for displaying the tasks
        view_window = tk.Toplevel(self.master)
        view_window.title("View Tasks")

        # create a Listbox widget to display the tasks
        tasks_listbox = tk.Listbox(view_window)
        tasks_listbox.pack()

        # iterate over the tasks and add them to the Listbox
        for task in self.tasks:
            task_name = task["name"]
            task_datetime = task["datetime"]
            task_str = f"{task_name} ({task_datetime.strftime('%Y-%m-%d %H:%M')})"
            tasks_listbox.insert(tk.END, task_str)

        # add buttons to edit and delete tasks
        def edit_task():
            index = tasks_listbox.curselection()[0]
            task = self.tasks[index]
            task_name = task["name"]
            task_datetime = task["datetime"]
            self.task_name_entry.delete(0, tk.END)
            self.task_date_entry.delete(0, tk.END)
            self.task_time_entry.delete(0, tk.END)
            self.task_name_entry.insert(0, task_date)
            self.task_time_entry.insert(0,
                task_datetime.strftime('%H:%M'))

        def delete_task():
            index = tasks_listbox.curselection()[0]
            task = self.tasks[index]
            task_name = task["name"]
            task_datetime = task["datetime"]
            confirm_delete = messagebox.askyesno("Delete Task",
                                                 f"Are you sure you want to delete the task '{task_name}' for {task_datetime}?")
            if confirm_delete:
                self.tasks.pop(index)
                tasks_listbox.delete(index)

        edit_button = tk.Button(view_window, text="Edit", command=edit_task)
        edit_button.pack(side=tk.LEFT, padx=(10, 0))

        delete_button = tk.Button(view_window, text="Delete", command=delete_task)
        delete_button.pack(side=tk.LEFT, padx=(10, 0))

        # add a button to close the window
        close_button = tk.Button(view_window, text="Close", command=view_window.destroy)
        close_button.pack(side=tk.RIGHT, padx=(0, 10))

    def exit_app(self):
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = SchedulingApp(root)
    root.mainloop()
