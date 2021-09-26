if (localStorage.getItem(login_user)) {
    document.getElementById('total_cart').innerHTML = JSON.parse(localStorage.getItem(login_user)).length
}
if (JSON.parse(localStorage.getItem(login_user)).length !== 0) {
    var shipping_price = document.getElementById('shipping_price')
    shipping_price.innerHTML = '10000'
}


function createHtml(product) {
    let product_ul = document.getElementById('user_product_list')
    let product_li = document.createElement('li')
    product_li.classList.add('items')
    let firstDiv = document.createElement('div')
    firstDiv.classList.add('infoWrap')
    let secondDiv = document.createElement('div')
    secondDiv.classList.add('cartSection')
    let image = document.createElement('img')
    image.classList.add('itemImg')
    image.setAttribute('src', `${product.image}`)
    secondDiv.appendChild(image)
    let h3 = document.createElement('h3')
    h3.innerHTML = product.title
    secondDiv.appendChild(h3)
    let firstP = document.createElement('p')
    let quantityInput = document.createElement('input')
    quantityInput.setAttribute('type', 'number')
    quantityInput.setAttribute('min', '1')
    quantityInput.setAttribute('max', `${product.stock}`)
    quantityInput.setAttribute('value', '1')
    quantityInput.classList.add('qty')
    quantityInput.setAttribute('data-price', `${product.price}`)
    quantityInput.setAttribute('data-id', `${product.id}`)
    firstP.appendChild(quantityInput)
    firstP.append(`x ${product.price}`)
    secondDiv.appendChild(firstP)
    let secondP = document.createElement('p')
    secondP.classList.add('stockStatus')
    secondP.innerHTML = 'In Stock'
    secondDiv.appendChild(secondP)
    firstDiv.appendChild(secondDiv)
    let thirdDiv = document.createElement('div')
    thirdDiv.classList.add('prodTotal')
    thirdDiv.classList.add('cartSection')
    let thirdP = document.createElement('p')
    thirdP.setAttribute('id', `total_price_${product.id}`)
    thirdP.classList.add('tot_price')
    thirdP.innerHTML = product.price
    thirdDiv.appendChild(thirdP)
    firstDiv.appendChild(thirdDiv)
    let forthDiv = document.createElement('div')
    forthDiv.classList.add('cartSection')
    let aTag = document.createElement('a')
    aTag.classList.add('remove')
    aTag.setAttribute('data-product', `${product.id}`)
    aTag.setAttribute('href', '#')
    aTag.innerHTML = 'X'
    forthDiv.appendChild(aTag)
    firstDiv.appendChild(forthDiv)
    product_li.appendChild(firstDiv)
    product_ul.appendChild(product_li)
}

var userOrders = JSON.parse(localStorage.getItem(login_user))
const url = 'http://127.0.0.1:8000/api/store/products/'
fetch(url, {
    method: 'GET',
})
    .then((response) => {
        return response.json()
    })
    .then((products) => {
        var userProducts = []
        if (userOrders) {
            for (let i = 0; i < userOrders.length; i++) {
                var userProductId = userOrders[i]
                for (let j = 0; j < products.length; j++) {
                    if (products[j].id.toString() === userProductId) {
                        userProducts.push(products[j])
                    }
                }
            }
        }
        for (let userProduct of userProducts) {
            // console.log(userProduct)
            createHtml(userProduct)
            calcPrice()
        }
        var removes = document.getElementsByClassName('remove')
        for (let i = 0; i < removes.length; i++) {
            removes[i].addEventListener('click', function (e) {
                e.preventDefault()
                this.parentElement.parentElement.parentElement.style.display = 'none'
                for (let product of userProducts) {
                    if (product.id.toString() === removes[i].dataset.product) {
                        var proPriceP = document.getElementById(`total_price_${product.id}`)
                        proPriceP.innerHTML = 0
                        let proIndex = userProducts.indexOf(product)
                        userProducts = [...userProducts.slice(0, proIndex), ...userProducts.slice(proIndex + 1)]
                        document.getElementById('total_cart').innerHTML -= 1
                        let locIndex = userOrders.indexOf(product.id.toString())
                        userOrders = [...userOrders.slice(0, locIndex), ...userOrders.slice(locIndex + 1)]
                        localStorage.setItem(login_user, JSON.stringify(userOrders))
                    }
                }
                calcPrice()
            })
        }
        var quantitiesInputs = document.getElementsByClassName('qty')
        for (let i = 0; i < quantitiesInputs.length; i++) {
            quantitiesInputs[i].addEventListener('change', function () {
                var min = this.getAttribute('min')
                var max = this.getAttribute('max')
                var proId = this.dataset.id
                var unitPrice = this.dataset.price
                var quantity = this.value
                console.log(typeof min)
                if (parseInt(min) > parseInt(quantity)) {
                    alert('Wrong Input for quantity !!!')
                }
                if (parseInt(quantity) > parseInt(max)) {
                    alert('Not In Stock')
                    this.value = 1
                    quantity = this.value
                }
                if (parseInt(min) <= parseInt(quantity) <= parseInt(max)) {
                    var productPrice = parseInt(quantity) * unitPrice
                    var proPriceP = document.getElementById(`total_price_${proId}`)
                    proPriceP.innerHTML = productPrice
                }
                calcPrice()
            })
        }
    })

function calcPrice() {
    var prices = document.getElementsByClassName('tot_price')
    let sum = 0
    for (let price of prices) {
        sum += parseInt(price.innerHTML)
    }
    if (sum === 0) {
        shipping_price.innerHTML = '0'
    }
    var shipping = shipping_price.innerHTML
    let tax = 0.09 * sum
    var total_products_price = document.getElementById('total_products_price')
    total_products_price.innerHTML = `${sum}`
    var tax_price = document.getElementById('tax_price')
    tax_price.innerHTML = `${tax}`
    var total_price = document.getElementById('total_price')
    total_price.innerHTML = `${sum + tax + parseInt(shipping)}`

}

const checkoutBtn = document.getElementById('checkout')
checkoutBtn.addEventListener('click', function (e){
    e.preventDefault()
})
