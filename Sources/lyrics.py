#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib.parse import quote_plus
import requests
import argparse


def get_lyrics(author, song):
    for arg in author+song:
        if arg.isdigit():
            return int
    tags = ['br', 'a', 'div', 'i']
    lyrics = ''
    url = quote_plus(' '.join(author+song))
    link = url_request(url)
    if link is None:
        return
    track_id = link[-1]
    req = requests.get(link)
    soup = BeautifulSoup(req.text, 'html.parser')
    element = soup.find('a', {'name':track_id})
    for sibling in element.parent.next_siblings:
        if sibling.name in tags:
            continue
        if sibling.name == 'h3':
            break
        lyrics += sibling
    lyrics = lyrics.lstrip()
    return lyrics

def url_request(arg):
    query = 'http://www.darklyrics.com/search?q='
    req = requests.get(query+arg)
    soup = BeautifulSoup(req.text, 'html.parser')
    for elements in soup.find_all('h2'):
        for info in elements.find_all('a'):
            url = info.get('href')
            url = 'http://www.darklyrics.com/' + url
            return url

def save_to_file(author, song, lyrics):
    if lyrics is None or lyrics is int:
        return
    outfile = author + '_' + song + '.txt'
    with open(outfile, 'w') as f:
        f.write(lyrics)

def main():
    parser = argparse.ArgumentParser(prog='lyrics.py',
                                     usage='%(prog)s [-h][-s on] author song')
    parser.add_argument('author', nargs='+', help='The author of the song')
    parser.add_argument('song', nargs='+', help='The name of the song')
    parser.add_argument('--save', '-s', type=str, help='Save the lyrics on a file')
    args = parser.parse_args()
    lyrics = get_lyrics(args.author, args.song)
    if lyrics is None:
        print('Lyrics not found')
        return
    if lyrics == int:
        print('Arguments must be string! Type -h for helping.')
        return
    if args.save == 'y':
        save_to_file('_'.join(args.author), '_'.join(args.song),
                              get_lyrics(args.author, args.song))
    else:
        print(' '.join(args.author).capitalize() + ' - ' +
              ' '.join(args.song).capitalize() + '\n')
        print(lyrics)


if __name__ == '__main__':
    main()
