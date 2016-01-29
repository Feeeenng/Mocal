/**
 * Created by Administrator on 2016/1/29.
 */
function check_illegal_character (str){
    var filterString = "";
    filterString = filterString == "" ? "'~`·!@#$%^&*()-+./" : filterString;
    var ch;
    var i;
    var temp;
    var error = false; // 当包含非法字符时，返回True
    for (i = 0; i <= (filterString.length - 1); i++) {
        ch = filterString.charAt(i);
        temp = str.indexOf(ch);
        if (temp != -1) {
            error = true;
            break;
        }
    }
    return error;
}