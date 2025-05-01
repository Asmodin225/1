from tkinter import *
from tkinter import ttk, messagebox
import random
import json
import os


BG_COLOR = "#FFF5E6"
BTN_COLOR = "#FFD166"
TEXT_COLOR = "#333333"

TOP_100_MOVIES = [
    {"title": "The Shawshank Redemption", "year": 1994, "rating": 9.3, "genre": "Drama",
     "directors": ["Frank Darabont"], "actors": ["Tim Robbins", "Morgan Freeman", "Bob Gunton"]},
    {"title": "The Godfather", "year": 1972, "rating": 9.2, "genre": "Crime",
     "directors": ["Francis Ford Coppola"], "actors": ["Marlon Brando", "Al Pacino", "James Caan"]},
    {"title": "The Dark Knight", "year": 2008, "rating": 9.0, "genre": "Action",
     "directors": ["Christopher Nolan"], "actors": ["Christian Bale", "Heath Ledger", "Aaron Eckhart"]},
    {"title": "Pulp Fiction", "year": 1994, "rating": 8.9, "genre": "Crime",
     "directors": ["Quentin Tarantino"], "actors": ["John Travolta", "Uma Thurman", "Samuel L. Jackson"]},
    {"title": "Fight Club", "year": 1999, "rating": 8.8, "genre": "Drama",
     "directors": ["David Fincher"], "actors": ["Brad Pitt", "Edward Norton", "Helena Bonham Carter"]},
    {"title": "Forrest Gump", "year": 1994, "rating": 8.8, "genre": "Drama",
     "directors": ["Robert Zemeckis"], "actors": ["Tom Hanks", "Robin Wright", "Gary Sinise"]},
    {"title": "Inception", "year": 2010, "rating": 8.8, "genre": "Sci-Fi",
     "directors": ["Christopher Nolan"], "actors": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page"]},
    {"title": "The Matrix", "year": 1999, "rating": 8.7, "genre": "Sci-Fi",
     "directors": ["Lana Wachowski", "Lilly Wachowski"],
     "actors": ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"]},
    {"title": "Goodfellas", "year": 1990, "rating": 8.7, "genre": "Crime",
     "directors": ["Martin Scorsese"], "actors": ["Robert De Niro", "Ray Liotta", "Joe Pesci"]},
    {"title": "The Silence of the Lambs", "year": 1991, "rating": 8.6, "genre": "Thriller",
     "directors": ["Jonathan Demme"], "actors": ["Jodie Foster", "Anthony Hopkins", "Lawrence A. Bonney"]},
    {"title": "The Grand Budapest Hotel", "year": 2014, "rating": 8.1, "genre": "Comedy",
     "directors": ["Wes Anderson"], "actors": ["Ralph Fiennes", "F. Murray Abraham", "Mathieu Amalric"]},
    {"title": "La La Land", "year": 2016, "rating": 8.0, "genre": "Musical",
     "directors": ["Damien Chazelle"], "actors": ["Ryan Gosling", "Emma Stone", "John Legend"]},
    {"title": "Blade Runner 2049", "year": 2017, "rating": 8.0, "genre": "Sci-Fi",
     "directors": ["Denis Villeneuve"], "actors": ["Ryan Gosling", "Harrison Ford", "Ana de Armas"]}
]


FAVORITES_FILE = "favorites.json"


def load_favorites():
    if os.path.exists(FAVORITES_FILE):
        with open(FAVORITES_FILE, 'r') as f:
            return json.load(f)
    return []
def show_all_movies():

    all_movies_win = Toplevel(win)
    all_movies_win.title("Список усіх фільмів")
    all_movies_win.geometry("800x600")
    all_movies_win.configure(bg=BG_COLOR)


    Label(all_movies_win, text="Список усіх фільмів",
          font=("Arial", 16, "bold"), bg=BG_COLOR).pack(pady=10)


    frame = Frame(all_movies_win, bg=BG_COLOR)
    frame.pack(fill=BOTH, expand=True, padx=20, pady=10)

    scrollbar = Scrollbar(frame)
    scrollbar.pack(side=RIGHT, fill=Y)


    text_area = Text(frame, wrap=WORD, yscrollcommand=scrollbar.set,
                     font=("Arial", 11), bg="white", padx=10, pady=10)
    text_area.pack(fill=BOTH, expand=True)
    scrollbar.config(command=text_area.yview)


    for movie in TOP_100_MOVIES:
        text_area.insert(END,
                         f"🎬 {movie['title']} ({movie['year']})\n"
                         f"⭐ Рейтинг: {movie['rating']}/10 | 🎭 Жанр: {movie['genre']}\n"
                         f"🎥 Режисери: {', '.join(movie['directors'])}\n"
                         f"👨‍🎤 Актори: {', '.join(movie['actors'][:3])}\n\n")

    text_area.config(state=DISABLED)


def save_favorites(favorites):
    with open(FAVORITES_FILE, 'w') as f:
        json.dump(favorites, f)


def add_to_favorites(movie):
    favorites = load_favorites()
    if movie not in favorites:
        favorites.append(movie)
        save_favorites(favorites)
        messagebox.showinfo("Улюблені", f"Фільм '{movie['title']}' додано до улюблених!")
    else:
        messagebox.showinfo("Улюблені", "Цей фільм вже є в улюблених")


def show_favorites():
    favorites = load_favorites()
    if not favorites:
        messagebox.showinfo("Улюблені", "У вас поки немає улюблених фільмів")
    else:
        fav_list = "\n\n".join([f"{m['title']} ({m['year']})" for m in favorites])
        messagebox.showinfo("Ваші улюблені фільми", f"Усього: {len(favorites)}\n\n{fav_list}")


def filter_movies():


    def apply_filter():
        try:
            year_from = int(year_from_entry.get()) if year_from_entry.get() else 1900
            year_to = int(year_to_entry.get()) if year_to_entry.get() else datetime.now().year
            filtered = [m for m in TOP_100_MOVIES if year_from <= m['year'] <= year_to]

            if not filtered:
                messagebox.showinfo("Результат", "Фільмів за вказаний період не знайдено")
                return

            result = "\n\n".join([f"{m['title']} ({m['year']}) - {m['genre']}" for m in filtered])
            messagebox.showinfo(f"Фільми з {year_from} по {year_to}", f"Знайдено {len(filtered)} фільмів:\n\n{result}")
            filter_win.destroy()
        except ValueError:
            messagebox.showerror("Помилка", "Введіть коректний рік (число)")

    filter_win = Toplevel(win)
    filter_win.title("Фільтрація за роком")
    filter_win.geometry("300x200")
    filter_win.configure(bg=BG_COLOR)

    Label(filter_win, text="Рік від:", bg=BG_COLOR).pack(pady=5)
    year_from_entry = Entry(filter_win)
    year_from_entry.pack()

    Label(filter_win, text="Рік до:", bg=BG_COLOR).pack(pady=5)
    year_to_entry = Entry(filter_win)
    year_to_entry.pack()

    Button(filter_win, text="Застосувати", command=apply_filter, bg=BTN_COLOR).pack(pady=15)


def show_movie_details(movie):
    details = (
        f"🎬 {movie['title']} ({movie['year']})\n\n"
        f"⭐ Рейтинг: {movie['rating']}/10\n"
        f"🎭 Жанр: {movie['genre']}\n"
        f"🎥 Режисери: {', '.join(movie['directors'])}\n"
        f"👨‍🎤 Актори: {', '.join(movie['actors'][:3])}"
    )

    detail_win = Toplevel(win)
    detail_win.title(movie['title'])
    detail_win.geometry("500x300")
    detail_win.configure(bg=BG_COLOR)

    Label(detail_win, text=details, font=("Arial", 11), justify=LEFT, bg=BG_COLOR).pack(pady=20)
    Button(detail_win, text="❤ Додати до улюблених", command=lambda: add_to_favorites(movie), bg=BTN_COLOR).pack(
        pady=10)



win = Tk()
win.title("Кіно-радник Pro")
win.geometry("650x450")
win.configure(bg=BG_COLOR)


style = ttk.Style()
style.configure("TButton", padding=6, relief="flat", background=BTN_COLOR, foreground=TEXT_COLOR)
style.map("TButton", background=[("active", "#FFAA00")])


main_frame = Frame(win, bg=BG_COLOR)
main_frame.pack(pady=20)

Label(main_frame, text="Кіно-радник IMDb Top-100",
      font=("Arial", 16, "bold"), bg=BG_COLOR).pack(pady=10)


buttons_frame = Frame(main_frame, bg=BG_COLOR)
buttons_frame.pack(pady=10)

ttk.Button(buttons_frame, text="🎲 Випадковий фільм",
           command=lambda: show_movie_details(random.choice(TOP_100_MOVIES))).grid(row=0, column=0, padx=5, pady=5)

ttk.Button(buttons_frame, text="📋 Список усіх фільмів",
           command=show_all_movies).grid(row=0, column=1, padx=5, pady=5)

ttk.Button(buttons_frame, text="🔍 Фільтрація за роком",
           command=filter_movies).grid(row=1, column=0, padx=5, pady=5)

ttk.Button(buttons_frame, text="❤ Мої улюблені",
           command=show_favorites).grid(row=1, column=1, padx=5, pady=5)


Label(win, text=f"У базі: {len(TOP_100_MOVIES)} фільмів | Оновлено: 2025",
      font=("Arial", 8), bg=BG_COLOR).pack(side=BOTTOM, pady=10)

win.mainloop()