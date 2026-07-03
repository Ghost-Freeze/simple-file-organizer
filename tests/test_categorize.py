from organizer.categorize import categorize

def test_audio_extension():
    assert categorize("scream.mp3") == "Audio"

def test_document_extension():
    assert categorize("contract.pdf") == "Documents"

def test_unknown_extension_falls_back_to_other():
    assert categorize("susfile.xyz123") == "Other"

def test_no_extension_falls_back_to_other():
    assert categorize("README") == "Other"

def test_dotfile_is_not_treated_as_extension():
    assert categorize(".gitignore") == "Other"

def test_case_insensitive_matching():
    assert categorize("gorgeous.JPG") == "Images"

# python -m pytest -v in the terminal to check if it categorize works