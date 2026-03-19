"""Quick test script for the Digital Growth Agent"""
import sys
sys.path.insert(0, 'backend')

from agent import DigitalGrowthAgent

def test_agent():
    print("Testing AI Digital Growth Agent...\n")
    
    # Initialize agent
    agent = DigitalGrowthAgent()
    
    # Test data
    test_business = {
        "business_name": "Sweet Delights Bakery",
        "business_type": "Bakery",
        "products_services": "Custom cakes, pastries, desserts",
        "location": "Downtown Chicago",
        "target_customers": "Families, event planners, dessert lovers",
        "price_range": "Mid-range",
        "current_presence": "None",
        "goals": "Increase local visibility and attract more customers"
    }
    
    # Generate strategy
    print("Generating strategy for:", test_business["business_name"])
    strategy = agent.generate_strategy(test_business)
    
    # Display results
    print("\n✓ Strategy generated successfully!\n")
    print("=" * 60)
    print("BUSINESS POSITIONING")
    print("=" * 60)
    print(f"Brand Personality: {strategy['business_positioning']['brand_personality']}")
    print(f"Value Proposition: {strategy['business_positioning']['value_proposition']}")
    
    print("\n" + "=" * 60)
    print("RECOMMENDED PLATFORMS")
    print("=" * 60)
    for platform in strategy['platform_strategy']['recommended_platforms']:
        print(f"{platform['priority']}. {platform['platform']}")
        print(f"   Reason: {platform['reason']}")
    
    print("\n" + "=" * 60)
    print("SAMPLE PROMOTIONAL CONTENT")
    print("=" * 60)
    for i, caption in enumerate(strategy['sample_content']['promotional_captions'], 1):
        print(f"{i}. {caption}\n")
    
    print("=" * 60)
    print("HASHTAGS")
    print("=" * 60)
    print(" ".join(strategy['sample_content']['hashtag_suggestions']))
    
    print("\n✓ All tests passed!")

if __name__ == "__main__":
    test_agent()
