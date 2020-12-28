#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 15:46:32 2020

"""

import pandas as pd
import glob
import json
import os

path = r"/Users/jonasschroeder/influencer_post_data"
os.chdir(path)

# list all files from folder
file_list = []
for file in glob.glob("*.info"):
    file_list.append(file)


post_table = pd.DataFrame(columns=["shortcode", "influencer_profile", "nb_comments", "nb_likes"])

# loop to load all files
for i in range(0, len(file_list)):
    
    print(i)
    
    # Empty temporary table
    temp_table = pd.DataFrame(columns=["shortcode", "influencer_profile", "nb_comments", "nb_likes"])

    data_temp = json.load(open(file_list[i]))
    
    # Shortcode
    temp_table.at[0, "shortcode"] = data_temp["shortcode"]
    
    # Influencer Profile
    temp_table.at[0, "influencer_profile"]  = data_temp["owner"]["username"]
    
    # Number of comments
    try: 
        temp_table.at[0, "nb_comments"] = data_temp["edge_media_preview_comment"]["count"]
    except: 
        temp_table.at[0, "nb_comments"] = data_temp["edge_media_to_comment"]["count"]
    
    # Number of likes
    try:
        temp_table.at[0, "nb_likes"] = data_temp["edge_media_preview_like"]["count"]
    except:
        temp_table.at[0, "nb_likes"] = data_temp["edge_media_to_like"]["count"]        

    
    print(temp_table)
    
    post_table = post_table.append(temp_table)


# Export dataframe as csv








