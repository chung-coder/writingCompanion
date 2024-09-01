import { useEffect, useState } from 'react';

// @mui material components
import Card from '@mui/material/Card';
import Grid from '@mui/material/Grid';

// Soft UI Dashboard React components
import SoftAvatar from 'ui-component/SoftAvatar';
import SoftBox from 'ui-component/SoftBox';
import SoftTypography from 'ui-component/SoftTypography';

// Images
import curved14 from 'assets/images/curved14.jpg';
import burceMars from 'assets/images/users/user-round.svg';

const breakpoints = {
  values: {
    xs: 0,
    sm: 576,
    md: 768,
    lg: 992,
    xl: 1200,
    xxl: 1400
  }
};

function Header() {
  const [tabsOrientation, setTabsOrientation] = useState('horizontal');

  useEffect(() => {
    // A function that sets the orientation state of the tabs.
    function handleTabsOrientation() {
      return window.innerWidth < breakpoints.values.sm ? setTabsOrientation('vertical') : setTabsOrientation('horizontal');
    }

    /** 
     The event listener that's calling the handleTabsOrientation function when resizing the window.
    */
    window.addEventListener('resize', handleTabsOrientation);

    // Call the handleTabsOrientation function to set the state with the initial value.
    handleTabsOrientation();

    // Remove event listener on cleanup
    return () => window.removeEventListener('resize', handleTabsOrientation);
  }, [tabsOrientation]);

  return (
    <SoftBox position="relative">
      <SoftBox
        display="flex"
        alignItems="center"
        position="relative"
        minHeight="18.75rem"
        borderRadius="xl"
        sx={{
          backgroundImage: ({ functions: { rgba, linearGradient }, palette: { gradients } }) =>
            `${linearGradient(rgba(gradients.info.main, 0.6), rgba(gradients.info.state, 0.6))}, url(${curved14})`,
          backgroundSize: 'cover',
          backgroundPosition: '50%',
          overflow: 'hidden'
        }}
      />
      <Card
        sx={{
          backdropFilter: `saturate(200%) blur(30px)`,
          backgroundColor: ({ functions: { rgba }, palette: { white } }) => rgba(white.main, 0.8),
          boxShadow: ({ boxShadows: { navbarBoxShadow } }) => navbarBoxShadow,
          position: 'relative',
          mt: -8,
          mx: 3,
          py: 2,
          px: 2
        }}
      >
        <Grid container spacing={3} alignItems="center">
          <Grid item>
            <SoftAvatar src={burceMars} alt="profile-image" variant="rounded" size="xl" shadow="sm" />
          </Grid>
          <Grid item>
            <SoftBox height="100%" mt={0.5} lineHeight={1}>
              <SoftTypography variant="h5" fontWeight="medium">
                王小明
              </SoftTypography>
              <SoftTypography variant="button" color="text" fontWeight="medium">
                ming.wang@gmail.com
              </SoftTypography>
            </SoftBox>
          </Grid>
        </Grid>
      </Card>
    </SoftBox>
  );
}

export default Header;
