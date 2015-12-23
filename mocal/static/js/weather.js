/**
 * Created by Administrator on 2015/12/23.
 */
$(document).ready(function(){
    $('.weather').hide();
    $('.weather-handle').css('left', '98%');

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
            });
        }
    });

    $(".weather-handle").click(function(){
        $('.weather-handle').animate({left:'80%'}, 'slow', function(){
            $('.weather').fadeIn();
            $(this).attr('class', 'weather-handle-open');
        });
    });

    $(".weather-handle-open").click(function(){
        $('.weather-handle-open').animate({left:'98%'}, 'slow', function(){
            $('.weather').fadeOut('slow');
            $(this).attr('class', 'weather-handle');
        });
    });
});
