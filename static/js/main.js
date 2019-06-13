$("[data-toggle='tooltip']").tooltip();

function everyday_sentence() {
    var dsapi = "/get_dsapi/";
    $.ajax({
        url: dsapi,
        type: 'GET',
        dataType: 'JSONP',
        success: function (data) {
            // console.log(data);
            $("#today").html(data.dateline);
            $("#es_content").html(data.content);
            $("#es_note").html(data.note);
            $("#es_from").html(data.caption);
            $("#es_img").attr("src", data.picture);
            $("#es_img").attr("alt", data.dateline);
        }
    });
}


function back_top() {
    $(window).scroll(function () {
        if ($(window).scrollTop() > 50) { //大于100行才出现跳转箭头
            $("#back_top").fadeIn(500);  //大于1500行时跳转箭头慢慢透明显示
        }
        else {
            $("#back_top").fadeOut(500);  //大于1500行时跳转箭头慢慢透明消失
        }
    });
    //当点击跳转链接后，回到页面顶部位置
    $("#back_top").click(function () {
        $('body,html').animate({scrollTop: 0}, 1000);//1s完成回到顶部
        return false;
    });
}

everyday_sentence();
back_top();




