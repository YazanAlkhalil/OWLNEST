import React, { useState, useRef, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { sendMessage, toggleChat, addUserMessage } from '../RTK/slices/chatSlice';

const ChatComponent = () => {
  const [input, setInput] = useState('');
  const { messages, isOpen, isLoading, error } = useSelector((state) => state.chat);
  const dispatch = useDispatch();
  const chatEndRef = useRef(null);

  const handleSend = () => {
    if (input.trim()) {
      dispatch(addUserMessage(input));
      dispatch(sendMessage(input));
      setInput('');
    }
  };

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  if (!isOpen) return null;

  return (
    <div className="fixed bottom-10 right-10 w-96 h-[70vh] bg-white border border-gray-300 rounded-lg shadow-lg flex flex-col">
      <div className="flex justify-between items-center p-4 border-b">
        <h2 className="font-semibold">Strix Assistant</h2>
        <button onClick={() => dispatch(toggleChat())} className="text-gray-500 hover:text-gray-700">
          <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      </div>
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {messages.map((msg, index) => (
          <div key={index} className={`flex ${msg.type === 'user' ? 'justify-end' : 'justify-start'}`}>
            <div className={`max-w-3/4 p-2 rounded-lg ${msg.type === 'user' ? 'bg-blue-500 text-white' : 'bg-gray-200'}`}>
              {msg.content}
            </div>
          </div>
        ))}
        {isLoading && <div className="text-center">Thinking...</div>}
        {error && <div className="text-red-500 text-center">{error}</div>}
        <div ref={chatEndRef} />
      </div>
      <div className="p-4 border-t flex">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && handleSend()}
          className="flex-1 border rounded-l-lg p-2"
          placeholder="Type a message..."
        />
        <button onClick={handleSend} className="bg-blue-500 text-white p-2 rounded-r-lg" disabled={isLoading}>
          Send
        </button>
      </div>
    </div>
  );
};

export default ChatComponent;