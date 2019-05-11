from web_page_downloader import WebPageDownloader
from web_page_downloader_flickr import WebPageDownloaderFlickr

import os

pre = 'FLICKR' #can be SHUTTER, GOOG, FLICKR, or SOLO
# keywords = ["LSD", "lysergic+Acid+diethylamide", "LSD+molecule", "LSD+blotter", "LSD+Tablet"]
# keywords = ["pills", "medication","prescription+drugs","drugs","medical+pills","medical+drugs","pharmacy+drugs"]
keywords = ["pharmaceutical+labs", "drug+labs", "science+lab", "laboratory", "chemistry+lab"]
    
url = "http://genekogan.com/works/deepdream/"
    
folder = './druglabs'
# os.mkdir(folder)



if pre == 'GOOG':
    PAGEDOWNLOAD=WebPageDownloader('https://www.shutterstock.com', folder, '', 0, 2)
    for i in range(len(keywords)):
        keyword = keywords[i]
        url = "https://www.google.com/search?q={}&hl=en&source=lnms&tbm=isch".format(keyword)
        PAGEDOWNLOAD.url = url 
        PAGEDOWNLOAD.prefix = pre+str(i)+'_'
        PAGEDOWNLOAD.scroll_n = 7
        PAGEDOWNLOAD.scroll_pause_time = 2
        PAGEDOWNLOAD.download_images()

if pre == 'SOLO':
    PAGEDOWNLOAD=WebPageDownloader('https://www.shutterstock.com', folder, '', 0, 2)
    PAGEDOWNLOAD.url = url 
    PAGEDOWNLOAD.prefix = pre+'_'
    PAGEDOWNLOAD.scroll_n = 7
    PAGEDOWNLOAD.scroll_pause_time = 2
    PAGEDOWNLOAD.download_images()

if pre == 'SHUTTER':
    PAGEDOWNLOAD=WebPageDownloader('https://www.shutterstock.com', folder, '', 0, 2)
    for i in range(0, 98):
        url = "https://www.shutterstock.com/search/pharmaceutical+production?ref_context=keyword&page={}".format(i)
        PAGEDOWNLOAD.url = url 
        PAGEDOWNLOAD.prefix = pre+str(i)+'_'
        PAGEDOWNLOAD.scroll_n = 1
        PAGEDOWNLOAD.scroll_pause_time = 2
        PAGEDOWNLOAD.download_images()    

if pre == 'FLICKR':
    PAGEDOWNLOAD=WebPageDownloaderFlickr('https://www.shutterstock.com', folder, '', 0, 2)
    for i in range(len(keywords)):
        keyword = keywords[i]
        url = "https://www.flickr.com/search/?media=photos&text={}&dimension_search_mode=min&height=640&width=640".format(keyword.replace('+','%20'))
        PAGEDOWNLOAD.url = url 
        PAGEDOWNLOAD.prefix = pre+str(i)+'_'
        PAGEDOWNLOAD.scroll_n = 20
        PAGEDOWNLOAD.scroll_pause_time = 5
        PAGEDOWNLOAD.download_images()