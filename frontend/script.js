// Switch to your Render URL after deployment, e.g.:
// const API_URL = 'https://digital-growth-agent.onrender.com';
const API_URL = 'http://localhost:8000';

document.getElementById('businessForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const businessData = {
        business_name: document.getElementById('businessName').value,
        business_type: document.getElementById('businessType').value,
        products_services: document.getElementById('products').value,
        location: document.getElementById('location').value,
        target_customers: document.getElementById('targetCustomers').value,
        price_range: document.getElementById('priceRange').value,
        current_presence: document.getElementById('currentPresence').value || 'None',
        goals: document.getElementById('goals').value
    };
    
    document.getElementById('loading').style.display = 'flex';
    
    try {
        const response = await fetch(`${API_URL}/generate-strategy`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(businessData)
        });
        
        if (!response.ok) throw new Error('Failed to generate strategy');
        
        const strategy = await response.json();
        displayStrategy(strategy);
        
        document.getElementById('outputSection').style.display = 'block';
        document.getElementById('outputSection').scrollIntoView({ behavior: 'smooth' });
        
    } catch (error) {
        alert('Error generating strategy. Please ensure the backend server is running.');
        console.error(error);
    } finally {
        document.getElementById('loading').style.display = 'none';
    }
});

function displayStrategy(strategy) {
    const output = document.getElementById('strategyOutput');
    
    let html = '';
    
    // Business Positioning
    html += createSection('Business Positioning', `
        <p><strong>Brand Personality:</strong> ${strategy.business_positioning.brand_personality}</p>
        <p><strong>Value Proposition:</strong> ${strategy.business_positioning.value_proposition}</p>
        <p><strong>Tone:</strong> ${strategy.business_positioning.tone}</p>
    `);
    
    // Platform Strategy
    html += createSection('Recommended Platforms', 
        strategy.platform_strategy.recommended_platforms.map(p => 
            `<div class="platform-card">
                <strong>${p.platform}</strong> (Priority ${p.priority})<br>
                <small>${p.reason}</small>
            </div>`
        ).join('')
    );
    
    // Growth Strategy
    html += createSection('Growth Strategy', `
        <h4>Customer Attraction</h4>
        <ul>${strategy.growth_strategy.customer_attraction.map(i => `<li>${i}</li>`).join('')}</ul>
        <h4>Trust Building</h4>
        <ul>${strategy.growth_strategy.trust_building.map(i => `<li>${i}</li>`).join('')}</ul>
        <h4>Visibility Improvement</h4>
        <ul>${strategy.growth_strategy.visibility_improvement.map(i => `<li>${i}</li>`).join('')}</ul>
    `);
    
    // Content Strategy
    html += createSection('Content Strategy', `
        <p><strong>Optimal Posting Times:</strong> ${strategy.content_strategy.optimal_times}</p>
        <h4>Content Mix</h4>
        <ul>
            <li>Educational: ${strategy.content_strategy.content_mix.Educational}</li>
            <li>Promotional: ${strategy.content_strategy.content_mix.Promotional}</li>
            <li>Engagement: ${strategy.content_strategy.content_mix.Engagement}</li>
        </ul>
    `);
    
    // Content Ideas
    html += createSection('Content Ideas', `
        <h4>Social Media Posts</h4>
        <ul>${strategy.content_ideas.social_posts.map(i => `<li>${i}</li>`).join('')}</ul>
        <h4>Video Ideas</h4>
        <ul>${strategy.content_ideas.video_ideas.map(i => `<li>${i}</li>`).join('')}</ul>
    `);
    
    // Sample Content
    html += createSection('Ready-to-Use Content', `
        <h4>Promotional Captions</h4>
        ${strategy.sample_content.promotional_captions.map(c => 
            `<div class="caption-box">${c}</div>`
        ).join('')}
        <h4>Suggested Hashtags</h4>
        <div class="hashtags">
            ${strategy.sample_content.hashtag_suggestions.map(h => 
                `<span class="hashtag">${h}</span>`
            ).join('')}
        </div>
    `);
    
    // 30-Day Action Plan
    html += createSection('30-Day Action Plan', `
        <h4>Week 1: Foundation</h4>
        <ul>${strategy.action_plan_30_days.week_1.map(i => `<li>${i}</li>`).join('')}</ul>
        <h4>Week 2: Content Launch</h4>
        <ul>${strategy.action_plan_30_days.week_2.map(i => `<li>${i}</li>`).join('')}</ul>
        <h4>Week 3: Campaigns</h4>
        <ul>${strategy.action_plan_30_days.week_3.map(i => `<li>${i}</li>`).join('')}</ul>
        <h4>Week 4: Optimization</h4>
        <ul>${strategy.action_plan_30_days.week_4.map(i => `<li>${i}</li>`).join('')}</ul>
    `);
    
    output.innerHTML = html;
}

function createSection(title, content) {
    return `
        <div class="strategy-section">
            <h3>${title}</h3>
            ${content}
        </div>
    `;
}
