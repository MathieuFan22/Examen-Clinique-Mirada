import { useState } from "react";
import { Editor, EditorState } from "draft-js";
import { useEditorLogic } from "./useEditorLogic";
import { Toolbar } from "./Toolbar";
import { CUSTOM_STYLE_MAP } from "./constants";

import "draft-js/dist/Draft.css";
import "./DraftWindow.css";

const DraftWindow: React.FC = () => {
  const [fileName, setFileName] = useState("Nouveau Document.txt");
  const [suggestion, setSuggestion] = useState<string>("");
  const {
    editorState,
    setEditorState,
    editorRef,
    focusEditor,
    toggleInlineStyle,
    changeFontSize,
  } = useEditorLogic();

  const handleExport = () => {
    console.log("Exporting:", fileName);
  };
  const onType = async (newState: EditorState) => {
    const forbidden_start = /^(nb|np|mk|nk|dt|bp|sz)/i;

    setEditorState(newState);

    const plainText = newState.getCurrentContent().getPlainText().split(/\s+/);

    // On récupère le dernier mot non vide
    const last_word = plainText.filter((w) => w.length > 0).at(-1);

    if (last_word && !forbidden_start.test(last_word)) {
      try {
        const response = await fetch(
          "http://192.168.86.241:5000/bigram/get-words",
          {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({ text: last_word }),
          }
        );

        if (response.ok) {
          const data = await response.json();
          if (data.words && data.words.length > 0) {
            // On stocke le premier mot suggéré
            setSuggestion(data.words[0]);
            
          }
        }
      } catch (error) {
        console.error("Erreur lors de l'appel API :", error);
      }
    } else if (last_word && forbidden_start.test(last_word)) {
      console.log("Interdit : le mot commence par nb ou np");
    }
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
            <div className="editor-wrapper" style={{ position: "relative" }}>
              {/* On crée un conteneur flex pour garder la suggestion sur la même ligne */}
              <div
                style={{
                  display: "flex",
                  flexWrap: "wrap",
                  alignItems: "baseline",
                }}
              >
                <div className="draft-inline-container">
                  <Editor
                    ref={editorRef}
                    editorState={editorState}
                    onChange={onType}
                    placeholder="Commencez à taper ici..."
                    customStyleMap={CUSTOM_STYLE_MAP}
                  />
                </div>

                {suggestion && (
                  <span
                    style={{
                      fontStyle: "italic",
                      color: "gray",
                      marginLeft: "4px",
                      pointerEvents: "none",
                      userSelect: "none",
                      whiteSpace: "nowrap",
                    }}
                  >
                    {suggestion}
                  </span>
                )}
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
};

export default DraftWindow;
