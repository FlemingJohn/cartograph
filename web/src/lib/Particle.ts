const reachRadius = 120;
const friction = 0.85;

export class Particle {
  x: number;
  y: number;
  originX: number;
  originY: number;
  speedX: number;
  speedY: number;
  size: number;
  colour: string;
  pushStrength: number;
  returnSpeed: number;

  constructor(
    originX: number,
    originY: number,
    size: number,
    colour: string,
    pushStrength: number,
    returnSpeed: number,
  ) {
    this.size = size;
    this.colour = colour;
    this.pushStrength = pushStrength;
    this.returnSpeed = returnSpeed;
    this.originX = originX;
    this.originY = originY;
    this.x = originX + (Math.random() - 0.5) * 10;
    this.y = originY + (Math.random() - 0.5) * 10;
    this.speedX = (Math.random() - 0.5) * 5;
    this.speedY = (Math.random() - 0.5) * 5;
  }

  update(pointerX: number, pointerY: number) {
    this.pushAwayFrom(pointerX, pointerY);
    this.speedX = (this.speedX + (this.originX - this.x) * this.returnSpeed) * friction;
    this.speedY = (this.speedY + (this.originY - this.y) * this.returnSpeed) * friction;
    this.x += this.speedX;
    this.y += this.speedY;
  }

  draw(context: CanvasRenderingContext2D) {
    context.fillStyle = this.colour;
    context.beginPath();
    context.arc(this.x, this.y, this.size, 0, Math.PI * 2);
    context.fill();
  }

  private pushAwayFrom(pointerX: number, pointerY: number) {
    const distanceX = pointerX - this.x;
    const distanceY = pointerY - this.y;
    const distance = Math.hypot(distanceX, distanceY);
    if (distance === 0 || distance >= reachRadius) return;
    const force = ((reachRadius - distance) / reachRadius) * this.pushStrength;
    this.speedX -= (distanceX / distance) * force;
    this.speedY -= (distanceY / distance) * force;
  }
}
