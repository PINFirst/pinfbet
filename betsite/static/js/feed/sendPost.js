async function sendPost() {

    let csrfToken = getCookie('csrftoken')
    let userName = 'jeff'

    let subject = $('#subjectControlSelect')
    let bet = $('#betControlSelect')
    let grade = $('#gradeControlSelect')
    let message = $('#messageFormControlTextArea')


    if (subject.val() && bet.val() && grade.val() && message.val()) {
        try {
            let response = await fetch("send_post",
                {
                    method: "post",
                    headers: {
                        "Accept": 'application/json',
                        "Content-Type": 'application/json',
                        "X-CSRFToken": csrfToken,
                    },
                    body: JSON.stringify({
                        user: userName,
                        subject: subject.val(),
                        bet: bet.val(),
                        grade: grade.val()[0],
                        comment: message.val(),
                    })
                })
            if (!response.ok) {
                console.log(response)
                throw {
                    status: response.status,
                    statusText: response.statusText
                }

            }
            let profilePic = 'https://images.pexels.com/photos/1370750/pexels-photo-1370750.jpeg'
            // await addComment(user, profilePic, index, message.result)
            //
            // textarea.removeClass('error')
            // textarea.attr('placeholder', 'Escribe un comentario...')

            console.log('sa enviao?')


        } catch (e) {
            console.log(e)

        } finally {

        }
    } else {

        console.log("NO sa enviao")
        // bet.val("")
        // subject.val("")
        // subject.attr('placeholder', 'elija una opcion')
        // message.val("")
        // message.attr('placeholder', 'Debe de escribir un comentario.')
    }
}