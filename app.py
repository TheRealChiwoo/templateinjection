from flask import Flask, render_template_string, request

app = Flask(__name__)

def read_flag_from_file():
    try:
        with open('flag.txt', 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return ''

def calculate_expression(expression):
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return str(e)

@app.route('/')
def index():
    return render_template_string(open('index.html').read())

@app.route('/search')
def search():
    search_query = request.args.get('query', '')
    
    if search_query == '{{flag}}':
        flag = read_flag_from_file()
        return render_template_string("Congratulations! Flag: {{ flag }}", flag=flag)
    else:
        result = calculate_expression(search_query)
        return render_template_string(open('index.html').read(), query_result=result, query=search_query)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
