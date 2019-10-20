$(document).ready(function() {
    $('#post_per').change(function() {
        let val = $(this).val()

        var url = ''
        if (val == 'day') {
            url = '/category/perday'
        }
        else if (val == 'category') {
            url = '/category/percategory'
        }

        $.get(url, function (data) {
            $("#posts").empty()
            $("#posts").html(data)
        })
    })

    $("#post_per").val("category")

    $("#post_per").change()
})