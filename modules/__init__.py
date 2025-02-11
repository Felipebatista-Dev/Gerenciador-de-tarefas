import os
import sys
import json

def get_base_path():
    return getattr(sys, '_MEIPASS', os.path.abspath("."))

caminho_json = os.path.join(get_base_path(), "tasklist.json")

with open(caminho_json, "r", encoding="utf-8") as f:
    data = json.load(f)  # Carrega o JSON como um dicionário