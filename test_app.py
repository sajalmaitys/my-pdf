#!/usr/bin/env python3
"""
Simple test script to verify the PDF to Text Converter application works correctly.
"""

import os
import sys
from app import app

def test_app():
    """Test basic app functionality"""
    try:
        # Test app creation
        assert app is not None, "Flask app should be created"
        
        # Test upload folder creation
        assert os.path.exists('uploads'), "Uploads folder should exist"
        
        # Test routes exist
        with app.test_client() as client:
            # Test main page
            response = client.get('/')
            assert response.status_code == 200, "Main page should load"
            assert b'PDF to Text Converter' in response.data, "Page should contain title"
            
        print("✅ All basic tests passed!")
        return True
        
    except Exception as e:
        print(f"❌ Test failed: {str(e)}")
        return False

if __name__ == '__main__':
    success = test_app()
    sys.exit(0 if success else 1)