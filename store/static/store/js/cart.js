var updateBtns = document.getElementsByClassName('update-cart')
for (var i = 0; i < updateBtns.length; i++) {
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
    })
}