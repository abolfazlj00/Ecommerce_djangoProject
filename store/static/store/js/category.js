const mainUl = document.getElementById('todos')
const cat_url = 'http://127.0.0.1:8000/api/store/categories/'
fetch(cat_url, {
    method: 'GET',
})
    .then((response) => {
        return response.json()
    })
    .then((categories) => {
        for (let category of categories) {
            if (!category.parent) {
                let liTag = document.createElement('li')
                liTag.classList.add('todo')
                liTag.setAttribute('id', `cat_${category.id}`)
                liTag.innerHTML = category.name
                mainUl.appendChild(liTag)
            } else {
                let parId = `cat_${category.parent}`
                let parTag = document.getElementById(parId)
                let parName = parTag.innerHTML
                parTag.innerHTML = ''
                parTag.classList.remove('todo')
                parTag.setAttribute('id', '')
                let divTag = document.createElement('div')
                divTag.setAttribute('id', `${parId}`)
                divTag.classList.add('toggler')
                divTag.innerHTML = parName
                parTag.appendChild(divTag)
                let ulTag = document.createElement('ul')
                ulTag.classList.add('toggler-target')
                let liTag = document.createElement('li')
                liTag.setAttribute('id', `cat_${category.id}`)
                liTag.classList.add('todo')
                liTag.style.marginLeft = '1rem'
                liTag.innerHTML = category.name
                let liTag2 = document.createElement('li')
                liTag2.classList.add('all')
                liTag2.style.marginLeft = '1rem'
                liTag2.innerHTML = 'All'
                ulTag.appendChild(liTag2)
                ulTag.appendChild(liTag)
                parTag.appendChild(ulTag)
            }
        }

        var togglers = document.querySelectorAll('.toggler')
        togglers.forEach((toggler) => {
            toggler.addEventListener('click', () => {
                toggler.classList.toggle('active')
                toggler.nextElementSibling.classList.toggle('active')
            })
        })

        const todos = document.querySelectorAll('.todo')
        todos.forEach((todo) =>{
            todo.addEventListener('click', function (){
                let categoryId = todo.getAttribute('id').substr(4)
                window.location.href = `http://127.0.0.1:8000/store/category/all/${categoryId}`
            })
        })

        const alls = document.querySelectorAll('.all')
        alls.forEach((all) =>{
            all.addEventListener('click', ()=> {
                let relatedCatId = all.parentElement.parentElement.firstChild.id.substr(4)
                window.location.href = `http://127.0.0.1:8000/store/category/all/${relatedCatId}`
            })
        })

        const catButton = document.getElementById('categories')
        catButton.addEventListener('click', (e) => {
            e.preventDefault()
            catButton.classList.toggle('active')
            mainUl.classList.toggle('active')
        })
    })

if (document.getElementById('pre_home')){
    if (document.getElementById('nxt_home')){
        document.getElementById('nxt_home').style.display = 'none'
    }
}