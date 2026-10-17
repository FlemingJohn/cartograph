import type { ReactNode } from "react";

export function Pane({
  title,
  aside,
  children,
}: {
  title: string;
  aside?: ReactNode;
  children: ReactNode;
}) {
  return (
    <section className="pane" aria-label={title}>
      <header className="pane-head">
        <h2 className="label">{title}</h2>
        {aside}
      </header>
      <div className="pane-body">{children}</div>
    </section>
  );
}
