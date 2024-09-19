import React, { useEffect, useRef } from 'react';

interface ChatDisplayProps {
  responses: { user: string; bot: string }[];
}

const ChatDisplay: React.FC<ChatDisplayProps> = ({ responses }) => {
  const chatEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (chatEndRef.current) {
      chatEndRef.current.scrollIntoView({ behavior: 'smooth' });
    }
  }, [responses]);

  return (
    <div 
      className="chat-display" 
      style={{ overflowY: 'scroll', maxHeight: '400px', scrollbarWidth: 'none', msOverflowStyle: 'none' }} // Updated by Efaz to hide scroll bar
    >
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
      <div ref={chatEndRef} /> 
    </div>
  );
};

export default ChatDisplay;
