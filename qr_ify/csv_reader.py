#!/usr/bin/python3

""" Using the CSV library to work with CSV data."""

# standard library import
import csv


def csv_reader(file_path):
    """
    Parses through csv files containing urls and returns a list
    :param file_path: filepath to csv files
    :return: a list of urls
    """
    result = []
    # open our csv data (we want to loop across this)
    try:
        with open(file_path, "r") as csvfile:
            print(f"csv file location: {file_path}...")
            # counter to create unique file names
            i = 0
            # loop across our open file line by line
            for row in csv.reader(csvfile):
                i = i + 1  # increase i by 1 (to create unique admin.rc file names)
                result.append(row)  # this f string says "fill in the value of i"
    except Exception as e:
        print(f"Oops, seems like theres an error: {e.__class__}")

    print("CSV files read and parsed!")
    return result
