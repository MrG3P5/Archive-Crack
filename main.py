#!/usr/bin/env python3
# Author : X - MrG3P5
# Version : 1.0
import pyfiglet
import os
import zipfile
import subprocess
import sys
from colorama import Fore, init
from rarfile import RarFile

init()

# Config Color
red = Fore.LIGHTRED_EX
reset = Fore.RESET
BOLD = '\033[1m'
white = Fore.WHITE
cyan = Fore.CYAN
yellow = Fore.YELLOW
green = Fore.GREEN


def __banner__(_str_):
  print(BOLD)
  os.system("cls||clear")
  banner = pyfiglet.figlet_format(f"{_str_}", font="slant", justify="center")
  print(f"{red}{banner}")
  print(f"{cyan}\t\t\t[ {reset}Created By X-MrG3P5 {cyan}]{reset}\n")
  print("")


def _crack_zip_():
  __banner__("Zip - Cracker")
  ask_path_zip = input(f"{cyan}[ {white}? {cyan}] {white}Input File Path Zip : ")
  ask_path_wordlist = input(f"{cyan}[ {white}? {cyan}] {white}Input File Path Wordlist (ex: default.txt) : ")

  if os.path.exists(ask_path_zip) and os.path.exists(ask_path_wordlist):
    zip_file = zipfile.ZipFile(ask_path_zip)
    password = None
    found = False
    with open(ask_path_wordlist, "r") as f:
      for line in f.readlines():
        password = line.strip("\n")
        print(f"{cyan}[ {white}- {cyan}] {white}Trying : {yellow}{password}{reset}")

        try:
          zip_file.extractall(pwd=bytes(password, "utf-8"))
          print(f"{cyan}[ {green}# {cyan}] {white}Password Is : {green}{password}{reset}")
          found = True
          break
        except:
          pass
    if not found:
      print(f"{cyan}[ {red}! {cyan}] {white}Sorry can't find password")
  else:
    print(f"{cyan}[ {red}! {cyan}] {white}File Path Not Found!")


def _crack_rar_():
  __banner__('RAR - Cracker')
  ask_path_rar = input(f"{cyan}[ {white}? {cyan}] {white}Input File Path RAR : ")
  ask_path_wordlist = input(f"{cyan}[ {white}? {cyan}] {white}Input File Path Wordlist (ex: default.txt) : ")

  if os.path.exists(ask_path_rar) and os.path.exists(ask_path_wordlist):
    found = False
    with open(ask_path_wordlist, "r") as f:
      for line in f.readlines():
        password = line.strip("\n")
        print(f"{cyan}[ {white}- {cyan}] {white}Trying : {yellow}{password}{reset}")

        try:
          rar_file = RarFile(ask_path_rar, 'r')
          rar_file.extractall(pwd=password)
          print(f"{cyan}[ {green}# {cyan}] {white}Password Is : {green}{password}{reset}")
          found = True
          break
        except:
          pass
    if not found:
      print(f"{cyan}[ {red}! {cyan}] {white}Sorry can't find password")
  else:
    print(f"{cyan}[ {red}! {cyan}] {white}File Path Not Found!")


def _crack_7zip_():
  __banner__('7Zip - Crack')
  ask_path_7zip =  input(f"{cyan}[ {white}? {cyan}] {white}Input File Path 7Zip : ")
  ask_path_wordlist = input(f"{cyan}[ {white}? {cyan}] {white}Input File Path Wordlist (ex: default.txt) : ")

  if os.path.exists(ask_path_7zip) and os.path.exists(ask_path_wordlist):
    found = False
    with open(ask_path_wordlist, 'r') as f:
      for line in f.readlines():
        password = line.strip("\n")
        print(f"{cyan}[ {white}- {cyan}] {white}Trying : {yellow}{password}{reset}")

        try:
          stdout = subprocess.call("7z t -p'{0}' {1}".format(password, ask_path_7zip), stderr = subprocess.DEVNULL, stdout = subprocess.DEVNULL, shell = True)
          if stdout == 0:
            print(f"{cyan}[ {green}# {cyan}] {white}Password Is : {green}{password}{reset}")
            found = True
            return
       #   pass
        except:
          pass
    if not found:
      print(f"{cyan}[ {red}! {cyan}] {white}Sorry can't find password")
  else:
    print(f"{cyan}[ {red}! {cyan}] {white}File Path Not Found!")


def __main__():
  __banner__("File - Crack")
  __menu__ = f"""{cyan}[ {white}1 {cyan}] {white}Crack Zip File
{cyan}[ {white}2 {cyan}] {white}Crack RAR File
{cyan}[ {white}3 {cyan}] {white}Crack 7Zip File
{cyan}[ {white}0 {cyan}] {white}Exit\n"""
  print(__menu__)
  __choice__ = int(input(f"{cyan}[ {white}? {cyan}] {white}Select Tools : "))
  if __choice__ == 1:
    _crack_zip_()
  elif __choice__ == 2:
    _crack_rar_()
  elif __choice__ == 3:
    _crack_7zip_()
  elif __choice__ == 0:
    print(f"{cyan}[ {white}- {cyan}] {white}Oke Byee")
    exit()
  else:
    print(f"{cyan}[ {red}! {cyan}] {white}Wrong Input!, Select 1, 2, 3, 0.")


if __name__ == "__main__":
  __main__()
