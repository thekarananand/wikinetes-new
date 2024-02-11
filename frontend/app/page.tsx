// import Image from "next/image";
import "@/styles/article_view.css";


const BASE_URL: string = "http://127.0.0.1:8000/";

async function getArticle() {
    const res = await fetch(BASE_URL + "?format=json");
    
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
            return ( <li data-hierarchy={hierarchy}>{topic}</li> )
        }
    }

}

function TableOfContent ( topic_list: any ) {

    let index: number = 1

    return (
        <ul>
            { topic_list['topic_list'].map( ( element: string ) => (
                <ElementTableOfContent key={index++} topic={element} />
            ))}
        </ul>
    )
}

export default async function ArticleView() {
    const data = await getArticle();

    return (
        <main className="flex jcc">
            <div className="grid article_container">
                <article>

                    <div className="article_header flex-v jcc">
                        <h1>{ data.title }</h1>

                        <div className='author'>
                            Written by: <span>{ data.author }</span>
                        </div>
                    </div>

                    <div className="article_body" dangerouslySetInnerHTML={ createMarkup( data.article_html_content ) }/>

                </article>
                <aside>
                    <section className="table_of_content">
                        <h3>Table of Content</h3>
                        <TableOfContent topic_list={ data.table_of_content } />
                    </section>
                </aside>
            </div>
        </main>
    );
}