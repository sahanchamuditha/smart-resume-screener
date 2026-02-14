def validate_file_type(filename: str):
    allowed_extensions = ("pdf", "docx")
    return filename.lower().endswith(allowed_extensions)
