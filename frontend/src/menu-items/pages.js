// assets
import { IconFilePencil, IconUsers } from '@tabler/icons-react';

// constant
const icons = {
  IconFilePencil,
  IconUsers
};

// ==============================|| EXTRA PAGES MENU ITEMS ||============================== //

const pages = {
  id: 'pages',
  title: '日記',
  type: 'group',
  children: [
    {
      id: 'login3',
      title: '自行撰寫',
      type: 'item',
      url: '/diary/self-writing',
      icon: icons.IconFilePencil,
      breadcrumbs: false
    },
    {
      id: 'register3',
      title: '互動模式',
      type: 'item',
      url: '/diary/interaction',
      icon: icons.IconUsers,
      breadcrumbs: false
    }
  ]
};

export default pages;
