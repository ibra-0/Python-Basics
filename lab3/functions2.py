# 1. 
def is_highly_rated(movie):
    return movie["imdb"] > 5.5

# 2. 
def high_rated_movies(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]

# 3. 
def movies_by_category(movies, category):
    return [movie for movie in movies if movie["category"] == category]

# 4. 
def average_imdb(movies):
    return sum(movie["imdb"] for movie in movies) / len(movies)

# 5. 
def average_imdb_by_category(movies, category):
    category_movies = movies_by_category(movies, category)
    if not category_movies:
        return 0  
    return sum(movie["imdb"] for movie in category_movies) / len(category_movies)

if __name__ == "__main__":
    print(is_highly_rated(movies[0]))  # Проверяем первый фильм
    print(high_rated_movies(movies))  # Фильмы с рейтингом выше 5.5
    print(movies_by_category(movies, "Romance"))  # Фильмы в категории Romance
    print(average_imdb(movies))  # Средний рейтинг всех фильмов
    print(average_imdb_by_category(movies, "Romance"))  # Средний рейтинг в категории Romance
