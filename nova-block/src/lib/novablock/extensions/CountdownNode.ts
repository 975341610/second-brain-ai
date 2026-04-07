import { Node, mergeAttributes } from '@tiptap/core';
import { ReactNodeViewRenderer } from '@tiptap/react';
import { CountdownComponent } from '../../../components/widgets/CountdownComponent';

export const CountdownNode = Node.create({
  name: 'countdown',
  group: 'block',
  atom: true,
  draggable: true,
  selectable: true,

  addAttributes() {
    return {
      targetDate: {
        default: new Date(Date.now() + 7 * 24 * 60 * 60 * 1000).toISOString(),
      },
      title: {
        default: '倒计时',
      },
    };
  },

  parseHTML() {
    return [{ tag: 'div[data-type="countdown"]' }];
  },

  renderHTML({ HTMLAttributes }) {
    return ['div', mergeAttributes(HTMLAttributes, { 'data-type': 'countdown' })];
  },

  addNodeView() {
    return ReactNodeViewRenderer(CountdownComponent);
  },
});
