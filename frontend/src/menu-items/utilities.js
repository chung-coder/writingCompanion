// assets
import { IconChartBar, IconChartDots3, IconShadow, IconWindmill } from '@tabler/icons-react';

// constant
const icons = {
  IconChartDots3,
  IconChartBar,
  IconShadow,
  IconWindmill
};

// ==============================|| UTILITIES MENU ITEMS ||============================== //

const utilities = {
  id: 'utilities',
  title: '分析',
  type: 'group',
  children: [
    {
      id: 'diary-analytics',
      title: '日記分析',
      type: 'item',
      url: '/utils/diary-analytics',
      icon: icons.IconChartDots3,
      breadcrumbs: false
    },
    {
      id: 'util-color',
      title: '寫作統計分析',
      type: 'item',
      url: '/utils/util-statistic',
      icon: icons.IconChartBar,
      breadcrumbs: false
    }
  ]
};

export default utilities;
