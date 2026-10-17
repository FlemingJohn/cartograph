import { useRef } from "react";
import { cn } from "@/lib/cn";
import { getThemeToken } from "@/lib/getThemeToken";
import { useParticleText } from "@/hooks/useParticleText";

export function CursorDrivenParticleTypography({
  text,
  className,
  fontSize = 160,
  particleSize = 1.4,
  density = 4,
  pushStrength = 15,
  returnSpeed = 0.08,
}: {
  text: string;
  className?: string;
  fontSize?: number;
  particleSize?: number;
  density?: number;
  pushStrength?: number;
  returnSpeed?: number;
}) {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  useParticleText(canvasRef, {
    text,
    fontSize,
    fontFamily: getThemeToken("font-display"),
    colour: getThemeToken("ink"),
    particleSize,
    density,
    pushStrength,
    returnSpeed,
  });
  return (
    <div className={cn("relative h-full w-full touch-none", className)}>
      <canvas ref={canvasRef} className="block h-full w-full" />
    </div>
  );
}
