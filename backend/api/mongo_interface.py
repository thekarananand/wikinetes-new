import pymongo

# Create/Access MongoClient to connect to Mongo Contianer
mongo_container = pymongo.MongoClient( 'localhost' , 80 )

# Create/Access DB named wikinetes
db_wikinetes = mongo_container["wikinetes"]

# Create/Access Collection named articles
col_articles = db_wikinetes["articles"]

def fetch_article():
    pass

def fetch_markdown():
    pass