"""Test the API endpoints"""
import sys
import time

def test_backend():
    print("Testing Backend API...\n")
    
    try:
        import requests
        print("[OK] requests library available")
    except ImportError:
        print("[INFO] Installing requests library...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
        import requests
        print("[OK] requests installed")
    
    # Test root endpoint
    print("\nTesting root endpoint...")
    try:
        response = requests.get("http://localhost:8000", timeout=5)
        if response.status_code == 200:
            print(f"[OK] Backend is running: {response.json()}")
        else:
            print(f"[FAIL] Unexpected status code: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("[FAIL] Cannot connect to backend")
        print("\nPlease start the backend server first:")
        print("  run_backend.bat")
        return False
    except Exception as e:
        print(f"[FAIL] Error: {e}")
        return False
    
    # Test strategy generation
    print("\nTesting strategy generation...")
    test_data = {
        "business_name": "Test Bakery",
        "business_type": "Bakery",
        "products_services": "Cakes and pastries",
        "location": "Test City",
        "target_customers": "Families",
        "price_range": "Mid-range",
        "current_presence": "None",
        "goals": "Increase visibility"
    }
    
    try:
        response = requests.post(
            "http://localhost:8000/generate-strategy",
            json=test_data,
            timeout=10
        )
        
        if response.status_code == 200:
            strategy = response.json()
            print("[OK] Strategy generated successfully")
            print(f"[OK] Recommended platforms: {len(strategy['platform_strategy']['recommended_platforms'])}")
            print(f"[OK] Promotional captions: {len(strategy['sample_content']['promotional_captions'])}")
            print(f"[OK] Hashtags: {len(strategy['sample_content']['hashtag_suggestions'])}")
            return True
        else:
            print(f"[FAIL] Status code: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"[FAIL] Error: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("API Test")
    print("=" * 60)
    
    success = test_backend()
    
    print("\n" + "=" * 60)
    if success:
        print("All API tests passed!")
        print("=" * 60)
        print("\nYou can now use the frontend at: http://localhost:8001")
    else:
        print("API tests failed!")
        print("=" * 60)
        print("\nMake sure the backend is running:")
        print("  run_backend.bat")
    print()
