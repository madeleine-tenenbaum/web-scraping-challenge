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
    
    
    #nasa mars website news
    ####################################
    browser = init_browser()
    
    # nasa mars website url
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # get news title - list then div tag
    headline_list = soup.find('li', class_='slide')
    # --- save the content_title ---
    latest_title = headline_list.find('div', class_='content_title').text
    print(latest_title)

    #   Get the paragraph text
    paragraph = soup.find("div", class_="article_teaser_body").text
    print(paragraph)

    #nasa mars image
    #########################

    browser = init_browser()
    
    # nasa jpl mars website url
    jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(jpl_url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")


    # --- find 'full image'
    relative_image_path = soup.find('a', id='full_image')['data-fancybox-href']
    
    mars_img = "https://jpl.nasa.gov"+relative_image_path

    print(mars_img)

    #nasa mars facts
    ####################################

    browser = init_browser()
    
    # nasa jpl mars website url
    facts_url = "https://space-facts.com/mars/"
    browser.visit(facts_url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")


    # --- find 'full image'
    mars_table = pd.read_html(html)

    # --- use indexing to slice the table to a dataframe ---
    mars_df = mars_table[0]
    mars_df.columns =['Description', 'Value']

    # --- convert the dataframe to a HTML table and pass parameters for styling ---
    mars_facts = mars_df.to_html(index=False, header=False, border=0, classes="table table-sm table-striped font-weight-light")

    print("Mars Facts: Scraping Complete!")

    print(mars_facts)

    #Store data in a dictionary
    mars_data = {
         "mars_img": mars_img,
         "paragraph": paragraph,
         "latest_title": latest_title,
         "mars_facts": mars_facts
    }


    # Return results
    return mars_data
print(scrape_info())

    
