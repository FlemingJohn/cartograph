export function getScanId(): string {
  return import.meta.env.VITE_SCAN_ID ?? "scan-1";
}
