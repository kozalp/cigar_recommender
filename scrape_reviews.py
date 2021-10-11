#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 15:13:26 2021

This code gets all cigar brands with descriptions, descriptions,
reviewer names, reviews, review dates, and ratings.

@author: mk
"""

from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

data = pd.read_csv("/Users/mk/Documents/web_scraping/cigars.csv", index_col=0)

links = data.Link
brand = []
commenter = []
user_type = []
date = []
comment = []
rating = []
description = []

for link in links:
    html_text = requests.get(link).text
    soup = BeautifulSoup(html_text,"lxml")
    
    if soup.find("div", class_="kw-details-desc") != None:
        text = soup.find("div", class_="kw-details-desc").text
    else:
        text = ""
    
    if soup.find("li", class_ = re.compile("review byuser comment")) != None:
        revs = soup.find_all("li", class_ = re.compile("review byuser comment"))
        
        for rev in revs:
            reviewer = rev.find("div", class_="comment_container")
            reviewer_meta = reviewer.find("p", class_="meta")
            rev_name = reviewer_meta.find("strong", class_="woocommerce-review__author").text.strip()
            commenter.append(rev_name)
            utype = reviewer_meta.find("em", class_="woocommerce-review__verified verified").text.strip("()")
            user_type.append(utype)
            dt = reviewer_meta.find("time", class_="woocommerce-review__published-date").text
            date.append(dt)
            review = reviewer.find("div", class_="description").text
            comment.append(review)
            rating_val = reviewer.find("div", class_="star-rating").get("aria-label").split()[1]
            rating.append(rating_val)
            title = soup.find("h2", class_="subheader-maintitle").text
            brand.append(title)
            description.append(text)
    else:
        pass

final_data = pd.DataFrame({"Brand":brand, "Description":description, "Reviewer":commenter, "User_Type":user_type, "Date":date, "Review":comment, "Rating":rating})

final_data.to_csv("/Users/mk/Documents/web_scraping/cigar_reviews.csv")