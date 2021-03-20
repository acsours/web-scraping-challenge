# web-scraping-challenge

This is a web scraping app written using python, pymongo, and flask. 

* scrape_mars.py scrapes most current data from four different Mars websites
* app.py calls the scrape_mars script using flask and stores data in a pymongo database
* data is retrieved from database and rendered with jinja in an HTML template
* When the main button is clicked in the index.html file, the end route is changed and the scrape_mars.py app is called to populate the dashboard with most current Mars data. 

#### Dashboard Preview

![dashboard.png](Mission_to_Mars/images/dashboard.png?raw=true "Title")

![hemispheres.png](Mission_to_Mars/images/hemispheres.png?raw=true "Title")