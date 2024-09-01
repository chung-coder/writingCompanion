import axios from 'axios';
import { useState, useEffect } from 'react';
import { Avatar, Box, Button, Card, CardMedia, FilledInput, FormControl, Grid, InputLabel, Typography } from '@mui/material';
import MuiTypography from '@mui/material/Typography';
import { gridSpacing } from 'store/constant';
import SubCard from 'ui-component/cards/SubCard';
import AnimateButton from 'ui-component/extended/AnimateButton';
import PasswordInput from 'views/sample-page/PasswordInput';

// import MainCard from 'ui-component/cards/MainCard';
import background from 'assets/images/background.png';
import burceMars from 'assets/images/bruce-mars.jpg';

function SamplePage() {
  const [student_info, setStudentInfo] = useState({});

  const api = 'http://localhost:8000/api/';
  const token =
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI2MTUxOTU3LCJpYXQiOjE3MjM1NTk5NTcsImp0aSI6IjQ0OTAzYTc1OTU1YzRlYzdiNWVmMGU0YzVjMDc0MzI5IiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJhZG1pbiJ9.Az67tkxL0qnmUdloW4nOjKFx8Wq3UbQv51rVrd6w1rI';

  useEffect(() => {
    const instance = axios.create({
      baseURL: api,
      headers: { Authorization: `Bearer ${token}` }
    });

    instance
      .get('/student_info/')
      .then((response) => {
        setStudentInfo(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);
  return (
    <Grid>
      <div style={{ position: 'relative', marginBottom: 80 }}>
        <CardMedia component="img" height="345" image={background} alt="background" />
        <Card
          sx={{
            position: 'absolute',
            left: '50%',
            bottom: '0',
            width: '90%',
            transform: 'translate(-50%,50%)',
            backdropFilter: `saturate(200%) blur(30px)`,
            backgroundColor: 'white',
            boxShadow: 1,
            py: 2,
            px: 2
          }}
        >
          <Grid container spacing={3} alignItems="center">
            <Grid item>
              <Avatar src={burceMars} alt="profile-image" variant="rounded" size="xl" shadow="sm" />
            </Grid>
            <Grid item>
              <Box height="100%" mt={0.5} lineHeight={1}>
                <Typography variant="h5" fontWeight="medium">
                  {student_info.user_name}
                </Typography>
                <Typography color="text" fontWeight="medium">
                  {student_info.email}
                </Typography>
              </Box>
            </Grid>
          </Grid>
        </Card>
      </div>
      <Grid container spacing={gridSpacing}>
        <Grid item xs={12} sm={6}>
          <SubCard title="學生檔案">
            <Grid container direction="column" spacing={1}>
              <Grid item>
                <MuiTypography variant="body1" gutterBottom>
                  姓名：{student_info.user_name}
                </MuiTypography>
              </Grid>
              <Grid item>
                <MuiTypography variant="body1" gutterBottom>
                  性別：{student_info.gender}
                </MuiTypography>
              </Grid>
              <Grid item>
                <MuiTypography variant="body1" gutterBottom>
                  電子郵件：{student_info.email}
                </MuiTypography>
              </Grid>
              <Grid item>
                <MuiTypography variant="body1" gutterBottom>
                  班級：{student_info.class_name}
                </MuiTypography>
              </Grid>
              <Grid item>
                <MuiTypography variant="body1" gutterBottom>
                  導師：{student_info.teacher_name}
                </MuiTypography>
              </Grid>
            </Grid>
          </SubCard>
        </Grid>
        <Grid item xs={12} sm={6}>
          <SubCard title="帳號修改">
            <Grid container direction="column" spacing={1}>
              <Grid item>
                <FormControl
                  disabled
                  sx={{
                    width: '100%',
                    marginBottom: '2%',
                    '& .css-e6zq6f-MuiInputBase-input-MuiFilledInput-input': { background: 'white' }
                  }}
                  variant="filled"
                >
                  <InputLabel shrink htmlFor="bootstrap-input">
                    帳號
                  </InputLabel>
                  <FilledInput placeholder={student_info.user_name} id="input-name" />
                </FormControl>
              </Grid>
              <Grid item>
                <FormControl
                  sx={{
                    width: '100%',
                    marginBottom: '2%',
                    '& .css-e6zq6f-MuiInputBase-input-MuiFilledInput-input': { background: 'white' }
                  }}
                  variant="filled"
                >
                  <InputLabel shrink htmlFor="bootstrap-input">
                    電子郵件
                  </InputLabel>
                  <FilledInput placeholder={student_info.email} id="input-email" />
                </FormControl>
              </Grid>
              <Grid item>
                <PasswordInput name="輸入舊密碼" />
              </Grid>
              <Grid item>
                <PasswordInput name="輸入新密碼" />
              </Grid>
              <Grid item>
                <PasswordInput name="新密碼確認" />
              </Grid>
            </Grid>
            <Box sx={{ mt: 2 }}>
              <AnimateButton>
                <Button disableElevation fullWidth borderRadius="8" size="medium" type="submit" variant="contained" color="primary">
                  確認修改
                </Button>
              </AnimateButton>
            </Box>
          </SubCard>
        </Grid>
      </Grid>
    </Grid>
  );
}

export default SamplePage;
