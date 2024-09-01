import { Box, Grid, Typography } from '@mui/material';
import Stack from '@mui/material/Stack';
import { useTheme } from '@mui/material/styles';
import { Gauge } from '@mui/x-charts/Gauge';
import MainCard from 'ui-component/cards/MainCard';

const GaugeCard = ({ name, icon, num, ratio }) => {
  const theme = useTheme();
  return (
    <MainCard>
      <Box>
        <Grid container>
          <Grid item container>
            <Grid item xs={6}>
              <Grid container spacing={1} marginBottom={3}>
                <Grid item>{icon}</Grid>
                <Grid item>
                  <Typography
                    variant="h4"
                    sx={{
                      color: theme.palette.grey[500]
                    }}
                  >
                    {name}
                  </Typography>
                </Grid>
              </Grid>
              <Typography variant="h1">{num} 篇</Typography>
            </Grid>
            <Grid item xs={6}>
              <Stack direction={{ xs: 'column', md: 'row' }} spacing={{ xs: 1, md: 3 }}>
                <Gauge width={150} height={150} value={ratio} text={({ value }) => `${value} %`} />
              </Stack>
            </Grid>
          </Grid>
        </Grid>
      </Box>
    </MainCard>
  );
};

export default GaugeCard;
