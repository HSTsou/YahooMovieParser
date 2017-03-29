# -*- coding: UTF-8 -*-
'''
Created on 2017年2月16日

@author: hs
'''
class Movie():
    '''
    classdocs
    '''
    def __init__(self, chName, enName):
        self.chName = chName
        self.enName = enName     
    
    def printInfo(self):
        print  self.chName, '\n' , self.enName