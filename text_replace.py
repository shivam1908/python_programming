# To read file text then search and replace the text with new text and write to file
def find_and_replace(source, text, replacement):
    with open(source, "r+") as source_file:
        data = source_file.read()
        updated_data = data.replace(text, replacement)
        source_file.seek(0)
        source_file.write(updated_data)

find_and_replace("data/sample_data.txt", "is" , "haha")

