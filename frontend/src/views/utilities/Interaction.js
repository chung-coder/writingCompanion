import PropTypes from 'prop-types';

// material-ui
import { Box, Card, Grid } from '@mui/material';
import SubCard from 'ui-component/cards/SubCard';
// project imports
import { gridSpacing } from 'store/constant';
import Chat from 'views/utilities/Chat';
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
  <Grid container spacing={gridSpacing} sx={{ height: '100%' }}>
    <Grid item xs={12} sm={6}>
      <SubCard sx={{ height: '100%' }}>
        <Diary />
      </SubCard>
    </Grid>
    <Grid item xs={12} sm={6}>
      <Card sx={{ p: 2.5, height: '100%' }}>
        <Chat />
      </Card>
    </Grid>
  </Grid>
);

export default UtilitiesShadow;
