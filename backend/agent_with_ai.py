"""
AI-Enhanced Digital Growth Agent
Uses OpenAI GPT for content generation
"""

import json
import os

class DigitalGrowthAgent:
    def __init__(self):
        # Try to use OpenAI if API key is available
        try:
            import openai
            api_key = os.getenv("OPENAI_API_KEY")
            if api_key:
                openai.api_key = api_key
                self.use_ai = True
                print("✓ Digital Growth Agent initialized with AI")
            else:
                self.use_ai = False
                print("✓ Digital Growth Agent initialized (template mode)")
        except ImportError:
            self.use_ai = False
            print("✓ Digital Growth Agent initialized (template mode)")
    
    def generate_strategy(self, business_data):
        """Generate comprehensive digital marketing strategy"""
        
        # Extract business info
        name = business_data.get("business_name", "")
        biz_type = business_data.get("business_type", "")
        products = business_data.get("products_services", "")
        location = business_data.get("location", "")
        target = business_data.get("target_customers", "")
        goals = business_data.get("goals", "")
        
        # Generate each component
        positioning = self._generate_positioning(name, biz_type, products, target)
        platform_strategy = self._generate_platform_strategy(biz_type, target, goals)
        growth_strategy = self._generate_growth_strategy(biz_type, target, goals)
        content_strategy = self._generate_content_strategy(biz_type, target)
        content_ideas = self._generate_content_ideas(biz_type, products)
        
        # Use AI for content generation if available
        if self.use_ai:
            sample_content = self._ai_generate_content(name, biz_type, products)
        else:
            sample_content = self._template_generate_content(name, biz_type, products)
        
        local_expansion = self._generate_local_expansion(biz_type, location)
        action_plan = self._generate_action_plan(biz_type)
        
        return {
            "business_positioning": positioning,
            "platform_strategy": platform_strategy,
            "growth_strategy": growth_strategy,
            "content_strategy": content_strategy,
            "content_ideas": content_ideas,
            "sample_content": sample_content,
            "local_expansion": local_expansion,
            "action_plan_30_days": action_plan
        }
    
    def _ai_generate_content(self, name, biz_type, products):
        """Use OpenAI to generate content"""
        import openai
        
        try:
            # Generate promotional captions
            promo_prompt = f"""
            Create 3 engaging promotional social media captions for a {biz_type} 
            called "{name}" that sells {products}. Include emojis and make them 
            suitable for Instagram/Facebook. Keep each caption under 150 characters.
            """
            
            promo_response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": promo_prompt}],
                temperature=0.7
            )
            
            promo_captions = promo_response.choices[0].message.content.strip().split('\n')
            promo_captions = [c.strip() for c in promo_captions if c.strip()][:3]
            
            # Generate hashtags
            hashtag_prompt = f"""
            Suggest 8 relevant hashtags for a {biz_type} selling {products}.
            Include both general and specific hashtags. Format: #hashtag
            """
            
            hashtag_response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": hashtag_prompt}],
                temperature=0.5
            )
            
            hashtags = hashtag_response.choices[0].message.content.strip().split()
            hashtags = [h for h in hashtags if h.startswith('#')][:8]
            
            return {
                "promotional_captions": promo_captions,
                "engagement_captions": [
                    f"What's your favorite {products}? Tell us in the comments! 👇",
                    f"Quick poll: Which would you choose? Option A or Option B? 🗳️",
                    f"Share your experience with us! Tag us in your photos. 📸"
                ],
                "hashtag_suggestions": hashtags
            }
            
        except Exception as e:
            print(f"AI generation failed: {e}, falling back to templates")
            return self._template_generate_content(name, biz_type, products)
    
    def _template_generate_content(self, name, biz_type, products):
        """Use templates to generate content (current approach)"""
        return {
            "promotional_captions": [
                f"✨ Discover quality {products} at {name}! Visit us today and experience the difference. 📍",
                f"🎉 Special offer this week! Get amazing {products}. Limited time only! DM us to order. 💬",
                f"💯 Why choose {name}? Quality, service, and community. See what our customers are saying! ⭐"
            ],
            "engagement_captions": [
                f"❓ What's your favorite {products}? Tell us in the comments! 👇",
                f"🤔 Quick poll: Which would you choose? Option A or Option B? Vote below! 🗳️",
                f"💭 Share your experience with us! Tag us in your photos for a chance to be featured. 📸"
            ],
            "hashtag_suggestions": [
                f"#{biz_type.replace(' ', '')}",
                "#LocalBusiness",
                "#ShopLocal",
                "#SmallBusiness",
                "#CommunityFirst",
                f"#{products.split()[0] if products else 'Quality'}",
                "#SupportLocal",
                "#SmallBusinessLove"
            ]
        }
    
    # ... (rest of the methods remain the same as agent.py)
    # Copy all other methods from agent.py here
