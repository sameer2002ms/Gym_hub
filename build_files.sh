# build_files.sh
echo "BUILD START"
pip install -r requirements.txt


echo "Make Migrations"
python 3.9 manage.py makemigrations
python 3.9 manage.py migrate

python3.9 manage.py collectstatic
echo "BUILD END"