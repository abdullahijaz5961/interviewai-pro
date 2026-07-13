import React, { useState } from 'react';
import axios from 'axios';

// Ensure your backend is running at this URL
const API = axios.create({ baseURL: 'http://localhost:8000/api/v1' });

export default function App() {
  const [jobTitle, setJobTitle] = useState('');
  const [session, setSession] = useState(null);
  const [answers, setAnswers] = useState({});
  const [result, setResult] = useState(null);

  const startInterview = async () => {
    try {
      const res = await API.post('/interviews/generate', { job_title: jobTitle, job_description: "General software role" });
      setSession(res.data);
    } catch (err) { alert("Backend error: " + err.message); }
  };

  const submitAnswers = async () => {
    const payload = { answers: session.qa_pairs.map(qa => ({ qa_id: qa.id, user_answer: answers[qa.id] })) };
    const res = await API.post(`/interviews/${session.id}/submit`, payload);
    setResult(res.data);
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h1>InterviewAI Dashboard</h1>
      {!session ? (
        <div>
          <input value={jobTitle} onChange={e => setJobTitle(e.target.value)} placeholder="Target Job Title" />
          <button onClick={startInterview}>Start Interview</button>
        </div>
      ) : !result ? (
        <div>
          {session.qa_pairs.map(qa => (
            <div key={qa.id}>
              <p>{qa.question_text}</p>
              <textarea onChange={e => setAnswers({...answers, [qa.id]: e.target.value})} />
            </div>
          ))}
          <button onClick={submitAnswers}>Submit</button>
        </div>
      ) : <div>Score: {result.overall_score}% - {result.message}</div>}
    </div>
  );
}