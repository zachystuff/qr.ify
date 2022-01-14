#!/usr/bin/python3

from qrcode_generator import qr_gen
from csv_reader import csv_reader
from file_compressor import zip_directory
from art import *
import os


def app():

    def inputvalidation(usrinput):
        if usrinput.endswith(".com"):
            print(".com string input")
            return usrinput
        elif os.path.isfile(usrinput):
            print(f"filepath: {usrinput}")
            return csv_reader(usrinput)
        else:
            print("Enter a valid url or csv file")
            app()

    intro = text2art("Welcome to QR.ify", "random")
    print(intro)
    print("In qr.ify, we know how hard you've worked as a small business owner.\nWe want to make marketing easier for "
          "you so you can focus your energy on what matters, Making money and being the BOSS.\nOur application allows "
          "you to convert your website, social media and other things into a qr code so people can connect with you.\n"
          "Enter your qr code below and start today \n")

    user_input = input("==>")

    processed_user_input = inputvalidation(user_input)

    adv_settings = input("Would you like to make any customizations to your qrcode?\nYes (y) or No (n) ==>")

    if adv_settings.lower() == 'y':
        qr_box_size = input("Size? \n>")
        qr_border = input("Thick borders? \n>")
        qr_color = input("Color? \n>")
        qr_bg_color = input("Background color? \n>")
        if type(processed_user_input) == str:
            print("single url input")
            qr_gen(processed_user_input, qr_box_size, qr_border, qr_color, qr_bg_color)
        elif type(processed_user_input) == list:
            print("csv file input")
            for singleqr in processed_user_input:
                qr_gen(singleqr, qr_box_size, qr_border, qr_color, qr_bg_color)
    elif adv_settings.lower() == 'n':
        if type(processed_user_input) == str:
            qr_gen(processed_user_input)
        elif type(processed_user_input) == list:
            for singleqr in processed_user_input:
                qr_gen(singleqr)


