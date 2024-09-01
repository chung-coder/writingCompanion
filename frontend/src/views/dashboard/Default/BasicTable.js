import CircleIcon from '@mui/icons-material/Circle';
import Paper from '@mui/material/Paper';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import MainCard from 'ui-component/cards/MainCard';

function createData(day, date, mood, content) {
  return { day, date, mood, content };
}

const rows = [
  createData(
    '週日',
    '7/28',
    <CircleIcon sx={{ color: 'success.dark' }} fontSize="small" />,
    '今天我們全家去動物園玩，我看到了很多動物，有長頸鹿、獅子和大象，最有趣的是看到了企鵝，它們走起路來非常可愛，這是一次很難忘的經歷。'
  ),
  createData(
    '週一',
    '7/29',
    <CircleIcon sx={{ color: 'success.dark' }} fontSize="small" />,
    '今天是我的生日，我很開心！爸爸媽媽帶我去吃了我最喜歡的披薩，還送我一個玩具車，晚上我們一起吃了生日蛋糕，大家都唱了生日快樂歌給我，這真是一個快樂的日子。'
  ),
  createData(
    '週二',
    '7/30',
    <CircleIcon sx={{ color: 'success.dark' }} fontSize="small" />,
    '我有一隻小狗，牠叫小白，小白非常可愛，牠喜歡跟我玩球，我每天放學後都會帶牠去公園散步，我覺得有小白陪伴我很幸福。'
  ),
  createData(
    '週三',
    '7/31',
    <CircleIcon sx={{ color: 'grey.400' }} fontSize="small" />,
    '我有一個好朋友，叫小明，我們經常一起玩耍、做作業，他很聰明，經常幫助我解決難題，我覺得有這樣的朋友真好。'
  ),
  createData(
    '週四',
    '8/01',
    <CircleIcon sx={{ color: 'grey.400' }} fontSize="small" />,
    '今天下午，我和同學們在學校打了一場籃球賽，我們隊贏了，大家都非常開心，我覺得團隊合作很重要，我們一起努力才取得了勝利。'
  ),
  createData(
    '週五',
    '8/02',
    <CircleIcon sx={{ color: 'error.main' }} fontSize="small" />,
    '今天心情很差，因為數學考試沒考好，早上老師發回考卷，我看到成績時，眼淚都快掉下來了，我明明已經很努力複習，但還是錯了很多題，回家後，媽媽安慰我說失敗是成功之母，下次一定會做得更好，我雖然難過，但會努力改進，爭取下次考得更好。'
  ),
  createData(
    '週六',
    '8/03',
    <CircleIcon sx={{ color: 'success.dark' }} fontSize="small" />,
    '今天心情不好，因為跟最好的朋友小明吵架了，上午我們在公園玩耍，因為一個小誤會，他不小心撞到了我，我生氣地大聲吼了他，結果他也生氣了，然後我們就不說話了，下午回家後，我想了很久，覺得自己應該主動道歉，因為朋友之間不應該為小事吵架，明天我會跟他道歉，希望我們能和好如初。'
  )
];

const BasicTable = () => (
  <MainCard content={true}>
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 800 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>星期</TableCell>
            <TableCell>日期</TableCell>
            <TableCell align="right">心情</TableCell>
            <TableCell align="right">內容</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow key={row.day} sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
              <TableCell component="th" scope="row">
                {row.day}
              </TableCell>
              <TableCell component="th" scope="row">
                {row.date}
              </TableCell>
              <TableCell align="right">{row.mood}</TableCell>
              <TableCell align="left">{row.content}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  </MainCard>
);

export default BasicTable;
