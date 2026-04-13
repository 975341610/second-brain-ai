import { ReactRenderer } from '@tiptap/react';
import tippy, { sticky } from 'tippy.js';
import { SlashMenu, type SlashItem } from './SlashMenu';

export const getSuggestionConfig = (itemsRef: React.MutableRefObject<SlashItem[]>, isAiEnabled: boolean = true) => ({
  items: ({ query }: { query: string }) => {
    const items = itemsRef.current;
    const filtered = items.filter(item => {
      // AI 过滤逻辑
      if (item.requiresAI && !isAiEnabled) return false;

      const q = query.toLowerCase();
      return item.label.toLowerCase().includes(q) || item.keywords.some(k => k.toLowerCase().includes(q));
    });
    return filtered.slice(0, 50);
  },

  render: () => {
    let component: any;
    let popup: any;

    return {
      onStart: (props: any) => {
        component = new ReactRenderer(SlashMenu, {
          props,
          editor: props.editor,
        });

        if (!props.clientRect) {
          return;
        }

        popup = tippy('body', {
          getReferenceClientRect: props.clientRect,
          appendTo: () => document.body,
          content: component.element,
          showOnCreate: true,
          interactive: true,
          trigger: 'manual',
          placement: 'bottom-start',
          theme: 'slash-menu',
          arrow: false,
          sticky: true,
          plugins: [sticky],
        });
      },

      onUpdate(props: any) {
        component.updateProps(props);

        if (!props.clientRect) {
          return;
        }

        popup[0].setProps({
          getReferenceClientRect: props.clientRect,
        });
      },

      onKeyDown(props: any) {
        if (props.event.key === 'Escape') {
          popup[0].hide();
          return true;
        }

        return component.ref?.onKeyDown(props);
      },

      onExit() {
        if (popup && popup.length > 0) {
          popup[0].destroy();
        }
        if (component) {
          component.destroy();
        }
      },
    };
  },
});
