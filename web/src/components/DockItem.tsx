import { AnimatePresence, motion, type MotionValue } from "framer-motion";
import { useRef, useState } from "react";
import { useMagneticSize } from "../hooks/useMagneticSize";
import type { DockItemData } from "../types/DockItemData";

export function DockItem({
  item,
  pointerX,
  iconSize,
  maxScale,
  magneticDistance,
  isReducedMotion,
}: {
  item: DockItemData;
  pointerX: MotionValue<number>;
  iconSize: number;
  maxScale: number;
  magneticDistance: number;
  isReducedMotion: boolean;
}) {
  const buttonRef = useRef<HTMLButtonElement>(null);
  const [isPointedAt, setIsPointedAt] = useState(false);
  const { size, lift } = useMagneticSize(buttonRef, pointerX, iconSize, maxScale, magneticDistance);
  return (
    <motion.button
      ref={buttonRef}
      type="button"
      className="dock-item"
      aria-label={item.label}
      aria-current={item.isActive ? "page" : undefined}
      onClick={item.onClick}
      onPointerEnter={() => setIsPointedAt(true)}
      onPointerLeave={() => setIsPointedAt(false)}
      onFocus={() => setIsPointedAt(true)}
      onBlur={() => setIsPointedAt(false)}
      style={{
        width: isReducedMotion ? iconSize : size,
        height: isReducedMotion ? iconSize : size,
        y: isReducedMotion ? 0 : lift,
      }}
      whileTap={isReducedMotion ? undefined : { scale: 0.9 }}
    >
      <span className="dock-icon" aria-hidden="true">
        {item.icon}
      </span>
      {item.isActive && <motion.span layoutId="dock-active" className="dock-active-dot" />}
      <AnimatePresence>
        {isPointedAt && (
          <motion.span
            className="dock-label"
            initial={{ opacity: 0, y: 6, scale: 0.9 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            exit={{ opacity: 0, y: 6, scale: 0.9 }}
            transition={{ duration: 0.15, ease: "easeOut" }}
          >
            {item.label}
          </motion.span>
        )}
      </AnimatePresence>
    </motion.button>
  );
}
