// for show of page
let getSiblings = function (e) {
    // for collecting siblings
    let siblings = [];
    // if no parent, return no sibling
    if (!e.parentNode) {
        return siblings;
    }
    // first child of the parent node
    let sibling = e.parentNode.firstChild;
    // collecting siblings
    while (sibling) {
        if (sibling.nodeType === 1 && sibling !== e) {
            siblings.push(sibling);
        }
        sibling = sibling.nextSibling;
    }
    return siblings;
};
const tabBtn = document.querySelectorAll(".tab")
const tab = document.querySelectorAll(".tabShow")

function tabs(panelIndex) {
    tab.forEach(function (node) {
        node.style.display = "none"
    })
    tab[panelIndex].style.display = "block"
}

tabs(0);

tabBtn.forEach(function (icon) {
    icon.addEventListener('click', function () {
        icon.classList.add("clicked")
        let siblings = getSiblings(document.querySelector('.clicked'))
        siblings.forEach(function (node) {
            node.classList.remove("active")
            icon.classList.add("active")
            icon.classList.remove("clicked")
        })
    })
})


// change password without reloading
const pass1 = document.getElementById('password').value
const pass2 = document.getElementById('confirm_password').value
const changePassForm = document.getElementById('change_pass')
changePassForm.addEventListener('submit', async function (e) {
    console.log(pass2, pass1)
    e.preventDefault() // avoid to execute the actual submit of the form.
    const changePassFormData = new FormData(changePassForm)
    const url = changePassForm.getAttribute('action')
    const formDataSerialized = Object.fromEntries(changePassFormData)
    const csrf_token = changePassForm.getElementsByTagName("input")[0].value
    if (pass1 === pass2) {
        try {
            const response = await fetch(url, {
                method: 'POST',
                body: JSON.stringify(formDataSerialized),
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrf_token
                }
            })
            const json = await response.json()
            console.log(json)
        } catch (e) {
            console.log(e)
            alert('something wrong, try again')
        }
    } else {
        alert('The password and its confirm do not match')
    }
})
