$(function () {
    /* 1. OPEN THE FILE EXPLORER WINDOW */
    $(".js-upload-photos").click(function () {
        $("#fileupload").click();
    });

    /* 2. INITIALIZE THE FILE UPLOAD COMPONENT */
    $("#fileupload").fileupload({
        dataType: 'json',
        url:'album/create/',
        done: function (e, data) {  /* 3. PROCESS THE RESPONSE FROM THE SERVER */
            if (data.result.is_valid) {
                $("#gallery tbody").prepend(
                    "<tr><td><a href='" + data.result.url + "'> <img src='" + data.result.url + " ' class='img-thumbnail' width='200' height='200'> " + data.result.name + "</a></td></tr>"
                )
            }
        }
    });

});