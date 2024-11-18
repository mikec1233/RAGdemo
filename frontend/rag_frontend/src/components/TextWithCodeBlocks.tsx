import React from 'react';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { dracula } from 'react-syntax-highlighter/dist/esm/styles/prism';
import CopyCode from './CopyCode';

interface TextWithCodeBlocksProps {
  text: string;
}

const TextWithCodeBlocks: React.FC<TextWithCodeBlocksProps> = ({ text }) => {
  const parts = text.split(/(`[^`]+`|```[\s\S]*?```)/);

  return (
    <div className="text-with-code-blocks">
      {parts.map((part, index) => {
        if (part.startsWith('```') && part.endsWith('```')) {
          // Handle code blocks
          const languageMatch = part.match(/```({(\w+)}|(\w*))/);
          const language = languageMatch ? languageMatch[2] || languageMatch[3] || 'text' : 'text';
          const codeContent = part.replace(/```({[\w\s]+}|[\w]*)\n/, '').replace(/```$/, '');

          return (
            <div key={index} style={{ position: 'relative', border: '1px solid #ddd', borderRadius: '5px', marginBottom: '1em' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: '#333', color: '#fff', padding: '0.5em', borderTopLeftRadius: '5px', borderTopRightRadius: '5px' }}>
                <span>{language}</span>
                <div style={{ display: 'flex', alignItems: 'center' }}>
                  <CopyCode code={codeContent.trim()} />
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
                {codeContent.trim()}
              </SyntaxHighlighter>
            </div>
          );
        } else if (part.startsWith('`') && part.endsWith('`')) {
          // Handle inline code
          return (
            <code key={index} style={{ backgroundColor: '#f0f0f0', padding: '2px 4px', borderRadius: '3px' }}>
              {part.slice(1, -1)} {/* Remove the backticks */}
            </code>
          );
        } else if (part.trim() !== '') {
          // Regular text
          return <span key={index}>{part}</span>;
        } else {
          return null; // Skip empty parts
        }
      })}
    </div>
  );
};

export default TextWithCodeBlocks;
