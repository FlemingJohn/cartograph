import { useSpring, useTransform, type MotionValue } from "framer-motion";
import type { RefObject } from "react";

const springSettings = { damping: 20, stiffness: 300, mass: 0.5 };

export function useMagneticSize(
  elementRef: RefObject<HTMLElement | null>,
  pointerX: MotionValue<number>,
  iconSize: number,
  maxScale: number,
  magneticDistance: number,
) {
  const distance = useTransform(pointerX, (x: number) => {
    const bounds = elementRef.current?.getBoundingClientRect();
    return bounds ? x - (bounds.left + bounds.width / 2) : magneticDistance + 1;
  });
  const scale = useTransform(
    distance,
    [-magneticDistance, 0, magneticDistance],
    [1, maxScale, 1],
  );
  const smoothScale = useSpring(scale, springSettings);
  const size = useTransform(smoothScale, (value) => value * iconSize);
  const lift = useSpring(
    useTransform(smoothScale, (value) => (value - 1) * -8),
    springSettings,
  );
  return { size, lift };
}
