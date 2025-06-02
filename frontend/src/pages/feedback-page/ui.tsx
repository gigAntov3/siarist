import { useEffect, useRef } from "react";
import { observer } from "mobx-react-lite";
import { FeedbackCard } from "../../features/feedback/ui/feedback-card";
import { Separator } from "../../shared/ui/separator";
import { TabBar } from "../../shared/ui/tabbar";
import styles from "./styles.module.css";
import { feedbackStore } from "./store";

const adaptFeedback = (raw) => ({
  date: new Date(raw.created_at).toLocaleDateString("ru-RU", {
    day: "2-digit",
    month: "long",
    year: "numeric",
  }),
  text: raw.content,
  userName: raw.author.username,
});

export const FeedbackPage = observer(() => {
  const bottomRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    feedbackStore.loadMore();
    feedbackStore.loadCount(); // получаем общее количество отзывов
  }, []);

  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        if (entries[0].isIntersecting) {
          feedbackStore.loadMore();
        }
      },
      {
        rootMargin: "200px",
      }
    );

    const target = bottomRef.current;
    if (target) observer.observe(target);
    return () => target && observer.unobserve(target);
  }, []);

  return (
    <div>
      <div className={styles.feedbackContainer}>
        <div className={styles.titleWrapper}>
          <span className={styles.feedbackTitle}>Отзывы</span>
          <span className={styles.numberReviews}>
            {feedbackStore.totalCount}
          </span>
        </div>

        {feedbackStore.feedbacks.map((fb, idx) => {
          const adapted = adaptFeedback(fb);
          return (
            <div className={styles.feedbackItems} key={fb.id}>
              <FeedbackCard {...adapted} />
              {idx !== feedbackStore.feedbacks.length - 1 && <Separator />}
            </div>
          );
        })}

        <div ref={bottomRef} className={ styles.bottomRef } />

        {feedbackStore.loading && (
          <div className={styles.loadingText}>Загрузка...</div>
        )}
      </div>

      <TabBar />
    </div>
  );
});