window.onload = function(){
    loadImages()
}

function scrollPage(){
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

var count = 0;
function loadImages(){
    if(count < 10){
        $.ajax({
            url: "load",
            data: {
                "request":"images"
            },
            success: function fun(response){
                var ptag = document.createElement("p")
                ptag.innerHTML = response.image
                document.body.appendChild(ptag)
                count += 1
                loadImages()
            }
        })
    }
}

$(window).scroll(function () {
    console.log(document.documentElement.scrollTop || document.body.scrollTop)
    if((document.documentElement.scrollTop || document.body.scrollTop) > 800){
        document.getElementById("arrow").style.display = "block";
    }else if((document.documentElement.scrollTop || document.body.scrollTop) < 200){
        document.getElementById("arrow").style.display = "none";
    }
    if ($(window).scrollTop() + $(window).height() > $(document).height() - 400){
        if(count > 8){
            count = 0
            loadImages()
        }
    }
});
