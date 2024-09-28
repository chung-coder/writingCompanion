import Visibility from '@mui/icons-material/Visibility';
import VisibilityOff from '@mui/icons-material/VisibilityOff';
import { FilledInput, FormControl, IconButton, InputAdornment, InputLabel } from '@mui/material';
import { useState } from 'react';

const PasswordInput = (props) => {
  const [showPassword, setShowPassword] = useState(false);
  const handleClickShowPassword = () => {
    setShowPassword(!showPassword);
  };

  const handleInputChange = (e) => {
    const value = e.target.value;

    props.onPasswordChange(value);
  };

  return (
    <FormControl
      fullWidth
      sx={{
        width: '100%',
        marginBottom: '2%',
        '& .css-1g4r557-MuiInputBase-root-MuiFilledInput-root': { backgroundColor: 'white' },
        '& .css-1azz9p3-MuiInputBase-input-MuiFilledInput-input': { backgroundColor: 'white' },
        '& .css-1g4r557-MuiInputBase-root-MuiFilledInput-root:hover': { backgroundColor: 'white' }
      }}
      variant="filled"
    >
      <InputLabel shrink htmlFor="outlined-adornment-password-register">
        {props.name}
      </InputLabel>
      <FilledInput
        id={props.id}
        type={showPassword ? 'text' : 'password'}
        name={props.id}
        label={props.value}
        onChange={handleInputChange}
        endAdornment={
          <InputAdornment position="end">
            <IconButton aria-label="toggle password visibility" onClick={handleClickShowPassword} edge="end" size="large">
              {showPassword ? <Visibility /> : <VisibilityOff />}
            </IconButton>
          </InputAdornment>
        }
        inputProps={{}}
      />
    </FormControl>
  );
};

export default PasswordInput;
