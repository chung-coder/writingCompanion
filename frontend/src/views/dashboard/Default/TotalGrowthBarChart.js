import axios from 'axios';

import PropTypes from 'prop-types';
import { useEffect, useState } from 'react';
import { useSelector } from 'react-redux';

// material-ui
import { Grid, MenuItem, TextField, Typography } from '@mui/material';
import { useTheme } from '@mui/material/styles';

// third-party
import ApexCharts from 'apexcharts';
import Chart from 'react-apexcharts';

// project imports
import { gridSpacing } from 'store/constant';
import MainCard from 'ui-component/cards/MainCard';
import SkeletonTotalGrowthBarChart from 'ui-component/cards/Skeleton/TotalGrowthBarChart';

// chart data
import chartData from './chart-data/total-growth-bar-chart';

const status = [
  {
    value: 'year',
    label: '2024年'
  }
];

// ==============================|| DASHBOARD DEFAULT - TOTAL GROWTH BAR CHART ||============================== //

const TotalGrowthBarChart = () => {
  const [value, setValue] = useState('year');
  const [isLoading, setIsLoading] = useState(false);

  const theme = useTheme();
  const customization = useSelector((state) => state.customization);

  const { navType } = customization;
  const { primary } = theme.palette.text;
  const darkLight = theme.palette.dark.light;
  const grey200 = theme.palette.grey[200];
  const grey500 = theme.palette.grey[500];

  const primaryMain = theme.palette.primary.main;
  const primaryDark = theme.palette.primary.dark;
  const secondaryMain = theme.palette.secondary.main;
  const secondaryLight = theme.palette.secondary.light;
  const api = 'http://localhost:8000/api/';
  const token =
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI4OTkzOTQ0LCJpYXQiOjE3MjY0MDE5NDQsImp0aSI6IjkzZTFmNjBlY2FjZjRmY2JhMTdlOWI1MDc2ZWEzNzhmIiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJhZG1pbiJ9.cKjXkDwIW4QpETYMUdFDH1IZ2RLirHLidICw72G1MDU';

  useEffect(() => {
    const instance = axios.create({
      baseURL: api,
      headers: { Authorization: `Bearer ${token}` }
    });
    instance
      .get('/word-count-statistics/')
      .then((response) => {
        const wordCountStatistics = Object.values(response.data.word_count_statistics);

        const newChartData = {
          ...chartData.options,
          series: [
            {
              name: '總字數',
              data: wordCountStatistics
            }
          ],
          colors: [primaryMain],
          xaxis: {
            labels: {
              style: {
                colors: [primary, primary, primary, primary, primary, primary, primary, primary, primary, primary, primary, primary]
              }
            }
          },
          yaxis: {
            labels: {
              style: {
                colors: [primary]
              }
            }
          },
          grid: {
            borderColor: grey200
          },
          tooltip: {
            theme: 'light'
          },
          legend: {
            labels: {
              colors: grey500
            }
          }
        };
        ApexCharts.exec(`bar-chart`, 'updateOptions', newChartData);
        setIsLoading(false);
      })
      .catch((error) => {
        console.error('Error fetching word count statistics:', error);
        setIsLoading(false);
      });
  }, [navType, primaryMain, primaryDark, secondaryMain, secondaryLight, primary, darkLight, grey200, grey500]);

  return (
    <>
      {isLoading ? (
        <SkeletonTotalGrowthBarChart />
      ) : (
        <MainCard>
          <Grid container spacing={gridSpacing}>
            <Grid item xs={12}>
              <Grid container alignItems="center" justifyContent="space-between">
                <Grid item>
                  <Grid container direction="column" spacing={1}>
                    <Grid item>
                      <Typography variant="h3">日記字數統計</Typography>
                    </Grid>
                  </Grid>
                </Grid>
                <Grid item>
                  <TextField id="standard-select-currency" select value={value} onChange={(e) => setValue(e.target.value)}>
                    {status.map((option) => (
                      <MenuItem key={option.value} value={option.value}>
                        {option.label}
                      </MenuItem>
                    ))}
                  </TextField>
                </Grid>
              </Grid>
            </Grid>
            <Grid item xs={12}>
              <Chart {...chartData} />
            </Grid>
          </Grid>
        </MainCard>
      )}
    </>
  );
};

TotalGrowthBarChart.propTypes = {
  isLoading: PropTypes.bool
};

export default TotalGrowthBarChart;
