from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
# import time

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': ChromeDriverManager().install()}
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
    news_p=first_article.find('div', class_='article_teaser_body').text

    mars_data['news_title']=news_title
    mars_data['news_p']=news_p


    # Mars Facts tables scraping using pandas
    tables = pd.read_html(url_3)
    mars_facts_df=tables[0]
    mars_facts_df.columns=['Metric', 'measurement']
    mars_facts_df=mars_facts_df.set_index('Metric')
    html_table = mars_facts_df.to_html()

    mars_data['table']=html_table

    # Mars Hemispheres objects
    browser.visit(url_4)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    photos = soup.find_all('div', class_='description')
    base_url='https://astrogeology.usgs.gov'
    img_dict_list=[]


    for each_photo in photos:
    #     find img_url
        h3 = each_photo.find('h3')
        link = each_photo.find('a')
        href = link['href']
        title=h3.text

        # print(f'Getting {title} link')

    #     this will click on each photo link.
        browser.links.find_by_partial_text(title).click()
        pic_html = browser.html
        pic_soup = BeautifulSoup(pic_html, 'html.parser')
        source_photo=pic_soup.find('img', class_="wide-image")['src']
        img_url=(base_url+source_photo)

    #     create dictionary with title and img url and append to list of dictionaries
        img_dict_list.append({'title': title, 'img_url': img_url})
        
    #     go back to original page to follow next link
        browser.visit(url_4)
        mars_data['hemispheres']=img_dict_list


    browser.quit()

    return mars_data
