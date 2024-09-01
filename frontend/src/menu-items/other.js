// assets
import { IconUser, IconHelp } from '@tabler/icons-react';

// constant
const icons = { IconUser, IconHelp };

// ==============================|| SAMPLE PAGE & DOCUMENTATION MENU ITEMS ||============================== //

const other = {
  id: 'sample-docs-roadmap',
  title: '基本資料',
  type: 'group',
  children: [
    {
      id: 'sample-page',
      title: '個人資料',
      type: 'item',
      url: '/sample-page',
      icon: icons.IconUser,
      breadcrumbs: false
    }
  ]
};

export default other;
