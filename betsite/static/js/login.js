const username = document.getElementById('username')
const password = document.getElementById('password')

form.addEventListener('submit', (e) => {
    const userForm = username.parentElement;
    const userSmall = userForm.querySelector('small');
    const passwordForm = password.parentElement;
    const passwordSmall = passwordForm.querySelector('small');

    if(username.value.trim() === ''){
        e.preventDefault();
        userSmall.innerText = 'Usuario obligatorio';
        userForm.className = 'form-group error';
    }
    if(password.value.trim() === ''){
        e.preventDefault();
        passwordSmall.innerText = 'Contraseña obligatoria';
        passwordForm.className = 'form-group error';
    }
})

