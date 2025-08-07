import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import os
from datetime import datetime
import csv

class SpendingAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Monthly Spending Analyzer")
        self.root.geometry("600x500")
        self.root.configure(bg="#222831")

        self.data_file = "spending_data.json"
        self.spending_data = self.load_data()

        self.create_widgets()
        self.update_summary()

    def create_widgets(self):
        title = tk.Label(self.root, text="💸 Monthly Spending Analyzer", font=("Arial", 18, "bold"), bg="#222831", fg="white")
        title.pack(pady=10)

        form_frame = tk.Frame(self.root, bg="#393E46")
        form_frame.pack(pady=10, padx=20, fill='x')

        tk.Label(form_frame, text="Date (YYYY-MM-DD):", bg="#393E46", fg="white").grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = tk.Entry(form_frame)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)
        self.date_entry.insert(0, datetime.today().strftime('%Y-%m-%d'))

        tk.Label(form_frame, text="Category:", bg="#393E46", fg="white").grid(row=1, column=0, padx=5, pady=5)
        self.category_entry = tk.Entry(form_frame)
        self.category_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Amount (₹):", bg="#393E46", fg="white").grid(row=2, column=0, padx=5, pady=5)
        self.amount_entry = tk.Entry(form_frame)
        self.amount_entry.grid(row=2, column=1, padx=5, pady=5)

        add_btn = tk.Button(form_frame, text="➕ Add Expense", command=self.add_expense, bg="#00ADB5", fg="white")
        add_btn.grid(row=3, columnspan=2, pady=10)

        self.tree = ttk.Treeview(self.root, columns=("Date", "Category", "Amount"), show="headings")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Category", text="Category")
        self.tree.heading("Amount", text="Amount (₹)")
        self.tree.pack(pady=10, padx=10, fill='both', expand=True)

        summary_frame = tk.Frame(self.root, bg="#222831")
        summary_frame.pack(pady=10)

        self.total_label = tk.Label(summary_frame, text="Total this month: ₹0", font=("Arial", 12, "bold"), bg="#222831", fg="white")
        self.total_label.pack()

        export_btn = tk.Button(self.root, text="📤 Export to CSV", command=self.export_data, bg="#F96D00", fg="white")
        export_btn.pack(pady=5)

        self.refresh_treeview()

    def add_expense(self):
        date = self.date_entry.get().strip()
        category = self.category_entry.get().strip()
        amount = self.amount_entry.get().strip()

        if not (date and category and amount):
            messagebox.showwarning("Input Error", "Please fill all fields.")
            return

        try:
            datetime.strptime(date, "%Y-%m-%d")
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Input Error", "Invalid date or amount format.")
            return

        entry = {"date": date, "category": category, "amount": amount}
        self.spending_data.append(entry)
        self.save_data()
        self.refresh_treeview()
        self.clear_fields()
        self.update_summary()

    def refresh_treeview(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for item in self.spending_data:
            self.tree.insert('', 'end', values=(item["date"], item["category"], f"₹{item['amount']:,.2f}"))

    def update_summary(self):
        month = datetime.today().strftime("%Y-%m")
        total = sum(item['amount'] for item in self.spending_data if item['date'].startswith(month))
        self.total_label.config(text=f"Total this month: ₹{total:,.2f}")

    def clear_fields(self):
        self.category_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                return json.load(f)
        return []

    def save_data(self):
        with open(self.data_file, "w") as f:
            json.dump(self.spending_data, f, indent=4)

    def export_data(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if file_path:
            with open(file_path, "w", newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Date", "Category", "Amount"])
                for item in self.spending_data:
                    writer.writerow([item["date"], item["category"], item["amount"]])
            messagebox.showinfo("Exported", "Spending data exported successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = SpendingAnalyzerApp(root)
    root.mainloop()
