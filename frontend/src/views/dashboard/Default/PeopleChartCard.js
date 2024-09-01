import { Typography } from '@mui/material';
import { useTheme } from '@mui/material/styles';
import { BarChart } from '@mui/x-charts/BarChart';
// import { useState } from 'react';

import MainCard from 'ui-component/cards/MainCard';

const chartSetting = {
  xAxis: [
    {
      label: '篇數'
    }
  ],
  height: 240
};

const valueFormatter = (value) => `${value}篇`;

function PeopleChartCard({ total, self_count, friend_count, family_count, other_count }) {
  let dataset = [
    {
      num: self_count,
      month: '自己'
    },
    {
      num: friend_count,
      month: '朋友'
    },
    {
      num: family_count,
      month: '家人'
    },
    {
      num: other_count,
      month: '其他'
    }
  ];

  const theme = useTheme();
  return (
    <MainCard>
      <Typography
        variant="h4"
        sx={{
          color: theme.palette.grey[500]
        }}
        marginBottom={1}
      >
        書寫對象
      </Typography>
      <Typography variant="h3">總篇數 {total}</Typography>
      <BarChart
        dataset={dataset}
        yAxis={[{ scaleType: 'band', dataKey: 'month' }]}
        series={[{ color: theme.palette.primary.main, dataKey: 'num', valueFormatter }]}
        layout="horizontal"
        {...chartSetting}
      />
    </MainCard>
  );
}

export default PeopleChartCard;
