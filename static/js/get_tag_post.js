function get_tag_post(id) {
    $("#posts").empty()
    $.get('/post/tag',{'tag_id':id}, function(data) {
        $("#posts").html(data)
    })
}