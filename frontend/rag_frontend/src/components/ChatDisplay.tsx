import React from 'react';

interface ChatDisplayProps {
  responses: { user: string; bot: string }[];
}

const ChatDisplay: React.FC<ChatDisplayProps> = ({ responses }) => {
  return (
    <div className="chat-display">
      {responses.map((res, index) => (
        <div key={index} className="message">
          <div className="user-message">
            <strong>You:</strong> {res.user}
          </div>
          <div className="bot-message">
            <strong>Bot:</strong> {res.bot}
          </div>
        </div>
      ))}
    </div>
  );
};

export default ChatDisplay;
