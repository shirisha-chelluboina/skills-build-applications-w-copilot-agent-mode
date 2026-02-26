import React, { useEffect, useState } from 'react';

const Teams = () => {
  const [teams, setTeams] = useState([]);
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  const endpoint = codespace
    ? `https://${codespace}-8000.app.github.dev/api/teams/`
    : 'http://localhost:8000/api/teams/';

  useEffect(() => {
    console.log('Teams endpoint:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = Array.isArray(data) ? data : data.results || [];
        setTeams(results);
        console.log('Fetched teams:', results);
      })
      .catch(err => console.error('Error fetching teams:', err));
  }, [endpoint]);

  return (
    <div className="container mt-4">
      <h2>Teams</h2>
      <ul className="list-group">
        {teams.map((team, idx) => (
          <li key={team.id || idx} className="list-group-item">
            {team.name} {team.description ? `- ${team.description}` : ''}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Teams;
