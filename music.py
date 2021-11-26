#!/usr/local/bin/python3

import sys, os, re, subprocess, shlex, urllib.request, urllib.parse, spotipy, config
from spotipy.oauth2 import SpotifyClientCredentials
from colorama import Fore

songs = []

def downloadalbum(sp):
    que = []
    album = input('{}Album name?: {}'.format(Fore.MAGENTA, Fore.RESET))
    results = sp.search(q = "album:" + album, type = "album")
    album_id = results['albums']['items'][0]['uri']
    artist = results['albums']['items'][0]['artists'][0]['name']
    album_name = results['albums']['items'][0]['name'].replace(' ', '').replace('/', '').replace("'", '')
    run_command(Fore.WHITE, "mkdir {} ".format(album_name))
    os.chdir(album_name)
    album_art = results['albums']['items'][0]['images'][0]['url']
    urllib.request.urlretrieve(album_art, "{}.jpg".format(album_name))

    tracks = sp.album_tracks(album_id)
    for track in tracks['items']:
        que.append("{}".format(track['name']))
    print(que)
    for q in que:
        download("{} {}".format(q, artist))


def singledownload(title):
    search = title + " official lyric"
    download(search)


def multidownload():
    while(True):
        searchx = input('{}Song name?: {}'.format(Fore.MAGENTA, Fore.RESET))
        query = searchx.split(',')
        for search in query:
            if search == "Q" or search == "q":
                print(Fore.RED + "Have fun being broke")
                quit()
            songs.append(input)
            search += " official lyric"
            download(search)


def download(search):
    query_string = urllib.parse.urlencode({"search_query" : search})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
    search_result = "http://www.youtube.com/watch?v=" + search_results[0]
    print('{}{} song found{}'.format(Fore.GREEN, search, Fore.RESET))
    run_command(Fore.CYAN, "youtube-dl --extract-audio --ignore-errors -x --audio-format mp3 " + search_result)


def albumdownload(trackname, search):
    query_string = urllib.parse.urlencode({"search_query" : search})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
    search_result = "http://www.youtube.com/watch?v=" + search_results[0]
    print('{}{} song found{}'.format(Fore.GREEN, search, Fore.RESET))
    run_command(Fore.CYAN, "youtube-dl --extract-audio --ignore-errors -x --audio-format mp3 -o '{}'{}".format(trackname, search_result))


def run_command(color, command):
    process = subprocess.Popen(shlex.split(command), stdout = subprocess.PIPE)
    while True:
        output = process.stdout.readline().decode()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(color + str(output.strip()) + Fore.RESET)
    process.poll()


def help():
    print('options and arguments:')
    print(f'{Fore.GREEN}-s: single track downlaoad')
    print('-a: entire album downlaoad')
    print('-m: multitrack download')
    print(f'-h: help menu{Fore.RESET}')


def main():
    sp = spotipy.Spotify(client_credentials_manager = SpotifyClientCredentials())
    print("{}Welcome to MusicPy!{}".format(Fore.RED, Fore.RESET))
    try:
        tag = sys.argv[1]
        if tag == '-h':
            help()
        elif tag == '-s':
            singledownload(sys.argv[2])
        elif tag == '-a':
            downloadalbum(sys.argv[2])
        elif tag == '-m':
            multidownload(sys.argv[2])
        else:
            singledownload(sys.argv[2])
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
