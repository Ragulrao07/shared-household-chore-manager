import { useState, useEffect } from 'react';

const API_URL = 'http://127.0.0.1:8000/api/chores/';

export default function App() {
  const [chores, setChores] = useState([]);
  const [newTitle, setNewTitle] = useState('');

  useEffect(() => {
    fetch(API_URL)
      .then((res) => res.json())
      .then((data) => setChores(data))
      .catch((err) => console.log('Backend not connected or using mock:', err));
  }, []);

  const addChore = async (e) => {
    e.preventDefault();
    if (!newTitle.trim()) return;

    try {
      const res = await fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title: newTitle, is_completed: false })
      });
      const data = await res.json();
      setChores([...chores, data]);
      setNewTitle('');
    } catch {
      setChores([...chores, { id: Date.now(), title: newTitle, is_completed: false }]);
      setNewTitle('');
    }
  };

  return (
    <div style={{ maxWidth: '600px', margin: '40px auto', fontFamily: 'sans-serif', padding: '0 16px' }}>
      <h2>Shared Household Chore Board</h2>
      <form onSubmit={addChore} style={{ display: 'flex', gap: '8px', marginBottom: '20px' }}>
        <input 
          style={{ flex: 1, padding: '8px' }}
          placeholder="New chore description..." 
          value={newTitle} 
          onChange={(e) => setNewTitle(e.target.value)} 
        />
        <button style={{ padding: '8px 16px' }} type="submit">Add Chore</button>
      </form>
      <ul style={{ listStyle: 'none', padding: 0 }}>
        {chores.length === 0 ? (
          <li style={{ color: '#888' }}>No chores yet. Add one above!</li>
        ) : (
          chores.map((chore) => (
            <li key={chore.id} style={{ padding: '10px', borderBottom: '1px solid #ddd', display: 'flex', justifyContent: 'space-between' }}>
              <span>{chore.title}</span>
              <span>{chore.is_completed ? '✅ Done' : '⏳ Pending'}</span>
            </li>
          ))
        )}
      </ul>
    </div>
  );
}