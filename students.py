# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 09:37:10 2020

@author: 10529473
"""

# https://github.com/10529473/new

class Student:
    def __init__(self,studentNumber,name,courseCode):
        self.__studentNumber = studentNumber
        self.__name = name
        self.__courseCode = courseCode
        
    
    def getStudentNumber(self):
        return self.__studentNumber

    def getStudentName(self):
        return self.__studentName
    
    def getCourseCode(self):
        return self.__courseCode
    
students=[]
def add(self, student)