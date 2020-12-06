async function getPosts() {
    let response = await fetch("get_posts")
    let data = await response.json()
    console.log(data)
}