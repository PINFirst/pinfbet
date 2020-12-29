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

            $("#betForm").trigger('reset')

        } catch (e) {
            console.log(e)

        } finally {

        }
    } else {
        
        if (!bet.val()) {
            bet.toggleClass('error')
        }
        if (!subject.val()) {
            subject.toggleClass('error')
        }
        if (grade.val().length === 0) {
            grade.toggleClass('error')
        }
        if (!message.val()) {
            message.toggleClass('error')
            message.attr('placeholder', 'No puede enviar un comentario vacio.')
        }
    }
}