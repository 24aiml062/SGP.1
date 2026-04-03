"""
Hybrid AI Digital Growth Agent
Uses Hugging Face Inference API (Mistral-7B) for content generation
with rule-based fallback when the API key is not set.
"""

import json
import os
import re
import requests
from typing import Dict, Any
from huggingface_hub import InferenceClient

HF_MODEL = "Qwen/Qwen2.5-7B-Instruct"


class DigitalGrowthAgent:
    """
    Hybrid agent:
    - Hugging Face (Mistral-7B) for creative, personalised content
    - Rule-based logic for platform recommendations and structure
    """

    def __init__(self):
        self.use_ai = False
        self._hf = None

        api_key = os.getenv("HF_API_KEY")
        if api_key and not api_key.startswith("hf_your"):
            self._hf = InferenceClient(api_key=api_key)
            self.use_ai = True
            print("✓ Digital Growth Agent initialized with AI (HuggingFace Qwen2.5-7B)")
        else:
            print("⚠️  HF_API_KEY not set — running in rule-based mode")
            print("✓ Digital Growth Agent initialized (rule-based mode)")

    # ------------------------------------------------------------------ #
    # Public entry point                                                   #
    # ------------------------------------------------------------------ #

    def generate_strategy(self, business_data: Dict[str, Any]) -> Dict[str, Any]:
        name             = business_data.get("business_name", "")
        biz_type         = business_data.get("business_type", "")
        products         = business_data.get("products_services", "")
        location         = business_data.get("location", "")
        target           = business_data.get("target_customers", "")
        goals            = business_data.get("goals", "")
        price_range      = business_data.get("price_range", "")
        current_presence = business_data.get("current_presence", "None")

        # Always rule-based
        platform_strategy = self._generate_platform_strategy(biz_type, target, goals)
        local_expansion   = self._generate_local_expansion(biz_type, location)
        action_plan       = self._generate_action_plan(biz_type)

        # AI-powered creative content
        if self.use_ai:
            try:
                ai = self._call_hf(name, biz_type, products, location,
                                   target, goals, price_range, current_presence)
                return {
                    "business_positioning": ai.get("business_positioning",
                        self._generate_positioning(name, biz_type, products, target)),
                    "platform_strategy":    platform_strategy,
                    "growth_strategy":      ai.get("growth_strategy",
                        self._generate_growth_strategy(biz_type, target, goals)),
                    "content_strategy":     ai.get("content_strategy",
                        self._generate_content_strategy(biz_type, target)),
                    "content_ideas":        ai.get("content_ideas",
                        self._generate_content_ideas(biz_type, products)),
                    "sample_content":       ai.get("sample_content",
                        self._generate_sample_content(name, biz_type, products)),
                    "local_expansion":      local_expansion,
                    "action_plan_30_days":  action_plan,
                }
            except Exception as e:
                print(f"⚠️  HF generation failed: {e} — falling back to rules")

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
    # Hugging Face call                                                    #
    # ------------------------------------------------------------------ #

    def _call_hf(self, name, biz_type, products, location,
                 target, goals, price_range, current_presence) -> Dict[str, Any]:

        user_prompt = (
            f"Create a digital marketing strategy JSON for:\n"
            f"Business: {name}, Type: {biz_type}, Products: {products}\n"
            f"Location: {location}, Customers: {target}, Goals: {goals}\n\n"
            "Return ONLY this JSON structure (no extra text):\n"
            '{"business_positioning":{"brand_personality":"...","value_proposition":"...","tone":"..."},'
            '"growth_strategy":{"customer_attraction":["tip1","tip2","tip3"],"trust_building":["tip1","tip2","tip3"]},'
            '"sample_content":{"promotional_captions":["caption1 with emoji","caption2 with emoji","caption3 with emoji"],'
            '"hashtag_suggestions":["#tag1","#tag2","#tag3","#tag4","#tag5","#tag6","#tag7","#tag8"]}}'
        )

        response = self._hf.chat.completions.create(
            model=HF_MODEL,
            messages=[
                {"role": "system", "content": "You are an expert digital marketing strategist. Always respond with valid JSON only. No explanation, no markdown."},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=1200,
            temperature=0.7,
        )
        text = response.choices[0].message.content or ""

        # Extract first valid JSON object using brace matching
        start = text.find("{")
        if start == -1:
            raise ValueError(f"No JSON found in HF response: {text[:200]}")

        depth = 0
        for i, ch in enumerate(text[start:], start):
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    return json.loads(text[start:i + 1])

        raise ValueError("Unmatched braces in HF response")

    # ------------------------------------------------------------------ #
    # Rule-based helpers                                                   #
    # ------------------------------------------------------------------ #

    def _generate_positioning(self, name, biz_type, products, target):
        return {
            "brand_personality": self._get_brand_personality(biz_type),
            "value_proposition": f"Quality {products} for {target} in your local community",
            "ideal_customer": target,
            "tone": "Friendly, authentic, and community-focused",
        }

    def _generate_platform_strategy(self, biz_type, target, goals):
        return {
            "recommended_platforms": self._recommend_platforms(biz_type, target),
            "priority_order": [p["platform"] for p in self._recommend_platforms(biz_type, target)],
            "rationale": "Based on your target audience and business type",
        }

    def _recommend_platforms(self, biz_type, target):
        visual = ["bakery", "salon", "restaurant", "retail", "cafe", "food", "beauty"]
        platforms = []
        if any(v in biz_type.lower() for v in visual):
            platforms.append({"platform": "Instagram", "priority": 1,
                               "reason": "Visual content showcases your products effectively"})
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
                "Send personalised thank you messages",
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
