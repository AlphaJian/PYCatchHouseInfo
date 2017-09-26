# -*- coding: utf-8 -*-
import re

class StringUtil:

    @classmethod
    def remove_space(self, word):
        return word.replace(" ","").replace("\n", "").replace("\t","")

    @classmethod
    def fetch_number(self, word):
        return filter(str.isdigit, word)
