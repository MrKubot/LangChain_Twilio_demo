**---------- WSL ----------**

git clone https://github.com/MrKubot/LangChain_Twilio_demo.git

cd LangChain_Twilio_demo

python -m venv env

source env/bin/activate

sudo apt update && sudo apt install -y postgresql libpq-dev

pip install -r requirements.txt

sudo -u postgres psql -c "CREATE DATABASE langchain_db;"

sudo -u postgres psql -c "CREATE USER langchain_user WITH PASSWORD 'strongpassword';"

sudo -u postgres psql -c "ALTER ROLE langchain_user SET client_encoding TO 'utf8';"

sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE langchain_db TO langchain_user;"

**---------- .env ----------**

DB_NAME=langchain_db

DB_USER=langchain_user

DB_PASSWORD=strongpassword

TWILIO_ACCOUNT_SID=

TWILIO_AUTH_TOKEN=

TWILIO_PHONE_NUMBER=

OPENAI_API_KEY=

SECRET_KEY=

DEBUG=


**python manage.py migrate**

**python manage.py createsuperuser**

**python manage.py runserver**

http://127.0.0.1:8000/notifications/send/


**---------- ERRORS? ----------**

sudo apt install python3-dev libpq-dev

pip install psycopg2-binary --force-reinstall

sudo apt install build-essential python3-venv
