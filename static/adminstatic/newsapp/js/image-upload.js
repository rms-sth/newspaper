//Upload photos
$(function () {
    /* 1. OPEN THE FILE EXPLORER WINDOW */
    $(".js-upload-photos").click(function () {
        $("#fileupload").click();
    });

    /* 2. INITIALIZE THE FILE UPLOAD COMPONENT */
    $("#fileupload").fileupload({
        dataType: 'json',
        url: 'album/create/',
        done: function (e, data) {
            /* 3. PROCESS THE RESPONSE FROM THE SERVER */
            var id = data.result.id;
            console.log(id);
            if (data.result.is_valid) {
                $("#gallery tbody").load(document.URL + '#gallery tbody')
                //     `<tr id="row${id}">
                //         <td>
                //             <a href="${data.result.url}"> <img src="${data.result.url}" class='img-thumbnail' width='200' height='200'>${data.result.name}</a>
                //         </td>
                //         <td>
                //             <button id="ramesh" class='del-photo btn btn-danger' style='margin: 50px;' photos-id='${data.result.id}' onclick="del(${data.result.id})">Delete ${data.result.id}</button>
                //         </td>
                //     </tr>`
                // )
            }
        }
    });
});





// Deletes recently uploaded photos of JQuery
function del(id) {
    // var id = $('#ramesh').attr('photos-id')
    console.log(id);
    var confirmation = confirm('Are you sure you want to delete?' + id);
    if (confirmation) {
        $.ajax({
            type: "POST",
            url: "/album/delete/" + id,
            dataType: "json",
            success: function (data) {
                $('#row' + id).remove();
            }
        });
    } else {
        return false;
    }
};




// CSRF TOKEN
$(document).ready(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });


    // // DELETE PHOTO BY ID
    // $('.delete-photo').on('click', deletePhoto);

    // function deletePhoto() {
    //   var id = $(this).attr('photo-id')
    //   console.log(id);
    //   var confirmation = confirm('Are you sure you want to delete?' +id +"'");


    //   if (confirmation) {
    //     $.ajax({
    //     type: "POST",
    //     url: "/album/delete/" + id,
    //     dataType: "json",
    //     data: id,
    //     success: function (data) {
    //       $('#row' + id).remove();
    //     }
    //   });
    //   } else {
    //     return false;
    //   }
    // };
});