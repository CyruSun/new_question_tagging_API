# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 11:02:29 2019

@author: Utilisateur_1
"""

import re

REGEX = r'\w{1}\W{1,2}|\w+\.\w+|\w+'

def regex_tokenizer(phrase, regex=REGEX):
    """Tokenization without nltk"""
    pattern = re.compile(regex)
    tokenized = [match for match in pattern.findall(phrase)]
    return tokenized
