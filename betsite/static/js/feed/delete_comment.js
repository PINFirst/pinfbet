async function deleteComments(postIndex, commentIndex) {
    let comment = document.querySelector("#post" + postIndex + " #comment" + commentIndex)
    console.log("el comentario " + commentIndex + " del post " + postIndex + " ha sido eliminado")

    let csrfToken = getCookie('csrftoken')


    if (comment) {
        try {
            let response = await fetch("delete_comment",
                {
                    method: "post",
                    headers: {
                        "Accept": 'application/json',
                        "Content-Type": 'application/json',
                        "X-CSRFToken": csrfToken,
                    },
                    body: JSON.stringify({
                        post: postIndex,
                        comment: commentIndex,
                    })
                })
            if (!response.ok) {
                throw {
                    status: response.status,
                    statusText: response.statusText
                }

            }
            comment.remove()

            let commentsCounter = $("#commentsCounter" + postIndex)
            commentsCounter.html(parseInt(commentsCounter.html()) - 1)

        } catch (e) {
            console.log(e)

        } finally {

        }
    }
}