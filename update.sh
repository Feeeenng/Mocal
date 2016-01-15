echo "更新代码库"
git pull origin master
echo "重启uwsgi"
uwsgi --reload mocal.pid
echo "更新结束"