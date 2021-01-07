function createSocialSection(index, userLoggedImage, userName) {
    args = userName+","+index
    console.log(args)
    return " <div class=\"d-flex flex-column comment-section \" id=\"myGroup" + index + "\">\n" +
        "    <div class=\"p-2 p-2 border-bottom\">\n" +
        "        <div class=\"d-flex flex-row fs-12\">\n" +
        "            <div class=\"like p-2 cursor\" id=\"likeBtn-" + index + "\" onclick=\"handleLike("+ index +")\">\n" +
        "                <i class=\"fa fa-thumbs-up\"><span id=\"likesCounter" + index + "\" class=\"badge badge-light\"></span></i>\n" +
        "            </div>\n" +
        "            <div class=\"like p-2 cursor action-collapse\" data-toggle=\"collapse\"\n" +
        "                 aria-expanded=\"true\" aria-controls=\"collapse-" + index + "\" href=\"#collapse-" + index + "\">\n" +
        "                <i class=\"fa fa-comments-o\"><span id=\"commentsCounter" + index + "\" class=\"badge badge-light\"></span></i>\n" +
        "            </div>\n" +
        "            <div class=\"like p-2 cursor action-collapse\" data-toggle=\"collapse\" aria-expanded=\"true\"\n" +
        "                 aria-controls=\"collapse-2\">\n" +
        "                <i class=\"fa fa-share\"></i>\n" +
        "            </div>\n" +
        "        </div>\n" +
        "    </div>\n" +
        "    <div id=\"collapse-" + index + "\" class=\"p-2 collapse\" data-parent=\"#myGroup" + index + "\">\n" +
        "        <div id=\"comments" + index + "\" class=\"d-flex flex-column p-2\">\n" +
        "\n" +
        "\n" +
        "        </div>\n" +
        "        <div class=\"d-flex flex-row align-items-start\" style=\"margin-top: 20px;\">\n" +
        "        <div class ='circle-img img-circle rounded-circle'>\n" +
        "            <img src=" + userLoggedImage + ">\n" +
        "        </div>  \n" +
        "            <textarea class=\"form-control ml-1 shadow-none textarea\" id=\"comment-message" + index + "\" placeholder=\"Escriba un comentario...\"></textarea>\n" +
        "        </div>\n" +
        "        <div class=\"mt-2 text-right action-collapse \">\n" +
        "            <button class=\"btn btn-primary btn-sm shadow-none\" type=\"button\" id=\"comment-button\" onclick=submitComment(" + index + ")>Comment</button>\n" +
        "            <button class=\"btn btn-outline-primary btn-sm ml-1 shadow-none \" data-toggle=\"collapse\"\n" +
        "                    aria-expanded=\"true\" aria-controls=\"collapse-" + index + "\" href=\"#collapse-" + index + "\" href=\"#collapse-" + index + "\" type=\"button\">\n" +
        "                Cancel\n" +
        "            </button>\n" +
        "        </div>\n" +
        "    </div>\n" +
        "</div>\n"
}


function createCard(card) {

    console.log(card)

    let socialSection = createSocialSection(card.id, card.profile_img, card.User)

    let post =
        "<div class=\"bg-white border mt-2\" id=\"post" + card.id + "\">\n" +
        "    <div id =\"post-header\" class=\" d-flex flex-row justify-content-between align-items-center p-3 \">\n" +
        "        <div class=\"d-flex flex-row align-items-center feed-text\">\n" +
        "            <div class=\"circle-img img-circle rounded-circle\">\n" +
        "                <img src=\"https://images.pexels.com/photos/1370750/pexels-photo-1370750.jpeg\">\n" +
        "            </div>\n" +
        "            <div id=\"post-info\" class=\"d-flex flex-column flex-wrap ml-2\">\n" +
        "                <span class=\"font-weight-bold\" id=\"post-user\">@" + card.User + "</span>\n" +
        "                <span id=\"post-type\"><b>Apostó "+card.coins +" coins: </b>" + card.bet + "</span>\n" +
        "                <span class=\"text-black-50 time\" id=\"post-time\">" + card.time + "</span>\n" +
        "            </div>\n" +
        "        </div>\n" +
        "        <div class='dropdown ml-auto p-2'>" +
        "           <i class=\"feed-icon px-2 fa fa-ellipsis-v ml-auto p-2\" data-toggle='dropdown' role='button' aria-haspopup=\"true\" aria-expanded='false' id=\"postOption" + card.id + "\"></i>\n" +
        "           <ul aria-labelledby=\"postOption" + card.id + "\" class='dropdown-menu'>\n" +
        "               <li> <a class='dropdown-item' onclick=deletePost(" + card.id + ") role='button'>Eliminar</a></li>\n" +
        "           </ul>" +
        "       </div>" +
        "    </div>\n" +
        "    <div id=\"post-content\"></div>\n" +
        "    <span class=\"p-2 px-3\" id=\"post-message\">" + card.message + "</span>\n" +
        "\n" + socialSection +
        "</div>"

    $("#posts-content").append(post)


    card.comments.forEach((comment) => {
        console.log(comment)
        addComment("@" + comment.User, comment.profile_img, card.id, comment.message)
    })

    $("#commentsCounter" + card.id).html(card.comments.length)
    $("#likesCounter" + card.id).html(card.likes.length)
    let userId = 1
    console.log('user id')
    console.log(userId)
    console.log(card.likes)

    console.log(userId in card.likes)
    if (card.likes.includes(userId)) {

        document.getElementById("likeBtn-" + card.id ).style.color = 'orange'
    }
    else {
        document.getElementById("likeBtn-" + card.id ).style.color = 'black'
    }
}

function createPost(posts) {

    console.log(posts)

    // data['posts'].forEach(createCard)
    posts.forEach(createCard)

}

async function getPosts(page) {
    try {
        let response = await fetch("get_posts/"+page)
        if (!response.ok)
            throw {
                status: response.status,
                statusText: response.statusText,
            }
        let posts = await response.json()
        if(posts.length >0) {
            createPost(posts)
            return true
        }
        else {
            return false
        }

    } catch (e) {
        console.log(e)

    } finally {

    }
}


getPosts(0)
