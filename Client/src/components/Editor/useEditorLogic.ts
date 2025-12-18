import { useState, useRef } from "react";
import { Editor, EditorState, RichUtils, Modifier } from "draft-js";

export const useEditorLogic = () => {
  const [editorState, setEditorState] = useState(EditorState.createEmpty());
  const editorRef = useRef<Editor>(null);

  const focusEditor = () => editorRef.current?.focus();

  const toggleInlineStyle = (e: React.MouseEvent, style: string) => {
    e.preventDefault();
    setEditorState(RichUtils.toggleInlineStyle(editorState, style));
  };

  const changeFontSize = (size: string) => {
    if (!size) return;

    const selection = editorState.getSelection();
    const contentState = editorState.getCurrentContent();
    let newContentState = contentState;
    const currentStyles = editorState.getCurrentInlineStyle();

    // Remove existing font sizes
    currentStyles.forEach((style) => {
      if (style?.startsWith("FONTSIZE-")) {
        newContentState = Modifier.removeInlineStyle(newContentState, selection, style);
      }
    });

    // Apply new size
    newContentState = Modifier.applyInlineStyle(newContentState, selection, `FONTSIZE-${size}`);

    const nextState = EditorState.push(editorState, newContentState, "change-inline-style");
    setEditorState(EditorState.forceSelection(nextState, selection));
    setTimeout(() => focusEditor(), 0);
  };

  return {
    editorState,
    setEditorState,
    editorRef,
    focusEditor,
    toggleInlineStyle,
    changeFontSize,
  };
};