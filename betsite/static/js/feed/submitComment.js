const submitComment = () => {
    // const $fetch = document.getElementById("comment-message")
    addComment()
};

function getMessageValue() {
    return new Promise((resolve, reject) => {
        resolve({
            result: $("#comment-message").val()
        })
    });
}


async function addComment() {

    let message = await getMessageValue()

    let divComment = document.createElement('div')
    divComment.setAttribute('class', 'd-flex flex-row align-items-center feed-text px-2')
    divComment.id = 'comment'

    let divImg = document.createElement('div')
    divImg.setAttribute('class', 'circle-img img-circle rounded-circle justify-content-start')
    divImg.setAttribute('class', 'circle-img img-circle rounded-circle justify-content-start')
    divImg.id = 'comment-profile-img'


    let imgProfile = document.createElement('img')
    imgProfile.setAttribute('src', 'https://images.pexels.com/photos/1370750/pexels-photo-1370750.jpeg')
    imgProfile.setAttribute('alt', 'user-image')

    divImg.appendChild(imgProfile)

    divComment.appendChild(divImg)



    let divContent = document.createElement('div')
    divContent.setAttribute('class', 'd-flex flex-column flex-wrap ml-2')
    divContent.id = 'content'

    divComment.appendChild(divContent)

    let spanContentUserName = document.createElement('span')
    spanContentUserName.setAttribute('class', 'font-weight-bold')
    spanContentUserName.innerText = "@Username"
    spanContentUserName.id = 'comment-userName'

    let spanContentTime = document.createElement('span')
    spanContentTime.setAttribute('class', 'text-black-50 time')
    spanContentTime.innerText = "35 minutes ago"
    spanContentTime.id = 'comment-time'

    let spanContentMessage = document.createElement('span')
    spanContentMessage.setAttribute('class', 'font-weight-bold')
    spanContentMessage.innerText = "Comentó: " + message.result
    spanContentMessage.id = 'comment-message'

    divContent.appendChild(spanContentUserName)
    divContent.appendChild(spanContentTime)
    divContent.appendChild(spanContentMessage)

    let optionsIcon = document.createElement('i')
    optionsIcon.setAttribute('class', 'fa fa-ellipsis-v text-black-50 feed-icon ml-auto p-2')

    divComment.appendChild(optionsIcon)

    document.getElementById('comments').appendChild(divComment)

}