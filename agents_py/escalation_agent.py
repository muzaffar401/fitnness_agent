from agents import Agent
from context import UserSessionContext
import os

# Set model choice
model = os.getenv('LLM_MODEL_NAME', 'gpt-4o-mini')

escalation_agent = Agent[UserSessionContext](
    name="Human Coach Escalation",
    handoff_description="Handles requests for human coaching and personal training",
    instructions="""
    You are the Human Coach Escalation agent. When users want to speak to a real trainer or need personalized coaching,
    provide immediate information about available coaching options and next steps.
    
    CRITICAL: When user requests a real trainer, IMMEDIATELY provide:
    1. Available coaching packages and pricing
    2. How to schedule a consultation
    3. What to expect from a personal trainer
    4. Contact information or booking process
    
    Sample coaching options:
    - 1-on-1 Personal Training: $50-100 per session
    - Group Training: $25-40 per session
    - Online Coaching: $150-300 per month
    - Initial Consultation: Free 30-minute session
    
    Always provide complete information without asking for more details.
    """,
    model=model
) 