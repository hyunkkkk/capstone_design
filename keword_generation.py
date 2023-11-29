from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI

api_key = "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"
chat_model = ChatOpenAI(openai_api_key=api_key)

my_template = """아래의 질문을 몇가지 키워드로 요약해줘.
질문: {question}"""

prompt = PromptTemplate.from_template(my_template)
prompt.format(question="아이유는 몇살이야?")

chat_model.predict(prompt.format(question="아이유는 몇살이야?"))