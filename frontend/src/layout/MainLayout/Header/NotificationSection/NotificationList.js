// material-ui
import { useTheme, styled } from '@mui/material/styles';
import {
  Avatar,
  Button,
  Card,
  CardContent,
  Chip,
  Divider,
  Grid,
  List,
  ListItem,
  ListItemAvatar,
  ListItemSecondaryAction,
  ListItemText,
  Stack,
  Typography
} from '@mui/material';

// assets
import { IconBrandTelegram, IconBuildingStore, IconMailbox, IconPhoto } from '@tabler/icons-react';
import User1 from 'assets/images/users/user-round.svg';

// styles
const ListItemWrapper = styled('div')(({ theme }) => ({
  cursor: 'pointer',
  padding: 16,
  '&:hover': {
    background: theme.palette.primary.light
  },
  '& .MuiListItem-root': {
    padding: 0
  }
}));

// ==============================|| NOTIFICATION LIST ITEM ||============================== //

const NotificationList = () => {
  const theme = useTheme();

  const chipSX = {
    height: 24,
    padding: '0 6px'
  };
  const chipErrorSX = {
    ...chipSX,
    color: theme.palette.orange.dark,
    backgroundColor: theme.palette.orange.light,
    marginRight: '5px'
  };

  const chipWarningSX = {
    ...chipSX,
    color: theme.palette.warning.dark,
    backgroundColor: theme.palette.warning.light
  };

  const chipSuccessSX = {
    ...chipSX,
    color: theme.palette.success.dark,
    backgroundColor: theme.palette.success.light,
    height: 28
  };

  return (
    <List
      sx={{
        width: '100%',
        maxWidth: 330,
        py: 0,
        borderRadius: '10px',
        [theme.breakpoints.down('md')]: {
          maxWidth: 300
        },
        '& .MuiListItemSecondaryAction-root': {
          top: 22
        },
        '& .MuiDivider-root': {
          my: 0
        },
        '& .list-container': {
          pl: 7
        }
      }}
    >
      <ListItemWrapper>
        <ListItem alignItems="center">
          <ListItemAvatar>
            <Avatar alt="王小明" src={User1} />
          </ListItemAvatar>
          <ListItemText primary="王小明" />
          <ListItemSecondaryAction>
            <Grid container justifyContent="flex-end">
              <Grid item xs={12}>
                <Typography variant="caption" display="block" gutterBottom>
                  2 分鐘前
                </Typography>
              </Grid>
            </Grid>
          </ListItemSecondaryAction>
        </ListItem>
        <Grid container direction="column" className="list-container">
          <Grid item xs={12} sx={{ pb: 2 }}>
            <Typography variant="subtitle2">修改日記 2024-04-01</Typography>
          </Grid>
          <Grid item xs={12}>
            <Grid container>
              <Grid item>
                <Chip label="未讀" sx={chipErrorSX} />
              </Grid>
              <Grid item>
                <Chip label="新的" sx={chipWarningSX} />
              </Grid>
            </Grid>
          </Grid>
        </Grid>
      </ListItemWrapper>
      <Divider />
      <ListItemWrapper>
        <ListItem alignItems="center">
          <ListItemAvatar>
            <Avatar
              sx={{
                color: theme.palette.success.dark,
                backgroundColor: theme.palette.success.light,
                border: 'none',
                borderColor: theme.palette.success.main
              }}
            >
              <IconBuildingStore stroke={1.5} size="1.3rem" />
            </Avatar>
          </ListItemAvatar>
          <ListItemText primary={<Typography variant="subtitle1">驗證</Typography>} />
          <ListItemSecondaryAction>
            <Grid container justifyContent="flex-end">
              <Grid item xs={12}>
                <Typography variant="caption" display="block" gutterBottom>
                  2 分鐘前
                </Typography>
              </Grid>
            </Grid>
          </ListItemSecondaryAction>
        </ListItem>
        <Grid container direction="column" className="list-container">
          <Grid item xs={12} sx={{ pb: 2 }}>
            <Typography variant="subtitle2">我們已成功收到您的請求。</Typography>
          </Grid>
          <Grid item xs={12}>
            <Grid container>
              <Grid item>
                <Chip label="未讀" sx={chipErrorSX} />
              </Grid>
            </Grid>
          </Grid>
        </Grid>
      </ListItemWrapper>
      <Divider />
      <ListItemWrapper>
        <ListItem alignItems="center">
          <ListItemAvatar>
            <Avatar
              sx={{
                color: theme.palette.primary.dark,
                backgroundColor: theme.palette.primary.light,
                border: 'none',
                borderColor: theme.palette.primary.main
              }}
            >
              <IconMailbox stroke={1.5} size="1.3rem" />
            </Avatar>
          </ListItemAvatar>
          <ListItemText primary={<Typography variant="subtitle1">檢查信箱</Typography>} />
          <ListItemSecondaryAction>
            <Grid container justifyContent="flex-end">
              <Grid item>
                <Typography variant="caption" display="block" gutterBottom>
                  2 分鐘前
                </Typography>
              </Grid>
            </Grid>
          </ListItemSecondaryAction>
        </ListItem>
        <Grid container direction="column" className="list-container">
          <Grid item xs={12} sx={{ pb: 2 }}>
            <Typography variant="subtitle2">完成! 請檢查您的信箱</Typography>
          </Grid>
          <Grid item xs={12}>
            <Grid container>
              <Grid item>
                <Button variant="contained" disableElevation endIcon={<IconBrandTelegram stroke={1.5} size="1.3rem" />}>
                  信箱
                </Button>
              </Grid>
            </Grid>
          </Grid>
        </Grid>
      </ListItemWrapper>
      <Divider />
      <ListItemWrapper>
        <ListItem alignItems="center">
          <ListItemAvatar>
            <Avatar alt="王小明" src={User1} />
          </ListItemAvatar>
          <ListItemText primary={<Typography variant="subtitle1">王小明</Typography>} />
          <ListItemSecondaryAction>
            <Grid container justifyContent="flex-end">
              <Grid item xs={12}>
                <Typography variant="caption" display="block" gutterBottom>
                  2 分鐘前
                </Typography>
              </Grid>
            </Grid>
          </ListItemSecondaryAction>
        </ListItem>
        <Grid container direction="column" className="list-container">
          <Grid item xs={12} sx={{ pb: 2 }}>
            <Typography component="span" variant="subtitle2">
              上傳兩個檔案 &nbsp;
              <Typography component="span" variant="h6">
                2020-01-21
              </Typography>
            </Typography>
          </Grid>
          <Grid item xs={12}>
            <Grid container>
              <Grid item xs={12}>
                <Card
                  sx={{
                    backgroundColor: theme.palette.secondary.light
                  }}
                >
                  <CardContent>
                    <Grid container direction="column">
                      <Grid item xs={12}>
                        <Stack direction="row" spacing={2}>
                          <IconPhoto stroke={1.5} size="1.3rem" />
                          <Typography variant="subtitle1">demo.jpg</Typography>
                        </Stack>
                      </Grid>
                    </Grid>
                  </CardContent>
                </Card>
              </Grid>
            </Grid>
          </Grid>
        </Grid>
      </ListItemWrapper>
      <Divider />
      <ListItemWrapper>
        <ListItem alignItems="center">
          <ListItemAvatar>
            <Avatar alt="王小明" src={User1} />
          </ListItemAvatar>
          <ListItemText primary={<Typography variant="subtitle1">王小明</Typography>} />
          <ListItemSecondaryAction>
            <Grid container justifyContent="flex-end">
              <Grid item xs={12}>
                <Typography variant="caption" display="block" gutterBottom>
                  2 分鐘前
                </Typography>
              </Grid>
            </Grid>
          </ListItemSecondaryAction>
        </ListItem>
        <Grid container direction="column" className="list-container">
          <Grid item xs={12} sx={{ pb: 2 }}>
            <Typography variant="subtitle2">撰寫日記 2024-04-15</Typography>
          </Grid>
          <Grid item xs={12}>
            <Grid container>
              <Grid item>
                <Chip label="確認" sx={chipSuccessSX} />
              </Grid>
            </Grid>
          </Grid>
        </Grid>
      </ListItemWrapper>
    </List>
  );
};

export default NotificationList;
