/**
 * Common Types for NovaBlock
 */

export interface NoteMetadata {
  id: number;
  title: string;
  created_at: string;
  updated_at: string;
  tags?: string[];
  parent_id?: number | null;
  notebook_id?: number | null;
  icon?: string | null;
  is_title_manually_edited?: boolean;
  file_path?: string;
  [key: string]: any;
}

export interface SaveNoteParams {
  id: number;
  content: string;
  metadata: NoteMetadata;
  silent?: boolean;
}

export interface NoteData {
  content: string;
  metadata: NoteMetadata;
}
