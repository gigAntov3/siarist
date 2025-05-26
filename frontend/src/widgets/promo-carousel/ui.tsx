import { useState, useRef, useEffect } from 'react';

import FifaImage from './assets/fifa.png';
import styles from './styles.module.css';

const images = [
  { id: 1, src: FifaImage, alt: 'fifa' },
  { id: 2, src: FifaImage, alt: 'fifa' },
  { id: 3, src: FifaImage, alt: 'fifa' },
];

export const PromoCarousel = () => {
  const [activeIndex, setActiveIndex] = useState(0);
  const [translateX, setTranslateX] = useState(0);
  const [transitionEnabled, setTransitionEnabled] = useState(false);
  const [containerWidth, setContainerWidth] = useState(window.innerWidth);

  const touchStartX = useRef<number | null>(null);
  const touchCurrentX = useRef<number | null>(null);

  const minSwipeDistance = 50;

  const sidePadding = 8;
  const gap = 16;

  // ширина слайда с учётом паддинга и gap между слайдами
  const slideWidth = containerWidth - 2 * sidePadding - gap;

  useEffect(() => {
    const handleResize = () => {
      setContainerWidth(window.innerWidth);
    };
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);

  const onTouchStart = (e: React.TouchEvent) => {
    setTransitionEnabled(false);
    touchStartX.current = e.changedTouches[0].clientX;
  };

  const onTouchMove = (e: React.TouchEvent) => {
    if (touchStartX.current === null) return;
    touchCurrentX.current = e.changedTouches[0].clientX;
    const deltaX = touchCurrentX.current - touchStartX.current;
    setTranslateX(deltaX);
  };

  const onTouchEnd = () => {
    if (touchStartX.current === null || touchCurrentX.current === null) {
      setTranslateX(0);
      return;
    }

    const deltaX = touchCurrentX.current - touchStartX.current;
    setTransitionEnabled(true);

    if (Math.abs(deltaX) > minSwipeDistance) {
      if (deltaX < 0) {
        setActiveIndex((prev) => (prev + 1) % images.length);
      } else {
        setActiveIndex((prev) => (prev === 0 ? images.length - 1 : prev - 1));
      }
    }

    setTranslateX(0);
    touchStartX.current = null;
    touchCurrentX.current = null;
  };

  const selectDot = (index: number) => {
    setActiveIndex(index);
    setTransitionEnabled(true);
  };

  // Центрируем активный слайд, учитывая gap и паддинги
  const centerOffset =
    containerWidth / 2 - sidePadding - (activeIndex * (slideWidth + gap) + slideWidth / 2);

  const translateXFinal = centerOffset + translateX;

  return (
    <div className={styles.wrapper}>
      <div
        className={styles.imageContainer}
        onTouchStart={onTouchStart}
        onTouchMove={onTouchMove}
        onTouchEnd={onTouchEnd}
        style={{
          width: '100vw',
          padding: `0 ${sidePadding}px`,
          boxSizing: 'border-box',
          touchAction: 'pan-y',
          userSelect: 'none',
          cursor: 'grab',
          position: 'relative',
          overflow: 'hidden',
        }}
      >
        <div
          style={{
            display: 'flex',
            gap: `${gap}px`,
            transform: `translateX(${translateXFinal}px)`,
            transition: transitionEnabled ? 'transform 0.3s ease' : 'none',
          }}
        >
          {images.map(({ id, src, alt }) => (
            <div
              key={id}
              style={{
                width: `${slideWidth}px`,
                flexShrink: 0,
                borderRadius: 24,
                overflow: 'hidden',
              }}
            >
              <img
                src={src}
                alt={alt}
                draggable={false}
                style={{
                  width: '100%',
                  height: '180px',
                  objectFit: 'cover',
                  userSelect: 'none',
                  pointerEvents: 'none',
                }}
              />
            </div>
          ))}
        </div>
      </div>

      <div className={styles.dotsContainer}>
        {images.map((_, index) => (
          <span
            key={index}
            className={`${styles.dot} ${index === activeIndex ? styles.active : ''}`}
            onClick={() => selectDot(index)}
          />
        ))}
      </div>
    </div>
  );
};
