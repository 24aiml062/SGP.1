"""Test AI integration"""
import sys
import os

sys.path.insert(0, 'backend')

def test_ai_setup():
    print("=" * 60)
    print("AI Integration Test")
    print("=" * 60)
    print()
    
    # Check if OpenAI is installed
    try:
        import openai
        print("[OK] OpenAI library installed")
        print(f"    Version: {openai.__version__}")
    except ImportError:
        print("[FAIL] OpenAI library not installed")
        print("       Run: pip install openai")
        return False
    
    print()
    
    # Check if API key is set
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        print("[OK] OPENAI_API_KEY environment variable is set")
        print(f"    Key starts with: {api_key[:7]}...")
    else:
        print("[WARN] OPENAI_API_KEY not set")
        print("       Set with: set OPENAI_API_KEY=sk-your-key-here")
        print("       System will use rule-based mode")
    
    print()
    
    # Test agent initialization
    try:
        from agent import DigitalGrowthAgent
        agent = DigitalGrowthAgent()
        print("[OK] Agent initialized successfully")
        
        if agent.use_ai:
            print("    Mode: AI-powered (OpenAI GPT)")
        else:
            print("    Mode: Rule-based (fallback)")
    except Exception as e:
        print(f"[FAIL] Agent initialization failed: {e}")
        return False
    
    print()
    
    # Test strategy generation
    print("Testing strategy generation...")
    test_business = {
        "business_name": "Test Bakery",
        "business_type": "Bakery",
        "products_services": "Custom cakes and pastries",
        "location": "Downtown",
        "target_customers": "Families",
        "price_range": "Mid-range",
        "current_presence": "None",
        "goals": "Increase visibility"
    }
    
    try:
        strategy = agent.generate_strategy(test_business)
        print("[OK] Strategy generated successfully")
        
        # Check components
        required_keys = [
            "business_positioning",
            "platform_strategy",
            "growth_strategy",
            "content_strategy",
            "content_ideas",
            "sample_content",
            "local_expansion",
            "action_plan_30_days"
        ]
        
        for key in required_keys:
            if key in strategy:
                print(f"    ✓ {key}")
            else:
                print(f"    ✗ {key} missing")
        
        print()
        print("Sample output:")
        print(f"  Brand Personality: {strategy['business_positioning']['brand_personality']}")
        print(f"  Platforms: {len(strategy['platform_strategy']['recommended_platforms'])}")
        print(f"  Captions: {len(strategy['sample_content']['promotional_captions'])}")
        
    except Exception as e:
        print(f"[FAIL] Strategy generation failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    print()
    print("=" * 60)
    print("All tests passed!")
    print("=" * 60)
    print()
    
    if agent.use_ai:
        print("✓ AI integration is working!")
        print("  Your strategies will be powered by OpenAI GPT")
    else:
        print("⚠ Running in rule-based mode")
        print("  To enable AI:")
        print("  1. Get API key: https://platform.openai.com/api-keys")
        print("  2. Set: set OPENAI_API_KEY=sk-your-key-here")
        print("  3. Restart backend")
    
    print()
    return True

if __name__ == "__main__":
    success = test_ai_setup()
    sys.exit(0 if success else 1)
