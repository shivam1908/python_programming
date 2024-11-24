import requests
import json

apikey = 'a2276e96'

def get_movie_data(name: str):
    """Returns a dictionary of movie information from the OMDb API.
    """
    response_obj = requests.get("http://www.omdbapi.com/", params={"t": name, "r": "json", "apikey": apikey})
    data = response_obj.json()
    print(f"The respponse of movies list is -----{data}")
    if data["Response"]=='True':
        return response_obj.json()
    else:
        return ("")

def rt_rating(movie_data: dict):
    """Returns the Rotten Tomatoes rating from a dictionary of movie information.
    """
    if movie_data:
        for dictionary in movie_data['Ratings']:
            if dictionary['Source'] == 'Rotten Tomatoes':
                return int(dictionary['Value'].replace('%', ''))
        return -1
    return -1



def get_joke_data(word: str):
    """Returns the dictionary with information about up to two jokes
    """
    response_obj = requests.get("https://icanhazdadjoke.com/search", headers = {'Accept': 'application/json'}, params={'term': word, 'limit': '2'})
    return response_obj.json()

def get_jokes(plot: str):
    """Returns a tuple containing the longest word for which jokes were found
    and the joke itself. Break ties for longest word using the order in `plot`.
    Make sure that you strip punctuation from the word before you search for a joke.
    """

    words = plot.split()  # split into separate words
    words = [w.strip(',.!;:') for w in words]  # remove punctuation for each word

    word_s = sorted(words, key=lambda word: len(word), reverse=True)
    final_joke = []
    word_s =["asdsd","Asdasd"]
    for w in word_s:
        if len(get_joke_data(w)['results']) == 2:
            for dictionary in get_joke_data(w)['results']:
                final_joke.append(dictionary['joke'])
            return (w, final_joke,"true")

    if not final_joke:
        return (w,final_joke,"false")







def highlight(word: str, sentence: str) -> str:
    """ Highlights a specific word in a sentence by surrounding it with asterisks (**).
    The highlighting is case-insensitive."""
    import re
    return re.sub(re.escape(word), f"**{word}**", sentence, flags=re.IGNORECASE)

def haha_me(movie_title: str) -> str:
    """Returns a string containing a movie title, the Rotten Tomatoes rating, a plot summary,
    and two jokes about the movie. If no jokes are found, a message is returned instead.
    """
    final_tuple = ()
    results = get_movie_data(movie_title)
    if results:
        ratings = rt_rating(results)
        print(f"-----------ratins is ------ {ratings}")
        plot_string = results["Plot"]

        final_tuple = get_jokes(plot_string)
        print(final_tuple)
        if final_tuple[2]:
            print("-----------The jokes is returnes-------")
            joke = "\n".join(final_tuple[1])

            h_plotstring = highlight(final_tuple[0], plot_string)

            if ratings == -1:
                return f"{movie_title}\nRotten Tomatoes rating: {ratings}%\n{h_plotstring}\nSpeaking of **{final_tuple[0]}**, that reminds me of some jokes.\nHope you like them!\n\n{highlight(final_tuple[0], joke)}"

            elif ratings < 70:
                return f"{movie_title}\nRotten Tomatoes rating: {ratings}%\n{h_plotstring}\nSpeaking of **{final_tuple[0]}**, that reminds me of some jokes.\nHope they're better than the movie!\n\n{highlight(final_tuple[0], joke)}"

            elif ratings > 70:
                return f"{movie_title}\nRotten Tomatoes rating: {ratings}%\n{h_plotstring}\nSpeaking of **{final_tuple[0]}**, that reminds me of some jokes.\nHope they're as good as the movie!\n\n{highlight(final_tuple[0], joke)}"
    else:
       return "-----No Jokes Available-----"


print(haha_me("black panther"))