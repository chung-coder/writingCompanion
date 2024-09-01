import SmartToyIcon from '@mui/icons-material/SmartToy';
import Fab from '@mui/material/Fab';
import { useState } from 'react';
import SmallGPT from './SmallGPT';

const ChatBot = () => {
  const [showForm, setShowForm] = useState(false);

  const handleShowForm = () => {
    setShowForm(!showForm);
  };
  return (
    <div>
      <Fab variant="extended" size="medium" color="primary" onClick={handleShowForm} sx={{ position: 'fixed', bottom: '5%', right: '5%' }}>
        <SmartToyIcon sx={{ mr: 1 }} />
        輔助模式
      </Fab>
      {showForm && <SmallGPT />}
    </div>
  );
};

export default ChatBot;
