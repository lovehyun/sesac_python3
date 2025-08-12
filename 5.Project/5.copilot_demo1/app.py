from flask import Flask, render_template, request, redirect, url_for, jsonify
app = Flask(__name__)

# In-memory storage for todo items
todos = []

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', todos=todos)

@app.route('/todo', methods=['POST'])
def add_todo():
    # Add new todo item
    todo_text = request.form.get('todo')
    if todo_text:
        todos.append({'text': todo_text, 'completed': False})
    return redirect(url_for('index'))

@app.route('/todo', methods=['PUT'])
def update_todo():
    # Update the completion status of a todo item
    data = request.get_json()
    todo_text = data.get('todo')

    for todo in todos:
        if todo['text'] == todo_text:
            todo['completed'] = not todo['completed']
            return jsonify({'success': True}), 200
    return jsonify({'success': False}), 404

@app.route('/todo', methods=['DELETE'])
def delete_todo():
    # Delete a todo item
    data = request.get_json()
    todo_text = data.get('todo')

    global todos
    todos = [todo for todo in todos if todo['text'] != todo_text]

    return jsonify({'success': True}), 200

if __name__ == '__main__':
    app.run(debug=True)

