import os
import json
from openai import OpenAI

# Groq is OpenAI-compatible
client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

class AIService:
    @staticmethod
    def generate_interview_questions(job_title: str, job_description: str) -> list:
        prompt = f"""
        Generate 3 technical interview questions for a {job_title}.
        Context: {job_description}
        Return ONLY a JSON list of strings. No markdown, no backticks.
        """
        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                response_format={"type": "json_object"}
            )
            return json.loads(response.choices[0].message.content).get("questions", [])
        except Exception as e:
            print(f"Groq Error: {e}")
            return ["Tell me about your experience.", "What are your strengths?", "Describe a challenge."]

    @staticmethod
    def evaluate_individual_answer(question: str, answer: str) -> dict:
        prompt = f"""
        Grade this answer: {answer} for question: {question}.
        Return JSON with 'score' (1-10) and 'feedback'.
        """
        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                response_format={"type": "json_object"}
            )
            return json.loads(response.choices[0].message.content)
        except Exception:
            return {"score": 5, "feedback": "Evaluation failed."}