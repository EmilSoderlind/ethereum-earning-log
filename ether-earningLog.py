#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2017-18 Richard Hull and contributors
# See LICENSE.rst for details.

import os
import time
import argparse
import datetime
from datetime import date
from datetime import datetime
import json
import calendar
import requests


def mainLoop():

    #print("Parsing ethermine-api")
    url = "https://api.ethermine.org/miner/a4aBfc14202339cd55BFB94BD23cf07301443C24/currentStats"
    r = requests.get(url)
    usdPerMin = float(r.json()["data"]["usdPerMin"])
    #print("usdPerMin: ",usdPerMin)

    url = "http://www.apilayer.net/api/live?access_key=72b11244a3da622264f993de24423d06"
    r = requests.get(url)
    #print("USDSEK: ", r.json()["quotes"]["USDSEK"])
    USDSEK = float(r.json()["quotes"]["USDSEK"])

    sekPerMin = USDSEK*usdPerMin

    #print("sekPerMin: ", sekPerMin)

    sekPerDay = round(sekPerMin*60*24, 5)

    print("{0}${1}${2}".format(calendar.timegm(time.gmtime()),datetime.now().strftime('_%G-%b-%d_'), sekPerDay))


if __name__ == "__main__":
    try:
        #print("-> Starting ether-generatingLog <-")
        mainLoop()
        #print("Exiting program!")
    except KeyboardInterrupt:
        #print("Exiting program!")
        pass
    #except:
    #    print("Exiting program!")
    #    pass
