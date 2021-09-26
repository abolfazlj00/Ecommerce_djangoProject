if (localStorage.getItem(login_user)) {
    document.getElementById('total_cart').innerHTML = JSON.parse(localStorage.getItem(login_user)).length
}
var updateBtns = document.getElementsByClassName('update-cart')
for (var i = 0; i < updateBtns.length; i++) {

    if (localStorage.getItem(login_user)) {
        var list = JSON.parse(localStorage.getItem(login_user))
        var updateBtn = updateBtns[i]
        for (let i = 0; i < list.length; i++) {
            if (updateBtn.dataset.product.toString() === list[i]) {
                updateBtn.innerHTML = 'Remove From Cart'
                updateBtn.dataset.action = 'remove'
            }
        }
    }


    updateBtns[i].addEventListener('click', function () {
        var productId = this.dataset.product
        var action = this.dataset.action
        if (action === 'add') {
            if (typeof document.getElementById('total_cart').innerHTML === 'string') {
                document.getElementById('total_cart').innerHTML = parseInt(document.getElementById('total_cart').innerHTML) + 1
            } else {
                document.getElementById('total_cart').innerHTML += 1
            }
            this.innerHTML = 'Remove From Cart'
            this.dataset.action = 'remove'
        } else {
            document.getElementById('total_cart').innerHTML -= 1
            this.innerHTML = 'Add To Cart'
            this.dataset.action = 'add'
        }
        // if (login_user !== 'AnonymousUser') {
        //     updateUserOrder(productId, action)
        // } else {
        var orders = localStorage.getItem(login_user)
        if (orders) {
            orders = JSON.parse(orders)
            if (action === 'add') {
                orders.push(productId)
            } else {
                var index = orders.indexOf(productId)
                orders = [...orders.slice(0, index), ...orders.slice(index + 1)]
            }
            localStorage.setItem(login_user, JSON.stringify(orders))
        } else {
            // localStorage.setItem('orders', JSON.stringify([{'productId': productId, 'action': action}]))
            localStorage.setItem(login_user, JSON.stringify([productId,]))
        }
        // }
    })
}



// not used
function updateUserOrder(productId, action) {
    var url = 'http://127.0.0.1:8000/order/update-item/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf__token
        },
        body: JSON.stringify({'productId': productId, 'action': action})
    })
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            console.log({'data': data})
        })
}


