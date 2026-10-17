import { motion } from "framer-motion";
import { Icon } from "./Icon";

export function StartButton({ onClick }: { onClick: () => void }) {
  return (
    <motion.button
      type="button"
      className="start-button"
      onClick={onClick}
      initial={{ opacity: 0, y: 16 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: 0.6, duration: 0.5 }}
      whileHover={{ scale: 1.04 }}
      whileTap={{ scale: 0.96 }}
    >
      Start
      <span className="start-button-arrow">
        <Icon name="arrow" />
      </span>
    </motion.button>
  );
}
