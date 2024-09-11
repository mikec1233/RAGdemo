import React, { useState } from 'react';
import { DefaultApi, Configuration } from './api-client'; // Adjust path accordingly
import { SubmitQueryRequest } from './api-client'; // Adjust path accordingly

const App: React.FC = () => {
  const [queryText, setQueryText] = useState('');
  const [response, setResponse] = useState<any>(null);

  // Define the base URL in the configuration
  const config = new Configuration({
    basePath: 'http://localhost:8000',  // Set the correct base URL
  });
  const api = new DefaultApi(config); // Pass the configuration when instantiating DefaultApi

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    const requestBody: SubmitQueryRequest = {
      queryText: queryText,
      userId: '1234', // Example user ID
    };

    try {
      const result = await api.submitQueryEndpointSubmitQueryPost({
        submitQueryRequest: requestBody,
      });
      setResponse(result);
    } catch (error) {
      console.error('Error submitting query:', error);
    }
  };

  return (
    <div>
      <h1>Submit a Query</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="queryText">Query Text</label>
        <input
          type="text"
          id="queryText"
          value={queryText}
          onChange={(e) => setQueryText(e.target.value)}
        />
        <button type="submit">Submit Query</button>
      </form>

      {response && (
        <div>
          <h2>Response</h2>
          <pre>{JSON.stringify(response, null, 2)}</pre>
        </div>
      )}
    </div>
  );
};

export default App;
