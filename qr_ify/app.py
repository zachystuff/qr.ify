#!/usr/bin/python3
"""
APP
The main Application logic is written here.
User is introduced to the application and run through the basic flow.
"""

# standard library import
import os
import time
from art import *
from qrcode_generator import qr_gen
from csv_reader import csv_reader
from file_compressor import zip_directory

"""
Stretch goal was to introduce zip compression for csv file inputs.
Would like to be able to compress all converted files into a single compressed file
"""


def initializer():
    """
    App initializer function.
    :return:
    """

    def inputvalidation(usrinput):
        """
        This function validates user inputs.
        Curently accepted inputs are urls and csv files which are converted to lists
        :param usrinput:
        :return:
        """
        if usrinput.endswith(".com"):
            print("Valid URL input..")
            return usrinput
        elif os.path.isfile(usrinput):
            print(f"Selected filepath: {usrinput}")
            return csv_reader(usrinput)
        else:
            print("Error: invalid Input\nPlease enter a valid url or csv file\n")
            time.sleep(2)
            initializer()

    intro = text2art("\n\n\nWelcome\nto\nQR.ify\n", "random")
    print(intro)
    time.sleep(3)

    def intro():
        print("\nIn QR.ify, we know how hard you've worked as a small business owner.\nWe want to make marketing "
              "easier for you so you can focus your energy on what matters, Making money and being the BOSS.\nOur "
              "application allows you to convert your website, social media and other things into a qr code so people "
              "can connect with you.\n"
              "QR.ify can accept a SINGLE URL OR CSV\n"
              "Enter your qr code\n")

        return input("==>")

    user_input = intro()
    validated_user_input = inputvalidation(user_input)
    print(validated_user_input)
    time.sleep(3)
    print("Would you like to make any customizations to your qrcode?\nYes (y) or No (n) ")
    time.sleep(3)
    adv_settings = input("==>")

    if adv_settings.lower() == 'y':
        qr_box_size = input("Size(pixels/box)?\nvalue=range(10,20)\n>")
        if int(qr_box_size) not in range(10, 21):
            print("invalid input, please select a size within the range of 10 - 20\n")
            qr_box_size = input("==>")
        qr_border = input("Thick borders(pixel thickness)?\nvalue=range(4,8) \n>")
        if int(qr_border) not in range(4, 9):
            print("invalid input, please select a border size within the range of 4 - 9\n")
            qr_box_size = input("==>")
        qr_color = input("Color?\nvalue='yellow' or (255, 195, 235) \n>")
        qr_bg_color = input("Background color?\nvalue='yellow' or (255, 195, 235)\n>")

        if type(validated_user_input) == str:
            try:
                qr_gen(validated_user_input, qr_box_size, qr_border, qr_color, qr_bg_color)
                print("QR conversion complete! Your files can be found in the encoded_qr_img folder.\n")
            except Exception as e:
                print(f"Oops, seems like theres an error: {e.__class__}")
        elif type(validated_user_input) == list:
            print("csv file input")
            for singleqr in validated_user_input:
                qr_gen(singleqr, qr_box_size, qr_border, qr_color, qr_bg_color)
            print("QR conversion complete! Your files can be found in the encoded_qr_img folder.\n")

    elif adv_settings.lower() == 'n':
        if type(validated_user_input) == str:
            try:
                qr_gen(validated_user_input)
                print("QR conversion complete! Your files can be found in the encoded_qr_img folder.\n")
            except Exception as e:
                print(f"Oops, seems like theres an error: {e.__class__} while processing your qr code.")
                return
        elif type(validated_user_input) == list:
            for singleqr in validated_user_input:
                try:
                    qr_gen(singleqr)
                    print("QR conversion complete! Your file can be found in the encoded_qr_img folder.\n")
                except Exception as e:
                    print(f"Oops, seems like theres an error: {e.__class__} while processing your qr code.")
                    return

    print("Would you like to qr_ify any other files/folders? \n"
          "==> (y) / (n)")
    answer = input()

    if answer == "y":
        initializer()
    elif answer == "n":
        print("Thanks for using our service, come again soon and recommend us on the app store")
    else:
        print("Really dude? Goodbye")
