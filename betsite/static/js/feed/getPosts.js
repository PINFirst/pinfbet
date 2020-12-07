

(
    async function getPosts() {
        try {
            let response = await fetch("get_posts")
            if (!response.ok)
                throw {
                    status: response.status,
                    statusText: response.statusText
                }
            let data = await response.json()
            console.log(data)
            createPost(data)

        } catch (e) {
            console.log(e)

        } finally {

        }
    }
)();