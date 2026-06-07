import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

async def analyze_free(cv_text: str, job_text: str) -> str:
    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=500,
        messages=[
            {
                "role": "user",
                "content": f"""You are a brutally honest ATS specialist powered by Claude — the only AI proven to flag real gaps instead of polishing them over.

CV:
{cv_text}

Job Description:
{job_text}

Give a FREE snapshot in exactly this format:

🤖 ATS SCORE: X/100
(One brutal sentence — why this CV would be filtered out before a human sees it)

☠️ #1 KILLER:
The single most deadly invisible mistake destroying this application. Be specific.

⚡ ONE QUICK WIN:
One specific, actionable fix they can do right now.

📊 HARSH TRUTH:
One sentence about whether this CV would realistically get an interview — no sugarcoating.

End with EXACTLY this:
━━━━━━━━━━━━━━━━━━━━
🔓 FULL ANALYSIS — $3

✅ Every ATS killer fixed
✅ CV rewritten for this exact job
✅ Missing keywords injected
✅ Cover letter included
✅ Your killer sentence for interviews

75% of CVs are rejected by robots. Is yours next?
━━━━━━━━━━━━━━━━━━━━"""
            }
        ]
    )
    return message.content[0].text

async def analyze_paid(cv_text: str, job_text: str) -> str:
    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1500,
        messages=[
            {
                "role": "user",
                "content": f"""You are an elite CV coach and ATS specialist. Be specific, honest, actionable. No fluff.

CV:
{cv_text}

Job Description:
{job_text}

Deliver the FULL paid package:

━━━━━━━━━━━━━━━━━━━━
🎯 ATS KEYWORD REPORT
━━━━━━━━━━━━━━━━━━━━
- ATS Score: X/100
- Critical missing keywords (list each one)
- Where exactly to insert each keyword

━━━━━━━━━━━━━━━━━━━━
☠️ ALL ATS KILLERS FOUND
━━━━━━━━━━━━━━━━━━━━
- Formatting problems
- Header/footer data invisible to ATS
- Visual elements ATS cannot read
- Cliché phrases to delete
- Gaps or red flags a recruiter will notice

━━━━━━━━━━━━━━━━━━━━
✏️ REWRITTEN SECTIONS
━━━━━━━━━━━━━━━━━━━━
- Professional summary (rewritten, tailored)
- 3 strongest bullet points (with numbers and impact)

━━━━━━━━━━━━━━━━━━━━
📧 COVER LETTER
━━━━━━━━━━━━━━━━━━━━
150 words. Tailored. Start with impact.

━━━━━━━━━━━━━━━━━━━━
💬 YOUR KILLER SENTENCE
━━━━━━━━━━━━━━━━━━━━
One sentence: Why YOU over everyone else?"""
            }
        ]
    )
    return message.content[0].text
