# -*- coding: utf-8 -*-
import re
import time

class StringUtil:

    @classmethod
    def remove_space(cls, word):
        return word.replace(" ","").replace("\n", "").replace("\t","")

    @classmethod
    def fetch_number(cls, word):
        return filter(str.isdigit, word)

    @classmethod
    def get_str_today(cls):
        return time.strftime("%Y-%m-%d", time.localtime())

    @classmethod
    def get_date_from_str(cls, word):
        return time.strptime(word, "%Y-%m-%d")