#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple Bot to reply to Telegram messages
# Copyright (C) 2015 Leandro Toledo de Souza <leandrotoeldodesouza@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].

import sys  
sys.path.append("site-packages")
import logging
import telegram
from time import sleep
import urllib
import urllib2
import time
import ast
try:
    from urllib.error import URLError
except ImportError:
    from urllib2 import URLError  # python 2


def main():
    last_id = 0
    while True:
        url = 'http://shrouded-ravine-16002.herokuapp.com/telegram_get'
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        the_page = response.read()
        if (the_page == "Null"):
            sleep(10)
        else:
            dictionaryResponse = ast.literal_eval(the_page)
            if(last_id >= dictionaryResponse['update_id']):
                sleep(10)
            else:
                last_id = int(dictionaryResponse['update_id'])
                check_pages(dictionaryResponse['id'])


def check_pages(chat_id):
            f = open('D:\Projects\SushiBot\TeleCore\kushai.txt', 'r') 
            for line in f:
                try:
                    url = line
                    req = urllib2.Request(url)
                    response = urllib2.urlopen(req)
                    the_page = response.read()
                    the_page = the_page.decode('utf-8').lower()
                    #cnt = the_page.count(u'слона')
                    cnt = the_page.count(u'слон')
                    print(url+' '+str(cnt))
                    if(cnt>0):
                        send_msg(chat_id, url+' '+str(cnt))
                except Exception:
                    send_msg(chat_id, 'Error')
            f.close()
            send_msg(chat_id, 'Sup ok')
            
def send_msg(chat_id, msg):
    url = 'http://shrouded-ravine-16002.herokuapp.com/telegram_send'
    dict_data = {'id':chat_id, 'msg':msg}
    req = urllib2.Request(url, str(dict_data))
    response = urllib2.urlopen(req)

if __name__ == '__main__':
    main()
