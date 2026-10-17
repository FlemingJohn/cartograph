import { motion } from "framer-motion";
import { useState, type MouseEvent } from "react";
import { Icon } from "./Icon";
import { StartWipe } from "./StartWipe";

export function StartButton({ onClick }: { onClick: () => void }) {
  const [wipeOrigin, setWipeOrigin] = useState<{ x: number; y: number } | null>(null);

  function handleClick(event: MouseEvent<HTMLButtonElement>) {
    const bounds = event.currentTarget.getBoundingClientRect();
    setWipeOrigin({ x: bounds.left + bounds.width / 2, y: bounds.top + bounds.height / 2 });
  }

  return (
    <>
      <motion.button
        type="button"
        className="start-button"
        onClick={handleClick}
        disabled={wipeOrigin !== null}
        initial={{ opacity: 0, y: 16 }}
        animate={wipeOrigin ? { opacity: 1, y: 0, scale: 0.9 } : { opacity: 1, y: 0, scale: 1 }}
        transition={{ duration: 0.4 }}
        whileHover={{ scale: 1.05 }}
        whileTap={{ scale: 0.94 }}
      >
        Try now
        <span className="start-button-arrow">
          <motion.span
            className="start-button-arrow-icon"
            animate={{ x: [0, 4, 0] }}
            transition={{ duration: 1.4, repeat: Infinity, ease: "easeInOut" }}
          >
            <Icon name="arrow" />
          </motion.span>
        </span>
      </motion.button>
      {wipeOrigin && <StartWipe origin={wipeOrigin} onDone={onClick} />}
    </>
  );
}
