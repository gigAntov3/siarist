import { Link, useLocation } from 'react-router-dom';

import { ReactComponent as HomeIcon } from '../../assets/home.svg';
import { ReactComponent as BusketIcon } from '../../assets/busket.svg';
import { ReactComponent as StarIcon } from '../../assets/star.svg';
import { ReactComponent as FeedbackIcon } from '../../assets/feedback.svg';

import styles from './styles.module.css';


export const TabBar = () => {
    const location = useLocation();
    const currentPath = location.pathname;

    return (
        <div className={styles.tabBar}>
            <Link to="/" className={currentPath === '/' ? styles.active : ''}>
                <HomeIcon />
            </Link>
            <Link to="/bonus" className={currentPath === '/bonus' ? styles.active : ''}>
                <StarIcon />
            </Link>
            <Link to="/feedback" className={currentPath === '/feedback' ? styles.active : ''}>
                <FeedbackIcon />
            </Link>
            <Link to="/busket" className={currentPath === '/busket' ? styles.active : ''}>
                <BusketIcon />
            </Link>
        </div>
    );
};