import { useEffect, useState } from "react";

export function useCountUp(first: number, last: number, durationMs: number): number {
  const [count, setCount] = useState(first);

  useEffect(() => {
    let frame = 0;
    const startedAt = performance.now();
    const step = (now: number) => {
      const progress = Math.min((now - startedAt) / durationMs, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      setCount(Math.round(first + (last - first) * eased));
      if (progress < 1) frame = requestAnimationFrame(step);
    };
    frame = requestAnimationFrame(step);
    return () => cancelAnimationFrame(frame);
  }, [first, last, durationMs]);

  return count;
}
