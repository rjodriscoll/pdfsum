from langchain.llms import OpenAI


def get_response(index, question: str) -> str:
    return index.query(question, llm=OpenAI(model_name='text-davinci-003')
                       )
