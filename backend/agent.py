import json

class DigitalGrowthAgent:
    def __init__(self):
        # AI model initialization (optional - using rule-based logic for now)
        self.generator = None
        print("✓ Digital Growth Agent initialized")
    
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
        sample_content = self._generate_sample_content(name, biz_type, products)
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
    
    def _generate_positioning(self, name, biz_type, products, target):
        return {
            "brand_personality": self._get_brand_personality(biz_type),
            "value_proposition": f"Quality {products} for {target} in your local community",
            "ideal_customer": target,
            "tone": "Friendly, authentic, and community-focused"
        }
    
    def _generate_platform_strategy(self, biz_type, target, goals):
        platforms = self._recommend_platforms(biz_type, target)
        return {
            "recommended_platforms": platforms,
            "priority_order": [p["platform"] for p in platforms],
            "rationale": "Based on your target audience and business type"
        }
    
    def _generate_growth_strategy(self, biz_type, target, goals):
        return {
            "customer_attraction": [
                "Share behind-the-scenes content",
                "Post customer testimonials and reviews",
                "Run local promotions and special offers",
                "Use location tags and local hashtags"
            ],
            "trust_building": [
                "Respond promptly to comments and messages",
                "Share your business story and values",
                "Showcase quality and craftsmanship",
                "Highlight certifications or awards"
            ],
            "visibility_improvement": [
                "Post consistently (3-5 times per week)",
                "Use relevant hashtags (10-15 per post)",
                "Engage with local community accounts",
                "Collaborate with local influencers"
            ],
            "retention_tactics": [
                "Create loyalty programs",
                "Share exclusive offers for followers",
                "Run contests and giveaways",
                "Send personalized thank you messages"
            ]
        }

    def _generate_content_strategy(self, biz_type, target):
        return {
            "posting_frequency": {
                "Instagram": "Daily stories, 3-4 feed posts per week",
                "Facebook": "3-5 posts per week",
                "Google Business": "Weekly updates"
            },
            "optimal_times": "Weekdays 9-11 AM, 6-8 PM; Weekends 10 AM-2 PM",
            "content_mix": {
                "Educational": "30% - Tips, how-tos, industry insights",
                "Promotional": "30% - Products, offers, announcements",
                "Engagement": "40% - Questions, polls, user content"
            },
            "monthly_themes": [
                "Week 1: Product showcase",
                "Week 2: Customer stories",
                "Week 3: Behind-the-scenes",
                "Week 4: Community engagement"
            ]
        }
    
    def _generate_content_ideas(self, biz_type, products):
        return {
            "social_posts": [
                f"Showcase your {products} with high-quality photos",
                "Share customer success stories and testimonials",
                "Post 'day in the life' behind-the-scenes content",
                "Create before/after transformations",
                "Share tips related to your products/services"
            ],
            "video_ideas": [
                "Quick product demonstrations",
                "Time-lapse of your work process",
                "Customer testimonial videos",
                "Q&A sessions about your business",
                "Local community spotlights"
            ],
            "engagement_initiatives": [
                "Run a photo contest with your products",
                "Ask followers to share their experiences",
                "Create polls about preferences",
                "Host a giveaway for local followers",
                "Feature 'customer of the month'"
            ]
        }
    
    def _generate_sample_content(self, name, biz_type, products):
        return {
            "promotional_captions": [
                f"✨ Discover quality {products} at {name}! Visit us today and experience the difference. 📍 [Your Location]",
                f"🎉 Special offer this week! Get [X]% off on {products}. Limited time only! DM us to order. 💬",
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
    
    def _generate_local_expansion(self, biz_type, location):
        return {
            "community_collaborations": [
                "Partner with complementary local businesses",
                "Sponsor local events or sports teams",
                "Participate in community fairs and markets",
                "Join local business associations"
            ],
            "local_partnerships": [
                "Cross-promote with nearby businesses",
                "Create bundle offers with partners",
                "Host joint events or workshops",
                "Share each other's content"
            ],
            "referral_strategies": [
                "Implement a referral discount program",
                "Create shareable referral cards",
                "Reward customers who bring friends",
                "Build a loyalty program with benefits"
            ]
        }
    
    def _generate_action_plan(self, biz_type):
        return {
            "week_1": [
                "Set up/optimize Google Business Profile",
                "Create Instagram and Facebook business accounts",
                "Take high-quality photos of products/services",
                "Write business bio and story"
            ],
            "week_2": [
                "Post first 5 pieces of content",
                "Engage with 20 local accounts daily",
                "Respond to all comments and messages",
                "Research relevant hashtags"
            ],
            "week_3": [
                "Launch first promotional campaign",
                "Collect and post customer testimonials",
                "Create content calendar for next month",
                "Join local online community groups"
            ],
            "week_4": [
                "Analyze engagement metrics",
                "Adjust content strategy based on performance",
                "Plan collaboration with local business",
                "Set up referral program"
            ]
        }
    
    def _get_brand_personality(self, biz_type):
        personalities = {
            "bakery": "Warm, creative, and delightful",
            "restaurant": "Welcoming, flavorful, and authentic",
            "salon": "Stylish, confident, and caring",
            "retail": "Trendy, helpful, and customer-focused",
            "service": "Professional, reliable, and trustworthy"
        }
        return personalities.get(biz_type.lower(), "Authentic, professional, and community-oriented")
    
    def _recommend_platforms(self, biz_type, target):
        # Visual businesses prioritize Instagram
        visual_businesses = ["bakery", "salon", "restaurant", "retail", "cafe"]
        
        platforms = []
        
        if any(v in biz_type.lower() for v in visual_businesses):
            platforms.append({
                "platform": "Instagram",
                "priority": 1,
                "reason": "Visual content showcases your products effectively"
            })
        
        platforms.extend([
            {
                "platform": "Google Business Profile",
                "priority": 2,
                "reason": "Essential for local search visibility"
            },
            {
                "platform": "Facebook",
                "priority": 3,
                "reason": "Broad reach and community engagement"
            }
        ])
        
        return platforms
