#!/usr/bin/env python3

import ipdb

class Book:
    def __init__(self, title):
        self.title = title
        
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")