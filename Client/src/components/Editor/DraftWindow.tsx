import React, { useState } from "react";
import { Editor } from "draft-js";
import { useEditorLogic } from "./useEditorLogic";
import { Toolbar } from "./Toolbar";
import { CUSTOM_STYLE_MAP } from "./constants";

import "draft-js/dist/Draft.css";
import "./DraftWindow.css";

const DraftWindow: React.FC = () => {
  const [fileName, setFileName] = useState("Nouveau Document.txt");
  const { 
    editorState, 
    setEditorState, 
    editorRef, 
    focusEditor, 
    toggleInlineStyle, 
    changeFontSize 
  } = useEditorLogic();

  const handleExport = () => {
    console.log("Exporting:", fileName);
  
  };

  return (
    <div className="editor-container">
      <header className="editor-header">
        <div className="header-left">
          <input
            type="text"
            className="file-name-input"
            value={fileName}
            onChange={(e) => setFileName(e.target.value)}
          />
        </div>

        <Toolbar 
          onToggleStyle={toggleInlineStyle}
          onChangeFontSize={changeFontSize}
          onExport={handleExport}
          fileName={fileName}
        />
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
                customStyleMap={CUSTOM_STYLE_MAP}
              />
            </div>
          </div>
        </div>
      </main>
    </div>
  );
};

export default DraftWindow;