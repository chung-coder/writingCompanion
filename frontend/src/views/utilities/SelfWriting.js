import PropTypes from 'prop-types';

// material-ui
import { Box, Card } from '@mui/material';
// project imports
import MainCard from 'ui-component/cards/MainCard';
import ChatBot from 'ui-component/chat/ChatBot';
import Diary from 'views/utilities/Diary';

// ===============================|| SHADOW BOX ||=============================== //

const ShadowBox = ({ shadow }) => (
  <Card sx={{ mb: 3, boxShadow: shadow }}>
    <Box
      sx={{
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        py: 4.5,
        bgcolor: 'primary.light',
        color: 'grey.800'
      }}
    >
      <Box sx={{ color: 'inherit' }}>boxShadow: {shadow}</Box>
    </Box>
  </Card>
);

ShadowBox.propTypes = {
  shadow: PropTypes.string.isRequired
};

// ============================|| UTILITIES SHADOW ||============================ //

const UtilitiesShadow = () => (
  <MainCard sx={{ height: '100%' }}>
    <Diary />
    <ChatBot />
  </MainCard>
);

export default UtilitiesShadow;
