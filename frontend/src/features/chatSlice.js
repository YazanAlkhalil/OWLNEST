import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI("AIzaSyBgfnI-pvWxjAGo28Y_k7d5vW0fZF55UYI");
const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });
      const chat = model.startChat({
        history:[
          {
            role: "user",
            parts: [{ text: "Pretend you're a friendly AI assistant named Strix and stay in character for each response." }],
          },
          {
            role: "model",
            parts: [{ text: "Hello! I'm your friendly AI assistant. How can I help you today?" }],
          },
        ],
        generationConfig: {
          maxOutputTokens: 500,
        },
      });
export const sendMessage = createAsyncThunk(
  'chat/sendMessage',
  async (message, { getState, rejectWithValue }) => {
    try {
      const { history } = getState().chat;
      
      const result = await chat.sendMessage(message);
      const response = await result.response;
      const responseText = response.text();
      
      return {
          user: message, ai: responseText 
      };
    } catch (error) {
      console.error('Error sending message to Gemini:', error);
      return rejectWithValue(error.message);
    }
  }
);

const chatSlice = createSlice({
  name: 'chat',
  initialState: {
    messages: [{
      type: `ai`, content: `Hello, My name is Strix I am your AI assistant,
    how can i help you` }

    ],
    isOpen: false,
    isLoading: false,
    error: null,
    
  },
  reducers: {
    toggleChat: (state) => {
      state.isOpen = !state.isOpen;
    },
    addUserMessage: (state, action) => {
      state.messages.push({ type: 'user', content: action.payload });
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(sendMessage.pending, (state) => {
        state.isLoading = true;
        state.error = null;
      })
      .addCase(sendMessage.fulfilled, (state, action) => {
        state.isLoading = false;
        state.messages.push({ type: 'ai', content: action.payload.ai });
      })
      .addCase(sendMessage.rejected, (state, action) => {
        state.isLoading = false;
        state.error = action.payload;
      });
  },
});

export const { toggleChat, addUserMessage } = chatSlice.actions;
export default chatSlice.reducer;