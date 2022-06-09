#Crawler and indexing combined

from urllib.request import urlopen
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import os
import fnmatch
import codecs
import json

index = {}
graph = {}

index_titles = {}

crawled = []

for_in = {}
inv_in = {}

for_in = {'for_in': for_in}

def forward_index(for_in, title, desc):
    words = desc.split()
    if title in for_in:
        for word in words:
            if word not in for_in[title]:
                for_in[title].append(word)
            else:
                continue
    else:
        for_in[title] = [words]
    for key in sorted(for_in.keys()):
        with open('file_for.txt', 'a') as ffile:
           ffile.write(json.dumps(for_in))

inv_in = {'inv_in': inv_in}

def inverted_index(inv_in, url, desc, title):
    words= desc.split()
    title_words = title.split()
    for word in title_words:
        if word not in words:
            words.append(word)
        else:
            continue
    for word in words:
        if word in inv_in and url not in inv_in[word]:
            inv_in[word].append(url)
        else:
            inv_in[word] = [url]
    for key in sorted(for_in.keys()):
        with open('file_in.txt', 'a') as ffile:
            ffile.write(json.dumps(inv_in))
        
def compute_ranks(graph):
    d = 0.8 # damping factor
    numloops = 10
    
    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages
    
    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            for node in graph:
                if page in graph[node]:
                    newrank = newrank + d*(rank[nodes]/len(graph[node]))
            #Insert Code Here
            
            newranks[page] = newrank
        ranks = newranks
    return ranks


def search_keyword(index, word):
    word = word.lower()
    if word in index:
        url_array = index[word]
        for url in url_array:
            if url in index_titles:
                search = index_titles[url]
                for query in search:
                    print(query)
                    print(url)
    else:
        print("Doesn't exist")

def add_title_index(index_titles,url,title):
    title = title.lower()
    if url in index:
          return
    else:
        index_titles[url] = [title]


def add_to_index(index,keyword,url):
    keyword = keyword.lower()
    if keyword in index:
        if url in index[keyword]:
            return
        else:
            index[keyword].append(url)
            return
    else:
        index[keyword] = [url]


def add_url_to_index(index, url, line):
    words = line.split()
    for entry in words:
        add_to_index(index, entry, url)


def retrieve_title(page):
    start = page.find('<title')
    end = page.find('- Simple English Wikipedia, the free encyclopedia</title>')
    start_title = page.find('>', start)
    title= page[start_title+1:end]
    return title


def retrieve_description(page):
    soup = BeautifulSoup(page, 'html.parser')
    return soup.p.getText()
   
    
def get_url(page):
    start_link = page.find('<a href')
    if start_link==-1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote+1)
    url = page[start_quote+1:end_quote]
    return url, end_quote


def get_page(url):
    file = codecs.open(url, encoding='utf-8')
    return file.read()   
    

def all_links(page):
    links = [] 
    while page:
        url, endpos = get_url(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


def crawler(seed):
    fullname = []
    
    for path,dirs,files in os.walk(seed):
        for f in fnmatch.filter(files,'*.html'):
            fullname.append(os.path.abspath(os.path.join(path,f)))
    for file in fullname:
        
        try:    
            content = get_page(file)
        except:
            continue
        
        to_crawl = [content]
        for_in.clear()
        inv_in.clear()
        while to_crawl:
            page = to_crawl.pop()
            try:
                title = retrieve_title(page)
                
            except:
                continue
            try:
                desc = retrieve_description(page)
            except:
               desc = title+" is a page on Wikipedia Simple."
            url = get_url(page)
            
            if len(title)>0:
                #add_url_to_index(index, file, title)
                #add_url_to_index(index, file, desc)
                #add_title_index(index_titles, file, title)
                forward_index(for_in, title, desc)
                inverted_index(inv_in, url, desc, title)
                crawled.append(file)
            else:
                continue

    print("Number of documents read", len(crawled))
    
       
    
    return crawled
    

        
main_links = crawler('C:/Users/ShaheryarEhsanIHaque/OneDrive - seecs.nust.edu.pk/search engine/a')



print('Done')







