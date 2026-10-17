import { useFrame } from "@react-three/fiber";
import { useMemo } from "react";
import { Color } from "three";
import { heroFragmentShader } from "../lib/heroFragmentShader";
import { heroVertexShader } from "../lib/heroVertexShader";

export function GradientPlane({
  deepColour,
  paleColour,
  speed,
}: {
  deepColour: string;
  paleColour: string;
  speed: number;
}) {
  const uniforms = useMemo(
    () => ({
      uTime: { value: 0 },
      uColor1: { value: new Color(deepColour) },
      uColor2: { value: new Color(paleColour) },
    }),
    [deepColour, paleColour],
  );

  useFrame(({ clock }) => {
    uniforms.uTime.value = clock.getElapsedTime() * speed;
  });

  return (
    <mesh scale={[2, 2, 1]}>
      <planeGeometry args={[2, 2]} />
      <shaderMaterial
        vertexShader={heroVertexShader}
        fragmentShader={heroFragmentShader}
        uniforms={uniforms}
        transparent
        depthWrite={false}
        depthTest={false}
      />
    </mesh>
  );
}
