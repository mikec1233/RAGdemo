import React, { useEffect, useRef} from "react";
import TextWithCodeBlocks from "./TextWithCodeBlocks";

interface ChatDisplayProps {
  responses: { user: string; bot: string }[];
  username: string;
}

const ChatDisplay: React.FC<ChatDisplayProps> = ({ responses, username }) =>  {
  const chatEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (chatEndRef.current) {
      chatEndRef.current.scrollIntoView({ behavior: 'smooth' });
    }
  }, [responses]);

  return (
    <div className="chat-display"  style={{ overflowY: 'scroll', scrollbarWidth: 'none', msOverflowStyle: 'none' }}>
      {responses.map((res, index) => (
        <div key={index} className="message">
          <div className="user-message-container">
            <div className="user-message">
              <strong>{username}:</strong> {res.user}
            </div>
          </div>
          <div className="bot-message-container">
              <TextWithCodeBlocks text={res.bot} />
          </div>
        </div>
      ))}
      <div ref={chatEndRef} />
    </div>
  );
};

export default ChatDisplay;
