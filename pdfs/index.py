import os
import glob
from langchain.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma


def get_loader():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    pdf_dir = os.path.join(script_dir, '..', 'file')

    files = glob.glob(os.path.join(pdf_dir, '*.pdf'))
    print(files)

    if len(files) != 1:
        raise ValueError('You must provide only one file to load')

    loader = PyPDFLoader(files[0])
    return loader


def init_index() -> None:
    index = VectorstoreIndexCreator(vectorstore_cls=Chroma,
                                    embedding=OpenAIEmbeddings()).from_loaders([get_loader()])
    return index
