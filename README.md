**WSL**

git clone https://github.com/MrKubot/LangChain_Twilio_demo.git

cd LangChain_Twilio_demo


python -m venv env

source env/bin/activate


sudo apt update && sudo apt install -y postgresql libpq-dev


pip install -r requirements.txt



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

