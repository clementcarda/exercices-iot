#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import requests
import json

#https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=EUR,USD


#####functions#####
def getAPI(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Someting went wrong")
    data = json.loads(response.content.decode('utf-8'))
    return data

def getListCoins(data):
    for key in data:
        if data[key]['IsTrading'] == True:
            print(key)
def getCoinPrice(coin):
    data = getAPI("https://min-api.cryptocompare.com/data/price?fsym="+coin+"&tsyms=EUR,USD")
    print(coin+" :")
    print(data)
    for key in data:
        print(data[key], key)




#####code#####



print("Entrez liste pour avoir la liste des monnaies disponible\n"
          "Entrez le nom d'une monnaie pour avoir le prix\n"
          "Entrez exit pour quitter")

while True:
    command = input("que cherchez vous? ")

    if command == "exit":
        break
    elif command == "liste":
        data = getAPI("https://min-api.cryptocompare.com/data/all/coinlist")
        getListCoins(data['Data'])
    elif command != "":
        getCoinPrice(str.upper(command))
    else:
        print("veuillez entrez une valeur")