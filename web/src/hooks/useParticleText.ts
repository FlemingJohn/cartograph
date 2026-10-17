import { useEffect, type RefObject } from "react";
import { makeTextParticles } from "../lib/makeTextParticles";
import type { Particle } from "../lib/Particle";
import type { ParticleTextSettings } from "../types/ParticleTextSettings";

const pointerOutside = -1000;

export function useParticleText(
  canvasRef: RefObject<HTMLCanvasElement | null>,
  settings: ParticleTextSettings,
) {
  const { text, fontSize, fontFamily, colour, particleSize, density, pushStrength, returnSpeed } =
    settings;

  useEffect(() => {
    const canvas = canvasRef.current;
    const context = canvas?.getContext("2d");
    if (!canvas || !context) return;
    const current = { text, fontSize, fontFamily, colour, particleSize, density, pushStrength, returnSpeed };
    const pointer = { x: pointerOutside, y: pointerOutside };
    let particles: Particle[] = [];
    let frame = 0;

    const build = () => {
      particles = makeTextParticles(canvas, canvas.clientWidth, canvas.clientHeight, current);
    };
    const animate = () => {
      context.clearRect(0, 0, canvas.clientWidth, canvas.clientHeight);
      particles.forEach((particle) => {
        particle.update(pointer.x, pointer.y);
        particle.draw(context);
      });
      frame = requestAnimationFrame(animate);
    };
    const followPointer = (event: PointerEvent) => {
      const bounds = canvas.getBoundingClientRect();
      pointer.x = event.clientX - bounds.left;
      pointer.y = event.clientY - bounds.top;
    };
    const releasePointer = () => {
      pointer.x = pointerOutside;
      pointer.y = pointerOutside;
    };

    const resizeObserver = new ResizeObserver(build);
    resizeObserver.observe(canvas);
    canvas.addEventListener("pointermove", followPointer);
    canvas.addEventListener("pointerleave", releasePointer);
    document.fonts.load(`700 ${fontSize}px ${fontFamily}`).then(build);
    animate();

    return () => {
      cancelAnimationFrame(frame);
      resizeObserver.disconnect();
      canvas.removeEventListener("pointermove", followPointer);
      canvas.removeEventListener("pointerleave", releasePointer);
    };
  }, [canvasRef, text, fontSize, fontFamily, colour, particleSize, density, pushStrength, returnSpeed]);
}
