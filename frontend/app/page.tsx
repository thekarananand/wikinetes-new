// import Image from "next/image";
// import Script from "next/script";

import "@/styles/home-page.css";

import Link from "next/link";

import { inter } from '@/font/inter.js';

// Variable Imports
import BaseUrl from "@/variable/BaseUrl"

const getArticlesList = async () => {

    const res = await fetch( `${BaseUrl}/`, { cache: 'no-store' } );
    
    if (!res.ok) {
        throw new Error("Failed to fetch data");
    }
    
    return res.json();
}

const ArticleList = (list: any) => {

    list  = list["list"]

    return (
        <main>
            <section id="hero" className="flex-v jcc aic">
                <h1>
                    Explore, Learn, Share, <br />
                    The Power of Knowledge.
                </h1>
                <p>
                    Dive into a world of Information with WikiNetes, where the community <br /> curates articles on any topic imaginable.
                </p>
                <form action="">
                    <input type="text" name="" id="" className={ inter.className } placeholder="Search WikiNetes..."/>
                    <input type="submit" value="Search" className={ inter.className }/>
                </form>
            </section>
            <section id="list" className="flex jcc aic">
                <div>
                    <h2>Hot Articles</h2>
                    <ul className="grid">
                        { list.map( ( article:{id:string, title:string, author:string}, index: number ) => (
                            <li key={index}>
                                <Link href={'./wiki/' + article.id}>
                                    <h3 className="title">{article.title}</h3>
                                    <p className="author">{article.author}</p>
                                </Link>
                            </li>
                        ))}
                    </ul>
                </div>
            </section>
        </main>

    )
}

export default async function HomePage() {
    
    const data = await getArticlesList()

    return (
        <ArticleList list={ data } />
    )
}
