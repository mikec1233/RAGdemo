from load_doc_reader import _try_loading_included_file_formats
from pathlib import Path

def read_document(file_path: str):
    file_extension = Path(file_path).suffix
    reader_classes = _try_loading_included_file_formats()
    
    if file_extension in reader_classes:
        reader = reader_classes[file_extension]()
        document_content = reader.read(file_path)  # This will depend on the actual implementation of the reader
        return document_content
    else:
        raise ValueError(f"No reader available for the file format: {file_extension}")

# Example usage
file_path = "/home/patrick/Documents/RAGdemo/backend/data/test/admiral/adsl.html"  # or example_document.pdf
content = read_document(file_path)
print(content)
