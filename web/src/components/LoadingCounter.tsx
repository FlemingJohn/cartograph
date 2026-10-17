import { motion } from "framer-motion";

export function LoadingCounter({ count }: { count: number }) {
  return (
    <motion.div
      className="intro-loading"
      exit={{ opacity: 0, scale: 1.08, filter: "blur(8px)" }}
      transition={{ duration: 0.45 }}
      role="progressbar"
      aria-valuemin={1}
      aria-valuemax={100}
      aria-valuenow={count}
    >
      <span className="intro-counter">{count}</span>
      <span className="intro-progress">
        <span className="intro-progress-fill" style={{ width: `${count}%` }} />
      </span>
    </motion.div>
  );
}
