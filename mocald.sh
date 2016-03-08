#!/bin/bash
if [ ! -n "$1" ]
then
    echo "Usages: sh mocald.sh [start|stop|restart|update]"
    exit 0
fi

if [ $1 = start ]
then
    psid=`ps aux | grep "uwsgi" | grep -v "grep" | wc -l`
    if [ $psid -gt 4 ]
    then
        echo "mocald is running!"
        exit 0
    else
        uwsgi --ini /data/Mocal/mocal/conf/uwsgi-mocal.production.ini
        echo "Start mocald service [OK]"
    fi

elif [ $1 = stop ];then
    if [ $psid -lt 4 ]
    then
        echo "mocald is stopped!"
        exit 0
    else
        uwsgi --stop /data/Mocal/mocal/mocal.pid
        echo "Stop mocald service [OK]"
    fi

elif [ $1 = restart ];then
    uwsgi --reload /data/Mocal/mocal/mocal.pid
    echo "Restart mocald service [OK]"

elif [ $1 = update ];then
    echo "update code"
    git pull origin master
    echo "reload uwsgi"
    uwsgi --reload /data/Mocal/mocal/mocal.pid
    echo "Update mocald service [OK]"

else
    echo "Usages: sh mocald.sh [start|stop|restart|update]"
fi