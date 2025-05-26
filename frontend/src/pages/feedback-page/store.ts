import { makeAutoObservable } from "mobx";
import { getFeedbacks } from "../../shared/api/feedback";
import type { Feedback } from "../../shared/api/feedback/model";

const LIMIT = 10;

class FeedbackStore {
  feedbacks: Feedback[] = [];
  offset = 0;
  loading = false;
  hasMore = true;
  error: string | null = null;

  constructor() {
    makeAutoObservable(this);
  }

  async loadMore() {
    if (this.loading || !this.hasMore) return;
    this.loading = true;
    try {
      const newFeedbacks = await getFeedbacks(LIMIT, this.offset);
      this.feedbacks.push(...newFeedbacks);
      this.offset += LIMIT;
      if (newFeedbacks.length < LIMIT) {
        this.hasMore = false;
      }
    } catch (e) {
      this.error = "Ошибка при загрузке отзывов";
    } finally {
      this.loading = false;
    }
  }
}

export const feedbackStore = new FeedbackStore();