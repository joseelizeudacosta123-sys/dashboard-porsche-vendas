"""Compara as funções do curso com a planilha sanitizada, sem criar um XLSX.

Uso: python auditar_base.py BASE_CRUA.xlsx BASE_SANITIZADA.xlsx
"""
import argparse
import collections
import json
from pathlib import Path
from openpyxl import load_workbook
from sanitize_porsche import COLUMN_PIPELINE

def records(path):
    rows = list(load_workbook(path, data_only=True).active.values)
    if not rows:
        raise ValueError('Planilha vazia')
    headers = list(rows[0])
    result = {}
    for values in rows[1:]:
        row = dict(zip(headers, values))
        if row['sale_id'] in result:
            raise ValueError('Identificador de venda duplicado')
        result[row['sale_id']] = row
    return headers, result

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('crua', type=Path)
    parser.add_argument('sanitizada', type=Path)
    args = parser.parse_args()
    raw_headers, raw = records(args.crua)
    clean_headers, clean = records(args.sanitizada)
    expected = []
    for src, dst, fn in COLUMN_PIPELINE:
        expected.append(src)
        if dst:
            expected.append(dst)
    assert clean_headers == expected, 'Ordem ou nomes das colunas divergentes'
    assert set(raw) == set(clean), 'IDs divergentes entre as bases'
    invalid = collections.Counter()
    differences = collections.Counter()
    checked = 0
    for sale_id, row in raw.items():
        for source, target, sanitizer in COLUMN_PIPELINE:
            assert row[source] == clean[sale_id][source], 'Campo bruto alterado'
            if sanitizer:
                value = sanitizer(row[source])
                checked += 1
                if value == 'INVALID':
                    invalid[target] += 1
                if str(value) != str(clean[sale_id][target]):
                    differences[target] += 1
    report = {'registros': len(raw), 'campos_sanitizados_conferidos': checked,
              'colunas_originais_preservadas': True,
              'sanitizadas_imediatamente_apos_origem': True,
              'invalidos_por_coluna': dict(invalid),
              'divergencias_por_coluna': dict(differences)}
    (Path(__file__).resolve().parent / 'relatorio_tratamento.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if differences:
        raise SystemExit(1)

if __name__ == '__main__':
    main()
