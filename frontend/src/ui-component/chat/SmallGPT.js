import SendIcon from '@mui/icons-material/Send';
import { Box, Card, IconButton, InputBase, Paper } from '@mui/material';
import logo from 'assets/images/logo.svg';
import React from 'react';
const SmallGPT = () => {
  const [input, setInput] = React.useState();
  const handleSend = async () => {
    if (input === '') return;

    try {
      console.log(input);
      setInput('');
    } catch (err) {
      console.log(err);
    }
  };
  return (
    <Card variant="outlined" sx={{ width: '25%', minWidth: 300, padding: 2, position: 'fixed', bottom: '11%', right: '5%' }}>
      <Box p={1}>
        <img src={logo} alt="logo" width="100" />
      </Box>
      <Box>
        <Paper
          component="form"
          sx={{
            border: 1.5,
            borderColor: 'grey.200',
            borderBottom: '3px ' + 'secondary.main' + ' solid',
            display: 'flex',
            alignItems: 'center'
          }}
        >
          <InputBase
            fullWidth
            multiline
            rows={3}
            sx={{ ml: 1, flex: 1 }}
            placeholder="傳送訊息"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            inputProps={{ 'aria-label': 'message' }}
          />
          <IconButton sx={{ p: '10px', color: 'primary.main' }} onClick={handleSend} aria-label="directions">
            <SendIcon fontSize="small" />
          </IconButton>
        </Paper>
      </Box>
    </Card>
  );
};

export default SmallGPT;
