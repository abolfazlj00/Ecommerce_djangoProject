const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

sign_up_btn.addEventListener("click", () => {
    container.classList.add("sign-up-mode");
});
sign_in_btn.addEventListener("click", () => {
    container.classList.remove("sign-up-mode");
});

if (document.getElementById('registerState')) {
    registerState = document.getElementById('registerState')
    if (registerState.checked === true) {
        sign_up_btn.click()
    }
}


var registerForm = document.querySelector('#register_form')
const csrftoken = registerForm.getElementsByTagName("input")[0].value
registerForm.addEventListener('submit', async function (e) {
    e.preventDefault() // avoid to execute the actual submit of the form.
    var url = this.getAttribute('action')
    const formData = new FormData(registerForm)
    const formDataSerialized = Object.fromEntries(formData)
    try {
        const response = await fetch(url, {
            method: 'POST',
            body: JSON.stringify(formDataSerialized),
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            }
        })
        const json = await response.json()
        if (json['username']) {
            const signInBtn = document.getElementById('sign-in-btn')
            signInBtn.click()
            const username = document.getElementById('log-username')
            const password = document.getElementById('log-password')
            username.value = json['username']
            password.value = json['password']
        } else {
            alert(json['resp'])
        }
    } catch (e) {
        console.log(e)
        if (lang_code === 'en') {
            alert('something wrong, try again')
        } else {
            alert('مشکلی رخ داده است. دوباره امتحان کنید.')
        }
    }


})

// forget pass and send email
if (document.getElementById('send_email_link')) {

    const sendEmailBtn = document.getElementById('send_email_link')
    sendEmailBtn.addEventListener('click', async function () {
        var inputUsername = document.getElementById('log-username').value
        if (inputUsername === '') {
            if (lang_code === 'en') {
                alert('Enter your username to send you email')
            } else {
                alert('نام کاربری خود را وارد کنید تا ایمیل برایتان فرستاده شود.')
            }
        } else {
            var url = 'http://127.0.0.1:8000/account/send-email/' + inputUsername + '/'
            var response = await fetch(url)
            let javab = await response.text()
            alert(javab)
        }
    })
}
