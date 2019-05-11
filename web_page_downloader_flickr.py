from selenium import webdriver
import argparse
import urllib
import time


"""
https://stackoverflow.com/questions/28928068/scroll-down-to-bottom-of-infinite-page-with-phantomjs-in-python/28928684#28928684
https://medium.com/@erika_dike/how-to-download-100-pictures-from-a-site-with-selenium-e23b7ecacb85
https://stackoverflow.com/questions/45781388/how-to-download-all-images-from-webpage-using-python
"""
class WebPageDownloaderFlickr:
    def __init__(self, url, folder, prefix, scroll_n, scroll_pause_time):
        self.url = url
        print(url)
        self.uri = []
        self.folder = folder
        self.prefix = prefix
        self.im_i = 0
        self.scroll_n = scroll_n
        self.scroll_pause_time = scroll_pause_time
        self.driver=webdriver.Chrome('../chromedriver')
        
    def download_images(self):
        
        self.driver.get(self.url)
    
        for i in range(self.scroll_n):  
            srcs = []
            if i % 10 == 0:
                print(i)
            self.driver.execute_script("window.scrollTo("+ str(8000*i) + ", " + str(8000*(i+1)) + ")") 
            time.sleep(self.scroll_pause_time)
        self.r=self.driver.find_elements_by_class_name("photo-list-photo-view")
        for v in self.r:
            src = v.get_attribute('style').split('url("')[-1].replace('");', '')
            if src not in self.uri:
                self.uri.append(src)
                srcs.append(src)
                if src is None:
                    continue
                pos = len(src) - src[::-1].index('/')
#                 print src[pos:]
                self.im_i += 1
                self.g=urllib.urlretrieve(src, "/".join([self.folder, self.prefix + str(self.im_i)+'.jpg']))
            if self.im_i%100 == 0:
                print(self.im_i)
        # self.driver.close()
            

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Scrap Images from a website')
    parser.add_argument('--url', type=str, help='URL')
    parser.add_argument('--folder', type=str, help='folder')
    parser.add_argument('--pre', type=str, default='', help='prefix')

    args = parser.parse_args()
    PAGEDOWNLOAD=WebPageDownloader(args.url, args.folder, args.pre)
    PAGEDOWNLOAD.download_images()
    
