import React, { useState, useEffect } from "react";
import ChatForm from "./components/ChatForm";
import ChatDisplay from "./components/ChatDisplay";
import HistoryButton from './components/HistoryButton';
import { submitQuery } from "./api/ChatService";
import "./App.css";

const App: React.FC = () => {
  const [username, setUsername] = useState<string | null>(null); // Track the username
  const [responses, setResponses] = useState<{ user: string; bot: string }[]>(
    [],
  );

  // Handler for chat submission
  const handleChatSubmit = async (queryText: string) => {
    if (!username) return; // Ensure username is set

    // Immediately add the user's query to the chat with a placeholder for the bot's response
    setResponses((prev) => [
      ...prev,
      { user: queryText, bot: "..." }, // Bot response placeholder as "..."
    ]);

    try {
      // Fetch the bot's response
      const botResponse = await submitQuery(queryText);

      // Update the response once the bot's answer is received
      setResponses((prev) =>
        prev.map((resp, index) =>
          index === prev.length - 1
            ? { ...resp, bot: botResponse || "No response" } // Replace the placeholder with actual response
            : resp,
        ),
      );
    } catch (error) {
      // Handle errors, if bot response fails
      setResponses((prev) =>
        prev.map((resp, index) =>
          index === prev.length - 1
            ? { ...resp, bot: "Error: Unable to get response." }
            : resp,
        ),
      );
    }
  };

  // Handler for username submission
  const handleUsernameSubmit = (name: string) => {
    setUsername(name); // Store the username in state
  };

  const handleButtonClick = () => {
    alert("Button clicked!");
  };

  return (
    <div className="app-container">
      {/* <h1 className="title">OpenVal® Chat</h1> */}

      {/* Top-left button */}
      <HistoryButton onClick={handleButtonClick} label="History" />
      
        {!username ? (
          <div className="username-container">
          <div className="username-form">
          
            <h2>Please enter your username</h2>
            <input
              type="text"
              placeholder="Enter username"
              onKeyDown={(e) => {
                if (e.key === "Enter" && e.currentTarget.value.trim()) {
                  handleUsernameSubmit(e.currentTarget.value.trim());
                }
              }}
            />
            </div>
          </div>
        ) : (
          <div className="chat-container">
          <>
            <ChatDisplay responses={responses} username={username} />
            <ChatForm onSubmit={handleChatSubmit} />
          </>
          </div>
        )}
      </div>
  );
};

export default App;
