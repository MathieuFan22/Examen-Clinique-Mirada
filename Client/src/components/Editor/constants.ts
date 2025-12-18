/* eslint-disable @typescript-eslint/no-explicit-any */
import type { DraftStyleMap } from "draft-js";

export const FONT_SIZES = ["8", "10", "12", "14", "16", "18", "20", "24", "32"];

export const CUSTOM_STYLE_MAP: DraftStyleMap = FONT_SIZES.reduce((map, size) => {
  map[`FONTSIZE-${size}`] = { fontSize: `${size}pt` };
  return map;
}, {} as any);