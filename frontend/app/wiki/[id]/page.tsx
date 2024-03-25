// CSS
import "@/styles/article-view.css";
import "@/styles/readable-article.css";

// Next Component
import Link from "next/link";

const BASE_URL: string = "http://127.0.0.1:8000/";

async function getArticle(id: number) {

    const res = await fetch(BASE_URL + 'wiki/' + String(id) + "?format=json");
    
    if (!res.ok) {
        throw new Error("Failed to fetch data");
    }
    
    return res.json();
}

function createMarkup( content: string ) {
    return { __html: content };
}

function ElementTableOfContent ( topic: any ) {

    topic = topic['topic']

    let hierarchy = 0

    while (true) {
        if ( topic.substring(0,1) == '#') {
            topic = topic.substring(1)
            hierarchy += 1
        } else {
            if ( topic.substring(0,1) == ' ') {
                return ( <li data-hierarchy={hierarchy}>{topic.substring(1)}</li> )
            }
            return ( <li data-hierarchy={hierarchy}>{topic}</li> )
        }
    }

}

function TableOfContent ( topic_list: any ) {

    return (
        <ul>
            { topic_list['topic_list'].map( ( element: string, index: number ) => (
                <ElementTableOfContent key={index++} topic={element} />
            ))}
        </ul>
    )
}

export default async function ArticleView({ params }: { params: { id: number } }) {
    
    const id = params.id
    const data = await getArticle(id);

    return (
        <main className="flex jcc">
            <div className="grid">
                <article>

                    <div className="article-header flex-v jcsb">
                        <h1>{ data.title }</h1>

                        <div className='metadata'>
                            Written by: <span>{ data.author }</span>
                        </div>
                    </div>

                    <div className="article_body" dangerouslySetInnerHTML={ createMarkup( data.html_content ) }/>

                </article>

                <aside>
                    <div>
                        <section className="Table_of_Content">
                            <h3>Table of Content</h3>
                            <TableOfContent topic_list={ data.table_of_content } />
                        </section>

                        <section className="Toolkit">
                            <h3>Toolkit</h3>
                            <div className="flex">
                                <Link href= { '/wiki/'+id+'/edit' }  className="btn" >Edit</Link>
                            </div>
                        </section>
                    </div>
                </aside>
            </div>

        </main>

    );
}