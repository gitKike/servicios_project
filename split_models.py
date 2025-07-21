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
#class_defs = [node for node in tree.body if isinstance(node, ast.ClassDef)]
class_defs = [node for node in tree.body if isinstance(node, ast.ClassDef) and node.name != "Base"]

# Map: nombre_clase -> nombre_archivo
class_names = [(cls.name, cls.name.lower()) for cls in class_defs]
class_name_set = {name for name, _ in class_names}

for node in class_defs:
    class_name = node.name
    start_line = node.lineno - 1
    subsequent_lines = [n.lineno - 1 for n in class_defs if n.lineno - 1 > start_line]
    end_line = min(subsequent_lines) if subsequent_lines else len(lines)
    class_code = "\n".join(lines[start_line:end_line])

    filename = os.path.join(OUTPUT_DIR, f"{class_name.lower()}.py")

    # Detectar clases base (herencia)
    base_imports = []
    for base in node.bases:
        if isinstance(base, ast.Name) and base.id in class_name_set and base.id != "Base":
            base_imports.append(base.id)

    with open(filename, "w") as f:
        # ✅ Encabezado con todos los imports necesarios
        f.write("from __future__ import annotations\n")
        f.write("import decimal\n")
        f.write("import datetime\n")
        f.write("import uuid\n")
        f.write("from typing import Any, Optional, List, TYPE_CHECKING\n")
        f.write("from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime, Numeric, ForeignKey, ForeignKeyConstraint, PrimaryKeyConstraint, UniqueConstraint, CheckConstraint\n")
        #f.write("    ForeignKeyConstraint, PrimaryKeyConstraint, UniqueConstraint, CheckConstraint\n")
        f.write("from sqlalchemy.orm import relationship, Mapped, mapped_column\n")
        f.write("from sqlalchemy.sql import text\n")
        f.write("from sqlalchemy.dialects.postgresql import DOMAIN\n")
        f.write("from app.database.db import Base\n")
        f.write("from app.database.custom_types import CITEXT\n\n")

        # 🧠 Importar clases base reales para herencia
        for base in sorted(set(base_imports)):
            f.write(f"from app.models.separados.{base.lower()} import {base}\n")
        f.write("\n")

        # 👁️ También, por si usás mypy o editores
        f.write("if TYPE_CHECKING:\n")
        if base_imports:
            for base in sorted(set(base_imports)):
                f.write(f"    from app.models.separados.{base.lower()} import {base}\n")
        else:
            f.write("    pass\n")
        f.write("\n")

        f.write(class_code)

    exported_classes += 1

# Generar __init__.py
init_path = os.path.join(OUTPUT_DIR, "__init__.py")

with open(init_path, "w") as f:
    f.write("# Auto-generado por split_models.py\n\n")
    f.write("__all__ = [\n")
    for class_name, _ in sorted(class_names, key=lambda x: x[1]):
        f.write(f"    '{class_name}',\n")
    f.write("]\n\n")

    for class_name, module in sorted(class_names, key=lambda x: x[1]):
        f.write(f"from .{module} import {class_name}\n")

print(f"✅ Se generaron {exported_classes} archivos de modelo en: {OUTPUT_DIR}")
print(f"✅ Archivo __init__.py generado con imports de {exported_classes} clases.")
