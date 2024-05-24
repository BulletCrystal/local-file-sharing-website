from flask import Flask, render_template, request, jsonify, send_file
import os

app = Flask(__name__)

# Define the directory for downloads
download_dir = 'downloads'

@app.route('/')
def index():
    # Get the list of files in the download directory
    files = os.listdir(download_dir)
    return render_template('index.html', files=files)

@app.route('/order', methods=['POST'])
def order():
    file = request.files['file']

    # Save the file
    try:
        file.save(os.path.join(download_dir, file.filename))
        response = render_template('order.html')
    except:
        response = jsonify({'message': 'no file detected'})
    return response

@app.route('/download', methods=['GET'])
def download():
    try:
        filename = request.args.get('filename')
        response = send_file(os.path.join(download_dir, filename), as_attachment=True)
    except Exception as e:
        response = jsonify({'message': 'an error has occured','ERROR':f'{e}'})
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
