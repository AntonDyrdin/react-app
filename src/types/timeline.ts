export interface TimelineEvent {
  year: number;
  title: string;
  description: string;
}

export interface TimelinePeriod {
  id: number;
  title: string;
  startYear: number;
  endYear: number;
  events: TimelineEvent[];
}

export interface TimelineData {
  periods: TimelinePeriod[];
}
