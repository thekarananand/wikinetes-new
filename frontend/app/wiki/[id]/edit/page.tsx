// CSS
import "@/styles/article-edit.css";

// Component Imports
import Editor from "@/components/Editor";

const BASE_URL: string = "http://127.0.0.1:8000/";

export default async function ArticleEdit({ params }: { params: { id: string } }) {

    const id = params.id
    const res_url: string = BASE_URL + 'wiki/' + id + "/edit"
    const red_url: string = '/wiki/' + id

    const getMarkdown = async () => {

        const res = await fetch( res_url + "?format=json" );
    
        if (!res.ok) { throw new Error("Failed to fetch data"); }
        
        return res.json();
        
    }

    const data = await getMarkdown();

    return (
        <Editor
            resUrl = { res_url } 
            redUrl = { red_url }
            initTitle = { data.title }
            initAuthor = { data.author }
            initMD = { data.md_content }
        />
    )

}