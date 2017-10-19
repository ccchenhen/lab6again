#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 15:37:07 2017

@author: xg7
"""

class Student:
    def __init__(self, name, class_of="", major=""):
        self.name = name
        self.class_of = class_of
        self.major = major
        self.knowledge = 0
    
    def set_name(self, name):
        self.name = name
        
    def get_name(self):
        return self.name
    
    def get_knowledge(self):
        return self.knowledge
    
    #method
    def study(self, time_s):
        self.knowledge += 1.5 * time_s