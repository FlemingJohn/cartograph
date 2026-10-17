import { AnimatePresence, motion } from "framer-motion";
import { CursorDrivenParticleTypography } from "../components/CursorDrivenParticleTypography";
import { HeroGeometric } from "../components/HeroGeometric";
import { LoadingCounter } from "../components/LoadingCounter";
import { StartButton } from "../components/StartButton";
import { useCountUp } from "../hooks/useCountUp";

const countDurationMs = 2600;

export function IntroScreen({ onStart }: { onStart: () => void }) {
  const count = useCountUp(1, 100, countDurationMs);
  const hasLoaded = count >= 100;

  return (
    <main className="intro">
      <AnimatePresence mode="wait">
        {hasLoaded ? (
          <motion.div
            key="title"
            className="intro-title"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 0.6 }}
          >
            <HeroGeometric>
              <CursorDrivenParticleTypography text="CartoGraph" className="intro-particles" />
              <p className="intro-tagline">Attack paths, ranked by what an attacker can reach.</p>
              <StartButton onClick={onStart} />
            </HeroGeometric>
          </motion.div>
        ) : (
          <LoadingCounter key="counter" count={count} />
        )}
      </AnimatePresence>
    </main>
  );
}
