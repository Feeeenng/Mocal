/**
 * Created by Administrator on 2015/12/23.
 */
$(document).ready(function(){
    $('.weather').hide();
    $('.weather-handle').css('left', '98%');
    $('#l-btn-flag').hide();

    $(".r-button").click(function(){
        var element;
        $(".weather-content").each(function(i){
            if($(this).css('display')=='block'){
                element = this;
                return false;
            }
        });

        var item_id = $(element).attr('id');
        var id = parseInt(item_id);
        if(id>=0&&id<=2){
            $("#"+item_id).fadeOut('slow', function(){
                $('#'+(++id)).fadeIn('slow');
                if(id==3){
                    $('#r-btn-flag').hide();
                }else{
                    $('#l-btn-flag').show();
                    $('#r-btn-flag').show();
                }
            });
        }
    });

    $(".l-button").click(function(){
        var element;
        $(".weather-content").each(function(i){
            if($(this).css('display')=='block'){
                element = this;
                return false;
            }
        });

        var item_id = $(element).attr('id');
        var id = parseInt(item_id);
        if(id>=1&&id<=3){
            $("#"+item_id).fadeOut('slow', function (){
                $('#'+(--id)).fadeIn('slow');
                if(id==0){
                    $('#l-btn-flag').hide();
                }else{
                    $('#l-btn-flag').show();
                    $('#r-btn-flag').show();
                }
            });
        }
    });

    $(".weather-handle").click(function(){
        var open = $(this).attr('open');
        if(open){
            // �ر�
            $('.weather').fadeOut('normal', function(){
                $('.weather-handle').animate({left:'98%'}, 'normal', function(){
                    $(this).removeAttr('open');
                });
            });
        }else{
            // ��
            $('.weather-handle').animate({left:'80%'}, 'normal', function(){
                $('.weather').fadeIn('normal');
                $(this).attr('open', 'open');
            });
        }
    });
});

var weather_handle = $('.weather-handle');
var weather = $('.weather');

// ��ֹð���¼�
weather_handle.bind("click",function(event){
    event.stopPropagation();    //  ��ֹ�¼�ð��
});
weather.bind("click",function(event){
    event.stopPropagation();    //  ��ֹ�¼�ð��
});

$(document).click(function(e) {
	if(e.target != weather_handle[0] && e.target != weather[0]) {
        var open = weather_handle.attr('open');
        if(open) {
            weather.fadeOut('normal', function () {
                weather_handle.animate({left: '98%'}, 'normal', function () {
                    $(this).removeAttr('open');
                });
            });
        }
	}
});