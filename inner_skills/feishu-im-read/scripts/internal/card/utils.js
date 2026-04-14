/**
 * Copied from feishu-openclaw-plugin/src/messaging/converters/utils.js
 *
 * Adapted: safeParse accepts already-parsed objects (API history returns
 * json_attachment as an object, not a string).
 */
export function safeParse(raw) {
  if (raw != null && typeof raw === "object") return raw;
  try {
    return JSON.parse(raw);
  } catch {
    return undefined;
  }
}

export function escapeRegExp(str) {
  return str.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}
