from movie import Movie
import fresh_tomatoes

m1 = Movie("Toy Story",
			"3:00",
			"http://www.rotoscopers.com/wp-content/uploads/2013/10/Toy-Story-Poster.jpg",
			"A toy story",
			"http://www.youtube.com/watch?v=KYz2wyBy3kc")

m2 = Movie("Batman",
			"3:30",
			"http://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
			"A bat's story",
			"https://www.youtube.com/watch?v=yQ5U8suTUw0")

m3 = Movie("Superman",
			"2:50",
			"http://upload.wikimedia.org/wikipedia/en/1/10/Superman_Returns.jpg",
			"An alien's story",
			"https://www.youtube.com/watch?v=T6DJcgm3wNY")

m4 = Movie("Ironman",
			"2:45",
			"http://www.wired.com/images_blogs/underwire/2010/03/iron_man_int_1200.jpg",
			"An iron dude's story",
			"https://www.youtube.com/watch?v=8hYlB38asDY")

m5 = Movie("Spiderman",
			"2:50",
			"http://www.slantmagazine.com/assets/house/film/posterlabamazingspiderman_6.jpg",
			"Amazing Spiderman's story",
			"www.youtube.com/watch?v=DlM2CWNTQ84")

m6 = Movie("Hulk",
			"2:59",
			"http://static.comicvine.com/uploads/original/10/100818/1849560-incredible_hulk_official.jpg",
			"A green man's story",
			"https://www.youtube.com/watch?v=xbqNb2PFKKA")

# add movie instances to movies array
movies = [m1, m2, m3, m4, m5, m6]
# pass movies array to fresh tomatoes to crate a webpage
fresh_tomatoes.open_movies_page(movies)
