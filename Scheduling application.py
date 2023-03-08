import tkinter as tk
from tkinter import messagebox

class Application:
    def __init__(self, master):
        self.master = master
        self.master.title("Scheduling Application")

        # Create main window
        self.main_frame = tk.Frame(self.master, padx=10, pady=10)
        self.main_frame.pack()

        # Create label
        self.label = tk.Label(self.main_frame, text="Welcome to Scheduling Application!")
        self.label.pack(pady=10)

        # Create buttons
        self.create_button = tk.Button(self.main_frame, text="Create Schedule", command=self.create_schedule)
        self.create_button.pack(pady=5)

        self.view_button = tk.Button(self.main_frame, text="View Schedule", command=self.view_schedule)
        self.view_button.pack(pady=5)

        self.exit_button = tk.Button(self.main_frame, text="Exit", command=self.master.destroy)
        self.exit_button.pack(pady=5)

    def create_schedule(self):
        # Create secondary window
        self.create_frame = tk.Toplevel(self.master)
        self.create_frame.title("Create Schedule")

        # Create label
        self.create_label = tk.Label(self.create_frame, text="Enter Schedule Details:")
        self.create_label.pack(pady=10)

        # Create entry boxes
        self.title_label = tk.Label(self.create_frame, text="Title:")
        self.title_label.pack()
        self.title_entry = tk.Entry(self.create_frame)
        self.title_entry.pack()

        self.date_label = tk.Label(self.create_frame, text="Date:")
        self.date_label.pack()
        self.date_entry = tk.Entry(self.create_frame)
        self.date_entry.pack()

        self.time_label = tk.Label(self.create_frame, text="Time:")
        self.time_label.pack()
        self.time_entry = tk.Entry(self.create_frame)
        self.time_entry.pack()

        # Create button
        self.save_button = tk.Button(self.create_frame, text="Save", command=self.save_schedule)
        self.save_button.pack(pady=5)

    def view_schedule(self):
        # Create secondary window
        self.view_frame = tk.Toplevel(self.master)
        self.view_frame.title("View Schedule")

        # Create label
        self.view_label = tk.Label(self.view_frame, text="Your Schedule:")
        self.view_label.pack(pady=10)

        # Create text box
        self.schedule_text = tk.Text(self.view_frame, width=50, height=10)
        self.schedule_text.pack()

    def save_schedule(self):
        # Get input values
        title = self.title_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()

        # Validate input values
        if not title or not date or not time:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Save schedule
        schedule = f"{title}\t{date}\t{time}\n"
        with open("schedule.txt", "a") as f:
            f.write(schedule)

        # Clear input values
        self.title_entry.delete(0, tk

