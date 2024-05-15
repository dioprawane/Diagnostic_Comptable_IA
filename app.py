from flask import Flask, request, render_template
import openai
import os
from dotenv import load_dotenv
import pandas as pd
from werkzeug.utils import secure_filename

load_dotenv()  # Charger les variables d'environnement à partir du fichier .env

app = Flask(__name__)

# Configure OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

ALLOWED_EXTENSIONS = {'csv', 'xlsx', 'json'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def read_file(file):
    if file.filename.endswith('.csv'):
        return pd.read_csv(file).to_string(index=False)
    elif file.filename.endswith('.xlsx'):
        return pd.read_excel(file).to_string(index=False)
    elif file.filename.endswith('.json'):
        return pd.read_json(file).to_string(index=False)
    else:
        return None

def analyze_text(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Vous êtes un expert en détection d'anomalies comptables."},
            {"role": "user", "content": f"Analysez les écritures comptables suivantes et détectez les anomalies comme des champs de montant incorrects, des descriptions non valides, ou des comptes incorrects.\n\n{text}\n\nFournissez un résumé clair des anomalies détectées."}
        ]
    )
    return response.choices[0].message['content'].strip()

def analyze_financial_statement(statement):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Vous êtes un expert en analyse financière."},
            {"role": "user", "content": f"Analysez l'état financier suivant et fournissez une analyse :\n\n{statement}"}
        ]
    )
    return response.choices[0].message['content'].strip()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/diagnose', methods=['POST'])
def diagnose():
    content = request.form.get('content')
    file = request.files.get('file')
    analysis_type = request.form['analysis_type']
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_content = read_file(file)
        if analysis_type == 'entries':
            result = analyze_text(file_content)
        elif analysis_type == 'statement':
            result = analyze_financial_statement(file_content)
    elif content:
        if analysis_type == 'entries':
            result = analyze_text(content)
        elif analysis_type == 'statement':
            result = analyze_financial_statement(content)
    else:
        result = "Aucun contenu ou fichier valide fourni pour l'analyse."
    
    return render_template('result.html', content=content or filename, result=result)

if __name__ == '__main__':
    app.run(debug=True)
