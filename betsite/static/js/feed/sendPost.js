async function sendPost(type) {

    let csrfToken = getCookie('csrftoken')
    let userName = 'Jeff'

    let subject = $('#subjectControlSelect')
    let bet = $('#betControlSelect')
    let grade = $('#gradeControlSelect')
    let message = $('#messageFormControlTextArea')
    let coins = $('#cuantia')

    console.log('coins')
    console.log(coins.val())

    if (subject.val() && bet.val() && grade.val() && message.val() && coins.val() && coins.val() <= pinfCoins) {
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
                        message: message.val(),
                        coins: coins.val(),
                        type: type,
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
            const myNode = document.getElementById("posts-content");
            myNode.innerHTML = '';
            await getPosts(0)
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
        if(!coins.val() || coins.val() && coins.val() > pinfCoins) {
            coins.toggleClass('error')

        }
    }
}