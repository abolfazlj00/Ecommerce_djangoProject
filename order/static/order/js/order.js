const shipping_price = document.getElementById('shipping_price')

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
    quantityInput.setAttribute('value', userOrders[product.id])
    quantityInput.classList.add('qty')
    quantityInput.setAttribute('data-price', `${product.price}`)
    quantityInput.setAttribute('data-id', `${product.id}`)
    firstP.appendChild(quantityInput)
    let bTag = document.createElement('b')
    bTag.style.color = 'var(--black-color)'
    bTag.style.margin = 'auto 10px'
    bTag.innerHTML = 'x '
    firstP.append(bTag)
    firstP.append(`${product.price}`)
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
    thirdP.innerHTML = quantityInput.value * product.price
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

var userOrders
if (JSON.parse(localStorage.getItem(login_user))) {
    userOrders = JSON.parse(localStorage.getItem(login_user))
    if (Object.keys(JSON.parse(localStorage.getItem(login_user))).length !== 0) {
        shipping_price.innerHTML = '10000'
    }
} else {
    userOrders = {}
}
const url = 'http://127.0.0.1:8000/api/store/products/'
fetch(url, {
    method: 'GET',
})
    .then((response) => {
        return response.json()
    })
    .then((products) => {
        if (userOrders) {
            for (let j = 0; j < products.length; j++) {
                if (Object.keys(userOrders).includes(products[j].id.toString()) && userOrders[products[j].id.toString()] !== 0) {
                    createHtml(products[j])
                    calcPrice()
                }
            }
        }

        var removes = document.getElementsByClassName('remove')
        for (let i = 0; i < removes.length; i++) {
            removes[i].addEventListener('click', function (e) {
                e.preventDefault()
                this.parentElement.parentElement.parentElement.style.display = 'none'
                let delProId = removes[i].dataset.product
                userOrders[delProId] = 0
                localStorage.setItem(login_user, JSON.stringify(userOrders))
                document.getElementById('total_cart').innerHTML -= 1
                var proPriceP = document.getElementById(`total_price_${delProId}`)
                proPriceP.innerHTML = 0
                if (Object.keys(userOrders).length === 0) {
                    localStorage.removeItem(login_user)
                }
                calcPrice()
            })
        }
        const quantitiesInputs = document.getElementsByClassName('qty')
        for (let i = 0; i < quantitiesInputs.length; i++) {
            quantitiesInputs[i].value = userOrders[quantitiesInputs[i].dataset.id]
            quantitiesInputs[i].addEventListener('change', function () {
                var min = this.getAttribute('min')
                var max = this.getAttribute('max')
                var proId = this.dataset.id
                var unitPrice = this.dataset.price
                var quantity = this.value
                if (parseInt(min) > parseInt(quantity)) {
                    alert('Wrong Input for quantity !!!')
                    this.value = 1
                    quantity = this.value
                }
                if (parseInt(quantity) > parseInt(max)) {
                    alert('Not In Stock')
                    this.value = 1
                    quantity = this.value
                }
                if (parseInt(min) <= parseInt(quantity) <= parseInt(max)) {
                    var productPrice = parseInt(quantity) * unitPrice
                    var proPriceP = document.getElementById(`total_price_${proId}`)
                    proPriceP.innerHTML = productPrice.toString()
                    userOrders[proId] = parseInt(quantity)
                    localStorage.setItem(login_user, JSON.stringify(userOrders))
                }
                calcPrice()
            })
        }
    })

function calcPrice() {
    let prices = document.getElementsByClassName('tot_price')
    let sum = 0
    for (let price of prices) {
        sum += parseInt(price.innerHTML)
    }
    if (sum === 0) {
        shipping_price.innerHTML = '0'
    }
    let shipping = shipping_price.innerHTML
    let tax = 0.09 * sum
    const total_products_price = document.getElementById('total_products_price')
    total_products_price.innerHTML = `${sum}`
    const tax_price = document.getElementById('tax_price')
    tax_price.innerHTML = `${tax}`
    const discount_percent = document.getElementById('discount_percent').innerHTML
    const total_price = document.getElementById('total_price')
    let tot = (sum * (100 - discount_percent)/100) + tax + parseInt(shipping)
    total_price.innerHTML = numberWithCommas(tot)
}

const checkoutBtn = document.getElementById('checkout')
checkoutBtn.addEventListener('click', function (e) {
    const homeLogo = document.getElementById('home_logo')
    e.preventDefault()
    if (Object.keys(userOrders).length === 0) {
        alert('Your cart is empty !!!')
        homeLogo.click()
    } else {
        if (login_user === 'AnonymousUser') {
            alert('Please login first !!!')
        }
        location.href = this.getAttribute('href')
    }
})

if (localStorage.getItem('discount')){
    document.getElementById('promo').value = localStorage.getItem('discount')
    document.getElementById('discount_percent').innerHTML = localStorage.getItem('amount')
}


const discountCodeForm = document.getElementById('discount_code')
discountCodeForm.addEventListener('submit', async (e)=>{
    e.preventDefault()
    let code = document.getElementById('promo').value
    const discountUrl = `http://127.0.0.1:8000/order/check-discount/${code}/`
    await fetch(discountUrl, {
        method: 'GET',
    }).then((response)=>{
        return response.json()
    }).then((data)=>{
        if (data.error){
            alert(data.error)
            document.getElementById('discount_percent').innerHTML = 0
            localStorage.removeItem('discount')
            localStorage.removeItem('amount')
            calcPrice()
        }else{
            document.getElementById('discount_percent').innerHTML = data.amount
            localStorage.setItem('discount', code)
            localStorage.setItem('amount', data.amount)
            calcPrice()
        }
    })
})