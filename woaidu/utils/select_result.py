#-*-coding:utf-8-*-

from urlparse import urljoin

from w3lib.html import remove_entities

NULL = [None,'null']

list_first_item = lambda x:x[0] if x else None

def clean_link(link_text):
    return link_text.strip("\t\r\n '\"");

clean_url = lambda base_url,u,response_encoding: urljoin(base_url, remove_entities(clean_link(u.decode(response_encoding))))