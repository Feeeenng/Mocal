/**
 * Created by hannengfang on 15/8/10.
 */

//加载
function show_loading(){
    $('#bg').css('display', 'block');
    $('.spinner').css('display', 'block');
}


function hide_loading(){
    $('#bg').css('display', 'none');
    $('.spinner').css('display', 'none');
}


//检查邮箱格式
function check_email_format(email){
    var search_str = /^[\w\-\.]+@[\w\-\.]+(\.\w+)+$/;
    if(!search_str.test(email)){
        return false;
    }
    return true;
}


//弹出框
function show_msg(str,time){
    if($("#alertMsg").attr('id') == undefined){
        var msg = "<div id='alertMsg' style='font-family:微软雅黑;color:white;display:none;position:absolute;z-index:100000;background-color:#333;font-weight:bold;font-size:14pt;padding:25px 15px 25px 15px;border-radius: 5px 5px 5px 5px;box-shadow: 0 0 5px #222;'>"+str+"</div>";
        $("body").append(msg);
        msgObj = $("#alertMsg");
        msgObj.css('top',($(window).height()-msgObj.height())/2+$(document).scrollTop()-100);
        msgObj.css('left',($(document).width()-msgObj.width())/2 - 15);
        $("#alertMsg").show().delay( 100 ).fadeOut(time, function() {
            $(this).remove();
        });
    }
}

