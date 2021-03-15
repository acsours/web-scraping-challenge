from splinter import Browser
from bs4 import BeautifulSoup

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    mars_data = {}
    # NASA Mars News
    url_1 = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    # JPL Mars Space Images - Featured Image
    url_2 = "https://www.jpl.nasa.gov/images?search=&category=Mars"
    # Mars Facts
    url_3 = "https://space-facts.com/mars/"
    # Mars Hemispheres
    url_4 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    browser.visit(url_1)

    html=browser.html
    news_soup=BeautifulSoup(html,'html.parser')
    first_article=news_soup.find('ul', class_='item_list')
    news_title=first_article.find('div', class_='content_title').a.text
    news_p=first_article.a.text

    mars_data['news_title']=news_title
    mars_data['news_p']=news_p

    browser.quit()

    return mars_data