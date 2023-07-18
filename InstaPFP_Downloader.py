from instaloader import Instaloader

username = input("Enter Instagram username: ")

Instaloader().download_profile(username, profile_pic_only=True)