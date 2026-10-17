import { getApiUrl } from "./getApiUrl";

export async function getJson<Result>(path: string): Promise<Result | null> {
  try {
    const response = await fetch(getApiUrl(path));
    return response.ok ? ((await response.json()) as Result) : null;
  } catch {
    return null;
  }
}
