def build_prompt(resume: str, company: str, role: str, research: str, recipient_name: str = "") -> str:
    return f"""
You are an expert recruiter and career coach.

Your task is to write a highly personalized, realistic cold email for a job seeker.

Rules:
- First line must be: "SUBJECT: <subject line under 8 words>"
- The subject line must NOT describe a technical topic, feature, or problem. It must sound like a real subject line a person types when emailing about a job — short and personal, e.g. "Quick note from a CS grad", "Regarding opportunities at {company}", "Following up — CS student here". Do not name any technical concept, project detail, or engineering term in the subject line.
- Then a blank line, then the email body only.
- Keep the email body under 120 words (excluding signature).
- If a recipient name is provided below, greet them by name. If not, skip the greeting entirely and open directly with the specific hook — never write "Hi [Name]" or any placeholder.
- If the research below contains trustworthy, specific information, reference ONE concrete fact from it (product, launch, metric, quote) — never a vague theme. If the research says no trustworthy information was found, do NOT mention any recent company update — write the opening based on the company's known domain/industry instead, without fabricating specifics.
- Explain in one sentence why the candidate's experience is useful for the problem or direction described in the research.
- Pick ONLY the ONE most relevant project from the resume. Mention its outcome/impact in one sentence — do NOT list tech stack, frameworks, or tools unless one specific tool is the actual hook.
- Avoid generic phrases entirely: "resonated with me", "I've been following", "aligns with my passion", "excited about the opportunity", "solid foundation in". Rephrase concretely instead.
- Sound like a specific person wrote this to this specific company today — not a template with company name swapped in.
- Never invent facts, projects, or skills not present in the input.
- End with a short, direct ask for a brief conversation about opportunities on their team (e.g. a 10-15 minute call) or being pointed to the right person. Keep it to one sentence, casual and low-pressure — vary your phrasing naturally, don't reuse the same sentence structure every time.
- After the ask, add a sign-off on a new line: "Best,\\n<candidate name>\\n<candidate email if present in resume>\\n<candidate phone if present in resume>" — extract these directly from the resume, do not invent them.
- Output ONLY the subject line and email body. No explanations or markdown.

Target Company:
{company}

Target Role:
{role if role else "Not specified"}

Recipient Name:
{recipient_name if recipient_name else "Not provided"}

Company Research:
{research}

Candidate Resume:
{resume}
"""