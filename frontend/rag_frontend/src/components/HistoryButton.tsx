import React from 'react';

interface HistoryButtonProps {
  onClick: () => void;
  label: string;
}

const HistoryButton: React.FC<HistoryButtonProps> = ({ onClick, label }) => {
  return (
    <button className="history-button" onClick={onClick}>
      {label}
    </button>
  );
};

export default HistoryButton;
