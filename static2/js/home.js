$(document).ready(function(){

    $('.cate').click(function (e) {
        e.preventDefault()
        var pk = $(this).children('span').html()
        var url = '/category/' + pk
        $.ajax({
            type: "get",
            url: url,
            success: function (res) {
                $("div.real_post").empty()
                $("ul.post-list").empty()
                var html = ""
                if (res.result == 'success') {
                    var posts = res.data
                    for(i in posts) {
                        html += "<li class='post'>"
                        html += "<input type='hidden' value='"+posts[i].pk+"'/>"
w
                        html += "<h2 class='post_title'>" + posts[i].title + "</h2>"
                        // html += "<p>" + posts[i].formatted_markdown + "</p>"

                        if (posts[i].tags) {
                            html += "<ul class='tag-list>"
                            for (tag in posts[i].tags) {
                                html += "<li>" + "" + "</li>"
                            }
                            html += "</ul>"
                        }
                        html += "<div class='post-info'>" + posts[i].ins_dt+ "</div>"
                    }
                    $("ul.post-list").append(html)
                    if ($("#disqus").show() ) {
                        $("#disqus").hide()
                    }
                }

            }
        })
    })

})


    $(document).on('click','.post_title',function (e) {
        e.preventDefault()
        var pk = $(this).siblings("input[type=hidden]").val()
        var url ='/post/'+ pk
        $.ajax({
            type: "get",
            url: url,
            success: function (res) {
                $("div.real_post").empty()
                $("ul.post-list").empty()
                if (res.result == 'success') {
                    var html = ""

                    if (res.data) {
                        $("div.post").show();
                        var post = res.data

                        html += "<h2 class='title'><a href='#'>" + post.title + "</a></h2>"
                        html += "<div class=post_container><h3 class='right_date'>none <span class='right_date'>등록일 : "
                            + post.ins_dt
                            + "</span><span class='right_date'>/</span>"
                            +"<span class='right_date'> 수정일 : "
                            +post.upd_dt
                            + "</span>"
                            +"</h3>"
                        html += "<article class='post-content'> " + post.formatted_markdown + "</article>"
                        html += "</div>"
                    }
                    $("div.real_post").append(html)

                    if ($("#disqus").hide() ) {
                        $("#disqus").show()
                    }
                }
            }
        })

    })
