const EditorSendRes = async ( resUrl:string, title:string, author:string, md_content:string ) => {

    const res = await fetch(resUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
            title: title , 
            author: author ,
            md_content: md_content
        })
    });

    if (!res.ok) { throw new Error("Failed to POST data"); }

}

export default EditorSendRes