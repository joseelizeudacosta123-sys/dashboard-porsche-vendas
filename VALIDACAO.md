# Validação

Conferência independente da planilha: 100 registros, 93 não cancelados e 7 cancelados. Valores e ticket médio reconciliados com a base sanitizada. Foram conferidos os tipos numéricos, a unicidade dos registros e a exclusão dos campos com nomes de clientes e vendedores.

Conferência com o script original do curso: 900 campos sanitizados comparados, sem divergências. Colunas brutas preservadas e colunas tratadas imediatamente após as respectivas fontes. Apenas a coluna de datas produziu INVALID, em 24 registros. O relatório está em `relatorio_tratamento.json` e a conferência pode ser repetida com `auditar_base.py`.

O atualizador `preparar_dashboard.py` foi executado sobre a planilha sanitizada e manteve os 100 registros. Depois da atualização, os 94 recortes do teste de lógica passaram novamente.

O JavaScript do HTML foi executado em ambiente de teste com representação dos elementos da página. Foram testadas todas as opções individuais de modelo, estado, ano do modelo e pagamento, as situações, o botão de restauração e uma combinação sem registros. Quantidade, valor total, modelos distintos e número de linhas da tabela foram comparados a cálculos independentes.

GitHub Pages publicado e verificado no navegador em 7 de outubro de 2026. O fluxo de publicação terminou com sucesso. O layout no computador foi inspecionado e dois screenshots reais foram registrados: `dashboard-geral.jpg` e `dashboard-filtro-ca.jpg`.

O filtro Estado = CA apresentou 16 registros e US$ 1.973.350,00. As situações Todos e Somente cancelamentos apresentaram 100 e 7 registros; Limpar filtros restaurou 93. Não foram observados erros de console originados pela dashboard; o navegador registrou mensagens de sua própria extensão.

O layout possui regras responsivas, mas não houve inspeção visual em um aparelho celular.
