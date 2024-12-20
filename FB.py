from splinter import Browser
from bs4 import BeautifulSoup as soup
import time

#CURRENT BUGS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#The scraper currently works as intended however Facebook is known the change the class names regularly thus the scraper may break. However that can be fixed easily by using inspect
#element on the website. Additionally, for some reason some of the parameters don't work, such as max year, or transmission type. I believe this is due to the way that Facebook has
#anti-scraping measures in place and when you try to click the filters manually without being logged in, you'll be prompted to do so.
#Future plans to combat this could include logging into a burner account.

#Sets up Splinter
browser = Browser('chrome')

#Base URL of FB Marketplace
baseURL = "https://www.facebook.com/marketplace/toronto"

#FB Marketplace URL with parameters
minPrice = 500
maxPrice = 7000
maxYear = 2013
transType = "manual"

#You can edit this URL to change the filter option
paramURL = f"{baseURL}/vehicles?minPrice={minPrice}&maxPrice={maxPrice}&maxYear={maxYear}&sortBy=creation_time_descend&carType=convertible%2Ccoupe%2Chatchback%2Csedan&transmissionType={transType}&exact=false"

#Opens website
browser.visit(paramURL)

#Closes login button after 2 seconds
time.sleep(2)
if browser.is_element_present_by_css('div[aria-label="Close"]', wait_time=10):
    browser.find_by_css('div[aria-label="Close"]').first.click()

#I tried making the browser continuously scroll down, however FB has it set up so that when you
#reach a certain height, it'll prompt you to login and you cannot close out of it.
# time.sleep(2)
#Scrolls to find more results
# scrollCount = 4
# scrollDelay = 2
# scrollInc = 2000
# for i in range(scrollCount):
#     print("Scrolling")
#     browser.execute_script(f"window.scrollTo(0, {scrollInc});")
#     scrollInc += 2000
#     time.sleep(scrollDelay)

#Scrolls down to near the maximum to see the MOST available posts
print("Scrolling")
browser.execute_script("window.scrollTo(0, 2500)")

#Pases the HTML
html = browser.html

#Creates a BeautifulSoup object from the scraped HTML
marketSoup = soup(html, 'html.parser')

#Closes Browser
browser.quit()

print("Parsing data, one second...")

#Gets titles of all cars and puts them into a list
titlesDiv = marketSoup.find_all('span', class_= "x1lliihq x6ikm8r x10wlt62 x1n2onr6")
titlesList = [title.text.strip() for title in titlesDiv]

#Gets prices and puts them into list
pricesDiv = marketSoup.find_all('span', class_= "x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x676frb x1lkfr7t x1lbecb7 x1s688f xzsf02u")
pricesList = [price.text.strip() for price in pricesDiv]

#URLS
urlDiv = marketSoup.find_all('a', class_="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g x1sur9pj xkrqix3 x1lku1pv")
urlList = [url.get('href') for url in urlDiv]
urlList = ['www.facebook.com' + '/'.join(link.split('/')[:4]) for link in urlList]

#Cities (if applicable) and millage
milageDiv = marketSoup.find_all('span', "x1lliihq x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft x1j85h84")
milageList = [milage.text.strip() for milage in milageDiv]

#Organizes everything into a nice readable form
listOfCars = []
for i in range (len(titlesList)):
    print(titlesList[i] + " " + pricesList[i])
    print(milageList[i * 2] + " " + milageList[i * 2 + 1])
    print(urlList[i])
    print()


#Use this to find the 'a' class for URLS if they change in the future
#divs = marketSoup.find_all('div')
