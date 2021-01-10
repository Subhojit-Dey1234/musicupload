var audioContainers = document.querySelectorAll('.container-1')
var audios = document.querySelectorAll('.container-1 audio')
var play = document.querySelector('.play')
var pause = document.querySelector('.pause')
var likes = document.querySelectorAll('.like i')
var upload = document.querySelector('.upload')

var deleteButtons = document.querySelectorAll('.delete i');

upload.addEventListener('click',function(){
    console.log('hello')
    location.reload();
})

console.log(likes)
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

audioContainers.forEach(audioContainer =>{
    audioContainer.addEventListener('click',(event)=>{
        var container = event.target.parentElement
        var audio = container.querySelector('audio')
        if(event.target.className.includes('play')){
            audio.play()
            container.querySelector('.pause').classList.add('show')
            container.querySelector('.play').classList.remove('show')
        }else{
            audio.pause()
            container.querySelector('.pause').classList.remove('show')
            container.querySelector('.play').classList.add('show')
        }
    })
})
console.log(deleteButtons)
deleteButtons.forEach(d=>{
    d.addEventListener('click',(e)=>{
        var id = e.target.parentElement.className.split(' ')[1]
        console.log(id);
        DeleteMusic(id);
        DeleteHtml(id);
    })
})

function DeleteMusic(id){
    const xhr = new XMLHttpRequest()
    xhr.responseType = "json"
    const url = `http://127.0.0.1:8000/delete/${id}/`
    // userLikes =new FormData()
    // userLikes.append('id',id)
    // userLikes.append('value',data)
    // console.log(userLikes)
    const csrftoken = getCookie('csrftoken');
    xhr.open('POST',url,true)
    // xhr.setRequestHeader("Content-Type","application/json")
    // xhr.setRequestHeader("HTTP_X_REQUESTED_WITH","XMLHttpRequest")
    // xhr.setRequestHeader("X-Requested-With","XMLHttpRequest")
    xhr.setRequestHeader("X-CSRFToken",csrftoken)
    xhr.onload = function(){
        console.log(xhr.response)
    }
    xhr.send(id)
}

function DeleteHtml(id){
    var data = document.querySelector(`.music[key ='${id}']`);
    console.log(data);
    data.remove();
}


/* Likes */
function LikesInput(id,data){
    const xhr = new XMLHttpRequest()
    xhr.responseType = "json"
    const url = `http://127.0.0.1:8000/like/${id}/`
    userLikes =new FormData()
    userLikes.append('id',id)
    userLikes.append('value',data)
    // console.log(userLikes)
    const csrftoken = getCookie('csrftoken');
    xhr.open('POST',url,true)
    // xhr.setRequestHeader("Content-Type","application/json")
    // xhr.setRequestHeader("HTTP_X_REQUESTED_WITH","XMLHttpRequest")
    // xhr.setRequestHeader("X-Requested-With","XMLHttpRequest")
    xhr.setRequestHeader("X-CSRFToken",csrftoken)
    xhr.onload = function(){
        console.log(xhr.response)
    }
    xhr.send(userLikes)
}
likes.forEach(like=>{
    like.addEventListener('click',(e)=>{
        var id = e.target.parentElement.className.split(' ')[1]
        number = parseInt(e.target.nextSibling.innerText)
        console.log(number)
        // LikesInput(id)
        if (like.className.includes('far')){
            like.className = 'fas fa-thumbs-up'
            number = number +1;
            e.target.nextSibling.innerText = number
            LikesInput(id,true)
        }
        else{
        if (like.className.includes('fas')){
            like.className = 'far fa-thumbs-up'
            number = number -1;
            e.target.nextSibling.innerText = number
            LikesInput(id,false)
        }
        }
    })
})