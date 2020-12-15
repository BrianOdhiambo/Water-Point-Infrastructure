import pandas as pd
import numpy as np
import urllib, json

def getData(url='http://somedata.com'):
    """
    This function gets json data using url.
    From the data it determines the number of functional
    water points, number of water points per community,
    and the rank of each community by the percentage of broken water points.
    """
    p_data = pd.read_json(url)

    # functional water points
    water_is_func = p_data.loc[p_data.water_functioning == "yes"]
    print("*" * 20)
    print("NUMBER OF WATER POINTS THAT ARE FUNCTIONAL")
    print("Number functional: {0} \n".format(len(water_is_func)))

    # Number of water points per community
    water_point_per_community = p_data.groupby('communities_villages').water_point_id.count()
    print("\n")
    print("*" * 20)
    print("NUMBER OF WATER POINTS PER COMMUNITY")
    print(water_point_per_community)

    # Rank of each community by the percentage of the broken water points
    # water points not functioning per community
    not_func_per_community = p_data.groupby('communities_villages').water_not_functioning.count()

    # finding the percentages
    percent_damage_per_comm = (not_func_per_community / water_point_per_community) * 100
    print("\n")
    print("*" * 20)
    print("RANK OF COMMUNITIES BY THE PERCENTAGES OF BROKEN WATER POINTS")
    print(percent_damage_per_comm)

if __name__ == "__main__":
     getData(url='https://raw.githubusercontent.com/onaio/ona-tech/master/data/water_points.json')