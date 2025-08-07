# import requests
# import tkinter as tk
# from tkinter import ttk
# from PIL import Image, ImageTk
# import io
# import webbrowser
#
# # ----------------- Open URL in browser -----------------
# def open_url(event, url):
#     webbrowser.open_new(url)
#
# # ----------------- Fetch News -----------------
# def fetch_news():
#     url = "https://newsapi.org/v2/everything"
#     params = {
#         "q": "tesla",
#         "from": "2025-07-01",
#         "sortBy": "publishedAt",
#         "apiKey": "4a391eb2d1394a038152fb079373b327"
#     }
#
#     try:
#         response = requests.get(url, params=params)
#         response.raise_for_status()
#         data = response.json()
#         articles = data.get("articles", [])
#
#         for widget in frame.winfo_children():
#             widget.destroy()
#
#         if not articles:
#             ttk.Label(frame, text="No articles found.", foreground="red").pack()
#             return
#
#         for i, article in enumerate(articles[:10], 1):
#             title = article.get('title', 'No Title')
#             author = article.get('author', 'Unknown Author')
#             source = article.get('source', {}).get('name', 'Unknown Source')
#             published = article.get('publishedAt', 'No Date')
#             link_url = article.get('url', '')
#             image_url = article.get('urlToImage', '')
#
#             # Frame for each article
#             article_frame = ttk.Frame(frame)
#             article_frame.pack(fill='x', padx=10, pady=10)
#
#             # Fetch and show image (thumbnail)
#             if image_url:
#                 try:
#                     img_data = requests.get(image_url, timeout=5).content
#                     img = Image.open(io.BytesIO(img_data))
#                     img.thumbnail((150, 100))
#                     photo = ImageTk.PhotoImage(img)
#
#                     img_label = ttk.Label(article_frame, image=photo)
#                     img_label.image = photo  # Save reference
#                     img_label.pack(side='left', padx=5)
#                 except:
#                     pass  # Skip image if it fails
#
#             # Textual details
#             text_frame = ttk.Frame(article_frame)
#             text_frame.pack(side='left', fill='x', expand=True)
#
#             ttk.Label(text_frame, text=f"{i}. {title}", font=('Arial', 12, 'bold')).pack(anchor='w')
#             ttk.Label(text_frame, text=f"By {author} | Source: {source}", font=('Arial', 10)).pack(anchor='w')
#             ttk.Label(text_frame, text=f"Published At: {published}", font=('Arial', 9)).pack(anchor='w')
#
#             link = ttk.Label(text_frame, text=link_url, foreground="blue", cursor="hand2")
#             link.pack(anchor='w', pady=(0, 5))
#             link.bind("<Button-1>", lambda e, url=link_url: open_url(e, url))
#
#     except requests.exceptions.RequestException as e:
#         ttk.Label(frame, text=f"API Error: {e}", foreground="red").pack()
#     except Exception as e:
#         ttk.Label(frame, text=f"Error: {e}", foreground="red").pack()
#
# # ----------------- GUI Setup -----------------
# root = tk.Tk()
# root.title("Tesla News with Images")
# root.geometry("800x600")
#
# canvas = tk.Canvas(root)
# scroll_y = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
#
# frame = ttk.Frame(canvas)
# frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
#
# canvas.create_window((0, 0), window=frame, anchor="nw")
# canvas.configure(yscrollcommand=scroll_y.set)
#
# canvas.pack(side="left", fill="both", expand=True)
# scroll_y.pack(side="right", fill="y")
#
# fetch_news()
#
# root.mainloop()
import requests
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import io
import webbrowser

# --------------- Function: Open URL in browser ---------------
def open_url(url):
    webbrowser.open_new(url)

# --------------- Function: Open Detail Screen ---------------
def open_detail(article):
    detail_win = tk.Toplevel(root)
    detail_win.title("Article Details")
    detail_win.geometry("600x600")

    title = article.get("title", "No Title")
    author = article.get("author", "Unknown Author")
    source = article.get("source", {}).get("name", "Unknown Source")
    published = article.get("publishedAt", "No Date")
    url = article.get("url", "")
    image_url = article.get("urlToImage", "")

    ttk.Label(detail_win, text=title, wraplength=550, font=('Arial', 14, 'bold')).pack(pady=10)
    ttk.Label(detail_win, text=f"By {author}", font=('Arial', 10)).pack()
    ttk.Label(detail_win, text=f"Source: {source}", font=('Arial', 10)).pack()
    ttk.Label(detail_win, text=f"Published: {published}", font=('Arial', 9)).pack(pady=5)

    # Show full image if available
    if image_url:
        try:
            img_data = requests.get(image_url, timeout=5).content
            img = Image.open(io.BytesIO(img_data))
            img.thumbnail((500, 300))
            photo = ImageTk.PhotoImage(img)

            img_label = ttk.Label(detail_win, image=photo)
            img_label.image = photo  # Prevent garbage collection
            img_label.pack(pady=10)
        except:
            pass

    # Button to open link in browser
    open_btn = ttk.Button(detail_win, text="Read Full Article", command=lambda: open_url(url))
    open_btn.pack(pady=20)

# --------------- Function: Fetch and Show News ---------------
def fetch_news():
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": "ahmedabad",
        "from": "2025-07-10",
        "sortBy": "publishedAt",
        "apiKey": "4a391eb2d1394a038152fb079373b327"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        articles = data.get("articles", [])

        for widget in frame.winfo_children():
            widget.destroy()

        if not articles:
            ttk.Label(frame, text="No articles found.", foreground="red").pack()
            return

        for i, article in enumerate(articles[:10], 1):
            title = article.get('title', 'No Title')
            image_url = article.get('urlToImage', '')

            # Container for one article
            article_frame = ttk.Frame(frame)
            article_frame.pack(fill='x', padx=10, pady=10)

            # Thumbnail
            if image_url:
                try:
                    img_data = requests.get(image_url, timeout=5).content
                    img = Image.open(io.BytesIO(img_data))
                    img.thumbnail((120, 80))
                    photo = ImageTk.PhotoImage(img)

                    img_label = ttk.Label(article_frame, image=photo, cursor="hand2")
                    img_label.image = photo
                    img_label.pack(side='left', padx=5)
                    img_label.bind("<Button-1>", lambda e, art=article: open_detail(art))
                except:
                    pass

            # Title and info
            text_frame = ttk.Frame(article_frame)
            text_frame.pack(side='left', fill='x', expand=True)

            title_label = ttk.Label(text_frame, text=f"{i}. {title}", font=('Arial', 12, 'bold'), wraplength=500, cursor="hand2")
            title_label.pack(anchor='w')
            title_label.bind("<Button-1>", lambda e, art=article: open_detail(art))

    except requests.exceptions.RequestException as e:
        ttk.Label(frame, text=f"API Error: {e}", foreground="red").pack()
    except Exception as e:
        ttk.Label(frame, text=f"Error: {e}", foreground="red").pack()

# --------------- GUI Setup ---------------
root = tk.Tk()
root.title("Tesla News")
root.geometry("800x600")

canvas = tk.Canvas(root)
scroll_y = tk.Scrollbar(root, orient="vertical", command=canvas.yview)

frame = ttk.Frame(canvas)
frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

canvas.create_window((0, 0), window=frame, anchor="nw")
canvas.configure(yscrollcommand=scroll_y.set)

canvas.pack(side="left", fill="both", expand=True)
scroll_y.pack(side="right", fill="y")

fetch_news()

root.mainloop()
