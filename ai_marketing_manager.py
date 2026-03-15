import datetime

# Simulation of AI-generated images for a client (e.g., for Social Media)
ai_content = [
    {"file": "product_01.jpg", "topic": "modern coffee machine", "platform": "Instagram"},
    {"file": "lifestyle_02.jpg", "topic": "person with laptop in a cafe", "platform": "LinkedIn"},
    {"file": "ads_03.jpg", "topic": "close-up of coffee beans", "platform": "Facebook"},
    {"file": "product_03.jpg", "topic": "modern art shot", "platform": "Instagram"},
    {"file": "product_04.jpg", "topic": "video production advertisement", "platform": "Facebook"}
]

def generate_marketing_plan(data):
    print("--- AI MARKETING ASSISTANT ACTIVE ---")
    today = datetime.date.today()
    file_name = f"content_plan_{today}.txt"
    
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(f"MARKETING CONTENT PLAN - DATE: {today}\n")
        f.write("="*45 + "\n\n")
        
        for item in data:
            # AI Simulation: Automatic generation of hashtags and captions
            # Removing spaces for hashtags
            hashtags = f"#{item['topic'].replace(' ', '')} #AIart #MarketingAutomation"
            caption = f"Social media post for {item['platform']} regarding {item['topic']}."
            
            f.write(f"FILE: {item['file']}\n")
            f.write(f"CAPTION: {caption}\n")
            f.write(f"HASHTAGS: {hashtags}\n")
            f.write("-" * 25 + "\n")
            
            print(f"Processing plan for: {item['file']}...")

    return f"Plan successfully exported to {file_name}!"

# Running the manager
status = generate_marketing_plan(ai_content)
print(status)
