$(document).ready(function(){
    let imgArray = [
        "/static/img/main/bily.jpg",
        "/static/img/main/girl.jpg",
        "/static/img/main/img1.jpg",
        "/static/img/main/img2.jpg",
        "/static/img/main/img3.jpg"
    ]

    let num = Math.round(Math.random() * 4 )
    let mainImg = document.getElementById("main_img")
    mainImg.src = imgArray[num];
})