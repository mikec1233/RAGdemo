import logging
from pathlib import Path
from llama_index.core.readers.base import BaseReader

logger = logging.getLogger(__name__)

def _try_loading_included_file_formats() -> dict[str, type[BaseReader]]:
    """
    Attempt to load file readers for various document formats.

    Returns:
        dict[str, type[BaseReader]]: A mapping of file extensions to their corresponding reader classes.

    Raises:
        ImportError: If required readers cannot be imported.
    """
    default_file_reader_cls: dict[str, type[BaseReader]] = {}

    try:
        from llama_index.readers.file.docs import PDFReader
        default_file_reader_cls[".pdf"] = PDFReader
        logger.info("Successfully loaded PDFReader.")
    except ImportError as e:
        logger.warning("PDFReader import failed: %s", e)

    try:
        from llama_index.readers.file import UnstructuredReader
        default_file_reader_cls[".html"] = UnstructuredReader
        logger.info("Successfully loaded UnstructuredReader for html")
    except ImportError as e:
        logger.warning("UnstructuredReader for html import failed: %s", e)

    if not default_file_reader_cls:
        raise ImportError("No file readers were loaded. Please check the llama_index installation.")

    return default_file_reader_cls
