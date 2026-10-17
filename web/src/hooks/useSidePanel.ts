import { useState } from "react";

const storageKey = "cartograph-side-panel-folded";

export function useSidePanel() {
  const [isFolded, setIsFolded] = useState(readSavedFolded);

  function toggleFolded() {
    setIsFolded((current) => {
      saveFolded(!current);
      return !current;
    });
  }

  return { isFolded, toggleFolded };
}

function readSavedFolded(): boolean {
  try {
    return localStorage.getItem(storageKey) === "true";
  } catch {
    return false;
  }
}

function saveFolded(isFolded: boolean) {
  try {
    localStorage.setItem(storageKey, String(isFolded));
  } catch {
    return;
  }
}
