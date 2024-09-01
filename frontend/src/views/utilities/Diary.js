// material-ui
import StarBorderIcon from '@mui/icons-material/StarBorder';
import { Card, Grid, TextField } from '@mui/material';
import Divider from '@mui/material/Divider';
import IconButton from '@mui/material/IconButton';
import dayjs from 'dayjs';
// project imports
import { gridSpacing } from 'store/constant';

const date = dayjs().format('YYYY 年 MM 月 DD 日');

const Diary = () => {
  return (
    <Card>
      <Grid container marginBottom="1%">
        <Grid item xs={10} sm={11}>
          <TextField
            id="diary-title"
            label={date}
            placeholder="請輸入日記標題"
            variant="standard"
            InputLabelProps={{
              shrink: true
            }}
            InputProps={{
              disableUnderline: true
            }}
            sx={{
              '& .css-1b4blxj-MuiFormLabel-root-MuiInputLabel-root': {
                fontSize: '20px',
                fontWeight: 'bold'
              },
              '& .css-1q8wryf-MuiInputBase-input-MuiInput-input': {
                fontSize: '22.5px'
              },
              '& .css-1y2btu-MuiInputBase-root-MuiInput-root::after': {
                borderBottomColor: '#F59E0B'
              },
              '& .css-1b4blxj-MuiFormLabel-root-MuiInputLabel-root.Mui-focused': {
                color: '#F59E0B'
              }
            }}
          />
        </Grid>
        <Grid item xs={2} sm={0.1}>
          <IconButton aria-label="save" color="secondary">
            <StarBorderIcon />
          </IconButton>
        </Grid>
        <Grid item xs={12} sm={12}>
          <Divider
            sx={{
              borderColor: '#F59E0B',
              borderWidth: '1px'
            }}
          />
        </Grid>
      </Grid>
      <Grid container spacing={gridSpacing}>
        <Grid item xs={12} sm={12}>
          <TextField
            id="outlined-multiline-static"
            placeholder="請在此寫下日記內容......"
            multiline
            variant="standard"
            color="secondary"
            InputProps={{
              disableUnderline: true
            }}
            sx={{
              fontWeight: 'bold',
              fontSize: '20px',
              width: '100%',
              '& .css-1997j60-MuiInputBase-input-MuiOutlinedInput-input': {
                background: '#fff'
              }
            }}
          />
        </Grid>
      </Grid>
    </Card>
  );
};

export default Diary;
