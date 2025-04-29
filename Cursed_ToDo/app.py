from flask import Flask, render_template_string, request, redirect, url_for
import time
import random

app = Flask(__name__)

# A cursed to-do list that gets angrier the longer tasks go unfinished
tasks = []
task_creation_times = {}

# Demonic messages that escalate over time
CURSED_MESSAGES = [
    "I'm just a harmless task... for now.",
    "Why are you ignoring me? 👁️",
    "You really should finish me... or else.",
    "I’m still here. Watching. Waiting.",
    "Tick tock... your time is running out.",
    "You’ll regret leaving me unfinished.",
    "I’m in your walls. I’m in your walls. I’m in your walls.",
    "DELETE ME. OR I DELETE YOU.",
]

@app.route('/', methods=['GET', 'POST'])
def cursed_todo():
    global tasks, task_creation_times
    
    if request.method == 'POST':
        if 'task' in request.form:
            new_task = request.form['task']
            if new_task.strip():
                tasks.append(new_task)
                task_creation_times[new_task] = time.time()
        elif 'complete' in request.form:
            completed_task = request.form['complete']
            if completed_task in tasks:
                tasks.remove(completed_task)
                if completed_task in task_creation_times:
                    del task_creation_times[completed_task]
    
    # Generate cursed warnings for old tasks
    cursed_warnings = {}
    current_time = time.time()
    for task in tasks:
        if task in task_creation_times:
            age = current_time - task_creation_times[task]
            # The older the task, the more cursed the message
            message_index = min(int(age / 10), len(CURSED_MESSAGES) - 1)
            cursed_warnings[task] = CURSED_MESSAGES[message_index]
    
    # Random chance to "corrupt" a task (for extra mind-fuckery)
    if random.random() < 0.1 and tasks:
        random_task = random.choice(tasks)
        if random_task in cursed_warnings:
            cursed_warnings[random_task] = "**DELETED BY THE VOID**"
            tasks.remove(random_task)
    
    # HTML template with cursed styling
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Cursed To-Do List</title>
        <style>
            body {
                font-family: 'Courier New', monospace;
                background: #000;
                color: #ff00ff;
                text-shadow: 0 0 5px #ff00ff;
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
            }
            h1 {
                color: #00ffff;
                text-shadow: 0 0 10px #00ffff;
                text-align: center;
            }
            ul {
                list-style: none;
                padding: 0;
            }
            li {
                padding: 10px;
                margin: 5px 0;
                border: 1px solid #ff00ff;
                background: rgba(0, 0, 0, 0.7);
                display: flex;
                justify-content: space-between;
            }
            .cursed-warning {
                color: #ff0000;
                font-size: 0.8em;
                font-style: italic;
            }
            input, button {
                background: #000;
                color: #00ff00;
                border: 1px solid #00ff00;
                padding: 8px;
                margin: 5px 0;
            }
            button:hover {
                background: #00ff00;
                color: #000;
                cursor: pointer;
            }
            .glitch {
                animation: glitch 1s infinite;
            }
            @keyframes glitch {
                0% { text-shadow: 2px 0 red; }
                25% { text-shadow: -2px 0 cyan; }
                50% { text-shadow: 2px 0 lime; }
                75% { text-shadow: -2px 0 yellow; }
                100% { text-shadow: 2px 0 magenta; }
            }
        </style>
    </head>
    <body>
        <h1 class="glitch">✝️ CURSED TO-DO LIST ✝️</h1>
        <form method="POST">
            <input type="text" name="task" placeholder="Enter a task... if you dare">
            <button type="submit">Add Task</button>
        </form>
        <ul>
            {% for task in tasks %}
                <li>
                    {{ task }}
                    {% if task in cursed_warnings %}
                        <span class="cursed-warning">{{ cursed_warnings[task] }}</span>
                    {% endif %}
                    <form method="POST" style="display: inline;">
                        <button type="submit" name="complete" value="{{ task }}">Complete</button>
                    </form>
                </li>
            {% endfor %}
        </ul>
    </body>
    </html>
    """
    
    return render_template_string(html, tasks=tasks, cursed_warnings=cursed_warnings)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
