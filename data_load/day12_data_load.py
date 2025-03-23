import os

def load_text_data(filepath: str):
    #docstring
    """
    Loads text data from a text file.
    filepath: str
        Path to the file
    """
    if not os.path.exists(filepath):
        content = ""
        # msg = "File doesn't exist"
        status = False
    else:
        with open(filepath, 'r')as file:
            content = file.read()
            # msg = "File exist"
            status = True

    return status, content

        # raise Exception("No file found")

    # try:
    #     with open(filepath, 'r')as file:
    #         content = file.read()
    # except FileNotFoundError as e:
    #     content = ''

    # return content
        
    # print(f"{filepath = }")
    # pass

def load_excel_data(filepath: str):
    return ""