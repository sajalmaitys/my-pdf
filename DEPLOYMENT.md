# Deployment Guide

## 🚀 Vercel Deployment (Recommended)

This project is optimized for Vercel deployment with serverless functions.

### Quick Deploy to Vercel

1. **Fork this repository** or use the deploy button:
   
   [![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/sajalmaitys/PDF-to-Text-Converterx-)

2. **Manual Deployment:**
   - Go to [vercel.com](https://vercel.com)
   - Click "New Project"
   - Import from GitHub: `https://github.com/sajalmaitys/PDF-to-Text-Converterx-.git`
   - Vercel will auto-detect the configuration
   - Click "Deploy"

### Configuration Files

- ✅ `vercel.json` - Vercel deployment configuration
- ✅ `index.py` - Serverless-optimized Flask app
- ✅ `runtime.txt` - Python version specification
- ✅ `.vercelignore` - Deployment exclusions

### Environment Variables (Optional)

No environment variables are required for basic functionality.

## 🐳 Docker Deployment

Create a `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

Build and run:
```bash
docker build -t pdf-converter .
docker run -p 5000:5000 pdf-converter
```

## 🌐 Other Platforms

### Heroku
1. Create `Procfile`:
   ```
   web: gunicorn app:app
   ```
2. Deploy via Heroku CLI or GitHub integration

### Railway
1. Connect your GitHub repository
2. Railway will auto-detect Python and deploy

### PythonAnywhere
1. Upload files to your account
2. Configure WSGI file to point to `app.py`

## 🧪 Testing Your Deployment

After deployment, test these endpoints:
- `/` - Main application interface
- `/api/health` - Health check endpoint
- `/upload` - PDF upload functionality
- `/download` - File download functionality

## 🔧 Troubleshooting

### Common Issues:

1. **404 Error**: Ensure `index.py` exists and `vercel.json` is configured correctly
2. **Import Errors**: Check `requirements.txt` has all dependencies
3. **File Upload Issues**: Verify temporary file handling works in serverless environment
4. **Memory Limits**: Large PDFs may exceed serverless memory limits

### Debug Steps:

1. Check deployment logs in your platform's dashboard
2. Test the `/api/health` endpoint first
3. Verify all files are included in deployment
4. Check Python version compatibility

## 📊 Performance Notes

- **File Size Limit**: 16MB (configurable)
- **Processing Time**: ~5-30 seconds depending on PDF complexity
- **Memory Usage**: ~50-200MB per request
- **Concurrent Users**: Scales automatically on Vercel

## 🔒 Security Considerations

- Files are processed in temporary storage and automatically deleted
- No persistent file storage
- CORS headers configured for web access
- Input validation for PDF files only