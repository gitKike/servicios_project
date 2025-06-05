import os
import ast

ORIGINAL_FILE = "app/models/models.py"
OUTPUT_DIR = "app/models/separados"

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(ORIGINAL_FILE, "r") as f:
    content = f.read()
    lines = content.splitlines()

tree = ast.parse(content)

exported_classes = 0

for node in tree.body:
    if isinstance(node, ast.ClassDef):
        class_name = node.name
        start_line = node.lineno - 1

        # Encuentra el final de la clase
        subsequent_classes = [n.lineno - 1 for n in tree.body if isinstance(n, ast.ClassDef) and n.lineno - 1 > start_line]
        end_line = min(subsequent_classes) if subsequent_classes else len(lines)

        class_code = "\n".join(lines[start_line:end_line])

        filename = os.path.join(OUTPUT_DIR, f"{class_name.lower()}.py")

        with open(filename, "w") as f:
            # 🧠 Imports para que no subraye nada
            f.write("from __future__ import annotations\n")
            f.write("from typing import Any, Optional, List, TYPE_CHECKING\n")
            f.write("from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime, Numeric, ForeignKey, ForeignKeyConstraint, PrimaryKeyConstraint, UniqueConstraint, CheckConstraint\n")
            #f.write("    ForeignKeyConstraint, PrimaryKeyConstraint, UniqueConstraint, CheckConstraint\n")
            f.write("from sqlalchemy.orm import relationship, Mapped, mapped_column\n")
            f.write("from sqlalchemy.sql import text\n")
            f.write("from sqlalchemy.dialects.postgresql import DOMAIN\n")
            f.write("from app.database.db import Base\n")
            f.write("from app.database.custom_types import CITEXT\n\n")
            f.write("# Opcional: imports de otras entidades para type checking\n")
            f.write("if TYPE_CHECKING:\n")
            f.write("    pass  # aquí puedes agregar from ... import ... si querés autocompletado\n\n")
            f.write(class_code)

        exported_classes += 1

print(f"✅ Se generaron {exported_classes} archivos de modelo en: {OUTPUT_DIR}")
