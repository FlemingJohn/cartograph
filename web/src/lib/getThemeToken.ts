export function getThemeToken(tokenName: string): string {
  return getComputedStyle(document.documentElement).getPropertyValue(`--${tokenName}`).trim();
}
