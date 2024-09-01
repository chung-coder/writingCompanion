import { Typography } from '@mui/material';
import { useTheme } from '@mui/material/styles';
import { BarChart } from '@mui/x-charts/BarChart';
import MainCard from 'ui-component/cards/MainCard';

const chartSetting = {
  xAxis: [
    {
      label: '篇數'
    }
  ],
  height: 280
};

const valueFormatter = (value) => `${value}篇`;

function BarChartCard({ total, normal, very_good, good, bad, very_bad }) {
  let dataset = [
    {
      num: normal,
      month: '普通'
    },
    {
      num: good,
      month: '好'
    },
    {
      num: very_bad,
      month: '很差'
    },
    {
      num: very_good,
      month: '很好'
    },
    {
      num: bad,
      month: '差'
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
        心情
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

export default BarChartCard;
