import React from 'react';
// material-ui
import SendIcon from '@mui/icons-material/Send';
import { Box, IconButton, InputBase, Paper } from '@mui/material';
import { useTheme } from '@mui/material/styles';
// project imports
import logo from 'assets/images/logo.svg';
import ChatCard from 'ui-component/chat/ChatCard';
const Chat = () => {
  const [input, setInput] = React.useState();
  const [messages, setMessages] = React.useState([]);
  const theme = useTheme();
  const handleSend = async () => {
    if (input === '') return;

    try {
      setMessages([...messages, input]);
      setInput(null);
    } catch (err) {
      console.log(err);
    }
  };

  const renderedMessages = messages.map((messages, index) => {
    return <ChatCard type="user" key={index} message={messages} />;
  });

  const handleKeyPress = (event) => {
    if (event.key === 'Enter') {
      handleSend();
      event.preventDefault();
    }
  };

  return (
    <Box
      sx={{
        display: 'flex',
        flexDirection: 'column',
        height: '100%'
      }}
    >
      <Box
        item
        marginBottom="1%"
        sx={{
          display: 'flex',
          justifyContent: 'center'
        }}
      >
        <img src={logo} alt="logo" width="100" />
      </Box>
      <Box
        item
        xs={12}
        sm={12}
        sx={{ display: 'flex', flexDirection: 'column', marginTop: 1, marginBottom: 1, flexGrow: 1, height: 400, overflowY: 'scroll' }}
      >
        {renderedMessages}
        <ChatCard type="gpt" message="聽起來你今天過得非常愉快！你可以描述一下你看的電影是什麼，這些細節能讓你的日記更生動有趣。" />
        <ChatCard
          type="user"
          message="我看了一部叫做腦筋急轉彎的電影，這是一個動畫片，在講述跟情緒有關的議題，邊看電影的同時，我還吃了媽媽買的樂事洋芋片。"
        />
        <ChatCard type="gpt" message="非常好！你已經提供了很多有趣的細節。我們可以把你的日記進一步組織起來。" />
        <ChatCard
          type="user"
          message="今天是颱風天，凱米颱風來台，所以今天跟昨天我們都放假，不用上課。這兩天我待在家裡，看電影、吃零食、玩電腦，都不用讀書，心情非常愉快。今天，我看了一部叫做《腦筋急轉彎》的動畫片，這部影片講述了跟情緒相關的議題。看電影的時候，我還享用了媽媽買的樂事洋芋片，味道真是棒極了！"
        />
        <ChatCard type="gpt" message="這樣的日記已經相當完整，但我建議可以再加一點點關於電影的感受。" />
      </Box>
      <Box item xs={12} sm={12}>
        <Paper
          component="form"
          sx={{
            border: 1.5,
            borderColor: theme.palette.grey[200],
            borderBottom: '3px ' + theme.palette.secondary.main + ' solid',
            display: 'flex',
            alignItems: 'center'
          }}
        >
          <InputBase
            fullWidth
            sx={{ ml: 1, flex: 1 }}
            placeholder="傳送訊息"
            value={input == null ? '' : input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyPress}
            inputProps={{ 'aria-label': 'message' }}
          />
          <IconButton sx={{ p: '10px', color: theme.palette.primary.main }} onClick={handleSend} aria-label="directions">
            <SendIcon fontSize="small" />
          </IconButton>
        </Paper>
      </Box>
    </Box>
  );
};

export default Chat;
