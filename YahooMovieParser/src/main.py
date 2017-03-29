# -*- coding: UTF-8 -*-
'''
Created on 2017年2月13日

@author: hs
'''
#import this
from urllib import urlopen
from bs4 import BeautifulSoup
from movie import Movie 

def getMovieFuture():
    futureIDs=[]
    data = urlopen(yMoiveMainUrl + movieFuture)
    soup = BeautifulSoup(data, 'html.parser')
    futureMovies = soup.select('div[class="row-container"] > div > div > a[href]')
    for v in futureMovies:
        print v.get('href').split("id=")[1]
    
    return
    
if __name__ == '__main__':
    yMoiveMainUrl = 'https://tw.movies.yahoo.com/'
    thisWeekUrl ='movie_thisweek.html'
    movieInfoUrl = 'movieinfo_main.html/id='
    movieTimeUrl ='movietime_result.html?id='
    movieFuture = 'movie_comingsoon.html?p='
    
    movieIDs=[]
    
    data = urlopen(yMoiveMainUrl + thisWeekUrl)
    soup = BeautifulSoup(data, 'html.parser')
    #result = soup.find('title')直接找head底下的title
    #print(result.get_text())將其中的文字印出
    playingMovie = soup.select('select[hpp="thisweek-quicksearch"] > option')
    for v in playingMovie:
        if len(v.get('value')) != 0:
            movieIDs.append(v.get('value'))
            
    thisWeekMovie = soup.select('div[class="row-container"] > div > div > a[href]')
    for v in thisWeekMovie:
        movieIDs.append(v.get('href').split("id=")[1])
    getMovieFuture()
        
    for id in movieIDs:
        print(id) 
        data = urlopen(yMoiveMainUrl + movieInfoUrl + id)
        soup = BeautifulSoup(data, 'html.parser')
        #info = soup.select('div.text.bulletin').find('h5')
        movieInfo = soup.find('div', class_='text bulletin')
        movie = Movie(movieInfo.h4.getText(), movieInfo.h5.getText())
        movie.printInfo()
        #titleLsit = movieInfo.select('p > span[class="tit"]')
        #dataList = movieInfo.select('p > span[class="dta"]')
            
        #for i in range(len(titleLsit)):
        #print titleLsit[i].getText(), dataList[i].getText() 
        #print soup.find('div', class_='text full').getText()    
        
       
    
