import React from 'react';

interface ChatDisplayProps {
  responses: { user: string; bot: string }[];
  username: string;
}

const ChatDisplay: React.FC<ChatDisplayProps> = ({ responses, username }) => {
  return (
    <div className="chat-display">
      {responses.map((res, index) => (
        <div key={index} className="message">
          <div className="user-message-container">
          <div className="user-message">
            <strong>{username}:</strong> {res.user}
          </div>
        </div>
          <div className="bot-message-container">
          <div className="bot-message">
            {res.bot}
            </div>
          </div>
        </div>
      ))}
    </div>
  );
};

export default ChatDisplay;
