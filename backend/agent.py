"""
Hybrid AI Digital Growth Agent
Combines rule-based logic with Anthropic Claude for content generation
"""

import json
import os
from typing import Dict, Any

# Try to import Anthropic - graceful fallback if not available
try:
    import anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False
    print("⚠️  Anthropic not installed. Install with: pip install anthropic")


class DigitalGrowthAgent:
    """
    Hybrid AI Agent:
    - Anthropic Claude for creative content and personalized strategies
    - Rule-based logic for platform recommendations and structure
    """

    def __init__(self):
        self.use_ai = False
        self.client = None

        if ANTHROPIC_AVAILABLE:
            api_key = os.getenv("ANTHROPIC_API_KEY")
            if api_key:
                try:
                    self.client = anthropic.Anthropic(api_key=api_key)
                    self.use_ai = True
                    print("✓ Digital Growth Agent initialized with AI (Anthropic Claude)")
                except Exception as e:
                    print(f"⚠️  Anthropic initialization failed: {e}")
                    print("✓ Digital Growth Agent initialized (rule-based mode)")
            else:
                print("⚠️  ANTHROPIC_API_KEY not found in environment")
                print("✓ Digital Growth Agent initialized (rule-based mode)")
        else:
            print("✓ Digital Growth Agent initialized (rule-based mode)")

    def generate_strategy(self, business_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate comprehensive digital marketing strategy.
        HYBRID: AI for creative content, rules for structure.
        """
        name             = business_data.get("business_name", "")
        biz_type         = business_data.get("business_type", "")
        products         = business_data.get("products_services", "")
        location         = business_data.get("location", "")
        target           = business_data.get("target_customers", "")
        goals            = business_data.get("goals", "")
        price_range      = business_data.get("price_range", "")
        current_presence = business_data.get("current_presence", "None")

        # RULE-BASED: always deterministic
        platform_strategy = self._generate_platform_strategy(biz_type, target, goals)
        local_expansion   = self._generate_local_expansion(biz_type, location)
        action_plan       = self._generate_action_plan(biz_type)

        # AI-POWERED: creative content via Claude
        if self.use_ai:
            try:
                ai_content = self._generate_ai_content(
                    name, biz_type, products, location,
                    target, goals, price_range, current_presence
                )
                return {
                    "business_positioning": ai_content.get(
                        "business_positioning",
                        self._generate_positioning(name, biz_type, products, target)
                    ),
                    "platform_strategy": platform_strategy,
                    "growth_strategy": ai_content.get(
                        "growth_strategy",
                        self._generate_growth_strategy(biz_type, target, goals)
                    ),
                    "content_strategy": ai_content.get(
                        "content_strategy",
                        self._generate_content_strategy(biz_type, target)
                    ),
                    "content_ideas": ai_content.get(
                        "content_ideas",
                        self._generate_content_ideas(biz_type, products)
                    ),
                    "sample_content": ai_content.get(
                        "sample_content",
                        self._generate_sample_content(name, biz_type, products)
                    ),
                    "local_expansion": local_expansion,
                    "action_plan_30_days": action_plan,
                }
            except Exception as e:
                print(f"⚠️  AI generation failed: {e} — using rule-based fallback")

        # FALLBACK: pure rule-based
        return {
            "business_positioning": self._generate_positioning(name, biz_type, products, target),
            "platform_strategy":    platform_strategy,
            "growth_strategy":      self._generate_growth_strategy(biz_type, target, goals),
            "content_strategy":     self._generate_content_strategy(biz_type, target),
            "content_ideas":        self._generate_content_ideas(biz_type, products),
            "sample_content":       self._generate_sample_content(name, biz_type, products),
            "local_expansion":      local_expansion,
            "action_plan_30_days":  action_plan,
        }

    # ------------------------------------------------------------------ #
    # AI GENERATION (Anthropic Claude)                                     #
    # ------------------------------------------------------------------ #

    def _generate_ai_content(
        self,
        name: str, biz_type: str, products: str, location: str,
        target: str, goals: str, price_range: str, current_presence: str
    ) -> Dict[str, Any]:
        """Call Anthropic Claude and return parsed JSON strategy."""

        prompt = f"""You are an expert digital marketing strategist for small local businesses.

Generate a comprehensive digital marketing strategy for:

Business Name: {name}
Business Type: {biz_type}
Products/Services: {products}
Location: {location}
Target Customers: {target}
Business Goals: {goals}
Price Range: {price_range}
Current Digital Presence: {current_presence}

Return ONLY valid JSON with this exact structure (no markdown, no extra text):

{{
  "business_positioning": {{
    "brand_personality": "5-7 word description",
    "value_proposition": "compelling one-sentence statement",
    "ideal_customer": "detailed customer profile",
    "tone": "recommended communication tone"
  }},
  "growth_strategy": {{
    "customer_attraction": ["tip 1", "tip 2", "tip 3", "tip 4"],
    "trust_building": ["tip 1", "tip 2", "tip 3", "tip 4"],
    "visibility_improvement": ["tip 1", "tip 2", "tip 3", "tip 4"],
    "retention_tactics": ["tip 1", "tip 2", "tip 3", "tip 4"]
  }},
  "content_strategy": {{
    "posting_frequency": {{
      "Instagram": "frequency",
      "Facebook": "frequency",
      "Google Business": "frequency"
    }},
    "optimal_times": "best posting times",
    "content_mix": {{
      "Educational": "30% - description",
      "Promotional": "30% - description",
      "Engagement": "40% - description"
    }},
    "monthly_themes": ["theme 1", "theme 2", "theme 3", "theme 4"]
  }},
  "content_ideas": {{
    "social_posts": ["idea 1", "idea 2", "idea 3", "idea 4", "idea 5"],
    "video_ideas": ["idea 1", "idea 2", "idea 3", "idea 4", "idea 5"],
    "engagement_initiatives": ["idea 1", "idea 2", "idea 3", "idea 4"]
  }},
  "sample_content": {{
    "promotional_captions": ["caption with emojis", "caption with emojis", "caption with emojis"],
    "engagement_captions": ["caption with emojis", "caption with emojis", "caption with emojis"],
    "hashtag_suggestions": ["#tag1", "#tag2", "#tag3", "#tag4", "#tag5", "#tag6", "#tag7", "#tag8"]
  }}
}}"""

        # Call Claude — using the Messages API
        message = self.client.messages.create(
            model="claude-3-haiku-20240307",   # fast + affordable
            max_tokens=2048,
            messages=[{"role": "user", "content": prompt}]
        )

        raw = message.content[0].text.strip()

        # Strip markdown code fences if Claude wraps the JSON
        if raw.startswith("```"):
            raw = raw.split("```")[1]
            if raw.startswith("json"):
                raw = raw[4:]

        return json.loads(raw)

    # ------------------------------------------------------------------ #
    # RULE-BASED HELPERS                                                   #
    # ------------------------------------------------------------------ #

    def _generate_positioning(self, name, biz_type, products, target):
        return {
            "brand_personality": self._get_brand_personality(biz_type),
            "value_proposition": f"Quality {products} for {target} in your local community",
            "ideal_customer": target,
            "tone": "Friendly, authentic, and community-focused",
        }

    def _generate_platform_strategy(self, biz_type, target, goals):
        platforms = self._recommend_platforms(biz_type, target)
        return {
            "recommended_platforms": platforms,
            "priority_order": [p["platform"] for p in platforms],
            "rationale": "Based on your target audience and business type",
        }

    def _recommend_platforms(self, biz_type, target):
        visual = ["bakery", "salon", "restaurant", "retail", "cafe", "food", "beauty"]
        platforms = []
        if any(v in biz_type.lower() for v in visual):
            platforms.append({
                "platform": "Instagram",
                "priority": 1,
                "reason": "Visual content showcases your products effectively",
            })
        platforms.extend([
            {"platform": "Google Business Profile", "priority": 2,
             "reason": "Essential for local search visibility"},
            {"platform": "Facebook", "priority": 3,
             "reason": "Broad reach and community engagement"},
        ])
        return platforms

    def _generate_growth_strategy(self, biz_type, target, goals):
        return {
            "customer_attraction": [
                "Share behind-the-scenes content",
                "Post customer testimonials and reviews",
                "Run local promotions and special offers",
                "Use location tags and local hashtags",
            ],
            "trust_building": [
                "Respond promptly to comments and messages",
                "Share your business story and values",
                "Showcase quality and craftsmanship",
                "Highlight certifications or awards",
            ],
            "visibility_improvement": [
                "Post consistently (3-5 times per week)",
                "Use relevant hashtags (10-15 per post)",
                "Engage with local community accounts",
                "Collaborate with local influencers",
            ],
            "retention_tactics": [
                "Create loyalty programs",
                "Share exclusive offers for followers",
                "Run contests and giveaways",
                "Send personalized thank you messages",
            ],
        }

    def _generate_content_strategy(self, biz_type, target):
        return {
            "posting_frequency": {
                "Instagram": "Daily stories, 3-4 feed posts per week",
                "Facebook": "3-5 posts per week",
                "Google Business": "Weekly updates",
            },
            "optimal_times": "Weekdays 9-11 AM, 6-8 PM; Weekends 10 AM-2 PM",
            "content_mix": {
                "Educational": "30% - Tips, how-tos, industry insights",
                "Promotional": "30% - Products, offers, announcements",
                "Engagement": "40% - Questions, polls, user content",
            },
            "monthly_themes": [
                "Week 1: Product showcase",
                "Week 2: Customer stories",
                "Week 3: Behind-the-scenes",
                "Week 4: Community engagement",
            ],
        }

    def _generate_content_ideas(self, biz_type, products):
        return {
            "social_posts": [
                f"Showcase your {products} with high-quality photos",
                "Share customer success stories and testimonials",
                "Post 'day in the life' behind-the-scenes content",
                "Create before/after transformations",
                "Share tips related to your products/services",
            ],
            "video_ideas": [
                "Quick product demonstrations",
                "Time-lapse of your work process",
                "Customer testimonial videos",
                "Q&A sessions about your business",
                "Local community spotlights",
            ],
            "engagement_initiatives": [
                "Run a photo contest with your products",
                "Ask followers to share their experiences",
                "Create polls about preferences",
                "Host a giveaway for local followers",
            ],
        }

    def _generate_sample_content(self, name, biz_type, products):
        return {
            "promotional_captions": [
                f"✨ Discover quality {products} at {name}! Visit us today. 📍",
                f"🎉 Special offer this week on {products}. Limited time only! DM us. 💬",
                f"💯 Why choose {name}? Quality, service, and community. ⭐",
            ],
            "engagement_captions": [
                f"❓ What's your favourite {products}? Tell us below! 👇",
                f"🤔 Quick poll: Option A or Option B? Vote below! 🗳️",
                f"💭 Tag us in your photos for a chance to be featured. 📸",
            ],
            "hashtag_suggestions": [
                f"#{biz_type.replace(' ', '')}",
                "#LocalBusiness", "#ShopLocal", "#SmallBusiness",
                "#CommunityFirst",
                f"#{products.split()[0] if products else 'Quality'}",
                "#SupportLocal", "#SmallBusinessLove",
            ],
        }

    def _generate_local_expansion(self, biz_type, location):
        return {
            "community_collaborations": [
                "Partner with complementary local businesses",
                "Sponsor local events or sports teams",
                "Participate in community fairs and markets",
                "Join local business associations",
            ],
            "local_partnerships": [
                "Cross-promote with nearby businesses",
                "Create bundle offers with partners",
                "Host joint events or workshops",
                "Share each other's content",
            ],
            "referral_strategies": [
                "Implement a referral discount program",
                "Create shareable referral cards",
                "Reward customers who bring friends",
                "Build a loyalty program with benefits",
            ],
        }

    def _generate_action_plan(self, biz_type):
        return {
            "week_1": [
                "Set up/optimize Google Business Profile",
                "Create Instagram and Facebook business accounts",
                "Take high-quality photos of products/services",
                "Write business bio and story",
            ],
            "week_2": [
                "Post first 5 pieces of content",
                "Engage with 20 local accounts daily",
                "Respond to all comments and messages",
                "Research relevant hashtags",
            ],
            "week_3": [
                "Launch first promotional campaign",
                "Collect and post customer testimonials",
                "Create content calendar for next month",
                "Join local online community groups",
            ],
            "week_4": [
                "Analyse engagement metrics",
                "Adjust content strategy based on performance",
                "Plan collaboration with local business",
                "Set up referral program",
            ],
        }

    def _get_brand_personality(self, biz_type):
        personalities = {
            "bakery":     "Warm, creative, and delightful",
            "restaurant": "Welcoming, flavorful, and authentic",
            "salon":      "Stylish, confident, and caring",
            "retail":     "Trendy, helpful, and customer-focused",
            "service":    "Professional, reliable, and trustworthy",
            "cafe":       "Cozy, friendly, and inviting",
            "food":       "Fresh, passionate, and quality-driven",
        }
        for key, personality in personalities.items():
            if key in biz_type.lower():
                return personality
        return "Authentic, professional, and community-oriented"
