import React from 'react';

const ProgressBar = ({ progress }) => {
  return (
    <div className="h-4 w-full bg-gray-200 rounded-full overflow-hidden">
      <div
        className="h-full bg-blue-500 transition-all duration-500"
        style={{ width: `${progress}%` }}
      ></div>
    </div>
  );
};

export default ProgressBar;