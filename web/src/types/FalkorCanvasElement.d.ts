import type { FalkorDBCanvas } from "@falkordb/canvas";
import type { DetailedHTMLProps, HTMLAttributes } from "react";

declare module "react" {
  namespace JSX {
    interface IntrinsicElements {
      "falkordb-canvas": DetailedHTMLProps<HTMLAttributes<FalkorDBCanvas>, FalkorDBCanvas>;
    }
  }
}
