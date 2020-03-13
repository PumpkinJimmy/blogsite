function handleContents(e){
    var cstag = document.getElementById('contents');
    var wheel = e.originalEvent.wheelDelta || -e.originalEvent.detail;
    var delta = Math.max(-1, Math.min(1, wheel) );
    if (cstag.classList[1] == 'fixed-top'){
        var navtag = document.getElementsByClassName("navbox")[0];
        // console.log(navtag.offsetTop+navtag.clientHeight+30);
        if (navtag.offsetTop+navtag.clientHeight+30 >= pageYOffset){
            cstag.classList.remove("fixed-top");
            cstag.style.width = "";
        }
    }
    else{
        if (cstag.offsetTop-30 < pageYOffset){
            var w = getComputedStyle(cstag).width;
            cstag.classList.add("fixed-top");
            cstag.style.width = w;
        }
    }   
}
function handleContentsT(){
    var cstag = document.getElementById('contents');
    if (cstag.classList[1] == 'fixed-top'){
        var navtag = document.getElementsByClassName("navbox")[0];
        // console.log(navtag.offsetTop+navtag.clientHeight+30);
        if (navtag.offsetTop+navtag.clientHeight+30 >= pageYOffset){
            cstag.classList.remove("fixed-top");
            cstag.style.width = "";
        }
    }
    else{
        if (cstag.offsetTop-30 < pageYOffset){
            var w = getComputedStyle(cstag).width;
            cstag.classList.add("fixed-top");
            cstag.style.width = w;
        }
    }   
}