const hamburger = document.querySelector('.hamburger')
    hamburger.addEventListener('click', function () {
        this.classList.toggle('close')
    })

if (document.getElementById('userState')){
    userState = document.getElementById('userState')
    if (userState.checked === true) {
        let loginBtn = document.getElementById('loginBtn')
        const parentLi = loginBtn.parentElement
        parentLi.setAttribute('class', 'dropdown')
        loginBtn.setAttribute('class', 'dropdown-toggle')
        loginBtn.setAttribute('href', '#')
        loginBtn.setAttribute('data-bs-toggle', 'dropdown')
        let user = userState.value
        console.log(user)
        loginBtn.innerHTML = user
        const ulTag = document.createElement('ul')
        ulTag.setAttribute('class', 'dropdown-menu')
        ulTag.setAttribute('aria-labelledby', 'loginBtn')
        const liTag1 = document.createElement('li')
        liTag1.setAttribute('class', 'dropdown-item')
        const liTag2 = document.createElement('li')
        liTag2.setAttribute('class', 'dropdown-item')
        const profile = document.createElement('a')
        const logout = document.createElement('a')
        profile.innerHTML = 'profile'
        logout.innerHTML = 'logOut'
        profile.setAttribute('href','#')
        logout.setAttribute('href','#')
        liTag1.appendChild(profile)
        liTag2.appendChild(logout)
        ulTag.appendChild(liTag1)
        ulTag.appendChild(liTag2)
        parentLi.appendChild(ulTag)
    }
}