import tkinter as tk
from tkinter import messagebox, font
from PIL import Image, ImageTk
from fpdf import FPDF
from tkcalendar import DateEntry
import os


class FlightReservationSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Flight Reservation System")
        self.root.geometry("800x500")
        self.root.config(bg="#2C3E50")

        self.flights = self.load_flights()
        self.bookings = []

        try:
            self.bg_image = Image.open("aeroplane.jpg")
            self.bg_image = self.bg_image.resize((800, 500), Image.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(self.bg_image)

            self.background_label = tk.Label(self.root, image=self.bg_photo)
            self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            print(f"Image not found or error: {e}")

        self.create_widgets()

    def create_widgets(self):
        title_font = font.Font(size=20, weight='bold')
        title_label = tk.Label(self.root, text="Flight Reservation System", font=title_font, bg="#2C3E50", fg="#ffffff")
        title_label.pack(pady=10)

        search_frame = tk.Frame(self.root, bg="#ffffff")
        search_frame.pack(pady=10)

        tk.Label(search_frame, text="From:", bg="#ffffff").grid(row=0, column=0, padx=5, pady=5)
        self.from_entry = tk.Entry(search_frame)
        self.from_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(search_frame, text="To:", bg="#ffffff").grid(row=1, column=0, padx=5, pady=5)
        self.to_entry = tk.Entry(search_frame)
        self.to_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(search_frame, text="Date:", bg="#ffffff").grid(row=2, column=0, padx=5, pady=5)
        self.date_entry = DateEntry(search_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.date_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Button(search_frame, text="Search Flights", command=self.search_flights, bg="#2980B9", fg="white").grid(row=3, columnspan=2, pady=10)

        self.flights_frame = tk.Frame(self.root, bg="#2C3E50")
        self.flights_frame.pack(pady=10)

        self.flights_listbox = tk.Listbox(self.flights_frame, width=70, height=10)
        self.flights_listbox.pack(padx=10, pady=10)

        tk.Button(self.flights_frame, text="Book Flight", command=self.book_flight, bg="#27AE60", fg="white").pack(pady=5)

        tk.Button(self.root, text="View All Scheduled Flights", command=self.view_all_flights, bg="#2980B9", fg="white").pack(pady=5)

        self.bookings_frame = tk.Frame(self.root, bg="#2C3E50")
        self.bookings_frame.pack(pady=10)

        tk.Button(self.bookings_frame, text="View My Bookings", command=self.view_bookings, bg="#2980B9", fg="white").pack(pady=5)

        tk.Button(self.root, text="Export Flights to PDF", command=self.export_flights_pdf, bg="#2980B9", fg="white").pack(pady=5)

    def load_flights(self):
        return [
            {"flight_no": "FL001", "from": "Delhi", "to": "London", "date": "01/10/2024",
             "departure": "22:00", "arrival": "05:30", "airline": "Air India"},
            {"flight_no": "FL002", "from": "Mumbai", "to": "New York", "date": "01/10/2024",
             "departure": "21:00", "arrival": "06:00", "airline": "Delta Airlines"},
            {"flight_no": "FL003", "from": "Chennai", "to": "Dubai", "date": "02/10/2024",
             "departure": "20:00", "arrival": "22:30", "airline": "Emirates"}
        ]

    def search_flights(self):
        from_city = self.from_entry.get().strip()
        to_city = self.to_entry.get().strip()
        date = self.date_entry.get()

        self.flights_listbox.delete(0, tk.END)
        matches = [
            flight for flight in self.flights
            if flight["from"].lower() == from_city.lower()
            and flight["to"].lower() == to_city.lower()
            and flight["date"] == date
        ]

        if matches:
            for flight in matches:
                self.flights_listbox.insert(tk.END, f"{flight['flight_no']} | {flight['from']} -> {flight['to']} | "
                                                    f"{flight['date']} | {flight['departure']} - {flight['arrival']} | "
                                                    f"{flight['airline']}")
        else:
            messagebox.showinfo("No Flights Found", "No flights found for the selected date.")
            self.show_alternative_flights(from_city, to_city)

    def show_alternative_flights(self, from_city, to_city):
        alternatives = [
            flight for flight in self.flights
            if flight["from"].lower() == from_city.lower()
            and flight["to"].lower() == to_city.lower()
        ]

        if alternatives:
            alt_msg = "Available flights on other dates:\n"
            for flight in alternatives:
                alt_msg += f"{flight['flight_no']} | {flight['date']} | {flight['departure']} - {flight['arrival']} | {flight['airline']}\n"
            messagebox.showinfo("Alternative Flights", alt_msg)
        else:
            messagebox.showinfo("No Flights", "No flights found for the selected route.")

    def view_all_flights(self):
        self.flights_listbox.delete(0, tk.END)
        for flight in self.flights:
            self.flights_listbox.insert(tk.END, f"{flight['flight_no']} | {flight['from']} -> {flight['to']} | "
                                                f"{flight['date']} | {flight['departure']} - {flight['arrival']} | "
                                                f"{flight['airline']}")

    def book_flight(self):
        selected = self.flights_listbox.curselection()
        if selected:
            flight_info = self.flights_listbox.get(selected)
            self.bookings.append(flight_info)
            messagebox.showinfo("Success", "Flight booked successfully!")
        else:
            messagebox.showwarning("Warning", "Please select a flight to book.")

    def view_bookings(self):
        if self.bookings:
            bookings_text = "\n".join(self.bookings)
            messagebox.showinfo("My Bookings", bookings_text)
        else:
            messagebox.showinfo("No Bookings", "You have no bookings yet.")

    def export_flights_pdf(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Flight Schedule", ln=True, align='C')

        for flight in self.flights:
            text = f"{flight['flight_no']} | {flight['from']} -> {flight['to']} | {flight['date']} | " \
                   f"{flight['departure']} - {flight['arrival']} | {flight['airline']}"
            pdf.cell(200, 10, txt=text, ln=True, align='L')

        filename = "flights_schedule.pdf"
        pdf.output(filename)
        messagebox.showinfo("Export Successful", f"Flights exported to {filename}")


# Start GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = FlightReservationSystem(root)
    root.mainloop()

