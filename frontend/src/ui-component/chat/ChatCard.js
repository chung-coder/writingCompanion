import SmartToyIcon from '@mui/icons-material/SmartToy';
import { Box, Typography } from '@mui/material';
import Avatar from '@mui/material/Avatar';

const ChatCard = ({ type, message }) => {
  if (type == 'user') {
    return (
      <Box
        p={1.5}
        sx={{
          alignSelf: 'end',
          marginBottom: 1,
          backgroundColor: 'primary.dark',
          borderRadius: 3,
          width: 'max-content',
          marginRight: '1%'
        }}
        maxWidth="50%"
      >
        <Typography variant="body2" sx={{ color: 'white' }}>
          {message}
        </Typography>
      </Box>
    );
  } else if (type == 'gpt') {
    return (
      <Box
        display="flex"
        flexDirection="row"
        sx={{
          marginBottom: 1
        }}
        maxWidth="50%"
      >
        <Avatar sx={{ marginRight: 1, alignSelf: 'center', bgcolor: 'grey.100' }}>
          <SmartToyIcon color="primary" />
        </Avatar>
        <Box
          p={1.5}
          sx={{
            backgroundColor: 'grey.200',
            borderRadius: 3,
            width: 'max-content'
          }}
        >
          <Typography variant="body2">{message}</Typography>
        </Box>
      </Box>
    );
  }
};

export default ChatCard;
