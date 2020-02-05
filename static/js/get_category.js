$(document).ready(function() {
    $.get('/category/getallcategory', function(data) {
        $("#category").html(data)
    })
})