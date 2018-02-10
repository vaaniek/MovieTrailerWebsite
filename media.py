import http.client
import json

class Movie():
    def __init__(self,movie_title,poster_image_url,trailer_youtube_url):
        self.movie_title=movie_title
        self.poster_image_url=poster_image_url
        self.trailer_youtube_url=trailer_youtube_url

def json_results_popular_movies():
    conn = http.client.HTTPSConnection("api.themoviedb.org")
    conn.request("GET", "/3/movie/popular?region=CAN&page=1&language=en-US&api_key=b51ba2c89c56de5c8f6b9454c20cd4ec")
    res = conn.getresponse()
    data = res.read()
    global jsonResults
    jsonResults=json.loads(data.decode("utf-8"))

def creating_movie_object():
    conn2 = http.client.HTTPSConnection("api.themoviedb.org")
    for i in jsonResults["results"]:
        picture="https://image.tmdb.org/t/p/w500"+str(i["poster_path"])
        conn2.request("GET", "/3/movie/"+str(i["id"])+"?api_key=b51ba2c89c56de5c8f6b9454c20cd4ec&append_to_response=videos")
        res2 = conn2.getresponse()
        data2 = res2.read()
        jsonResults2=json.loads(data2.decode("utf-8"))
        trailer="https://www.youtube.com/watch?v="+str(jsonResults2["videos"]["results"][0]["key"])
        movie=Movie(i["title"],picture,trailer)
        movies.append(movie)
    
