// assets
import { IconHome } from '@tabler/icons-react';

// constant
const icons = { IconHome };

// ==============================|| DASHBOARD MENU ITEMS ||============================== //

const dashboard = {
  id: 'dashboard',
  type: 'group',
  children: [
    {
      id: 'default',
      title: '首頁',
      type: 'item',
      url: '/dashboard/default',
      icon: icons.IconHome,
      breadcrumbs: false
    }
  ]
};

export default dashboard;
