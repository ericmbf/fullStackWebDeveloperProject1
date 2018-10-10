import media
import fresh_tomatoes

interstellar = media.Movie("Interstellar",
    "Interstellar is a 2014 science fiction film directed, co-written, and co-produced by Christopher Nolan. It stars Matthew McConaughey, Anne Hathaway, Jessica Chastain, Bill Irwin, Ellen Burstyn, and Michael Caine. Set in a dystopian future where humanity is struggling to survive, the film follows a group of astronauts who travel through a wormhole in search of a new home for humanity.", 
    "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
    "https://www.youtube.com/watch?v=zSWdZVtXT7E")

matrix = media.Movie("Matrix",
    "The Matrix is a 1999 science fiction action film written and directed by The Wachowskis[note 1] and starring Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss, Hugo Weaving, and Joe Pantoliano. It depicts a dystopian future in which reality as perceived by most humans is actually a simulated reality called 'the Matrix', created by sentient machines to subdue the human population, while their bodies' heat and electrical activity are used as an energy source. Cybercriminal and computer programmer Neo learns this truth and is drawn into a rebellion against the machines, which involves other people who have been freed from the 'dream world'.", 
    "https://upload.wikimedia.org/wikipedia/en/thumb/c/c1/The_Matrix_Poster.jpg/220px-The_Matrix_Poster.jpg",
    "https://www.youtube.com/watch?v=m8e-FF8MsqU")
                            
inception = media.Movie("Inception",
    "Inception is a 2010 science fiction action film[3] written, co-produced, and directed by Christopher Nolan, and co-produced by Emma Thomas. The film stars Leonardo DiCaprio as a professional thief who steals information by infiltrating the subconscious, and is offered a chance to have his criminal history erased as payment for the implantation of another person's idea into a target's subconscious.[4] The ensemble cast additionally includes Ken Watanabe, Joseph Gordon-Levitt, Marion Cotillard, Ellen Page, Tom Hardy, Dileep Rao, Cillian Murphy, Tom Berenger, and Michael Caine.", 
    "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
    "https://www.youtube.com/watch?v=YoHD9XEInc0")

the_dark_knight = media.Movie("The Dark Knight",
    "The Dark Knight is a 2008 superhero film directed, produced, and co-written by Christopher Nolan. Featuring the DC Comics character Batman, the film is the second part of Nolan's The Dark Knight Trilogy and a sequel to 2005's Batman Begins, starring an ensemble cast including Christian Bale, Michael Caine, Heath Ledger, Gary Oldman, Aaron Eckhart, Maggie Gyllenhaal and Morgan Freeman. In the film, Bruce Wayne / Batman (Bale), Police Lieutenant James Gordon (Oldman) and District Attorney Harvey Dent (Eckhart) form an alliance to dismantle organized crime in Gotham City, but are menaced by an anarchist mastermind known as the Joker (Ledger), who seeks to undermine Batman's influence and turn the city to chaos.", 
    "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
    "https://www.youtube.com/watch?v=EXeTwQWrcwY")

the_prestige = media.Movie("The Prestige",
    "The Prestige is a 2006 psychological thriller film directed by Christopher Nolan from a screenplay adapted by his brother Jonathan from Christopher Priest's 1995 novel of the same name. Its story follows Robert Angier and Alfred Borden, rival stage magicians in London at the end of the 19th century. Obsessed with creating the best stage illusion, they engage in competitive one-upmanship with tragic results and a renowned twist ending.", 
    "https://upload.wikimedia.org/wikipedia/en/thumb/d/d2/Prestige_poster.jpg/220px-Prestige_poster.jpg",
    "https://www.youtube.com/watch?v=o4gHCmTQDVI")

donnie_darko = media.Movie("Donnie Darko",
    "Donnie Darko is a 2001 science fiction film written and directed by Richard Kelly. It stars Jake Gyllenhaal, Jena Malone, Drew Barrymore, Mary McDonnell, Katharine Ross, Patrick Swayze, Noah Wyle, and Maggie Gyllenhaal. The film follows the adventures of the troubled title character as he seeks the meaning behind his doomsday-related visions.", 
    "https://upload.wikimedia.org/wikipedia/en/d/db/Donnie_Darko_poster.jpg",
    "https://www.youtube.com/watch?v=bzLn8sYeM9o")

# Create a list with de movies instantiates
movies = [interstellar, matrix, inception, the_dark_knight, the_prestige, donnie_darko]

# Create the html web page
fresh_tomatoes.open_movies_page(movies)
