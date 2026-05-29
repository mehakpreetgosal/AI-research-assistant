from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def summarize(results, topic):

    combined_text = ""

    for r in results:
        combined_text += f"""
        Title: {r['title']}
        Content: {r['content']}
        """

    prompt = f"""
    Topic: {topic}

    Analyze the following research data and provide:

    1. Summary
    2. Key Insights
    3. Important Trends

    Data:
    {combined_text}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
