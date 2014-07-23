import media
import fresh_tomatoes

toy_music = media.Movie("ad","music","http://", "https://www.youtube.com/")

toy_sotry = media.Movie("ad","Movie","http://", "https://www.youtube.com/")


#print(toy_sotry.storyline)

#toy_sotry.show_trailer()

movies = [toy_music, toy_sotry]
fresh_tomatoes.open_movies_page(movies)