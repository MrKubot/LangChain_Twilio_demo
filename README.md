**WSL**

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

**.env**


DB_NAME=

DB_USER=

DB_PASSWORD=


TWILIO_ACCOUNT_SID=

TWILIO_AUTH_TOKEN=

TWILIO_PHONE_NUMBER=


OPENAI_API_KEY=


SECRET_KEY=

DEBUG=

