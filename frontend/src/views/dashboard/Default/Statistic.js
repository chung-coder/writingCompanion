import axios from 'axios';
import { useEffect, useState } from 'react';

// material-ui
import { Grid } from '@mui/material';
import { useTheme } from '@mui/material/styles';

// project imports
import InsertDriveFileOutlinedIcon from '@mui/icons-material/InsertDriveFileOutlined';
import PeopleAltOutlinedIcon from '@mui/icons-material/PeopleAltOutlined';
import { gridSpacing } from 'store/constant';
import DiaryTable from './DiaryTable';
import GaugeCard from './GaugeCard';
import MoodChartCard from './MoodChartCard';
import PeopleChartCard from './PeopleChartCard';
import TotalGrowthBarChart from './TotalGrowthBarChart';

// ==============================|| DEFAULT DASHBOARD ||============================== //
const Statistic = () => {
  const theme = useTheme();
  const [isLoading, setLoading] = useState(true);
  useEffect(() => {
    setLoading(false);
  }, []);
  const [diaryType, setDiaryType] = useState({});
  const [totalDiary, setTotalDiary] = useState(0);
  const [ratioDiary, setRatioDiary] = useState(0);
  const [targetCounts, setTargetCounts] = useState(0);
  const [moodCounts, setMoodCounts] = useState(0);
  const [favoriteDiary, setFavoriteDiary] = useState([]);
  const api = 'http://localhost:8000/api/';
  const token =
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI2MTUxOTU3LCJpYXQiOjE3MjM1NTk5NTcsImp0aSI6IjQ0OTAzYTc1OTU1YzRlYzdiNWVmMGU0YzVjMDc0MzI5IiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJhZG1pbiJ9.Az67tkxL0qnmUdloW4nOjKFx8Wq3UbQv51rVrd6w1rI';

  useEffect(() => {
    const instance = axios.create({
      baseURL: api,
      headers: { Authorization: `Bearer ${token}` }
    });

    instance
      .get('/count_diaryType/')
      .then((response) => {
        setDiaryType(response.data);
        setTotalDiary(response.data.total);
        setRatioDiary(Math.round((response.data.assistance_diary_counter / response.data.total) * 100));
        setTargetCounts(response.data.target_counts);
        setMoodCounts(response.data.mood);
      })
      .catch((error) => {
        console.log(error);
      });

    instance
      .get('/favorite_diary/')
      .then((response) => {
        setFavoriteDiary([...favoriteDiary, response.data]);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);
  return (
    <Grid container spacing={gridSpacing}>
      <Grid item lg={8} xs={12}>
        <Grid container spacing={gridSpacing}>
          <Grid item lg={6} md={6} sm={6} xs={12}>
            <GaugeCard
              name="自行撰寫"
              num={diaryType.assistance_diary_counter}
              ratio={ratioDiary}
              icon={<InsertDriveFileOutlinedIcon sx={{ color: theme.palette.grey[500] }} />}
            />
          </Grid>
          <Grid item lg={6} md={6} sm={6} xs={12}>
            <GaugeCard
              name="互動模式"
              num={diaryType.interaction_diary_counter}
              ratio={100 - ratioDiary}
              icon={<PeopleAltOutlinedIcon sx={{ color: theme.palette.grey[500] }} />}
            />
          </Grid>
          <Grid item xs={12} md={12}>
            <TotalGrowthBarChart isLoading={isLoading} />
          </Grid>
        </Grid>
      </Grid>
      <Grid item lg={4} xs={12}>
        <Grid item lg={12} md={12} sm={12} xs={12}>
          <Grid container spacing={gridSpacing}>
            <Grid item sm={6} xs={12} md={6} lg={12}>
              <PeopleChartCard
                total={totalDiary}
                self_count={targetCounts.self_count}
                friend_count={targetCounts.friend_count}
                family_count={targetCounts.family_count}
                other_count={targetCounts.other_count}
              />
            </Grid>
            <Grid item sm={6} xs={12} md={6} lg={12}>
              <MoodChartCard
                total={totalDiary}
                normal={moodCounts.normal}
                very_good={moodCounts.very_good}
                good={moodCounts.good}
                bad={moodCounts.bad}
                very_bad={moodCounts.very_bad}
              />
            </Grid>
          </Grid>
        </Grid>
      </Grid>
      <Grid item lg={12} xs={12}>
        <DiaryTable favoriteDiary={favoriteDiary} />
      </Grid>
    </Grid>
  );
};

export default Statistic;
