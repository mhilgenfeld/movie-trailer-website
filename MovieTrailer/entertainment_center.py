import media
import fresh_tomatos

cars = media.Movie("Cars", 
                   "A hot-shot race-car named Lightning McQueen gets waylaid in Radiator Springs, where he finds the true meaning of friendship and family.", 
                   "https://www.youtube.com/watch?v=uxx75HVd-F0", 
                   "http://ia.media-imdb.com/images/M/MV5BMTg5NzY0MzA2MV5BMl5BanBnXkFtZTYwNDc3NTc2._V1_SX300.jpg",
                   "2006",
                   '$461.98M',
                   'PG',
                   "117 Mins",
                   "Owen Wilson", "Paul Newman", "Bonnie Hunt", "Larry The Cable Guy")

stars = media.Movie("Monty Python", 
                   "King Arthur and his knights embark on a low-budget search for the Grail, encountering many very silly obstacles.", 
                   "http://www.youtube.com/watch?v=RDM75-oXGmQ", 
                   "http://ia.media-imdb.com/images/M/MV5BMTkzODczMTgwM15BMl5BanBnXkFtZTYwNTAwODI5._V1_SX300.jpg",
                   "1975",
                   "$5M",
                   "PG",
                   "91 Mins",
                   "Graham Chapman", "John Cleese", "Eric Idle", "Terry Gilliam")

courageous = media.Movie("Courageous", 
                   "When a tragedy strikes close to home, four police officers struggle with their faith and their roles as husbands and fathers; together they make a decision that will change all of their lives.", 
                   "http://www.youtube.com/watch?v=i9VT_NBIVfs", 
                   "http://ia.media-imdb.com/images/M/MV5BMjEyODMxNjM4OF5BMl5BanBnXkFtZTcwMTg5OTg3NQ@@._V1_SX300.jpg",
                   "2011",
                   "$34.52M",
                   "PG-13",
                   "129 Mins",
                   "Ken Bevel", "Alex Kendrick", "Kevin Downes", "Renee Jewell")

kfp = media.Movie("Kung Fu Panda", 
                   "In the Valley of Peace, Po the Panda finds himself chosen as the Dragon Warrior despite the fact that he is obese and a complete novice at martial arts.", 
                   "http://www.youtube.com/watch?v=GEgk9XsFCR0", 
                   "http://ia.media-imdb.com/images/M/MV5BMTIxOTY1NjUyN15BMl5BanBnXkFtZTcwMjMxMDk1MQ@@._V1_SX300.jpg",
                   "2008",
                   "$631.70M",
                   "PG",
                   "92 Mins",
                   "Jack Black", "Dustin Hoffman", "Angelina Jolie", "Ian McShane")

ipMan = media.Movie("Ip Man", 
                   "A semi-biographical account of Yip Man, the successful martial arts master who taught the Chinese martial art of Wing Chun to the world.", 
                   "http://www.youtube.com/watch?v=1AJxXQ7xojE", 
                   "http://ia.media-imdb.com/images/M/MV5BMjE0NDUzMDcyOF5BMl5BanBnXkFtZTcwNzAxMTA2Mw@@._V1_SX300.jpg",
                   "2008",
                   "",
                   "R",
                   "106 Mins",
                   "Donnie Yen", "Simon Yam", "Ka Tung Lam", "Siu-Wong Fan")

pap = media.Movie("Pride & Prejudice", 
                   "Sparks fly when spirited Elizabeth Bennet meets single, rich, and proud Mr. Darcy. But Mr. Darcy reluctantly finds himself falling in love with a woman beneath his class. Can each overcome their own pride and prejudice?", 
                   "https://www.youtube.com/watch?v=fJA27Jujzq4", 
                   "http://ia.media-imdb.com/images/M/MV5BMTA1NDQ3NTcyOTNeQTJeQWpwZ15BbWU3MDA0MzA4MzE@._V1_SX300.jpg",
                   "2005",
                   "",
                   "PG",
                   "129 Mins",
                   "Keira Knightley", "Talulah Riley", "Rosamund Pike", "Jena Malone")

movies = {cars, stars, courageous, kfp, ipMan, pap}

raymond = media.Series("Everybody Loves Raymond", "The comical everyday life of a successful sports columnist and his dysfunctional family.",
                       "1996-2005", "https://www.youtube.com/watch?v=enTKltmtlnE", "http://ia.media-imdb.com/images/M/MV5BMTc2ODEyMzUwMV5BMl5BanBnXkFtZTcwNTAxODUyMQ@@._V1_SY317_CR8,0,214,317_AL_.jpg",
                       9, 210, "Ray Ramono", "Patricia Heaton", "Brad Garrett", "Doris Roberts", "Peter Doyle")

scrubs = media.Series("Scrubs", "In the unreal world of Sacred Heart Hospital, intern John ""J.D"" Dorian learns the ways of medicine, friendship and life.",
                      "2001-2010", "https://www.youtube.com/watch?v=Ji6-Pbfypys", "http://ia.media-imdb.com/images/M/MV5BMTc2NjgxMzc5Nl5BMl5BanBnXkFtZTcwOTc0OTM0MQ@@._V1._CR10,44,330,454_SY317_CR8,0,214,317_AL_.jpg",
                      9, 182, "Zach Braff", "Sarah Chalke", "Donald Faison", "Neil Flynn", "John C McGinley")

covert = media.Series("Covert Affairs", "A young CIA operative/trainee, Annie Walker, is sent into the field to work for the DPD (Domestic Protection Division).",
                      "2010-2014", "https://www.youtube.com/watch?v=pXXOg4Xe2xQ", "http://ia.media-imdb.com/images/M/MV5BMTM3Nzk5Njc3M15BMl5BanBnXkFtZTcwMTUxNzc4Nw@@._V1_SY317_CR11,0,214,317_AL_.jpg",
                      5, 75, "Piper Perabo", "Christopher Gorham", "Kari Matchett")

series = {scrubs, raymond, covert}

fresh_tomatos.open_movies_page(movies, series)

