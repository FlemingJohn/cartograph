import { useFrame } from "@react-three/fiber";
import { useMemo, useRef } from "react";
import { Color, type ShaderMaterial } from "three";
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
  const materialRef = useRef<ShaderMaterial>(null);
  const uniforms = useMemo(
    () => ({
      uTime: { value: 0 },
      uColor1: { value: new Color(deepColour) },
      uColor2: { value: new Color(paleColour) },
    }),
    [deepColour, paleColour],
  );

  useFrame((_state, secondsSinceLastFrame) => {
    const material = materialRef.current;
    if (material) material.uniforms.uTime.value += secondsSinceLastFrame * speed;
  });

  return (
    <mesh scale={[2, 2, 1]}>
      <planeGeometry args={[2, 2]} />
      <shaderMaterial
        ref={materialRef}
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
