"""Atualiza os dados públicos e o HTML a partir da planilha sanitizada.

Uso: python preparar_dashboard.py CAMINHO_DA_PLANILHA_SANITIZADA
Não altera a planilha de entrada. Não publica nomes nem campos brutos.
"""
import argparse
import csv
import datetime as dt
import json
import math
from pathlib import Path
from openpyxl import load_workbook

FIELDS = {
    'modelo': 'PorscheModelSanitized',
    'ano_modelo': 'ModelYearSanitized',
    'preco': 'SalesPriceSanitized',
    'cidade': 'CitySanitized',
    'estado': 'StateSanitized',
    'pagamento': 'PayMethodSanitized',
    'data_venda': 'SaleDateSanitized',
    'situacao': 'DeliveryStatusSanitized',
}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('planilha', type=Path)
    args = parser.parse_args()
    project = Path(__file__).resolve().parent
    rows = list(load_workbook(args.planilha, data_only=True).active.values)
    if not rows:
        raise ValueError('Planilha vazia')
    headers = list(rows[0])
    missing = set(FIELDS.values()) - set(headers)
    if missing:
        raise ValueError(f'Colunas sanitizadas ausentes: {sorted(missing)}')
    data = []
    for line, row in enumerate(rows[1:], start=2):
        if not any(value is not None for value in row):
            continue
        source = dict(zip(headers, row))
        item = {key: source[column] for key, column in FIELDS.items()}
        for key in FIELDS:
            if item[key] is None or str(item[key]).strip() == '':
                raise ValueError(f'Linha {line}: campo sanitizado vazio ({key})')
        try:
            price = float(item['preco'])
            year = float(item['ano_modelo'])
        except (ValueError, TypeError) as exc:
            raise ValueError(f'Linha {line}: preço ou ano inválido; revisar antes de publicar') from exc
        if not math.isfinite(price) or price < 0 or not math.isfinite(year) or not year.is_integer() or not 1990 <= year <= 2035:
            raise ValueError(f'Linha {line}: preço ou ano fora do formato esperado')
        item['preco'] = price
        item['ano_modelo'] = int(year)
        if item['data_venda'] == 'INVALID':
            item['data_venda'] = None
        else:
            value = str(item['data_venda'])
            if dt.date.fromisoformat(value).isoformat() != value:
                raise ValueError(f'Linha {line}: data não está no padrão ISO')
        data.append(item)
    payload = json.dumps(data, ensure_ascii=False, allow_nan=False)
    # Não deixa conteúdo externo encerrar a tag script do HTML.
    payload = payload.replace('<', '\\u003c').replace('>', '\\u003e').replace('&', '\\u0026')
    page = project / 'index.html'
    html = page.read_text(encoding='utf-8')
    start = html.index('const DATA=') + len('const DATA=')
    end = html.index(';\nconst money=', start)
    page.write_text(html[:start] + payload + html[end:], encoding='utf-8')
    (project / 'dados_sanitizados.json').write_text(json.dumps(data, ensure_ascii=False, indent=2, allow_nan=False), encoding='utf-8')
    with (project / 'dados_sanitizados.csv').open('w', newline='', encoding='utf-8-sig') as stream:
        writer = csv.DictWriter(stream, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(data)
    print(f'{len(data)} registros preparados. Nomes e campos brutos não foram exportados.')

if __name__ == '__main__':
    main()
