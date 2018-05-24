#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 15:10:35 2018

@author: Kangzi Li

LeetCode: 535. Encode and Decode TinyURL
"""

#TinyURL is a URL shortening service where you enter a URL such as 
#https://leetcode.com/problems/design-tinyurl and it returns a short URL such 
#as http://tinyurl.com/4e9iAk.
#
#Design the encode and decode methods for the TinyURL service. There is no 
#restriction on how your encode/decode algorithm should work. You just need to 
#ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded 
#to the original URL.
import string
import random

class Codec:

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
    
    alphabet = string.ascii_letters + string.digits
    
    def __init__(self):
        self.url2code = {}
        self.code2url = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        while longUrl not in self.url2code:
            code = ''.join(random.choice(Codec.alphabet) for _ in range(6))
            if code not in self.code2url:
                self.code2url[code] = longUrl
                self.url2code[longUrl] = code
        return 'http://tinyurl.com/' + self.url2code[longUrl]
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.code2url[shortUrl[-6:]]
        

