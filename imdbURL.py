#2 ideas
#just return the plot and relevant info from the api

#or get the id from the api and return the imdb link
import requests
import json


def giveURL(movie):
  #use string replace to format movie title for url
  strpmvie = movie.replace(' ', '&')

  #query omdb api for the imdb id of movie
  respString = 'http://www.omdbapi.com/?t='+ strpmvie+ '&apikey=18325552'
  r= requests.get(respString)

  #put api response into json format
  dictionary = r.json()

  #put imdb id into the imdb movie url to get their webpage for the given movie and return the result
  imdbURL = "https://www.imdb.com/title/" + dictionary['imdbID']
  return(imdbURL)



if __name__ == '__main__':
    #call function and pass in movie title as the parameter
    # movie = "good will hunting"
    # print(giveURL(movie))
    #print(giveURL("Forrest Gump"))
    
    '''
    Possible errors: 
    The movie title input must be formatted to not have spaces at the end or beginning or have any other errors

    No error checking has been done yet for anything

    Should provide a "Movie not found" error as default
    '''