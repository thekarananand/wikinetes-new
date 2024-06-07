import pymongo
from bson.objectid import ObjectId

from .md2html import md2html

# Create/Access MongoClient to connect to Mongo Container
mongo_container = pymongo.MongoClient( 'mongo' , 27017 )

# Create/Access DB named wikinetes
db_wikinetes = mongo_container["wikinetes"]

# Create/Access Collection named articles
col_articles = db_wikinetes["articles"]


def fetch_article_list():

    query = {}
    
    projection = {
        '_id': True,
        'title': True,
        'author': True
    }

    article_list = []

    for article in col_articles.find( query, projection ):

        list_entry = {}

        id= str(article['_id'])
        title = article['title']
        author = article['author']

        list_entry['id'] = id
        list_entry['title'] = title
        list_entry['author'] = author

        article_list.append(list_entry)

    return( article_list )

def fetch_article_view(id):

    query = { '_id': ObjectId(id) }

    projection = {
        '_id': False,
        'title': True,
        'author': True,
        'md_content': True,
        'table_of_content': True
    }

    article = col_articles.find_one( query, projection )
    
    article["html_content"] = md2html( article["md_content"] )
    article.pop("md_content")

    return(article)

def fetch_article_edit(id):

    query = { '_id': ObjectId(id) }

    projection = {
        '_id': False,
        'title': True,
        'author': True,
        'md_content': True,
    }

    markdown = col_articles.find_one( query, projection )

    return(markdown)

def update_article(id, new_values):

    query = { '_id': ObjectId(id) }

    projection = {
        '_id': False,
        'title': True,
        'author': True,
        'md_content': True,
    }

    old = col_articles.find_one( query, projection)

    new = { "$set": new_values }

    col_articles.update_one(old, new)
