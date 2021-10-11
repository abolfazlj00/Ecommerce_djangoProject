let navbar = document.querySelector('.navbar')
document.querySelector('#menu-bar').onclick = () => {
    navbar.classList.toggle('active');
}

document.querySelector('#close').onclick = () => {
    navbar.classList.remove('active');
}

window.onscroll = () => {
    navbar.classList.remove('active');
    if (window.scrollY > 0) {

        document.querySelector('header').classList.add('active');
    } else {
        document.querySelector('header').classList.remove('active');
    }

}

let themeToggler = document.querySelector('#theme-toggler');

themeToggler.onclick = () => {
    themeToggler.classList.toggle('fa-sun');
    if (themeToggler.classList.contains('fa-sun')) {
        document.querySelector('body').classList.add('active');
        localStorage.setItem('light', '0')
    } else {
        document.querySelector('body').classList.remove('active');
        localStorage.setItem('light', '1')
    }
}
