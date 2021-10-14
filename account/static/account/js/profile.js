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
const changePassForm = document.getElementById('change_pass')
changePassForm.addEventListener('submit', async function (e) {
    e.preventDefault() // avoid to execute the actual submit of the form.
    const username = document.getElementById('pass_username').value
    const pass1 = document.getElementById('password').value
    const pass2 = document.getElementById('confirm_password').value
    const url = 'http://127.0.0.1:8000/api/account/change-password/' + username + '/'
    const changePassFormData = new FormData(changePassForm)
    const passFormDataSerialized = Object.fromEntries(changePassFormData)
    const csrfToken = changePassForm.getElementsByTagName("input")[0].value
    if (pass1 === pass2) {
        try {
            const response = await fetch(url, {
                method: 'PUT',
                body: JSON.stringify(passFormDataSerialized),
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                }
            })
            const json = await response.json()
            if (json['resp'] === 'True') {
                const messageDiv = document.getElementById('resp_true')
                if (document.getElementById('resp_error')) {
                    document.getElementById('resp_error').style.display = 'none'
                }
                messageDiv.style.display = 'block'
            } else {
                const errorDiv = document.getElementById('resp_error')
                const errorP = document.getElementById('resp_error_p')
                errorP.innerHTML = json['resp']
                if (document.getElementById('resp_true')) {
                    document.getElementById('resp_true').style.display = 'none'
                }
                errorDiv.style.display = 'block'
            }
        } catch (e) {
            console.log(e)
            if (lang_code === 'en-us') {
                alert('something wrong, try again')
            } else {
                alert('مشکلی رخ داده است. دوباره امتحان کنید.')
            }
        }
    } else {
        const errorDiv = document.getElementById('resp_error')
        const errorP = document.getElementById('resp_error_p')
        errorP.innerHTML = 'The password and its confirm do not match'
        if (document.getElementById('resp_true')) {
            document.getElementById('resp_true').style.display = 'none'
        }
        errorDiv.style.display = 'block'
    }
})
if (document.getElementById('tbodyTag')) {
    var tbodyTagChildren = document.getElementById('tbodyTag').childElementCount
}
trash_icons = document.querySelectorAll('.delete_address')
trash_icons.forEach((trash_icon) => {
    trash_icon.addEventListener('click', () => {
        let deleteUrl = trash_icon.dataset.url
        fetch(deleteUrl, {
            method: 'GET',
        })
            .then((response) => {
                return response.json()
            })
            .then((data) => {
                if (data.data === 'True') {
                    let parent = trash_icon.parentElement.parentElement
                    parent.style.display = 'none'
                    tbodyTagChildren -= 1
                    if (tbodyTagChildren <= 0) {
                        document.getElementById('address_table').style.display = 'none'
                        let h3Tag = document.createElement('h3')
                        h3Tag.innerHTML = 'There is no address submitted !!!'
                        document.getElementById('address_div').appendChild(h3Tag)
                    }
                    if (lang_code === 'en-us') {
                        alert('Your address deleted successfully !!!')
                    } else {
                        alert('آدرس شما با موفقیت حذف شد !!!')
                    }

                }
            })
    })
})

if (document.getElementById('load_setting')) {
    document.getElementById('settingBut').click()
}