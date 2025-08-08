from flask import Flask, render_template, request, jsonify, send_file
from pypdf import PdfReader
from docx import Document
import os
from werkzeug.utils import secure_filename
import io
import tempfile
import traceback

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# For Vercel, we'll use /tmp directory for temporary files
app.config['UPLOAD_FOLDER'] = '/tmp'

# Add CORS headers
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'pdf'

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            text += page.extract_text() + "\n"
        
        if not text.strip():
            return "No text could be extracted from this PDF. It might be a scanned document or image-based PDF."
            
    except Exception as e:
        raise Exception(f"Error reading PDF: {str(e)}")
    return text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'message': 'PDF to Text Converter API is running',
        'version': '1.0.0'
    })

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file selected'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file and allowed_file(file.filename):
        try:
            filename = secure_filename(file.filename)
            # Use tempfile for Vercel compatibility
            with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_file:
                file.save(temp_file.name)
                filepath = temp_file.name
            
            extracted_text = extract_text_from_pdf(filepath)
            
            # Clean up temporary file
            if os.path.exists(filepath):
                os.remove(filepath)
            
            return jsonify({
                'success': True,
                'text': extracted_text,
                'filename': filename
            })
            
        except Exception as e:
            # Clean up file if it exists
            if 'filepath' in locals() and os.path.exists(filepath):
                os.remove(filepath)
            print(f"Error processing PDF: {str(e)}")
            print(traceback.format_exc())
            return jsonify({'error': f'Failed to process PDF: {str(e)}'}), 500
    
    return jsonify({'error': 'Please upload a valid PDF file'}), 400

@app.route('/download', methods=['POST'])
def download_text():
    try:
        data = request.get_json()
        text = data.get('text', '')
        filename = data.get('filename', 'extracted_text')
        format_type = data.get('format', 'txt')
        
        if not text:
            return jsonify({'error': 'No text to download'}), 400
        
        base_filename = filename.rsplit('.', 1)[0] if '.' in filename else filename
        
        if format_type == 'docx':
            # Create DOCX file
            doc = Document()
            # Split text into paragraphs for better formatting
            paragraphs = text.split('\n\n')
            for paragraph in paragraphs:
                if paragraph.strip():
                    doc.add_paragraph(paragraph.strip())
            
            docx_file = io.BytesIO()
            doc.save(docx_file)
            docx_file.seek(0)
            
            return send_file(
                docx_file,
                as_attachment=True,
                download_name=f"{base_filename}.docx",
                mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
            )
        else:
            # Create TXT file
            text_file = io.BytesIO()
            text_file.write(text.encode('utf-8'))
            text_file.seek(0)
            
            return send_file(
                text_file,
                as_attachment=True,
                download_name=f"{base_filename}.txt",
                mimetype='text/plain'
            )
    except Exception as e:
        print(f"Error creating download file: {str(e)}")
        return jsonify({'error': 'Failed to create download file'}), 500

# This is required for Vercel
if __name__ == '__main__':
    app.run(debug=True)
else:
    # For Vercel deployment
    application = app