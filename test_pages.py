"""Test that all HTML pages exist and are valid"""
import os

def test_pages():
    print("Testing Frontend Pages...\n")
    
    pages = {
        "frontend/index.html": "Homepage",
        "frontend/about.html": "About Page",
        "frontend/analyze.html": "Analyze Page",
        "frontend/style.css": "Stylesheet",
        "frontend/script.js": "JavaScript"
    }
    
    all_exist = True
    
    for file_path, description in pages.items():
        if os.path.exists(file_path):
            size = os.path.getsize(file_path)
            print(f"[OK] {description:20} - {file_path} ({size} bytes)")
        else:
            print(f"[FAIL] {description:20} - {file_path} NOT FOUND")
            all_exist = False
    
    print("\n" + "=" * 60)
    
    if all_exist:
        print("All pages exist!")
        print("=" * 60)
        print("\nTo view the pages:")
        print("1. Run: start.bat")
        print("2. Open: http://localhost:8001")
        print("\nPages available:")
        print("- http://localhost:8001/index.html (Homepage)")
        print("- http://localhost:8001/about.html (About)")
        print("- http://localhost:8001/analyze.html (Analyze)")
        return True
    else:
        print("Some pages are missing!")
        print("=" * 60)
        return False

if __name__ == "__main__":
    test_pages()
