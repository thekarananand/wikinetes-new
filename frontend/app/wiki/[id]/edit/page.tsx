// CSS
import "@/styles/article_edit.css";

// Next Component
import Link from "next/link";

// Font 
import { inter } from '@/font/inter.js';
import { jetbrain_mono } from '@/font/jetbrain_mono.js';

const BASE_URL: string = "http://127.0.0.1:8000/";

async function getMarkdown(id: string) {

    const res = await fetch(BASE_URL + 'wiki/' + id + "/edit?format=json");
    
    if (!res.ok) {
        throw new Error("Failed to fetch data");
    }
    
    return res.json();
}

export default async function ArticleEdit({ params }: { params: { id: string } }) {
    
    const id = params.id
    const data = await getMarkdown(id);

    return (
        <main className="flex-v aic">

            

            <section id='form' className="grid">

                <div id="top-bar" className="flex-v jcc">
                    
                    <h1 className="block">Edit Article</h1>

                    <div className="flex flex-wrap">
                        <Link href={ '/wiki/' + id + '/' } className="btn block">Back to Article</Link>
                        <button className={inter.className + " btn margin-left-auto" }>Save Changes</button>
                    </div>


                </div>

                <label htmlFor="title">Title</label>
                <input name="title" id="title" type="text" className={ inter.className } defaultValue={ data.title }/>

                <label htmlFor="author">Author</label>
                <input name="author" id="author" type="text" className={ inter.className } defaultValue={ data.author }/>

                <div className="label-and-description">
                    <label htmlFor="md_content">Article Content</label>
                    <p className="description">Basic Markdown Support Available, <Link href='/'>Know More</Link></p>
                </div>
                <textarea name="md_content" id="md_content" className={ jetbrain_mono.className }>
                    { data.md_content }
                </textarea>
            </section>
        </main>

    );
}