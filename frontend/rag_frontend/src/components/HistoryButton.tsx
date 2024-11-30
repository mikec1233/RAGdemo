import React, { useState } from "react";


interface HistoryButtonProps {
  onClick: () => void;
  label: string;
}

const HistoryButton: React.FC<HistoryButtonProps> = ({ onClick, label }) => {
  const [open, setOpen] = useState(false);

  const toggleSidebar = () => {
    setOpen(!open);
    onClick();
  };

  return (
    <div>
      <div className={`sidebar ${open ? "sidebar-open" : "sidebar-closed"}`}>
        <div className="menu-item">History Option 1</div>
        <div className="menu-item">History Option 2</div>
        <div className="menu-item">History Option 3</div>
      </div>
      <button
        className={`history-button ${open ? "button-open" : "button-closed"}`}
        onClick={toggleSidebar}
      >
        {open ? "Close Sidebar" : "☰ Open Sidebar"}
      </button>
    </div>
  );
};

export default HistoryButton;
