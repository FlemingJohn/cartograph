import { getApiUrl } from "./getApiUrl";

export async function sendJson(method: "POST" | "DELETE", path: string, body: object): Promise<void> {
  const response = await fetch(getApiUrl(path), {
    method,
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  }).catch(() => {
    throw new Error(
      `Could not reach the backend at ${getApiUrl("")}. Start it, or restart it if it runs old code.`,
    );
  });
  if (!response.ok) {
    throw new Error(`${path} answered ${response.status}: ${await response.text()}`);
  }
}
