import React from 'react';
import { CodeBlock, dracula } from 'react-code-blocks';

interface TextWithCodeBlocksProps {
  text: string;
}

const TextWithCodeBlocks: React.FC<TextWithCodeBlocksProps> = ({ text }) => {
  // Split the text into parts: normal text and code blocks
  const parts = text.split(/```(\w*)\n([\s\S]*?)```/);

  return (
    <div>
      {parts.map((part, index) => {
        if (index % 3 === 0) {
          // Regular text
          return <p key={index}>{part}</p>;
        } else if (index % 3 === 1) {
          // Language identifier; can be used for dynamic rendering
          return null;
        } else {
          // Code block
          return (
            <CodeBlock
              key={index}
              text={part.trim()}
              language="r" // Replace this with `{parts[index - 1]}` for dynamic language detection
              showLineNumbers={false}
              theme={dracula}
            />
          );
        }
      })}
    </div>
  );
};

export default TextWithCodeBlocks;
