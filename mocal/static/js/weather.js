/**
 * Created by Administrator on 2015/12/23.
 */
$(document).ready(function(){
    var width = $(".weather-content").width();

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
});
