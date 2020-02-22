$(document).ready(function() {
    $.get('/post/getrelatedposts',{'now_post': $("#post_pk").val()}, function(data) {
        $("#related_posts").html(data)
    })
})