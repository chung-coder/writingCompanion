import axios from 'axios';
import { useEffect } from 'react';

// material-ui
import { Grid } from '@mui/material';

// project imports
import BasicTable from './BasicTable';
import Calendar from './Calendar';

import { gridSpacing } from 'store/constant';

// ==============================|| DEFAULT DASHBOARD ||============================== //

const Dashboard = ({ start_date, end_date }) => {
  const api = 'http://localhost:8000/api/';
  const token =
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI2MTUxOTU3LCJpYXQiOjE3MjM1NTk5NTcsImp0aSI6IjQ0OTAzYTc1OTU1YzRlYzdiNWVmMGU0YzVjMDc0MzI5IiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJhZG1pbiJ9.Az67tkxL0qnmUdloW4nOjKFx8Wq3UbQv51rVrd6w1rI';

  useEffect(() => {
    const instance = axios.create({
      baseURL: api,
      headers: { Authorization: `Bearer ${token}` }
    });

    instance
      .get('/weekly_diary/', { params: { start_date: start_date, end_date: end_date } })
      .then((response) => {
        console.log(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  }, [start_date]);
  return (
    <Grid container spacing={gridSpacing}>
      <Grid item xs={12}>
        <Grid container spacing={gridSpacing}>
          <Grid item xs={12} md={12} lg={4.5}>
            <Calendar />
          </Grid>
          <Grid item xs={12} md={12} lg={7.5}>
            <BasicTable />
          </Grid>
        </Grid>
      </Grid>
    </Grid>
  );
};

export default Dashboard;
