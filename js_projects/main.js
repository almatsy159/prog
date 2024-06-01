console.log("it work !")

const left = document.querySelector(".left")
const right = document.querySelector(".right")
const slider = document.querySelector(".slider")
/*const image = document.querySelector('.image')*/
const wFrame = document.querySelector(".frame").width
const images = document.querySelectorAll(".image")


let slideNumber = 0


right.addEventListener("click",()=>{
    if(slideNumber<images.length){
    slider.style.transform = `translateY(-${slideNumber * 500}px)`
    slideNumber ++
    }else{
        slider.style.transform = `translateY(-0px)`
        slideNumber = 1
    }
})
left.addEventListener("click",()=>{
    if(slideNumber>=0){
        slider.style.transform = `translateY(${slideNumber * -500}px)`
        slideNumber --
    }else{
        slider.style.transform = `translateY(+${images.length-1 * +500}px)`
        slideNumber = images.length-1
    }
    })

slider.addEventListener("click",()=>{alert("well played!")})

/*
function translate(lst,val=100,k=1,unit="px"){
    for(i in lst){
        o = Object(lst[i])
        console.log(lst[i])
        o.style.translate = 'styletranslateX(' + toString(val*k) + toString(unit) +')'
}}*/