import React, { useState, useEffect } from "react";
import ChatForm from "./components/ChatForm";
import ChatDisplay from "./components/ChatDisplay";
import { submitQuery, getPreviousConversations } from "./api/ChatService";
import "./App.css";

const App: React.FC = () => {
  const [username, setUsername] = useState<string | null>(null); // Track the username
  const [responses, setResponses] = useState<{ user: string; bot: string }[]>(
    [],
  );

  // Fetch previous conversations when the username is set
  useEffect(() => {
    if (username) {
      (async () => {
        try {
          const previousConversations =
            await getPreviousConversations(username);
          if (previousConversations.length > 0) {
            // Map the previous conversations using correct camelCase fields and handle undefined answerText
            const mappedConversations = previousConversations.map((conv) => ({
              user: conv.queryText, // Corrected to use camelCase
              bot: conv.answerText ?? "No response", // Handle undefined by using 'No response'
            }));
            setResponses(mappedConversations.reverse());
          }
        } catch (error) {
          console.error("Error fetching previous conversations:", error);
        }
      })();
    }
  }, [username]); // This effect runs when the username is updated

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
      const botResponse = await submitQuery(username, queryText);

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

  return (
    <div className="app-container">
      <h1 className="title">OpenVal® Chat</h1>
      <div className="chat-container">
        {!username ? (
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
        ) : (
          <>
            <ChatDisplay responses={responses} username={username} />
            <ChatForm onSubmit={handleChatSubmit} />
          </>
        )}
      </div>
    </div>
  );
};

export default App;
