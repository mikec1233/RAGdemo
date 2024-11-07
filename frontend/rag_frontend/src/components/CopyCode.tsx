import React, { useState } from 'react';
import { FaRegCopy, FaCheck } from 'react-icons/fa';

interface CopyCodeProps {
  code: string;
}

const CopyCode: React.FC<CopyCodeProps> = ({ code }) => {
  const [isCopied, setIsCopied] = useState(false);

  const handleCopy = () => {
    navigator.clipboard.writeText(code).then(() => {
      setIsCopied(true);
      setTimeout(() => setIsCopied(false), 2000); // Reset to "Copy code" after 2 seconds
    }).catch((err) => {
      console.error('Failed to copy code:', err);
    });
  };

  return (
    <button
      onClick={handleCopy}
      style={{
        display: 'flex',
        alignItems: 'center',
        position: 'absolute',
        top: '0.5em',
        right: '0.5em',
        background: 'none',
        border: 'none',
        cursor: 'pointer',
        color: '#fff',
      }}
      title="Copy code"
    >
      {isCopied ? (
        <>
          <FaCheck size={16} style={{ marginRight: '0.5em' }} />
          <span style={{ fontSize: '0.9em' }}>Copied!</span>
        </>
      ) : (
        <>
          <FaRegCopy size={16} style={{ marginRight: '0.5em' }} />
          <span style={{ fontSize: '0.9em' }}>Copy code</span>
        </>
      )}
    </button>
  );
};

export default CopyCode;
