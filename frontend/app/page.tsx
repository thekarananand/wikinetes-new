// import Image from "next/image";
import Script from "next/script";

const BASE_URL: string = "http://127.0.0.1:8000/";

const getArticlesList = async () => {

    const res = await fetch(BASE_URL + "?format=json");
    
    if (!res.ok) {
        throw new Error("Failed to fetch data");
    }
    
    return res.json();
}

const ArticleList = (list: any) => {

    list  = list["list"]

    return (


        <ul>
            { list.map( ( article: object ) => (
                <li>
                    <a href={BASE_URL + 'wiki/' + article.id}>
                        <h3>{article.title}</h3>
                        <p>{article.author}</p>
                    </a>
                </li>
            ))}
        </ul>
    )
}

export default async function HomePage() {
    
    const data = await getArticlesList()

    return (
        <ArticleList list={ data } />
    )
}
