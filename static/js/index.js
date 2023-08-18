// @ts-nocheck
document.querySelector("#message").style.left = (innerWidth - 300) / 2;

setTimeout(function(){
    $('#message').fadeOut('slow');
}, 4000)


const watchlist = document.querySelector("#watchlist")

watchlist.addEventListener("click", () => {

    fetch(`/home/watchlist/${watchlist.dataset.id}`, {
        method: "POST"
    })
    .then( res => res.json())
    .then(data => {
       if ( data.message == "success"){
            if (data.action == "add"){
                watchlist.className = "fas fa-bookmark btn btn-primary"
            } else {
                watchlist.className = "fas fa-plus btn btn-primary"
            }
       } else {
        console.log("try again");
       }
    })

})



    fetch(`/home/watchlist/${watchlist.dataset.id}`)
    .then( res => res.json())
    .then(data => {
        if ( data.exist == "true"){
            watchlist.className = "fas fa-bookmark btn btn-primary"
        } else {
            watchlist.className = "fas fa-plus btn btn-primary"
        }
    })