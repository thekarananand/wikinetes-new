import pymongo
from bson.objectid import ObjectId

from .md2html import md2html

# Create/Access MongoClient to connect to Mongo Contianer
mongo_container = pymongo.MongoClient( 'localhost' , 80 )

# Create/Access DB named wikinetes
db_wikinetes = mongo_container["wikinetes"]

# Create/Access Collection named articles
col_articles = db_wikinetes["articles"]


def fetch_article_list():

    article_list = []

    for article in col_articles.find({}, {'_id': True, 'title': True, 'author': True}):

        list_entry = {}

        id = str(article['_id'])
        title = article['title']
        author = article['author']

        list_entry['id'] = id
        list_entry['title'] = title
        list_entry['author'] = author

        article_list.append(list_entry)

    return( article_list )

def fetch_article_view(id):
    article = col_articles.find_one({'_id': ObjectId(id)}, { '_id': False, 'title': True, 'author': True, 'md_content': True, 'table_of_content': True })

    print(article)

    print(article["md_content"])

    article["html_content"] = md2html( article["md_content"] )

    article.pop("md_content")

    return(article)

def fetch_markdown():
    pass