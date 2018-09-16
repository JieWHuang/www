function get_list(url) {
    $.ajax({
        cache: false,
        type: "GET",
        url: url,
        success: function (data) {
            if (data.data.length != 0) {
                for (var i = 0; i < data.data.length; i++) {
                    label_box_html = '';
                    tags = data.data[i].tag;
                    for (var j = 0; j < tags.length; j++) {
                        label_box_html = label_box_html + '<a href="/tag/' + tags[j].tag_id + '" class="label"><i class="fa fa-tag"></i>' + tags[j].tag_name + '</a>'
                    }
                    item_html = '<li class="post_item" id=' + data.data[i].id + '><h3><i class="fa fa-hand-o-right"></i> <a href="article/' + data.data[i].id + '" title="' + data.data[i].title + '" id="title">' + data.data[i].title + '</a></h3><div class="description"><span class="time">' + data.data[i].create_time + ' - </span>' + data.data[i].description + '</div><div class="article_info"><span class="classify"><a href="/category/' + data.data[i].category_id + '/"><i class="fa fa-hashtag"></i>' + data.data[i].category + '</a></span><div class="label_box">' + label_box_html + '</div><span class="view"><i class="fa fa-eye"></i> ' + data.data[i].click_nums + '</span>' + '<a href="article/' + data.data[i].id + '#comment">' + '<span class="reply"><i class="fa fa-comment"></i> ' + data.data[i].cmt_nums + '</span></a></div></li>';
                    $('#summary_list').append(item_html);
                }
                if (data.totals == data.current_page) {
                    $('#more').html("没有更多文章了...")
                } else {
                    $('#more').html('<a href="javascript:get_list_btn();" id="next">点击加载更多...</a>')
                }
            } else {
                $('#more').html("文章加载失败了...")
            }
        }
    });
}