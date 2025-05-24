import { Link, useLocation } from 'react-router-dom';

import HomeIcon from '../../assets/home.svg?react';
import BusketIcon from '../../assets/busket.svg?react';
import StarIcon from '../../assets/star.svg?react';
import FeedbackIcon from '../../assets/feedback.svg?react';

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