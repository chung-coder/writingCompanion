import dayjs from 'dayjs';
import axios from 'axios';
import { useState, useEffect } from 'react';
import CircleIcon from '@mui/icons-material/Circle';
import Paper from '@mui/material/Paper';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import MainCard from 'ui-component/cards/MainCard';

const BasicTable = ({ startOfWeek, endOfWeek }) => {
  const [rows, setRows] = useState([]);
  const daysOfWeek = ['週日', '週一', '週二', '週三', '週四', '週五', '週六'];
  const start = dayjs(startOfWeek);
  const api = 'http://localhost:8000/api/';
  const token =
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI4NDc5NTc0LCJpYXQiOjE3MjU4ODc1NzQsImp0aSI6Ijg5MTllMGRjYzNhNzRiZTdiYzEyZTc0Y2QwMzFlNjU3IiwidXNlcl9pZCI6MSwidXNlcm5hbWUiOiJhZG1pbiJ9.DtAVnr-7DG9SpSEYYfyN4SokKvHtD_vffIdHYpeDdQY';

  useEffect(() => {
    const newRows = [];

    const instance = axios.create({
      baseURL: api,
      headers: { Authorization: `Bearer ${token}` }
    });
    instance
      .get('/weekly_diary/', { params: { start_date: startOfWeek, end_date: endOfWeek } })
      .then((response) => {
        const result = response.data;

        if (result && result.length > 0) {
          for (let i = 0; i < 7; i++) {
            const currentDate = start.add(i, 'day').format('YYYY-MM-DD');
            const matchedData = result.find((entry) => entry.date === currentDate);
            const rowData = {
              id: start.add(i, 'day').format('MM/DD'),
              day: daysOfWeek[i],
              date: start.add(i, 'day').format('MM/DD'),
              mood: matchedData ? matchedData.mood : '',
              content: matchedData ? matchedData.content : '無'
            };
            newRows.push(rowData);
          }
        }

        setRows(newRows);
      })
      .catch((error) => {
        console.log(error);
      });
  }, [startOfWeek, endOfWeek]);

  return (
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
            {rows.length > 0 ? (
              rows.map((row) => (
                <TableRow key={row.id} sx={{ '&:last-child td, &:last-child th': { border: 0 } }}>
                  <TableCell component="th" scope="row">
                    {row.day}
                  </TableCell>
                  <TableCell component="th" scope="row">
                    {row.date}
                  </TableCell>
                  <TableCell align="right">
                    {row.mood ? (
                      <CircleIcon
                        sx={{
                          color:
                            row.mood === '普通'
                              ? 'grey.400'
                              : row.mood === '好'
                                ? 'success.main'
                                : row.mood === '很好'
                                  ? 'success.dark'
                                  : row.mood === '差'
                                    ? 'error.main'
                                    : 'error.dark'
                        }}
                        fontSize="small"
                      />
                    ) : (
                      row.mood
                    )}
                  </TableCell>
                  <TableCell align="left">{row.content}</TableCell>
                </TableRow>
              ))
            ) : (
              <TableRow>
                <TableCell
                  colSpan={4}
                  align="center"
                  style={{
                    writingMode: 'vertical-rl',
                    textAlign: 'center',
                    fontWeight: 'bold',
                    fontSize: '25px',
                    letterSpacing: '5px',
                    padding: '20px'
                  }}
                >
                  這週尚未撰寫日記
                </TableCell>
              </TableRow>
            )}
          </TableBody>
        </Table>
      </TableContainer>
    </MainCard>
  );
};

export default BasicTable;
