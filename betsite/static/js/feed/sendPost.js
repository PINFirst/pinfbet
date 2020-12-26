function sendPost() {
    let csrfToken = getCookie('csrftoken')
    const betForm = document.forms['betForm'];
    console.log(betForm)
    console.log(betForm['subjectControlSelect'].value)
    console.log(betForm['betControlSelect'].value)
    console.log(betForm['gradeControlSelect'].value)
    console.log(betForm['messageFormControlTextArea'].value)
}