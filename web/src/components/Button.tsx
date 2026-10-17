import type { ReactNode } from "react";

export function Button({
  children,
  onClick,
  isPrimary = false,
  isDisabled = false,
}: {
  children: ReactNode;
  onClick: () => void;
  isPrimary?: boolean;
  isDisabled?: boolean;
}) {
  return (
    <button
      type="button"
      className="button"
      data-variant={isPrimary ? "primary" : "plain"}
      disabled={isDisabled}
      onClick={onClick}
    >
      {children}
    </button>
  );
}
