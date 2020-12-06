function addComment() {

    let message = $("#comment-message")


    let comment = "<div id='comment' class='d-flex flex-row align-items-center feed-text px-2'>\n" +
        "                <div class=\"circle-img img-circle rounded-circle justify-content-start\">\n" +
        "                    <img id=\"comment-user-img\"\n" +
        "                         src=\"https://images.pexels.com/photos/1370750/pexels-photo-1370750.jpeg\" alt=\"user-image\">\n" +
        "                </div>\n" +
        "                <div class=\"d-flex flex-column flex-wrap ml-2\">\n" +
        "                    <span id=\"comment-userName\" class=\"font-weight-bold\">@Username</span>\n" +
        "                    <span id=\"comment-time\" class=\"text-black-50 time\">35 minutes ago</span>\n" +
        "                    <span id=\"comment-message\"><b>Comentó: </b>" + message.val() + "</span>\n" +
        "                </div>\n" +
        "\n" +
        "                <div class=\"feed-icon ml-auto p-2\"><i class=\"fa fa-ellipsis-v text-black-50\"></i></div>\n" +
        "            </div>"

    message.val("")
    $("#comments").append(comment)


}