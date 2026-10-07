# Validação

Conferência independente da planilha: 100 registros, 93 não cancelados e 7 cancelados. Valores e ticket médio reconciliados com a base sanitizada. Foram conferidos os tipos numéricos, a unicidade dos registros e a exclusão dos campos com nomes de clientes e vendedores.

Conferência com o script original do curso: 900 campos sanitizados comparados, sem divergências. Colunas brutas preservadas e colunas tratadas imediatamente após as respectivas fontes. Apenas a coluna de datas produziu INVALID, em 24 registros. O relatório está em `relatorio_tratamento.json` e a conferência pode ser repetida com `auditar_base.py`.

O atualizador `preparar_dashboard.py` foi executado sobre a planilha sanitizada e manteve os 100 registros. Depois da atualização, os 94 recortes do teste de lógica passaram novamente.

O JavaScript do HTML foi executado em ambiente de teste com representação dos elementos da página. Foram testadas todas as opções individuais de modelo, estado, ano do modelo e pagamento, as situações, o botão de restauração e uma combinação sem registros. Quantidade, valor total, modelos distintos e número de linhas da tabela foram comparados a cálculos independentes.

Limitação: não foi possível concluir a validação visual em navegador neste ambiente, pois o navegador local necessário não estava disponível. Não foram produzidos prints que simulem uma execução real. Depois da publicação, é necessário abrir o painel no navegador, confirmar o layout no computador e no celular e registrar um print geral e outro com filtro aplicado.

A publicação no GitHub Pages permanece pendente da conexão com a conta do autor. Não houve verificação de um link publicado.
