import React, { useEffect, useState } from 'react';

function App() {
  const [agents, setAgents] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/agents/list')
      .then(res => res.json())
      .then(data => setAgents(data));
  }, []);

  return (
    <div>
      <h2>HacknoverRMM Dashboard</h2>
      <ul>
        {agents.map((a, i) => (
          <li key={i}>{a.hostname} - {a.ip}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
