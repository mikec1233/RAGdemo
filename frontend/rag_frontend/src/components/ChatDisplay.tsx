import React, { useEffect, useRef } from "react";
import TextWithCodeBlocks from "./TextWithCodeBlocks";

interface ChatDisplayProps {
  responses: { user: string; bot: string }[];
  username: string;
}

const ChatDisplay: React.FC<ChatDisplayProps> = ({ responses, username }) => {
  const chatEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (chatEndRef.current) {
      chatEndRef.current.scrollIntoView({ behavior: 'smooth' });
    }
  }, [responses]);

  return (
    <div className="chat-display" style={{ overflowY: 'scroll', scrollbarWidth: 'none', msOverflowStyle: 'none' }}>
      {responses.map((res, index) => (
        <div key={index} className="message">
          <div className="user-message-container">
            <div className="user-message">
              <strong style={{ fontWeight: 'bold', color: '#000' }}>{username}:</strong> {/* User's name is bold */}
              <span style={{ fontWeight: 'normal'}}> {res.user}</span> {/* User input text */}
            </div>
          </div>
          <div className="bot-message-container code-block-wrapper">
            <TextWithCodeBlocks text={res.bot} />
          </div>
        </div>
      ))}
      <div ref={chatEndRef} />
    </div>
  );
};

export default ChatDisplay;
