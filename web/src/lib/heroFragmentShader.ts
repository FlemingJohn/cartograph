export const heroFragmentShader = `
uniform float uTime;
uniform vec3 uColor1;
uniform vec3 uColor2;
varying vec2 vUv;

vec3 permute(vec3 x) { return mod(((x * 34.0) + 1.0) * x, 289.0); }

float snoise(vec2 v) {
  const vec4 C = vec4(0.211324865405187, 0.366025403784439, -0.577350269189626, 0.024390243902439);
  vec2 i = floor(v + dot(v, C.yy));
  vec2 x0 = v - i + dot(i, C.xx);
  vec2 i1 = (x0.x > x0.y) ? vec2(1.0, 0.0) : vec2(0.0, 1.0);
  vec4 x12 = x0.xyxy + C.xxzz;
  x12.xy -= i1;
  i = mod(i, 289.0);
  vec3 p = permute(permute(i.y + vec3(0.0, i1.y, 1.0)) + i.x + vec3(0.0, i1.x, 1.0));
  vec3 m = max(0.5 - vec3(dot(x0, x0), dot(x12.xy, x12.xy), dot(x12.zw, x12.zw)), 0.0);
  m = m * m;
  m = m * m;
  vec3 x = 2.0 * fract(p * C.www) - 1.0;
  vec3 h = abs(x) - 0.5;
  vec3 ox = floor(x + 0.5);
  vec3 a0 = x - ox;
  m *= 1.79284291400159 - 0.85373472095314 * (a0 * a0 + h * h);
  vec3 g;
  g.x = a0.x * x0.x + h.x * x0.y;
  g.yz = a0.yz * x12.xz + h.yz * x12.yw;
  return 130.0 * dot(m, g);
}

float bayerDither(vec2 coord) {
  int x = int(mod(coord.x, 4.0));
  int y = int(mod(coord.y, 4.0));
  int levels[16];
  levels[0] = 0; levels[1] = 8; levels[2] = 2; levels[3] = 10;
  levels[4] = 12; levels[5] = 4; levels[6] = 14; levels[7] = 6;
  levels[8] = 3; levels[9] = 11; levels[10] = 1; levels[11] = 9;
  levels[12] = 15; levels[13] = 7; levels[14] = 13; levels[15] = 5;
  return float(levels[y * 4 + x]) / 16.0;
}

void main() {
  vec2 uv = vUv;
  float noise = snoise(uv * 1.5 + vec2(uTime * 0.05, uTime * 0.03)) * 0.25;
  float gradient = (uv.x + uv.y) * 0.5 * 1.2 + noise;

  vec3 deepBlue = uColor1;
  vec3 paleBlue = uColor2;
  vec3 softBlue = mix(deepBlue, paleBlue, 0.33);
  vec3 lightBlue = mix(deepBlue, paleBlue, 0.66);

  vec3 color = paleBlue;
  if (gradient < 0.3) { color = deepBlue; }
  else if (gradient < 0.55) { color = softBlue; }
  else if (gradient < 0.8) { color = lightBlue; }

  float dither = bayerDither(gl_FragCoord.xy);
  bool isStepEdge = fract(gradient * 4.0) > dither * 0.5;
  if (gradient < 0.3 && isStepEdge) { color = softBlue; }
  else if (gradient < 0.55 && isStepEdge) { color = lightBlue; }
  else if (gradient < 0.8 && isStepEdge) { color = paleBlue; }

  float cornerFade = smoothstep(0.0, 0.25, length(uv));
  color = mix(vec3(1.0), color, cornerFade);
  float vignette = smoothstep(1.2, 0.3, length(uv - 0.5));
  color = mix(color, color * 0.95, (1.0 - vignette) * 0.3);

  gl_FragColor = vec4(color, 1.0);
}
`;
