import type { ScoreParts } from "./ScoreParts";

export interface ScorePartRow {
  part: keyof ScoreParts;
  label: string;
  maximum: number;
}
