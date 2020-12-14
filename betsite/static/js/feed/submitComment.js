async function submitComment(index) {

    let userName = document.querySelector("#post" + index + " #post-info #post-user").textContent
    let message = await getMessageValue(index)
    let textarea = $("#comment-message" + index);
    textarea.val("")
    let csrfToken = getCookie('csrftoken')


    if (message.result) {
        try {
            let response = await fetch("post_comment",
                {
                    method: "post",
                    headers: {
                        "Accept": 'application/json',
                        "Content-Type": 'application/json',
                        "X-CSRFToken": csrfToken,
                    },
                    body: JSON.stringify({
                        user: userName,
                        post: index,
                        comment: message,
                    })
                })
            if (!response.ok) {
                throw {
                    status: response.status,
                    statusText: response.statusText
                }

            }
            let user = "@Jeff"
            let profilePic = 'https://images.pexels.com/photos/1370750/pexels-photo-1370750.jpeg'
            addComment(user, profilePic ,index, message.result)

            textarea.removeClass('error')
            textarea.attr('placeholder', 'Escribe un comentario...')


        } catch (e) {
            console.log(e)

        } finally {

        }
    } else {
        console.log("no puedes enviar un mensaje vacío")
        textarea.toggleClass('error')
        textarea.attr('placeholder', 'No puede enviar un comentario vacio.')

    }

}

function getMessageValue(index) {
    return new Promise((resolve, reject) => {
        resolve({
            result: $("#comment-message" + index).val()
        })
    });
}


async function addComment(userName, profilePic, postIndex, message) {


    let post = document.getElementById('comments' + postIndex)
    let n_comments = post.childElementCount? post.childElementCount : 0


    let divComment = document.createElement('div')
    divComment.setAttribute('class', 'd-flex flex-row align-items-center feed-text px-2')
    divComment.id = 'comment' + n_comments

    let divImg = document.createElement('div')
    divImg.setAttribute('class', 'circle-img img-circle rounded-circle justify-content-start')
    divImg.setAttribute('class', 'circle-img img-circle rounded-circle justify-content-start')
    divImg.id = 'comment-profile-img'


    let imgProfile = document.createElement('img')
    imgProfile.setAttribute('src', profilePic)
    imgProfile.setAttribute('alt', 'user-image')

    divImg.appendChild(imgProfile)

    divComment.appendChild(divImg)


    let divContent = document.createElement('div')
    divContent.setAttribute('class', 'd-flex flex-column flex-wrap ml-2')
    divContent.id = 'content'

    divComment.appendChild(divContent)

    let spanContentUserName = document.createElement('span')
    spanContentUserName.setAttribute('class', 'font-weight-bold')
    spanContentUserName.innerText = userName
    spanContentUserName.id = 'comment-userName'

    let spanContentTime = document.createElement('span')
    spanContentTime.setAttribute('class', 'text-black-50 time')
    spanContentTime.innerText = "35 minutes ago"
    spanContentTime.id = 'comment-time'

    let spanContentMessage = document.createElement('span')
    spanContentMessage.innerHTML = "<b>Comentó: </b>" + message
    spanContentMessage.id = 'comment-message'

    divContent.appendChild(spanContentUserName)
    divContent.appendChild(spanContentMessage)
    divContent.appendChild(spanContentTime)


    let dropDownOptions = document.createElement('div')
    dropDownOptions.setAttribute('class', 'dropdown ml-auto p-2')

    divComment.appendChild(dropDownOptions)


    let optionsIcon = document.createElement('i')
    optionsIcon.setAttribute('class', 'feed-icon px-2 fa fa-ellipsis-v ml-auto p-2')
    optionsIcon.setAttribute('data-toggle', "dropdown")
    optionsIcon.setAttribute('aria-expanded', "false")
    // optionsIcon.setAttribute('type', 'button')
    optionsIcon.setAttribute('id', 'commentOption' + postIndex)

    dropDownOptions.appendChild(optionsIcon)


    let options = document.createElement('ul')
    options.setAttribute('aria-labelledby', 'commentOption' + postIndex)
    options.setAttribute('class', 'dropdown-menu')

    dropDownOptions.appendChild(options)


    let optionDelete = document.createElement('li')

    let optionDeleteAction = document.createElement('a')
    optionDeleteAction.setAttribute('class', 'dropdown-item')
    optionDeleteAction.innerText = "Eliminar"
    optionDeleteAction.onclick = () => {
        deleteComments(postIndex, n_comments)
    }

    optionDelete.appendChild(optionDeleteAction)
    options.appendChild(optionDelete)

    post.appendChild(divComment)

}