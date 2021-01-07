const userName = 'Jeff'

function changeLikeColor(postIndex) {

    const likeBtn =  document.getElementById("likeBtn-" + postIndex );
    const likesCounter = $("#likesCounter" + postIndex)

     if (likeBtn.style.color === "black") {
         likeBtn.style.color ="orange"
         likesCounter.html(parseInt(likesCounter.html()) + 1)
     }
     else {
         
         likeBtn.style.color ="black"
         likesCounter.html(parseInt(likesCounter.html()) - 1)
     }

}

async function handleLike(postIndex) {
    let csrfToken = getCookie('csrftoken')
     try {
            let response = await fetch("handle_like",
                {
                    method: "post",
                    headers: {
                        "Accept": 'application/json',
                        "Content-Type": 'application/json',
                        "X-CSRFToken": csrfToken,
                    },
                    body: JSON.stringify({
                        user: userName,
                        post: postIndex,
                    })
                })
            if (!response.ok) {
                throw {
                    status: response.status,
                    statusText: response.statusText
                }
            }

            changeLikeColor(postIndex)

        } catch (e) {
            console.log(e)

        } finally {

        }


}