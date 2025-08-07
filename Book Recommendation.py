import tkinter as tk
from tkinter import ttk
from tkinter import font

# Book database
books = [
    {"title": "It Ends With Us", "author": "Colleen Hoover", "genre": "Romance"},
    {"title": "It Starts With Us", "author": "Colleen Hoover", "genre": "Romance"},
    {"title": "Ugly Love", "author": "Colleen Hoover", "genre": "Romance"},
    {"title": "Reminders of Him", "author": "Colleen Hoover", "genre": "Romance"},
    {"title": "The Alchemist", "author": "Paulo Coelho", "genre": "Fiction"},
    {"title": "Verity", "author": "Colleen Hoover", "genre": "Thriller"},
    {"title": "November 9", "author": "Colleen Hoover", "genre": "Romance"},
    {"title": "The Power of Habit", "author": "Charles Duhigg", "genre": "Self-help"},
    {"title": "Atomic Habits", "author": "James Clear", "genre": "Self-help"},
    {"title": "The 7 Habits of Highly Effective People", "author": "Stephen Covey", "genre": "Self-help"},
    {"title": "Think and Grow Rich", "author": "Napoleon Hill", "genre": "Finance"},
    {"title": "Rich Dad Poor Dad", "author": "Robert Kiyosaki", "genre": "Finance"},
    {"title": "The Psychology of Money", "author": "Morgan Housel", "genre": "Finance"},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "genre": "Fantasy"},
    {"title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "genre": "Fantasy"},
    {"title": "Harry Potter and the Prisoner of Azkaban", "author": "J.K. Rowling", "genre": "Fantasy"},
    {"title": "Sapiens", "author": "Yuval Noah Harari", "genre": "History"},
    {"title": "Ikigai", "author": "Francesc Miralles", "genre": "Self-help"},
    {"title": "The Subtle Art of Not Giving a F*ck", "author": "Mark Manson", "genre": "Self-help"},
    {"title": "Deep Work", "author": "Cal Newport", "genre": "Productivity"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction"},
    {"title": "1984", "author": "George Orwell", "genre": "Fiction"},
    {"title": "Gone Girl", "author": "Gillian Flynn", "genre": "Thriller"},
    {"title": "The Silent Patient", "author": "Alex Michaelides", "genre": "Thriller"},
    {"title": "Angels & Demons", "author": "Dan Brown", "genre": "Mystery"},
    {"title": "Inferno", "author": "Dan Brown", "genre": "Mystery"},
    {"title": "The Girl on the Train", "author": "Paula Hawkins", "genre": "Thriller"},
    {"title": "A Brief History of Time", "author": "Stephen Hawking", "genre": "Science"},
    {"title": "Becoming", "author": "Michelle Obama", "genre": "Biography"},
    {"title": "Educated", "author": "Tara Westover", "genre": "Biography"},
]

# Extract unique genres and authors
genres = sorted(set(book["genre"] for book in books))
authors = sorted(set(book["author"] for book in books))

# GUI logic
def recommend():
    results.delete(0, tk.END)
    if option.get() == "Genre":
        selected = genre_cb.get()
        for book in books:
            if book["genre"] == selected:
                results.insert(tk.END, f"{book['title']} by {book['author']}")
    elif option.get() == "Author":
        selected = author_cb.get()
        for book in books:
            if book["author"] == selected:
                results.insert(tk.END, f"{book['title']} ({book['genre']})")

# GUI setup
root = tk.Tk()
root.title("📚 Book Recommender")
root.geometry("480x580")
root.resizable(False, False)

# Fonts
title_font = font.Font(family="Helvetica", size=16, weight="bold")
label_font = font.Font(family="Segoe UI", size=12)
list_font = font.Font(family="Courier New", size=10)

# GUI layout with custom fonts
tk.Label(root, text="📖 Book Recommender", font=title_font).pack(pady=10)
tk.Label(root, text="Choose Recommendation Type:", font=label_font).pack(pady=5)

option = tk.StringVar(value="Genre")
ttk.Combobox(root, textvariable=option, values=["Genre", "Author"], state="readonly", font=label_font).pack(pady=5)

tk.Label(root, text="Select Genre:", font=label_font).pack(pady=5)
genre_cb = ttk.Combobox(root, values=genres, state="readonly", font=label_font)
genre_cb.pack(pady=5)

tk.Label(root, text="Select Author:", font=label_font).pack(pady=5)
author_cb = ttk.Combobox(root, values=authors, state="readonly", font=label_font)
author_cb.pack(pady=5)

tk.Button(root, text="🎯 Show Recommendations", command=recommend, font=label_font).pack(pady=10)

tk.Label(root, text="Recommended Books:", font=label_font).pack()
results = tk.Listbox(root, width=55, height=15, font=list_font)
results.pack(pady=5)

root.mainloop()
