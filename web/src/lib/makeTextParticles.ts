import { Particle } from "./Particle";
import type { ParticleTextSettings } from "../types/ParticleTextSettings";

export function makeTextParticles(
  canvas: HTMLCanvasElement,
  width: number,
  height: number,
  settings: ParticleTextSettings,
): Particle[] {
  const context = canvas.getContext("2d", { willReadFrequently: true });
  if (!context) return [];
  const pixelRatio = window.devicePixelRatio || 1;
  canvas.width = width * pixelRatio;
  canvas.height = height * pixelRatio;
  context.setTransform(pixelRatio, 0, 0, pixelRatio, 0, 0);
  drawTextOnce(context, width, height, settings);
  const pixels = context.getImageData(0, 0, canvas.width, canvas.height);
  context.clearRect(0, 0, width, height);
  return readParticles(pixels, pixelRatio, settings);
}

function drawTextOnce(
  context: CanvasRenderingContext2D,
  width: number,
  height: number,
  settings: ParticleTextSettings,
) {
  const fontSize = Math.min(settings.fontSize, width * 0.15);
  context.clearRect(0, 0, width, height);
  context.fillStyle = settings.colour;
  context.font = `700 ${fontSize}px ${settings.fontFamily}`;
  context.textAlign = "center";
  context.textBaseline = "middle";
  context.fillText(settings.text, width / 2, height / 2);
}

function readParticles(
  pixels: ImageData,
  pixelRatio: number,
  settings: ParticleTextSettings,
): Particle[] {
  const step = Math.max(1, Math.floor(settings.density * pixelRatio));
  const particles: Particle[] = [];
  for (let y = 0; y < pixels.height; y += step) {
    for (let x = 0; x < pixels.width; x += step) {
      const alpha = pixels.data[(y * pixels.width + x) * 4 + 3] ?? 0;
      if (alpha > 128) {
        particles.push(
          new Particle(
            x / pixelRatio,
            y / pixelRatio,
            settings.particleSize,
            settings.colour,
            settings.pushStrength,
            settings.returnSpeed,
          ),
        );
      }
    }
  }
  return particles;
}
