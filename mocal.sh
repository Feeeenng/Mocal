if [ ! -n "$1" ];then
    echo "Usages: sh mocal.sh [start|stop|restart|update|status]"
    exit 0
fi

if [ $1 = start ]
then
    supervisorctl -c ./mocal/conf/supervisor.conf start mocal  
elif [ $1 = stop ];then
    supervisorctl -c ./mocal/conf/supervisor.conf stop mocal
elif [ $1 = restart ];then
    supervisorctl -c ./mocal/conf/supervisor.conf stop mocal
    supervisorctl -c ./mocal/conf/supervisor.conf reload
    supervisorctl -c ./mocal/conf/supervisor.conf start mocal
elif [ $1 = update ];then
    echo "update code"
    git pull origin master
    echo "reload uwsgi"
    supervisorctl -c ./mocal/conf/supervisor.conf stop mocal
    supervisorctl -c ./mocal/conf/supervisor.conf reload
    supervisorctl -c ./mocal/conf/supervisor.conf start mocal
elif [ $1 = status ];then
    supervisorctl -c ./mocal/conf/supervisor.conf status
else
    echo "Usages: sh mocald.sh [start|stop|restart|update]"
fi

