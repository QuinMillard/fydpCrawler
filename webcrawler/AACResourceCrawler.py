import mechanicalsoup
import re
from baseCrawler import BaseCrawler
# from emailClient import EmailClient
from clothingInfo import ClothingInfo
import random
from bs4 import BeautifulSoup

class AACResourceCrawler(BaseCrawler):
    def crawl(self, request_wrapper):
        self.__bad_URL = []
        self.__browser = mechanicalsoup.StatefulBrowser()
        # self.__email_client = EmailClient()
        __siteurl = "https://smallbutkindamighty.com/blogs/news/printable-social-stories-social-narratives-on-stimming-and-aac"
   
        print(str(self.__browser.open(__siteurl)))
        if(str(self.__browser.open(__siteurl)) == "<Response [200]>"):
            __raw_contents = str(self.__browser.get_current_page().find(True))

            __website_soup = BeautifulSoup(__raw_contents,features="lxml")
            for script in __website_soup(["script", "style"]):
                script.decompose()    # rip it out

            # get text
            __text_on_site = __website_soup.get_text()

            # break into lines and remove leading and trailing space on each
            __lines = (line.strip() for line in __text_on_site.splitlines())
            # break multi-headlines into a line each
            chunks = (phrase.strip() for line in __lines for phrase in line.split("  "))
            # drop blank lines
            __text_on_site = '\n'.join(chunk for chunk in chunks if chunk)

            with open('smallbutkindamighty.txt', 'w') as f:
                f.write(__text_on_site)
            # if len(self.__links) == 0:
            #     __message = f'The link regex {__link_regex} did not come up with any values at the url {__siteurl}'
            #     print(__message)
            #     # self.__email_client.sendErrorMessage(__message)

            # self.__crawl_item_links(request_wrapper)

        else:
            pass
            # __message = f'exception raised when opening site: {__siteurl}'
            # print(__message)
            # self.__email_client.sendErrorMessage(__message)

        if len(self.__bad_URL) > 0:
            __bad_URL_string = self.__get_string_from_list(self.__bad_URL)
            # __message = f'exception raised in the following items: {__bad_URL_string}'
            # self.__email_client.sendErrorMessage(__message)

            
    # def __crawl_item_links(self, request_wrapper):
    #     __price_regex = r'CAD" data-react-helmet="true" property="og:price:currency"/><meta content=\"([\d\.]+)'
    #     __item_regex = r'\-helmet\=\"true\" name\=\"description\"\/><meta content\=\"([^\"]*)'
    #     __image_regex = r'image\" data-react-helmet=\"true\" href=\"([^\"]*)'
    #     print(len(self.__links), ' number of items found')
    #     for link in self.__links:
    #         if(str(self.__browser.open(link)) == "<Response [200]>"):
    #             __htmlContents = str(self.__browser.get_current_page().findAll(True))
                
    #             __nike_price = re.compile(__price_regex)
    #             __prices = __nike_price.findall(__htmlContents)

    #             __nike_item = re.compile(__item_regex)
    #             __items = __nike_item.findall(__htmlContents)

    #             __nike_image = re.compile(__image_regex)
    #             __images = __nike_image.findall(__htmlContents)

    #             if(len(__images) > 2 and len(__prices) > 0 and len(__items) > 0):
    #                 __clothing_info = ClothingInfo('Nike', link, __items[0],  __prices[0], __images[2])
    #                 print(__clothing_info.to_string())
    #                 response = request_wrapper.insert_into_db(__clothing_info.to_object())
    #                 print(response)
    #             else:
    #                 __clothing_info = ClothingInfo('Nike', link, __items, __prices, __images)
    #                 self.__bad_URL.append(__clothing_info.to_string())
    #         else:
    #             __clothing_info = ClothingInfo('Nike', link)
    #             self.__bad_URL.append(__clothing_info.to_string())
    
    def __get_string_from_list(self, list):
        __return_string = ""
        for item in list:
            __return_string = __return_string + item
        return __return_string
                