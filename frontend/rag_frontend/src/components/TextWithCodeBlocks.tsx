import React from 'react';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { dracula } from 'react-syntax-highlighter/dist/esm/styles/prism';
import CopyCode from './CopyCode';

interface TextWithCodeBlocksProps {
  text: string;
}

const TextWithCodeBlocks: React.FC<TextWithCodeBlocksProps> = ({ text }) => {
  const parts = text.split(/```(\w*)\n([\s\S]*?)```/);

  return (
    <div className="text-with-code-blocks">
      {parts.map((part, index) => {
        if (index % 3 === 0) {
          // Regular text
          return <p key={index}>{part}</p>;
        } else if (index % 3 === 1) {
          // Language identifier
          return null;
        } else {
          // Code block with language and copy button
          const language = parts[index - 1] || 'text';
          return (
            <div key={index} style={{ position: 'relative', border: '1px solid #ddd', borderRadius: '5px', marginBottom: '1em' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: '#333', color: '#fff', padding: '0.5em', borderTopLeftRadius: '5px', borderTopRightRadius: '5px' }}>
                <span>{language}</span>
                <div style={{ display: 'flex', alignItems: 'center' }}>
                  <CopyCode code={part.trim()} />
                </div>
              </div>
              <SyntaxHighlighter
                language={language}
                style={dracula}
                customStyle={{
                  borderRadius: '0 0 4px 4px',
                  padding: '1em',
                  margin: '0',
                }}
              >
                {part.trim()}
              </SyntaxHighlighter>
            </div>
          );
        }
      })}
    </div>
  );
};

export default TextWithCodeBlocks;
