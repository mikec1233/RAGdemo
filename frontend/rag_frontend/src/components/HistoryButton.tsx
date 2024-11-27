import React, { useState } from "react";

interface HistoryButtonProps {
  onClick: () => void;
  label: string;
}

const HistoryButton: React.FC<HistoryButtonProps> = ({ onClick, label }) => {
  // State to control the visibility of the dropdown menu
  const [isDropdownVisible, setIsDropdownVisible] = useState(false);

  // Toggle dropdown visibility when the button is clicked
  const handleButtonClick = () => {
    setIsDropdownVisible(!isDropdownVisible);  // Toggle the visibility of the dropdown
    onClick(); // Trigger the alert or any other action
  };

  return (
    <div className="history-container">
      <button className="history-button" onClick={handleButtonClick}>
        {label}
      </button>

      {/* Conditionally render the dropdown menu */}
      {isDropdownVisible && (
        <div className="dropdown-menu">
          <div className="menu-item">History Option 1</div>
          <div className="menu-item">History Option 2</div>
          <div className="menu-item">History Option 3</div>
        </div>
      )}
    </div>
  );
};

export default HistoryButton;
