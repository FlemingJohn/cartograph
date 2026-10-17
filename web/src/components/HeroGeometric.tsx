import { Canvas } from "@react-three/fiber";
import type { ReactNode } from "react";
import { getThemeToken } from "../lib/getThemeToken";
import { GradientPlane } from "./GradientPlane";

export function HeroGeometric({ children, speed = 1 }: { children: ReactNode; speed?: number }) {
  return (
    <div className="hero-geometric">
      <div className="hero-geometric-background" aria-hidden="true">
        <Canvas camera={{ position: [0, 0, 1] }} dpr={[1, 1]} gl={{ antialias: false, alpha: true }}>
          <GradientPlane
            deepColour={getThemeToken("gradient-deep")}
            paleColour={getThemeToken("gradient-pale")}
            speed={speed}
          />
        </Canvas>
      </div>
      <div className="hero-geometric-content">{children}</div>
    </div>
  );
}
