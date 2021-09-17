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

