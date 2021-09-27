if (localStorage.getItem(login_user)) {
    document.getElementById('total_cart').innerHTML = Object.keys(JSON.parse(localStorage.getItem(login_user))).length.toString()
}
var updateBtns = document.getElementsByClassName('update-cart')
for (var i = 0; i < updateBtns.length; i++) {

    if (localStorage.getItem(login_user)) {
        let list = JSON.parse(localStorage.getItem(login_user))
        let updateBtn = updateBtns[i]
        let productUpdateebtn = updateBtn.dataset.product.toString()
        if (Object.keys(list).includes(productUpdateebtn)) {
            updateBtn.innerHTML = 'Remove From Cart'
            updateBtn.dataset.action = 'remove'
        }
    }

    updateBtns[i].addEventListener('click', function () {
        var productId = this.dataset.product
        var action = this.dataset.action
        if (action === 'add') {
            document.getElementById('total_cart').innerHTML = (parseInt(document.getElementById('total_cart').innerHTML) + 1).toString()
            this.innerHTML = 'Remove From Cart'
            this.dataset.action = 'remove'
        } else {
            document.getElementById('total_cart').innerHTML -= (1).toString()
            this.innerHTML = 'Add To Cart'
            this.dataset.action = 'add'
        }
        updateUserOrder(productId, action)
    })
}

function updateUserOrder(productId, action) {
    let orders
    if (localStorage.getItem(login_user)) {
        orders = localStorage.getItem(login_user)
        orders = JSON.parse(orders)
        if (action === 'add') {
            orders[productId] = 1
        } else {
            delete orders[productId]
        }
        localStorage.setItem(login_user, JSON.stringify(orders))
    } else {
        orders = {}
        orders[productId] = 1
        localStorage.setItem(login_user, JSON.stringify(orders))
    }
}


