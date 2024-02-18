def block_md_to_block_html(input_array):

    output_array = []

    # status word
    paragraph = False
    unordered_list = False
    ordered_list = False

    # block elements only   
    for line in input_array:

        #check blankline or only whitespaces
        if ( ( len(line) == 0 ) or ( ( ( sorted(line)[0] == ' ' ) and ( sorted(line)[-1] == ' ' ) ) ) ):
            if ( paragraph ):
                output_array[-1] += '</p>'
                paragraph = False
            
            elif ( unordered_list ):
                output_array[-1] += '</li>'
                output_array.append('</ul>')
                unordered_list = False

        # no h1 as h1 is used for the title of the page and there should be only one h1 on a page
        
        #check H2
        elif ( line.strip()[0 : 2] == '# ' ):
            output_array.append(f'<h2>{line[ 2 : ]}</h2>')

        #check H3
        elif ( line.strip()[0 : 3] == '## ' ):
            output_array.append(f'<h3>{line[ 3 : ]}</h3>')

        #check H4
        elif ( line.strip()[0 : 4] == '### ' ):
            output_array.append(f'<h4>{line[ 4 : ]}</h4>')

        #check for ul
        elif ( line.strip()[0 : 2] == '- ' ):

                
            if ( output_array[-1] == '</ul>' ):
                output_array.pop()

            elif ( unordered_list ):
                output_array[-1] += '</li>'
            
            else:
                output_array.append('<ul>')
                
            unordered_list = True
            output_array.append( f'<li>{line.strip()[ 2 : ]}' )
            
        
        else:
            if ( unordered_list ):
                output_array[-1] += line

            elif ( paragraph ): 
                output_array[-1] += line

            else :
                paragraph = True
                output_array.append(f'<p>{line}')

    return output_array

def split_and_replace_logic(input_element, delimiter, opening_tag, closing_tag):
    
    splitted_element_array = input_element.split(delimiter)
    new_element = ''
    tag_open = False

    for i in range( len(splitted_element_array) ):
        new_element += splitted_element_array[i]

        if ( len(splitted_element_array) != i + 1 ): 
            if (tag_open):
                new_element += closing_tag
                tag_open = False
            else: 
                new_element += opening_tag
                tag_open = True
    
    return(new_element)

def inline_md_to_inline_html(input_array):

    output_array = []

    for element in input_array:

        new_element = element

        new_element = split_and_replace_logic( new_element, '***', '<em><strong>', '</strong></em>' )
        new_element = split_and_replace_logic( new_element, '**', '<strong>', '</strong>' )
        new_element = split_and_replace_logic( new_element, '*' , '<em>', '</em>' )
        new_element = split_and_replace_logic( new_element, '`' , '<code>', '</code>' )

        output_array.append(new_element)


    return(output_array)
            


def md2html(md):

    input_array = md.split('\n')

    intermediate_array = block_md_to_block_html(input_array)
    
    output_array = inline_md_to_inline_html(intermediate_array)

    output_string = ''.join(output_array)

    return(output_string)


# ----------------- Driver Code ----------------- 

# import pymongo
# from bson.objectid import ObjectId

# mongo_container = pymongo.MongoClient( 'localhost' , 80 )
# db_wikinetes = mongo_container["wikinetes"]
# col_articles = db_wikinetes["articles"]

# id = '65ce351652e91bc9fbb14b85'

# query ={ 
#     '_id': ObjectId(id)
# }

# projection = { 
#     '_id': False,
#     'article_html_content': True
# }

# article = col_articles.find_one(query, projection)
 

# md = md2html( article['article_html_content'] )

# for line in md:
#     print(line)