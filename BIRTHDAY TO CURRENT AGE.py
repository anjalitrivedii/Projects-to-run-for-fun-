import tkinter as tk
from tkinter import messagebox
from datetime import datetime


class AgeCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎂 Birthday to Age Calculator")
        self.root.geometry("400x250")
        self.root.config(bg="#222831")

        tk.Label(root, text="Enter Your Birthday (YYYY-MM-DD):", bg="#222831", fg="white", font=("Arial", 12)).pack(
            pady=10)

        self.birthday_entry = tk.Entry(root, font=("Arial", 12), width=25)
        self.birthday_entry.pack(pady=5)

        calc_btn = tk.Button(root, text="Calculate Age", command=self.calculate_age, bg="#00ADB5", fg="white",
                             font=("Arial", 12))
        calc_btn.pack(pady=15)

        self.result_label = tk.Label(root, text="", bg="#222831", fg="white", font=("Arial", 14, "bold"))
        self.result_label.pack(pady=10)

    def calculate_age(self):
        birth_str = self.birthday_entry.get().strip()
        try:
            birth_date = datetime.strptime(birth_str, "%Y-%m-%d")
            today = datetime.today()

            # Calculate age in years, months, days
            years = today.year - birth_date.year
            months = today.month - birth_date.month
            days = today.day - birth_date.day

            if days < 0:
                months -= 1
                days += 30  # Approximate, not exact days of the month

            if months < 0:
                years -= 1
                months += 12

            self.result_label.config(
                text=f"You are {years} years, {months} months,\n{days} days old 🎉"
            )
        except ValueError:
            messagebox.showerror("Invalid Date", "Please enter date in YYYY-MM-DD format.")


if __name__ == "__main__":
    root = tk.Tk()
    app = AgeCalculatorApp(root)
    root.mainloop()
