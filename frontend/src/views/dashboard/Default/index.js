import { useState } from 'react';
import dayjs from 'dayjs';

// material-ui
import { Grid } from '@mui/material';

// project imports
import BasicTable from './BasicTable';
import Calendar from './Calendar';

import { gridSpacing } from 'store/constant';

// ==============================|| DEFAULT DASHBOARD ||============================== //

const Dashboard = () => {
  const init_start = dayjs().startOf('week').format('YYYY-MM-DD');
  const init_end = dayjs().endOf('week').format('YYYY-MM-DD');

  const [startDate, setStartDate] = useState(init_start);
  const [endDate, setEndDate] = useState(init_end);

  const handleData = (start_date, end_date) => {
    setStartDate(start_date);
    setEndDate(end_date);
  };

  return (
    <Grid container spacing={gridSpacing}>
      <Grid item xs={12}>
        <Grid container spacing={gridSpacing}>
          <Grid item xs={12} md={12} lg={4.5}>
            <Calendar onData={handleData} />
          </Grid>
          <Grid item xs={12} md={12} lg={7.5}>
            <BasicTable startOfWeek={startDate} endOfWeek={endDate} />
          </Grid>
        </Grid>
      </Grid>
    </Grid>
  );
};

export default Dashboard;
