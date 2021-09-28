var state = 0;
var stateMax = 3;
const nextBtn = document.getElementById('next')
const backBtn = document.getElementById('back')

var userCart = JSON.parse(localStorage.getItem(login_user))
checkBack()

function checkBack() {
    if (state === 0) {
        backBtn.innerHTML = 'Back To Cart'
        backBtn.classList.remove('disabled')
    }
}


nextBtn.addEventListener('click', function () {
    if (state < stateMax) {
        if (state === 0) {
            for (let item in userCart) {
                sendUserOrder(item, userCart[item])
            }
        }
        if (state === 2) {
            checkout()
        }


        state += 1;

        if (state === 3) {
            backBtn.innerHTML = 'Home'
            backBtn.classList.remove('disabled')
        } else {
            backBtn.innerHTML = 'Back'
        }

        // Enables 'back' button if disabled
        backBtn.classList.remove("disabled");

        // Adds class to make nodes green
        for (let num = 0; num <= state; num++) {
            let NameClass = `nConfirm${num}`
            let x = document.getElementsByClassName(`${NameClass}`)
            for (let subx of x) {
                subx.classList.add('done')
            }
        }

        // Progress bar animation
        var pBar = (state / stateMax) * 100;
        const progressBar = document.getElementById('progressBar')
        progressBar.style.width = `${pBar}%`

        if (state === 2) {
            nextBtn.innerHTML = 'Confirm'
        }

        // Disables 'next' button if end of steps
        if (state === 3) {
            nextBtn.classList.add('disabled')
        }
    }
})
backBtn.addEventListener('click', function () {
    if (state === 0) {
        document.getElementById('total_cart').click()
    }
    if (state === 3) {
        document.getElementById('home_logo').click()
    }
    if (state > 0 && state < 3) {
        console.log(state)
        // Enables 'next' button if disabled
        nextBtn.classList.remove("disabled");

        // removes class that makes nodes green
        for (let num = 3; num >= state; num--) {
            let NameClass = `nConfirm${num}`
            let x = document.getElementsByClassName(`${NameClass}`)
            for (let subx of x) {
                subx.classList.remove('done')
            }
        }

        state -= 1;

        checkBack()

        // Progress bar animation
        var pBar = (state / stateMax) * 100;
        const progressBar = document.getElementById('progressBar')
        progressBar.style.width = `${pBar}%`

        // Disables 'back' button if end of steps
    }

});

function sendUserOrder(productId, quantity) {
    const url = 'http://127.0.0.1:8000/order/update-item/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf__token
        },
        body: JSON.stringify({'productId': productId, 'quantity': quantity})
    })
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            console.log({'data': data})
        })
}

function checkout() {
    localStorage.removeItem(login_user)
    const url_checkout = 'http://127.0.0.1:8000/order/checkout/'
    fetch(url_checkout, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf__token,
        }
    })
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            if (data === 'True'){
                alert('Sending...')
            }
        })
}

