from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")


# homeroute retrieves mars data from my mars database
@app.route("/")
def index():
    mars_data = mongo.db.mars_collection.find_one()
    return render_template("index.html", mars_stuff=mars_data)


# calls the scrape method, from scrape_mars
@app.route("/scrape")
def scraper():
    collection = mongo.db.mars_collection
    # call the scrape method, which returns a dictionary, and assign to variable
    mars_dict = scrape_mars.scrape()
    # update collection with the mars_dict 
    # {} no filter meants update everything, upsert will override, you are updating it with your mars dictionary with 2 keys

    collection.update({}, mars_dict, upsert=True)
    # after it calls the scrape method, redirect to the homepage
    return redirect("/", code=302)
    print('Scraping complete')


if __name__ == "__main__":
    app.run(debug=True)
