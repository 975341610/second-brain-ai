// import { NovaBlockEditor } from './novablock/NovaBlockEditor';
import { ErrorBoundary } from './ErrorBoundary';
import type { Note } from '../lib/types';

type EditorPanelProps = {
  note: Note | null;
  notes: Note[];
  isSaving: boolean;
  onSave: (payload: { id?: number; title: string; content: string; icon?: string; parent_id?: number | null; tags?: string[]; is_title_manually_edited?: boolean; silent?: boolean }) => Promise<void>;
  onUpdateTags?: (noteId: number, tags: string[]) => Promise<void>;
  onCreateSubPage: (parentId: number) => void;
  onSelectNote: (noteId: number) => void;
  onNotify?: (text: string, tone?: 'success' | 'error' | 'info') => void;
  outline: { id: string; text: string; level: number }[];
  references: string[];
  relatedNotes: Note[];
};

export function EditorPanel(props: EditorPanelProps) {
  // Directly delegate to the new NovaBlockEditor for Sprint 3
  return (
    <ErrorBoundary>
      {/* <NovaBlockEditor 
        note={props.note}
        onSave={props.onSave}
        onNotify={props.onNotify}
      /> */}
    </ErrorBoundary>
  );
}
