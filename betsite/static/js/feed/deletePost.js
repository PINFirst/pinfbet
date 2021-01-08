async function deletePost(index) {
    let post = document.querySelector("#post" + index)
    console.log("el post " + index + " ha sido eliminado")

    let csrfToken = getCookie('csrftoken')


    if (post) {
        try {
            let response = await fetch("delete_post",
                {
                    method: "post",
                    headers: {
                        "Accept": 'application/json',
                        "Content-Type": 'application/json',
                        "X-CSRFToken": csrfToken,
                    },
                    body: JSON.stringify({
                        post: index,
                    })
                })
            if (!response.ok) {
                throw {
                    status: response.status,
                    statusText: response.statusText
                }

            }
            post.remove()
        } catch (e) {
            console.log(e)

        } finally {

        }
    }
}
