import tkinter as tk
from tkinter import ttk
from datetime import datetime
import time
import winsound

class AlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock")
        self.root.geometry("300x200")

        self.time_label = ttk.Label(root, font=('Arial', 20))
        self.time_label.pack(pady=20)

        self.alarm_entry = ttk.Entry(root, font=('Arial', 12))
        self.alarm_entry.pack(pady=10)

        self.set_button = ttk.Button(root, text="Set Alarm", command=self.set_alarm)
        self.set_button.pack()

        self.cancel_button = ttk.Button(root, text="Cancel Alarm", command=self.cancel_alarm)
        self.cancel_button.pack()

        self.alarm_time = None
        self.update_time()

    def update_time(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        self.time_label.config(text=current_time)
        self.root.after(1000, self.update_time)

    def set_alarm(self):
        alarm_time_str = self.alarm_entry.get()
        try:
            self.alarm_time = datetime.strptime(alarm_time_str, "%H:%M")
            self.root.after(1000, self.check_alarm)
            self.alarm_entry.delete(0, tk.END)
            print("Alarm set for:", self.alarm_time.strftime("%H:%M"))
        except ValueError:
            print("Invalid time format. Please use HH:MM.")

    def check_alarm(self):
        current_time = datetime.now().strftime("%H:%M")
        if self.alarm_time.strftime("%H:%M") == current_time:
            print("Alarm!")
            winsound.Beep(1000, 1000)  # Beep sound for 1 second
        self.root.after(1000, self.check_alarm)

    def cancel_alarm(self):
        self.alarm_time = None
        print("Alarm canceled.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AlarmClock(root)
    root.mainloop()
