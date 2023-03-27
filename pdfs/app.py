import gradio as gr
from index import init_index
from question import get_response


def process_input(index, question: str) -> str:
    return get_response(index, question)


if __name__ == '__main__':
    index = init_index()

    iface = gr.Interface(
        fn=lambda question: process_input(index, question),
        inputs=[
            gr.inputs.Textbox(lines=2, label="Your Question"),
        ],
        outputs=gr.outputs.Textbox(label="Chatbot Answer"),
        title="Chatbot",
        description="Ask a question about your document to get a response from the LLM.",
    )

    iface.launch()
