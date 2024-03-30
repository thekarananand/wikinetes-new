"use client"

// React Hooks
import { useState } from "react";

// Next Component
import Link from "next/link";
import { useRouter } from 'next/navigation'

// Component Imports
import EditorSendRes from "@/components/EditorSendRes";

// Font 
import { inter } from '@/font/inter.js';
import { jetbrain_mono } from '@/font/jetbrain_mono.js';

const Editor = ( props: {
    resUrl:string ,
    redUrl:string ,
    initTitle:string,
    initAuthor:string,
    initMD:string 
}) => {

    const router = useRouter()

    const [title, setTitle] = useState(props.initTitle)
    const [author, setAuthor] = useState(props.initAuthor)
    const [md_content, setMD_content] = useState(props.initMD)



    return (
        <main className="flex-v aic">
            <form className="grid">

                <div id="top-bar" className="flex-v jcc">
                    <h1 className="block">Edit Article</h1>
                    <div className="flex flex-wrap flex-r">
                        {/* <Link href={'/wiki/' + id + '/'} className="btn block">Back to Article</Link> */}
                        <button
                            className={inter.className + " btn margin-left-auto"}
                            onClick={ (e) => {
                                    e.preventDefault()
                                    EditorSendRes( props.resUrl, title, author, md_content )
                                    router.push( props.redUrl )
                                } }>
                            Save Changes
                        </button>
                    </div>
                </div>

                <div className="flex aic"><label htmlFor="title">Title</label></div>
                <input
                    name="title"
                    id="title"
                    type="text"
                    className={inter.className}
                    value={title}
                    onChange={(e) => setTitle(e.target.value)} />

                <div className="flex aic"><label htmlFor="author">Author</label></div>
                <input
                    name="author"
                    id="author"
                    type="text"
                    className={inter.className}
                    value={author}
                    onChange={(e) => setAuthor(e.target.value)} />

                <div className="label-and-description">
                    <label htmlFor="md_content">Article Content</label>
                    <p className="description">Basic Markdown Support Available, <Link href='/help/markdown'>Know More</Link></p>
                </div>
                <textarea
                    name="md_content"
                    id="md_content"
                    className={jetbrain_mono.className}
                    onChange={(e) => setMD_content(e.target.value)}
                    value={md_content}>
                </textarea>

            </form>
        </main>
    );
}

export default Editor