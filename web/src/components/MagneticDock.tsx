import { motion, useMotionValue, useReducedMotion } from "framer-motion";
import type { DockItemData } from "../types/DockItemData";
import { DockItem } from "./DockItem";

export function MagneticDock({
  items,
  iconSize = 44,
  maxScale = 1.45,
  magneticDistance = 140,
}: {
  items: DockItemData[];
  iconSize?: number;
  maxScale?: number;
  magneticDistance?: number;
}) {
  const pointerX = useMotionValue(Infinity);
  const isReducedMotion = useReducedMotion() ?? false;
  return (
    <motion.nav
      aria-label="Screens"
      className="magnetic-dock"
      onMouseMove={(event) => pointerX.set(event.clientX)}
      onMouseLeave={() => pointerX.set(Infinity)}
      initial={{ opacity: 0, y: -16 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5, ease: [0.25, 0.46, 0.45, 0.94] }}
    >
      {items.map((item) => (
        <DockItem
          key={item.id}
          item={item}
          pointerX={pointerX}
          iconSize={iconSize}
          maxScale={maxScale}
          magneticDistance={magneticDistance}
          isReducedMotion={isReducedMotion}
        />
      ))}
    </motion.nav>
  );
}
