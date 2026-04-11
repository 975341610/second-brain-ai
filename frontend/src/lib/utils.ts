/**
 * Minimal utility for conditional class names
 * Filters out falsy values and joins with a space
 */
export function cn(...inputs: any[]) {
  return inputs.filter(Boolean).join(' ');
}
