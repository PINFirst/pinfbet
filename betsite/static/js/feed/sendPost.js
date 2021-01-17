async function sendPost(type) {

    let csrfToken = getCookie('csrftoken')

    let subject = $('#subjectControlSelect')
    let bet = $('#betControlSelect')
    let grade = $('#gradeControlSelect')
    let message = $('#messageFormControlTextArea')
    let coins = $('#cuantia')
    let pinfCoins = parseInt($('#coins').text())

    if (subject.val() && bet.val() && grade.val() && message.val() && coins.val() && parseInt(coins.val(), 10) <= pinfCoins && parseInt(coins.val(), 10) > 0) {
        try {
            console.log('entré')
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

            $('#coins').text(" ".concat(pinfCoins - parseInt(coins.val(), 10)))

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
        if (!coins.val() || coins.val() && parseInt(coins.val()) > pinfCoins) {
            console.log('entro')
            coins.toggleClass('error')
        }
    }
}