from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from django.conf import settings


def analyze_message(message: str) -> list:
    prompt = ChatPromptTemplate.from_messages(
        [("system",
        """
        Jesteś systemem klasyfikacji wiadomości w firmie.         
        Na podstawie treści {message} określ, do których ról pracowników należy wysłać wiadomość.
        Możliwe role to: Magazynier (MGZN), Brygadzista (BRGD) oraz Manager (MNGR).
        Zwróć jedynie oznaczenia ról, na przykład 'MGZN,MNGR' lub 'BRGD'.
        Jeżeli nie jesteś pewien, wybierz 'MNGR'.
        """
        )]
    )

    model = ChatOpenAI(
        api_key=settings.OPENAI_API_KEY,
        model='gpt-3.5-turbo'
    )

    chain = prompt | model
    response = chain.invoke({'message': message})

    return [r.strip() for r in response.content.split(',')]