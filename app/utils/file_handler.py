def validate_file_type(filename: str):
    allowed = ["pdf", "docx"]
    ext = filename.split(".")[-1].lower()
    return ext in allowed
