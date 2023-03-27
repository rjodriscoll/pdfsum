## PDF Chatbot

A chatbot that answers questions based on the content of a PDF file. Place your PDF file in the file folder located in the project root directory, set up the environment, and start the Gradio app to use the chatbot.

### Getting Started

Follow these steps to set up and run the PDF chatbot:

Place your PDF file in the file folder: The chatbot will use the content of this file to answer questions. Make sure there's only one PDF file in the folder.

Create a virtual environment and install dependencies: Set up a virtual environment (recommended) and install the required packages from requirements.txt. To do this, open a terminal, navigate to the project root directory, and run the following commands:

```
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
```
Set the OpenAI API key as an environment variable: Obtain your OpenAI API key and set it as an environment variable. Replace your_api_key_here with your actual API key:

```
    export OPENAI_API_KEY='your_api_key_here'
```
Run the app: Navigate to the pdfs directory and run app.py:

```
    cd pdfs
    python app.py
```
    The Gradio app will start, and you'll see a link to access the chatbot in your browser (usually http://127.0.0.1:7860/).

Now you can use the chatbot by entering your questions in the text input field, and the chatbot will provide answers based on the content of the PDF file you placed in the file folder.

Notes

- Ensure that the file folder contains only one PDF file. The chatbot is designed to work with a single file.
- If you want to use a different PDF file, replace the existing one in the file folder and restart the app.
- When running the app for the first time or changing the PDF file, the init process may take some time as the chatbot indexes the content of the PDF file.