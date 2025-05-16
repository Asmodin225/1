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
     "directors": ["Denis Villeneuve"], "actors": ["Ryan Gosling", "Harrison Ford", "Ana de Armas"]},
    {"title": "The Usual Suspects", "year": 1995, "rating": 8.5, "genre": "Crime",
     "directors": ["Bryan Singer"], "actors": ["Kevin Spacey", "Gabriel Byrne", "Chazz Palminteri"]},

    {"title": "American Beauty", "year": 1999, "rating": 8.4, "genre": "Drama",
     "directors": ["Sam Mendes"], "actors": ["Kevin Spacey", "Annette Bening", "Thora Birch"]},

    {"title": "Braveheart", "year": 1995, "rating": 8.4, "genre": "Biography",
     "directors": ["Mel Gibson"], "actors": ["Mel Gibson", "Sophie Marceau", "Patrick McGoohan"]},

    {"title": "Se7en", "year": 1995, "rating": 8.6, "genre": "Crime",
     "directors": ["David Fincher"], "actors": ["Morgan Freeman", "Brad Pitt", "Kevin Spacey"]},

    {"title": "The Sixth Sense", "year": 1999, "rating": 8.2, "genre": "Drama",
     "directors": ["M. Night Shyamalan"], "actors": ["Bruce Willis", "Haley Joel Osment", "Toni Collette"]},

    {"title": "Fargo", "year": 1996, "rating": 8.1, "genre": "Crime",
     "directors": ["Joel Coen", "Ethan Coen"], "actors": ["William H. Macy", "Frances McDormand", "Steve Buscemi"]},

    {"title": "The Big Lebowski", "year": 1998, "rating": 8.1, "genre": "Comedy",
     "directors": ["Joel Coen", "Ethan Coen"], "actors": ["Jeff Bridges", "John Goodman", "Julianne Moore"]},

    {"title": "Trainspotting", "year": 1996, "rating": 8.2, "genre": "Drama",
     "directors": ["Danny Boyle"], "actors": ["Ewan McGregor", "Ewen Bremner", "Jonny Lee Miller"]},

    {"title": "The Truman Show", "year": 1998, "rating": 8.2, "genre": "Comedy",
     "directors": ["Peter Weir"], "actors": ["Jim Carrey", "Ed Harris", "Laura Linney"]},

    {"title": "Jurassic Park", "year": 1993, "rating": 8.2, "genre": "Adventure",
     "directors": ["Steven Spielberg"], "actors": ["Sam Neill", "Laura Dern", "Jeff Goldblum"]},

    {"title": "Terminator 2: Judgment Day", "year": 1991, "rating": 8.6, "genre": "Action",
     "directors": ["James Cameron"], "actors": ["Arnold Schwarzenegger", "Linda Hamilton", "Edward Furlong"]},
    {"title": "Psycho", "year": 1960, "rating": 8.5, "genre": "Horror",
     "directors": ["Alfred Hitchcock"], "actors": ["Anthony Perkins", "Janet Leigh", "Vera Miles"]},

    {"title": "The Apartment", "year": 1960, "rating": 8.3, "genre": "Comedy",
     "directors": ["Billy Wilder"], "actors": ["Jack Lemmon", "Shirley MacLaine", "Fred MacMurray"]},

    {"title": "Lawrence of Arabia", "year": 1962, "rating": 8.3, "genre": "Adventure",
     "directors": ["David Lean"], "actors": ["Peter O'Toole", "Alec Guinness", "Anthony Quinn"]},

    {"title": "To Kill a Mockingbird", "year": 1962, "rating": 8.3, "genre": "Drama",
     "directors": ["Robert Mulligan"], "actors": ["Gregory Peck", "John Megna", "Frank Overton"]},

    {"title": "8½", "year": 1963, "rating": 8.0, "genre": "Drama",
     "directors": ["Federico Fellini"], "actors": ["Marcello Mastroianni", "Anouk Aimée", "Claudia Cardinale"]},

    {"title": "Dr. Strangelove", "year": 1964, "rating": 8.4, "genre": "Comedy",
     "directors": ["Stanley Kubrick"], "actors": ["Peter Sellers", "George C. Scott", "Sterling Hayden"]},

    {"title": "The Good, the Bad and the Ugly", "year": 1966, "rating": 8.8, "genre": "Western",
     "directors": ["Sergio Leone"], "actors": ["Clint Eastwood", "Lee Van Cleef", "Eli Wallach"]},

    {"title": "Persona", "year": 1966, "rating": 8.1, "genre": "Drama",
     "directors": ["Ingmar Bergman"], "actors": ["Bibi Andersson", "Liv Ullmann", "Margaretha Krook"]},

    {"title": "Cool Hand Luke", "year": 1967, "rating": 8.1, "genre": "Drama",
     "directors": ["Stuart Rosenberg"], "actors": ["Paul Newman", "George Kennedy", "Strother Martin"]},

    {"title": "2001: A Space Odyssey", "year": 1968, "rating": 8.3, "genre": "Sci-Fi",
     "directors": ["Stanley Kubrick"], "actors": ["Keir Dullea", "Gary Lockwood", "William Sylvester"]},

    {"title": "Rosemary's Baby", "year": 1968, "rating": 8.0, "genre": "Horror",
     "directors": ["Roman Polanski"], "actors": ["Mia Farrow", "John Cassavetes", "Ruth Gordon"]},

    {"title": "Once Upon a Time in the West", "year": 1968, "rating": 8.5, "genre": "Western",
     "directors": ["Sergio Leone"], "actors": ["Henry Fonda", "Charles Bronson", "Claudia Cardinale"]},

    {"title": "Midnight Cowboy", "year": 1969, "rating": 8.0, "genre": "Drama",
     "directors": ["John Schlesinger"], "actors": ["Dustin Hoffman", "Jon Voight", "Sylvia Miles"]},
    {"title": "Sunset Boulevard", "year": 1950, "rating": 8.4, "genre": "Drama",
     "directors": ["Billy Wilder"], "actors": ["William Holden", "Gloria Swanson", "Erich von Stroheim"]},

    {"title": "All About Eve", "year": 1950, "rating": 8.2, "genre": "Drama",
     "directors": ["Joseph L. Mankiewicz"], "actors": ["Bette Davis", "Anne Baxter", "George Sanders"]},

    {"title": "Singin' in the Rain", "year": 1952, "rating": 8.3, "genre": "Musical",
     "directors": ["Stanley Donen", "Gene Kelly"], "actors": ["Gene Kelly", "Donald O'Connor", "Debbie Reynolds"]},

    {"title": "Tokyo Story", "year": 1953, "rating": 8.1, "genre": "Drama",
     "directors": ["Yasujirō Ozu"], "actors": ["Chishū Ryū", "Chieko Higashiyama", "Setsuko Hara"]},

    {"title": "On the Waterfront", "year": 1954, "rating": 8.1, "genre": "Crime",
     "directors": ["Elia Kazan"], "actors": ["Marlon Brando", "Karl Malden", "Lee J. Cobb"]},

    {"title": "Seven Samurai", "year": 1954, "rating": 8.6, "genre": "Action",
     "directors": ["Akira Kurosawa"], "actors": ["Toshirō Mifune", "Takashi Shimura", "Keiko Tsushima"]},

    {"title": "Rear Window", "year": 1954, "rating": 8.5, "genre": "Mystery",
     "directors": ["Alfred Hitchcock"], "actors": ["James Stewart", "Grace Kelly", "Wendell Corey"]},

    {"title": "The Night of the Hunter", "year": 1955, "rating": 8.0, "genre": "Thriller",
     "directors": ["Charles Laughton"], "actors": ["Robert Mitchum", "Shelley Winters", "Lillian Gish"]},

    {"title": "12 Angry Men", "year": 1957, "rating": 9.0, "genre": "Drama",
     "directors": ["Sidney Lumet"], "actors": ["Henry Fonda", "Lee J. Cobb", "Martin Balsam"]},

    {"title": "Paths of Glory", "year": 1957, "rating": 8.4, "genre": "War",
     "directors": ["Stanley Kubrick"], "actors": ["Kirk Douglas", "Ralph Meeker", "Adolphe Menjou"]},

    {"title": "Vertigo", "year": 1958, "rating": 8.3, "genre": "Mystery",
     "directors": ["Alfred Hitchcock"], "actors": ["James Stewart", "Kim Novak", "Barbara Bel Geddes"]},

    {"title": "Some Like It Hot", "year": 1959, "rating": 8.2, "genre": "Comedy",
     "directors": ["Billy Wilder"], "actors": ["Marilyn Monroe", "Tony Curtis", "Jack Lemmon"]},

    {"title": "North by Northwest", "year": 1959, "rating": 8.3, "genre": "Adventure",
     "directors": ["Alfred Hitchcock"], "actors": ["Cary Grant", "Eva Marie Saint", "James Mason"]},

    {"title": "Ben-Hur", "year": 1959, "rating": 8.1, "genre": "Adventure",
     "directors": ["William Wyler"], "actors": ["Charlton Heston", "Jack Hawkins", "Stephen Boyd"]},{"title": "The Godfather", "year": 1972, "rating": 9.2, "genre": "Crime",
     "directors": ["Francis Ford Coppola"], "actors": ["Marlon Brando", "Al Pacino", "James Caan"]},

    {"title": "The Godfather Part II", "year": 1974, "rating": 9.0, "genre": "Crime",
     "directors": ["Francis Ford Coppola"], "actors": ["Al Pacino", "Robert De Niro", "Robert Duvall"]},

    {"title": "One Flew Over the Cuckoo's Nest", "year": 1975, "rating": 8.7, "genre": "Drama",
     "directors": ["Miloš Forman"], "actors": ["Jack Nicholson", "Louise Fletcher", "Will Sampson"]},

    {"title": "Apocalypse Now", "year": 1979, "rating": 8.4, "genre": "War",
     "directors": ["Francis Ford Coppola"], "actors": ["Martin Sheen", "Marlon Brando", "Robert Duvall"]},

    {"title": "Taxi Driver", "year": 1976, "rating": 8.2, "genre": "Crime",
     "directors": ["Martin Scorsese"], "actors": ["Robert De Niro", "Jodie Foster", "Cybill Shepherd"]},

    {"title": "Chinatown", "year": 1974, "rating": 8.1, "genre": "Mystery",
     "directors": ["Roman Polanski"], "actors": ["Jack Nicholson", "Faye Dunaway", "John Huston"]},

    {"title": "A Clockwork Orange", "year": 1971, "rating": 8.3, "genre": "Sci-Fi",
     "directors": ["Stanley Kubrick"], "actors": ["Malcolm McDowell", "Patrick Magee", "Michael Bates"]},

    {"title": "Star Wars: Episode IV - A New Hope", "year": 1977, "rating": 8.6, "genre": "Sci-Fi",
     "directors": ["George Lucas"], "actors": ["Mark Hamill", "Harrison Ford", "Carrie Fisher"]},

    {"title": "The Sting", "year": 1973, "rating": 8.3, "genre": "Comedy",
     "directors": ["George Roy Hill"], "actors": ["Paul Newman", "Robert Redford", "Robert Shaw"]},

    {"title": "Annie Hall", "year": 1977, "rating": 8.0, "genre": "Comedy",
     "directors": ["Woody Allen"], "actors": ["Woody Allen", "Diane Keaton", "Tony Roberts"]},

    {"title": "The Deer Hunter", "year": 1978, "rating": 8.1, "genre": "War",
     "directors": ["Michael Cimino"], "actors": ["Robert De Niro", "Christopher Walken", "John Cazale"]},

    {"title": "Alien", "year": 1979, "rating": 8.4, "genre": "Horror",
     "directors": ["Ridley Scott"], "actors": ["Sigourney Weaver", "Tom Skerritt", "John Hurt"]},

    {"title": "Monty Python and the Holy Grail", "year": 1975, "rating": 8.2, "genre": "Comedy",
     "directors": ["Terry Gilliam", "Terry Jones"], "actors": ["Graham Chapman", "John Cleese", "Eric Idle"]},

    {"title": "Network", "year": 1976, "rating": 8.1, "genre": "Drama",
     "directors": ["Sidney Lumet"], "actors": ["Faye Dunaway", "William Holden", "Peter Finch"]},

    {"title": "Rocky", "year": 1976, "rating": 8.1, "genre": "Drama",
     "directors": ["John G. Avildsen"], "actors": ["Sylvester Stallone", "Talia Shire", "Burt Young"]},
    {"title": "The Shining", "year": 1980, "rating": 8.4, "genre": "Horror",
     "directors": ["Stanley Kubrick"], "actors": ["Jack Nicholson", "Shelley Duvall", "Danny Lloyd"]},

    {"title": "Raging Bull", "year": 1980, "rating": 8.2, "genre": "Biography",
     "directors": ["Martin Scorsese"], "actors": ["Robert De Niro", "Cathy Moriarty", "Joe Pesci"]},

    {"title": "Blade Runner", "year": 1982, "rating": 8.1, "genre": "Sci-Fi",
     "directors": ["Ridley Scott"], "actors": ["Harrison Ford", "Rutger Hauer", "Sean Young"]},

    {"title": "The Thing", "year": 1982, "rating": 8.1, "genre": "Horror",
     "directors": ["John Carpenter"], "actors": ["Kurt Russell", "Wilford Brimley", "Keith David"]},

    {"title": "E.T. the Extra-Terrestrial", "year": 1982, "rating": 7.8, "genre": "Sci-Fi",
     "directors": ["Steven Spielberg"], "actors": ["Henry Thomas", "Drew Barrymore", "Peter Coyote"]},

    {"title": "Scarface", "year": 1983, "rating": 8.3, "genre": "Crime",
     "directors": ["Brian De Palma"], "actors": ["Al Pacino", "Michelle Pfeiffer", "Steven Bauer"]},

    {"title": "Back to the Future", "year": 1985, "rating": 8.5, "genre": "Adventure",
     "directors": ["Robert Zemeckis"], "actors": ["Michael J. Fox", "Christopher Lloyd", "Lea Thompson"]},

    {"title": "The Breakfast Club", "year": 1985, "rating": 7.8, "genre": "Comedy",
     "directors": ["John Hughes"], "actors": ["Emilio Estevez", "Judd Nelson", "Molly Ringwald"]},

    {"title": "Aliens", "year": 1986, "rating": 8.3, "genre": "Action",
     "directors": ["James Cameron"], "actors": ["Sigourney Weaver", "Michael Biehn", "Carrie Henn"]},

    {"title": "Platoon", "year": 1986, "rating": 8.1, "genre": "War",
     "directors": ["Oliver Stone"], "actors": ["Charlie Sheen", "Tom Berenger", "Willem Dafoe"]},

    {"title": "Full Metal Jacket", "year": 1987, "rating": 8.3, "genre": "War",
     "directors": ["Stanley Kubrick"], "actors": ["Matthew Modine", "R. Lee Ermey", "Vincent D'Onofrio"]},

    {"title": "Die Hard", "year": 1988, "rating": 8.2, "genre": "Action",
     "directors": ["John McTiernan"], "actors": ["Bruce Willis", "Alan Rickman", "Bonnie Bedelia"]},

    {"title": "Who Framed Roger Rabbit", "year": 1988, "rating": 7.7, "genre": "Animation",
     "directors": ["Robert Zemeckis"], "actors": ["Bob Hoskins", "Christopher Lloyd", "Joanna Cassidy"]},

    {"title": "Indiana Jones and the Last Crusade", "year": 1989, "rating": 8.2, "genre": "Adventure",
     "directors": ["Steven Spielberg"], "actors": ["Harrison Ford", "Sean Connery", "Alison Doody"]},

    {"title": "Batman", "year": 1989, "rating": 7.5, "genre": "Action",
     "directors": ["Tim Burton"], "actors": ["Michael Keaton", "Jack Nicholson", "Kim Basinger"]},
    {"title": "Citizen Kane", "year": 1941, "rating": 8.3, "genre": "Drama",
     "directors": ["Orson Welles"], "actors": ["Orson Welles", "Joseph Cotten", "Dorothy Comingore"]},

    {"title": "Casablanca", "year": 1942, "rating": 8.5, "genre": "Romance",
     "directors": ["Michael Curtiz"], "actors": ["Humphrey Bogart", "Ingrid Bergman", "Paul Henreid"]},

    {"title": "Double Indemnity", "year": 1944, "rating": 8.3, "genre": "Crime",
     "directors": ["Billy Wilder"], "actors": ["Fred MacMurray", "Barbara Stanwyck", "Edward G. Robinson"]},

    {"title": "It's a Wonderful Life", "year": 1946, "rating": 8.6, "genre": "Drama",
     "directors": ["Frank Capra"], "actors": ["James Stewart", "Donna Reed", "Lionel Barrymore"]},

    {"title": "The Third Man", "year": 1949, "rating": 8.1, "genre": "Film-Noir",
     "directors": ["Carol Reed"], "actors": ["Orson Welles", "Joseph Cotten", "Alida Valli"]},

    {"title": "The Maltese Falcon", "year": 1941, "rating": 8.0, "genre": "Film-Noir",
     "directors": ["John Huston"], "actors": ["Humphrey Bogart", "Mary Astor", "Gladys George"]},

    {"title": "The Great Dictator", "year": 1940, "rating": 8.4, "genre": "Comedy",
     "directors": ["Charles Chaplin"], "actors": ["Charles Chaplin", "Paulette Goddard", "Jack Oakie"]},

    {"title": "Rebecca", "year": 1940, "rating": 8.1, "genre": "Drama",
     "directors": ["Alfred Hitchcock"], "actors": ["Laurence Olivier", "Joan Fontaine", "George Sanders"]},

    {"title": "The Treasure of the Sierra Madre", "year": 1948, "rating": 8.2, "genre": "Adventure",
     "directors": ["John Huston"], "actors": ["Humphrey Bogart", "Walter Huston", "Tim Holt"]},

    {"title": "Notorious", "year": 1946, "rating": 8.0, "genre": "Film-Noir",
     "directors": ["Alfred Hitchcock"], "actors": ["Cary Grant", "Ingrid Bergman", "Claude Rains"]},

    {"title": "The Best Years of Our Lives", "year": 1946, "rating": 8.1, "genre": "Drama",
     "directors": ["William Wyler"], "actors": ["Fredric March", "Dana Andrews", "Myrna Loy"]},

    {"title": "The Red Shoes", "year": 1948, "rating": 8.1, "genre": "Musical",
     "directors": ["Michael Powell", "Emeric Pressburger"],
     "actors": ["Moira Shearer", "Anton Walbrook", "Marius Goring"]},

    {"title": "The Big Sleep", "year": 1946, "rating": 8.0, "genre": "Crime",
     "directors": ["Howard Hawks"], "actors": ["Humphrey Bogart", "Lauren Bacall", "John Ridgely"]},

    {"title": "Bicycle Thieves", "year": 1948, "rating": 8.3, "genre": "Drama",
     "directors": ["Vittorio De Sica"], "actors": ["Lamberto Maggiorani", "Enzo Staiola", "Lianella Carell"]},

    {"title": "The Philadelphia Story", "year": 1940, "rating": 7.9, "genre": "Comedy",
     "directors": ["George Cukor"], "actors": ["Cary Grant", "Katharine Hepburn", "James Stewart"]},
    {"title": "The Sixth Sense", "year": 1999, "rating": 8.2, "genre": "Drama",
     "directors": ["M. Night Shyamalan"], "actors": ["Bruce Willis", "Haley Joel Osment", "Toni Collette"]},

    {"title": "Fargo", "year": 1996, "rating": 8.1, "genre": "Crime",
     "directors": ["Joel Coen", "Ethan Coen"], "actors": ["William H. Macy", "Frances McDormand", "Steve Buscemi"]},

    {"title": "The Big Lebowski", "year": 1998, "rating": 8.1, "genre": "Comedy",
     "directors": ["Joel Coen", "Ethan Coen"], "actors": ["Jeff Bridges", "John Goodman", "Julianne Moore"]},

    {"title": "Trainspotting", "year": 1996, "rating": 8.2, "genre": "Drama",
     "directors": ["Danny Boyle"], "actors": ["Ewan McGregor", "Ewen Bremner", "Jonny Lee Miller"]},

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