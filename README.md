# PDF to Text Converter

A modern web application that extracts text from PDF files using Flask and pypdf.

## Features

- **Drag & Drop Upload** - Simply drag PDF files onto the upload area
- **Click to Browse** - Traditional file selection method
- **Real-time Processing** - Instant text extraction with loading indicators
- **Copy to Clipboard** - One-click text copying functionality
- **Download as TXT/DOCX** - Save extracted text as TXT or Word document
- **Responsive Design** - Works on desktop and mobile devices
- **File Validation** - Ensures only PDF files are processed
- **Size Limits** - Maximum 16MB file size for optimal performance

## Installation

1. **Clone or download** this project
2. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment:**
   ```bash
   # Windows
   .venv\Scripts\activate
   
   # macOS/Linux
   source .venv/bin/activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Start the application:**
   ```bash
   python app.py
   ```

2. **Open your browser** and navigate to `http://localhost:5000`

3. **Upload a PDF file** by:
   - Dragging and dropping it onto the upload zone
   - Clicking the upload zone to browse for files

4. **View the extracted text** and optionally:
   - Copy it to your clipboard
   - Download it as a .txt or .docx file

## Technical Details

- **Backend:** Flask web framework
- **PDF Processing:** pypdf library for text extraction
- **Document Generation:** python-docx for Word document creation
- **Frontend:** Bootstrap 5 with custom CSS
- **File Handling:** Secure filename processing with automatic cleanup
- **Error Handling:** Comprehensive error messages and validation

## File Structure

```
pdf-to-text-converter/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── README.md          # Documentation
├── templates/
│   └── index.html     # Web interface
└── uploads/           # Temporary file storage (auto-created)
```

## Browser Support

- Chrome/Edge (recommended)
- Firefox
- Safari
- Mobile browsers

## Limitations

- Maximum file size: 16MB
- PDF files only
- Text extraction quality depends on PDF structure
- Scanned PDFs may not extract text properly

## Development

To run in development mode:
```bash
python app.py
```

The application will start with debug mode enabled and auto-reload on file changes.

## Deployment

### Vercel Deployment

This application is configured for easy deployment on Vercel:

1. **Fork or clone** this repository
2. **Connect to Vercel:**
   - Go to [vercel.com](https://vercel.com)
   - Import your GitHub repository
   - Vercel will automatically detect the configuration

3. **Deploy:**
   - Vercel will automatically build and deploy your application
   - The `vercel.json` file contains all necessary configuration
   - Uses `index.py` as the entry point for serverless deployment

### Local Testing for Vercel

To test the Vercel version locally:
```bash
pip install vercel
vercel dev
```

### Files for Vercel Deployment

- `index.py` - Vercel-optimized Flask application
- `vercel.json` - Vercel configuration
- `runtime.txt` - Python version specification
- `.vercelignore` - Files to ignore during deployment