function createSocialSection(index, userLoggedImage) {
    return " <div class=\"d-flex flex-column comment-section \" id=\"myGroup" + index + "\">\n" +
        "    <div class=\"p-2 p-2 border-bottom\">\n" +
        "        <div class=\"d-flex flex-row fs-12\">\n" +
        "            <div class=\"like p-2 cursor\" id=\"likeBtn-" + index + "\" onclick=\"changeLikeColor(" + index + ")\">\n" +
        "                <i class=\"fa fa-thumbs-up\"></i>\n" +
        "            </div>\n" +
        "            <div class=\"like p-2 cursor action-collapse\" data-toggle=\"collapse\"\n" +
        "                 aria-expanded=\"true\" aria-controls=\"collapse-" + index + "\" href=\"#collapse-" + index + "\">\n" +
        "                <i class=\"fa fa-comments-o\"></i>\n" +
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


function createCard(card, index) {
    console.log(card.User)

    let socialSection = createSocialSection(index, card.profile_img)

    let post =
        "<div class=\"bg-white border mt-2\" id=\"post" + index + "\">\n" +
        "    <div id =\"post-header\" class=\" d-flex flex-row justify-content-between align-items-center p-3 \">\n" +
        "        <div class=\"d-flex flex-row align-items-center feed-text\">\n" +
        "            <div class=\"circle-img img-circle rounded-circle\">\n" +
        "                <img src=\"https://images.pexels.com/photos/1370750/pexels-photo-1370750.jpeg\">\n" +
        "            </div>\n" +
        "            <div id=\"post-info\" class=\"d-flex flex-column flex-wrap ml-2\">\n" +
        "                <span class=\"font-weight-bold\" id=\"post-user\">@" + card.User + "</span>\n" +
        "                <span id=\"post-type\"><b>Apostó: </b>" + card.bet + "</span>\n" +
        "                <span class=\"text-black-50 time\" id=\"post-time\">" + card.time + "</span>\n" +
        "            </div>\n" +
        "        </div>\n" +
        "        <div class='dropdown ml-auto p-2'>" +
        "           <i class=\"feed-icon px-2 fa fa-ellipsis-v ml-auto p-2\" data-toggle='dropdown' role='button' aria-haspopup=\"true\" aria-expanded='false' id=\"postOption" + index + "\"></i>\n" +
        "           <ul aria-labelledby=\"postOption" + index + "\" class='dropdown-menu'>\n" +
        "               <li> <a class='dropdown-item' onclick=deletePost(" + index + ") role='button'>Eliminar</a></li>\n" +
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
        addComment("@" + comment.User, comment.profile_img, index, comment.message)
    })

}

function createPost(data) {

    console.log(data)

    data['posts'].forEach(createCard)

}

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

(
     getPosts()
)();