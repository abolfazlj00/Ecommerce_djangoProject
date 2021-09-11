const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".register_login");

sign_up_btn.addEventListener("click", () => {
    container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
    container.classList.remove("sign-up-mode");
});

if (document.getElementById('registerState')){
    registerState = document.getElementById('registerState')
    if (registerState.checked === true) {
        sign_up_btn.click()
    }
}

