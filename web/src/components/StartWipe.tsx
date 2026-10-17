import { motion } from "framer-motion";

export function StartWipe({
  origin,
  onDone,
}: {
  origin: { x: number; y: number };
  onDone: () => void;
}) {
  return (
    <motion.span
      className="start-wipe"
      style={{ left: origin.x, top: origin.y }}
      initial={{ scale: 0 }}
      animate={{ scale: 1 }}
      transition={{ duration: 0.75, ease: [0.65, 0, 0.35, 1] }}
      onAnimationComplete={onDone}
      aria-hidden="true"
    />
  );
}
