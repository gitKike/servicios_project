import os
import ast

ORIGINAL_FILE = "app/models/models.py"
OUTPUT_DIR = "app/models/separados"

# 🧹 Crear o limpiar el directorio de salida
os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(ORIGINAL_FILE, "r") as f:
    content = f.read()
    lines = content.splitlines()

tree = ast.parse(content)
exported_classes = 0
class_names = []

for node in tree.body:
    if isinstance(node, ast.ClassDef):
        class_name = node.name
        class_names.append((class_name, class_name.lower()))
        start_line = node.lineno - 1

        # Encuentra el fin de la clase
        subsequent_classes = [n.lineno - 1 for n in tree.body if isinstance(n, ast.ClassDef) and n.lineno - 1 > start_line]
        end_line = min(subsequent_classes) if subsequent_classes else len(lines)

        class_code = "\n".join(lines[start_line:end_line])
        filename = os.path.join(OUTPUT_DIR, f"{class_name.lower()}.py")

        with open(filename, "w") as f:
            # ✨ Encabezado de imports
            f.write("from __future__ import annotations\n")
            f.write("from typing import Any, Optional, List, TYPE_CHECKING\n")
            f.write("from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime, Numeric, ForeignKey, ForeignKeyConstraint, PrimaryKeyConstraint, UniqueConstraint, CheckConstraint\n")
            #f.write("    ForeignKeyConstraint, PrimaryKeyConstraint, UniqueConstraint, CheckConstraint\n")
            f.write("from sqlalchemy.orm import relationship, Mapped, mapped_column\n")
            f.write("from sqlalchemy.sql import text\n")
            f.write("from sqlalchemy.dialects.postgresql import DOMAIN\n")
            f.write("from app.database.db import Base\n")
            f.write("from app.database.custom_types import CITEXT\n\n")
            f.write("if TYPE_CHECKING: pass\n\n")
            #f.write("    pass\n\n")

            # ✍️ Código real de la clase
            f.write(class_code)

        exported_classes += 1

# 🧩 Generar __init__.py con todos los imports y __all__
init_path = os.path.join(OUTPUT_DIR, "__init__.py")

with open(init_path, "w") as f:
    f.write("# Auto-generado por split_models.py\n\n")
    f.write("__all__ = [\n")
    for class_name, module in sorted(class_names, key=lambda x: x[1]):
        f.write(f"    '{class_name}',\n")
    f.write("]\n\n")

    for class_name, module in sorted(class_names, key=lambda x: x[1]):
        f.write(f"from .{module} import {class_name}\n")

print(f"✅ Se generaron {exported_classes} archivos de modelo en: {OUTPUT_DIR}")
print(f"✅ Archivo __init__.py generado con imports de {exported_classes} clases.")
