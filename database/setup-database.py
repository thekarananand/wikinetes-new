import pymongo

# Create/Access MongoClient to connect to Mongo Contianer
mongo_container = pymongo.MongoClient( 'localhost' , 80 )

# Create/Access DB named wikinetes
db_wikinetes = mongo_container["wikinetes"]

# Create/Access Collection named articles
col_articles = db_wikinetes["articles"]

sampledata = [
    {
        'title': 'How to Hack Google',
        'author': 'Karan Anand',
        'article_html_content': """# I don't Know

Water, the elixir of life. We gulp it down, splash in it, even cook with it, often taking its purity for granted. But lurking beneath its seemingly innocuous surface, a world of complexity unfolds, where unseen contaminants can wreak havoc on our health and well-being. So, what does "pure" water truly mean? And can we ensure we're getting the good stuff?
        """,
        'table_of_content': [
            "# I don't Know"
        ],
    },
    {
        'title': 'H2: H2O, Oh No! Unraveling the Mysteries of Water Purity?',
        'author': 'ChatGPT & Karan Anand',
        'article_html_content': """# Introduction

Water, the elixir of life. We gulp it down, splash in it, even cook with it, often taking its purity for granted. But lurking beneath its seemingly innocuous surface, a world of complexity unfolds, where unseen contaminants can wreak havoc on our health and well-being. So, what does "pure" water truly mean? And can we ensure we're getting the good stuff?

# What Exactly Makes Water "Pure"?

Purity is a relative term, especially when it comes to water. In its natural state, water collects minerals, organic matter, and even microorganisms as it flows through rivers, lakes, and underground aquifers. While some of these elements enhance its taste and provide essential nutrients, others can harbor harmful bacteria, heavy metals, or chemical pollutants.

The quest for "pure" water, then, involves removing these unwanted elements to a level deemed safe for human consumption. This process can vary depending on the source and intended use:

- **Public water systems** treat water using a multi-step approach, typically employing filtration, coagulation, disinfection, and sometimes additional processes like reverse osmosis. This ensures its compliance with national or regional drinking water quality standards.
- **Bottled water** undergoes filtration and purification processes, which can vary across brands and sources. While often marketed as "pure," it's essential to scrutinize labels and understand the treatment methods used.
- **Home filtration systems** offer varying levels of purification, from carbon filters targeting chlorine and taste impurities to reverse osmosis systems removing a wider range of contaminants. Choosing the right system depends on your specific water quality concerns and local regulations.
        
# Beyond Purity: Understanding the Human Factor

Even "pure" water isn't a guarantee of absolute safety. Contamination can occur after treatment, during storage, or even within our own homes through pipes and storage containers. It's crucial to practice good hygiene and proper water handling techniques to minimize risks.

## Be a Savvy Water Consumer

- **Be informed:** Familiarize yourself with your local water quality reports and understand the treatment processes used.
- **Read labels:** Scrutinize bottled water labels to understand the source, purification methods, and mineral content.
- **Consider home filtration:** If your water quality raises concerns, explore reputable home filtration systems tailored to your needs.
- **Practice good hygiene:** Wash your hands thoroughly before handling drinking water, and regularly clean containers and storage units.

Remember, the water you drink shapes your health. Stay informed, make informed choices, and enjoy the life-giving power of pure water with confidence!
        """,

        'table_of_content': [
            "# Introduction",
            "# What Exactly Makes Water \"Pure\"?",
            "# Beyond Purity: Understanding the Human Factor",
            "## Be a Savvy Water Consumer"
        ],
    }
]


_id = col_articles.insert_many(sampledata)

print(_id)