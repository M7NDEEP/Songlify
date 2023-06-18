import requests
import lyricsgenius

def songfnc(sname):
    details_url = "https://genius-song-lyrics1.p.rapidapi.com/search/"

    headers = {
        "X-RapidAPI-Key": "65cb3c1018msh65a33c10b84cb22p1a0e9bjsnc40f848a2740",
        "X-RapidAPI-Host": "genius-song-lyrics1.p.rapidapi.com"
    }

    # Getting Song details :- 
    querystring1 = {"q": sname, "per_page": "5", "page": "1"}
    response1 = requests.get(details_url, headers=headers, params=querystring1)
    res = response1.json()
    
    song_title = res['hits'][0]['result']['title']
    artist_name = res['hits'][0]['result']['artist_names']
    ''' Created by Mandeep Yadav'''
    release_date = res['hits'][0]['result']['release_date_for_display']
    song_id = res['hits'][0]['result']['id']

    print(f"\t: Song Name :- {song_title}\n\t: Artist Name :- {artist_name}\n\t: Release Date :- {release_date}\n\t: Song ID :- {song_id}")

    # Getting Lyrics of the song :- 
    genius = lyricsgenius.Genius('KpLlqz1u368eqY2XehhPMJiJBq5OcNEPaXwOHVJ_HbrBUBFJ4IYDiGUBDPkct4WS')
    artist_name = input("\n\t: Enter artist name for lyrics :- ")
    print("\n")
    artist = genius.search_artist(artist_name , max_songs=1,sort='title')
    song = artist.song(song_title)
    
    print(f"\n\t: Lyrics :- \n{song.lyrics}")

# Calling the mainfunction :-  
print("\n <----\t\tWelcome to Songlify\t\t----> \n")
songname = input("\t: Enter song name :- ")
songname = songname.lower()
songfnc(songname)