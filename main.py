from flask import Flask, request, render_template
import re
import docx2txt

app = Flask(__name__)

def find_most_frequent_word(content):
    words = re.findall(r'\w+', content.lower())
    if words:
        word_frequencies = {}
        for word in words:
            if word in word_frequencies:
                word_frequencies[word] += 1
            else:
                word_frequencies[word] = 1

        most_frequent_word = max(word_frequencies, key=word_frequencies.get)
        return most_frequent_word
    else:
        return ""

def read_file_content(file):
    if file.filename.endswith('.txt'):
        content = file.read().decode('utf-8')
    elif file.filename.endswith('.doc') or file.filename.endswith('.docx'):
        content = docx2txt.process(file)
    else:
        raise ValueError("Неподдерживаемый формат файла.")
    return content

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename:
            try:
                content = read_file_content(file)
                most_frequent_word = find_most_frequent_word(content)
                return render_template('index.html', most_frequent_word=most_frequent_word)
            except Exception as e:
                return render_template('index.html', error_message="Ошибка: " + str(e))
        else:
            return render_template('index.html', error_message="Пожалуйста, выберите файл для загрузки.")
    return render_template('index.html', most_frequent_word="")

if __name__ == '__main__':
    app.run()



