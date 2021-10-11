#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 10:24:46 2021

This code gets all the cigar brands, price, ratings, and links 
under the rare category from the Privada Cigar Club website.

@author: mk
"""

from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

html_text = requests.get("https://privadacigarclub.com/product-category/rare/").text

# print(html_text) # Response [200] means the operation
# # is successful

# 1. LET'S CREATE A BEAUTIFULSOUP INSTANCE AND SCRAPE THE TEXT-ONLY

soup = BeautifulSoup(html_text,"lxml")

# I had to use a different approach for the "class_" because the class names
# in this website are dynamic. I used a part of the code from this website:
# https://stackoverflow.com/questions/55199526/website-to-be-scraped-has-varying-class-names
brands = []
prices = []
ratings = []
links = []

cigars = soup.find_all("li", class_ = re.compile("prodpage-"))
for cigar in cigars:
    brand = cigar.find("h3", class_="kw-details-title text-custom-child").text
    brands.append(brand)
    price = cigar.find("span", class_="price").text
    prices.append(price)
    if cigar.find("div", class_="star-rating") != None:
        rating = cigar.find("div", class_="star-rating").get("aria-label").strip()[6:10]
        ratings.append(rating)
    elif cigar.find("div", class_="star-rating") == None:
        ratings.append("")
    link = cigar.a.get("href")
    links.append(link)



data = pd.DataFrame({"Brand":brands,"Link":links,"Price":prices,"Rating":ratings})
data.to_csv("cigars.csv")