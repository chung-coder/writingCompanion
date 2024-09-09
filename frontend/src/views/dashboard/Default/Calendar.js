import { useState, useEffect } from 'react';

import { styled } from '@mui/material/styles';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { DateCalendar } from '@mui/x-date-pickers/DateCalendar';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { PickersDay } from '@mui/x-date-pickers/PickersDay';
import dayjs from 'dayjs';
import isBetweenPlugin from 'dayjs/plugin/isBetween';
import * as React from 'react';
import MainCard from 'ui-component/cards/MainCard';
import './Calendar.css';

dayjs.extend(isBetweenPlugin);

const CustomPickersDay = styled(PickersDay, {
  shouldForwardProp: (prop) => prop !== 'isSelected' && prop !== 'isHovered'
})(({ theme, isSelected, isHovered, day }) => ({
  borderRadius: 0,
  ...(isSelected && {
    backgroundColor: theme.palette.primary.main,
    color: theme.palette.orange.dark,
    fontWeight: 'bold',
    '&:hover, &:focus': {
      backgroundColor: theme.palette.primary[200]
    }
  }),
  ...(isHovered && {
    backgroundColor: theme.palette.primary[theme.palette.mode],
    '&:hover, &:focus': {
      backgroundColor: theme.palette.primary[theme.palette.mode]
    }
  }),
  ...(day.day() === 0 && {
    borderTopLeftRadius: '50%',
    borderBottomLeftRadius: '50%'
  }),
  ...(day.day() === 6 && {
    borderTopRightRadius: '50%',
    borderBottomRightRadius: '50%'
  })
}));

const isInSameWeek = (dayA, dayB) => {
  if (dayB == null) {
    return false;
  }
  return dayA.isSame(dayB, 'week');
};

function Day(props) {
  const { day, selectedDay, hoveredDay, ...other } = props;
  return (
    <CustomPickersDay
      {...other}
      day={day}
      sx={{ px: '1%' }}
      selected={false}
      isSelected={isInSameWeek(day, selectedDay)}
      isHovered={isInSameWeek(day, hoveredDay)}
    />
  );
}

const Calendar = ({ onData }) => {
  const [hoveredDay, setHoveredDay] = useState(null);
  const [value, setValue] = useState(dayjs(new Date()));

  useEffect(() => {
    if (value) {
      const startOfWeek = value.startOf('week').format('YYYY-MM-DD');
      const endOfWeek = value.endOf('week').format('YYYY-MM-DD');
      onData(startOfWeek, endOfWeek);
    }
  }, [value]);

  return (
    <MainCard>
      <LocalizationProvider dateAdapter={AdapterDayjs}>
        <DateCalendar
          value={value}
          views={['month', 'day']}
          onChange={(newValue) => setValue(newValue)}
          minDate={dayjs('2024-1-1')}
          maxDate={dayjs('2024-12-31')}
          showDaysOutsideCurrentMonth
          slots={{ day: Day }}
          slotProps={{
            day: (ownerState) => ({
              selectedDay: value,
              hoveredDay,
              onPointerEnter: () => setHoveredDay(ownerState.day),
              onPointerLeave: () => setHoveredDay(null)
            })
          }}
        />
      </LocalizationProvider>
    </MainCard>
  );
};
export default Calendar;
