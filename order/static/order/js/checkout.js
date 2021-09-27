var state = 0;
var stateMax = 3;
const nextBtn = document.getElementById('next')
const backBtn = document.getElementById('back')

checkBack()

function checkBack() {
    if (state === 0) {
        backBtn.innerHTML = 'Back To Cart'
        backBtn.classList.remove('disabled')
    }
}


nextBtn.addEventListener('click', function () {
    if (state < stateMax) {

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
