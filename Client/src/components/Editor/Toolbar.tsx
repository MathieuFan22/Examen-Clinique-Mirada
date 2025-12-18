import React from "react";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faFileExport } from '@fortawesome/free-solid-svg-icons';

import { FONT_SIZES } from "./constants";

interface ToolbarProps {
  onToggleStyle: (e: React.MouseEvent, style: string) => void;
  onChangeFontSize: (size: string) => void;
  onExport: () => void;
  fileName: string;
}

export const Toolbar: React.FC<ToolbarProps> = ({ onToggleStyle, onChangeFontSize, onExport }) => {
  return (
    <>
      <div className="header-center">
        <div className="header-toolbar">
          <button className="toolbar-button" onMouseDown={(e) => onToggleStyle(e, "BOLD")}>
            <strong>B</strong>
          </button>
          <button className="toolbar-button" onMouseDown={(e) => onToggleStyle(e, "ITALIC")}>
            <em>I</em>
          </button>
          <button className="toolbar-button" onMouseDown={(e) => onToggleStyle(e, "UNDERLINE")}>
            <u>U</u>
          </button>

          <select className="font-size-select" onChange={(e) => onChangeFontSize(e.target.value)}>
            <option value="">Taille</option>
            {FONT_SIZES.map((size) => (
              <option key={size} value={size}>{size}pt</option>
            ))}
          </select>
        </div>
      </div>

      <div className="header-right">
        <button className="export-button" onClick={onExport}>
          <span className="export-icon">
            <FontAwesomeIcon icon={faFileExport} />
          </span>
          <span>Exporter</span>
        </button>
        <div className="profile-circle">
          <span className="profile-initial">M</span>
        </div>
      </div>
    </>
  );
};