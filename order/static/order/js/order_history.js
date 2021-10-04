const historyTotPrices = document.querySelectorAll('.historyTotPrice')
const historyUnitPrices = document.querySelectorAll('.historyUnitPrice')

historyTotPrices.forEach((totPrice) => {
    let price = totPrice.innerHTML
    let newPrice = numberWithCommas(price)
    totPrice.innerHTML = newPrice.toString()
})

historyUnitPrices.forEach((totPrice) => {
    let price = totPrice.innerHTML
    let newPrice = numberWithCommas(price)
    totPrice.innerHTML = newPrice.toString()
})
