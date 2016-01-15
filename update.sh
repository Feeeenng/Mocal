echo "update code"
git pull origin master
echo "reload uwsgi"
uwsgi --reload mocal.pid
echo "ending"
