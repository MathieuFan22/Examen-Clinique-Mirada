/* eslint-disable no-empty-pattern */
import React, { useState, useRef } from "react";
import {
  Editor,
  EditorState,
  RichUtils,
  Modifier,
  type DraftStyleMap,
} from "draft-js";
import "draft-js/dist/Draft.css";
import "./DraftWindow.css";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faFileExport } from '@fortawesome/free-solid-svg-icons';

interface DraftWindowProps {
  initialContent?: string;
}

const DraftWindow: React.FC<DraftWindowProps> = ({}) => {
  const [editorState, setEditorState] = useState(EditorState.createEmpty());
  const [fileName, setFileName] = useState<string>("Nouveau Document.txt");
  const editorRef = useRef<Editor>(null);

  const customStyleMap: DraftStyleMap = {
    "FONTSIZE-8": { fontSize: "8pt" },
    "FONTSIZE-10": { fontSize: "10pt" },
    "FONTSIZE-12": { fontSize: "12pt" },
    "FONTSIZE-14": { fontSize: "14pt" },
    "FONTSIZE-16": { fontSize: "16pt" },
    "FONTSIZE-18": { fontSize: "18pt" },
    "FONTSIZE-20": { fontSize: "20pt" },
    "FONTSIZE-24": { fontSize: "24pt" },
    "FONTSIZE-32": { fontSize: "32pt" },
  };

  const focusEditor = () => {
    editorRef.current?.focus();
  };

  const handleInlineStyle = (e: React.MouseEvent, style: string) => {
    e.preventDefault(); 
    setEditorState(RichUtils.toggleInlineStyle(editorState, style));
  };

  const changeFontSize = (size: string) => {
    if (!size) return;

    const selection = editorState.getSelection();
    const contentState = editorState.getCurrentContent();

    let newContentState = contentState;
    const currentStyles = editorState.getCurrentInlineStyle();
    
    currentStyles.forEach((style) => {
      if (style && style.startsWith("FONTSIZE-")) {
        newContentState = Modifier.removeInlineStyle(newContentState, selection, style);
      }
    });

    newContentState = Modifier.applyInlineStyle(
      newContentState,
      selection,
      `FONTSIZE-${size}`
    );

    const nextState = EditorState.push(editorState, newContentState, "change-inline-style");
    setEditorState(EditorState.forceSelection(nextState, selection));
    
    setTimeout(() => focusEditor(), 0);
  };

  return (
    <div className="editor-container">
      {/* Header */}
      <header className="editor-header">
        <div className="header-left">
          <input
            type="text"
            className="file-name-input"
            value={fileName}
            onChange={(e) => setFileName(e.target.value)}
            placeholder="Nom du fichier"
          />
        </div>

        <div className="header-center">
          <div className="header-toolbar">
            <button
              className="toolbar-button"
              onMouseDown={(e) => handleInlineStyle(e, "BOLD")}
              title="Gras"
            >
              <strong>B</strong>
            </button>
            <button
              className="toolbar-button"
              onMouseDown={(e) => handleInlineStyle(e, "ITALIC")}
              title="Italique"
            >
              <em>I</em>
            </button>
            <button
              className="toolbar-button"
              onMouseDown={(e) => handleInlineStyle(e, "UNDERLINE")}
              title="Souligné"
            >
              <u>U</u>
            </button>

            <select
              className="font-size-select"
              onChange={(e) => changeFontSize(e.target.value)}
              title="Taille de police"
            >
              <option value="">Taille</option>
              <option value="8">8pt</option>
              <option value="10">10pt</option>
              <option value="12">12pt</option>
              <option value="14">14pt</option>
              <option value="16">16pt</option>
              <option value="18">18pt</option>
              <option value="20">20pt</option>
              <option value="24">24pt</option>
              <option value="32">32pt</option>
            </select>
          </div>
        </div>

        <div className="header-right">
          <button className="export-button" onClick={() => console.log("Export:", fileName)}>
            <span className="export-icon"><FontAwesomeIcon icon={faFileExport} /></span>
            <span>Exporter</span>
          </button>
          <div className="profile-circle">
            <span className="profile-initial">M</span>
          </div>
        </div>
      </header>

      <main className="editor-main" onClick={focusEditor}>
        <div className="a4-container">
          <div className="a4-sheet">
            <div className="editor-wrapper">
              <Editor
                ref={editorRef}
                editorState={editorState}
                onChange={setEditorState}
                placeholder="Commencez à taper ici..."
                customStyleMap={customStyleMap}
              />
            </div>
          </div>
        </div>
      </main>
    </div>
  );
};

export default DraftWindow;