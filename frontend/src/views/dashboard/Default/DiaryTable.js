import CircleIcon from '@mui/icons-material/Circle';
import { Typography } from '@mui/material';
import Paper from '@mui/material/Paper';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import MainCard from 'ui-component/cards/MainCard';

function DiaryTable({ favoriteDiary }) {
  return (
    <MainCard content={true}>
      <Typography variant="h3">收藏日記</Typography>
      <TableContainer component={Paper}>
        <Table sx={{ minWidth: 650 }}>
          <TableHead>
            <TableRow>
              <TableCell>日期</TableCell>
              <TableCell>心情</TableCell>
              <TableCell>內容</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {favoriteDiary && favoriteDiary.length > 0 ? (
              favoriteDiary[0].map((item) => {
                const [, month, day] = item.date.split('-');
                const formattedDate = `${month}/${day}`;
                return (
                  <TableRow key={item.id} sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
                    <TableCell component="th" scope="row">
                      {formattedDate}
                    </TableCell>
                    <TableCell>
                      <CircleIcon
                        sx={{
                          color:
                            item.mood === '普通'
                              ? 'grey.400'
                              : item.mood === '好'
                                ? 'success.main'
                                : item.mood === '很好'
                                  ? 'success.dark'
                                  : item.mood === '差'
                                    ? 'error.main'
                                    : 'error.dark'
                        }}
                        fontSize="small"
                      />
                    </TableCell>
                    <TableCell>{item.content}</TableCell>
                  </TableRow>
                );
              })
            ) : (
              <h1>Loading...</h1>
            )}
          </TableBody>
        </Table>
      </TableContainer>
    </MainCard>
  );
}

export default DiaryTable;
