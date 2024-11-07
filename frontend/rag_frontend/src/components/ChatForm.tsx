import React, { useState } from "react";

interface ChatFormProps {
  onSubmit: (queryText: string) => void;
}

const ChatForm: React.FC<ChatFormProps> = ({ onSubmit }) => {
  const [queryText, setQueryText] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (queryText.trim()) {
      onSubmit(queryText.trim()); // Pass the query to parent
      setQueryText(""); // Clear the input field after submission
    }
  };

  return (
    <form className="chat-form" onSubmit={handleSubmit}>
      <input
        type="text"
        id="queryText"
        className="input-field"
        placeholder="Enter your query"
        value={queryText}
        onChange={(e) => setQueryText(e.target.value)}
        autoComplete="off"
      />
      <button type="submit" className="submit-btn">
        Submit
      </button>
    </form>
  );
};

export default ChatForm;
