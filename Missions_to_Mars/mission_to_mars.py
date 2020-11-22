from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import datetime as dt
import time
from webdriver_manager.chrome import ChromeDriverManager



def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path':ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    # nasa mars website url
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the news titles
    #latest_titles = soup.find("div", class_="content_title").text
    #print(latest_titles)

    # get news title - list then div tag
    headline_list = soup.find('li', class_='slide')
    # --- save the content_title ---
    latest_title = headline_list.find('div', class_='content_title').text
    print(latest_title)

    #latest_titles = soup.find_all('div', {'class': 'content_title'})
    #for title in latest_titles:
        #print(title.get_text())

    #   Get the paragraph text
    paragraph = soup.find("div", class_="article_teaser_body").text


    # # BONUS: Find the src for background img
    #relative_image_path = soup.findAll('img').get('src')
    
    #mars_img = "https://mars.nasa.gov/"+relative_image_path

    #Store data in a dictionary
    mars_data = {
 #        "mars_img": mars_img,
         "paragraph": paragraph,
         "latest_titles": latest_title
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data
print(scrape_info())

    
