# Prompts e decisões de implementação

## Briefing inicial

Criar uma dashboard de vendas Porsche a partir da planilha sanitizada disponibilizada no desafio DIO. Entregar um único index.html com CSS, JavaScript e dados embutidos. Responder: quais modelos geram mais receita, quais estados concentram mais vendas e como as vendas se distribuem pelos métodos de pagamento. Incluir indicadores de quantidade, valor total e ticket médio. Adicionar filtros de modelo, estado, ano do modelo e pagamento, com atualização conjunta dos gráficos e indicadores. Usar português, fundo grafite, detalhes dourados e tipografia Arial/Helvetica. Tornar o painel responsivo e acessível, sem dependências externas.

Este texto registra o briefing consolidado usado para a implementação nesta conversa. Não é uma transcrição de um prompt executado no Canvas.

## Refinamento após inspeção da base

Os valores são em USD e os estados são dos EUA. Preservar essas unidades. Há 24 datas sanitizadas INVALID e 7 registros Cancelled. Converter datas inválidas em nulo, sem inferir uma data substituta. Manter esses registros nas análises por modelo, estado e pagamento. Excluir cancelamentos no filtro inicial, mas permitir consultar todos os registros ou apenas cancelamentos. Diferenciar ano do modelo e data de venda. Não tratar o valor registrado como receita contábil reconhecida. Remover nomes de clientes, vendedores e campos brutos do HTML e dos arquivos tratados.

## Refinamento da experiência

Mostrar todos os modelos em barras ordenadas, com rolagem para evitar esconder categorias em um Top 10. Exibir participação percentual por estado e pagamento. Mostrar uma conclusão calculada abaixo de cada gráfico. Adicionar consulta dos registros filtrados, botão para limpar filtros e estado vazio com ticket médio indisponível quando não houver registros.

## Ferramenta utilizada

Após o acesso autorizado à DIO, foram consultados os materiais complementares e baixadas as versões originais do script Python e do schema. As nove funções do script foram aplicadas aos 100 registros brutos e comparadas com a base sanitizada: 900 campos conferidos, sem divergências. A documentação foi ampliada com arquivos para reproduzir essa conferência e atualizar os dados embutidos no HTML. Isso não significa que os vídeos tenham sido integralmente assistidos nem que um agente personalizado tenha sido criado.

ChatGPT no modo Work/Codex, com código HTML, CSS e JavaScript e análise local da planilha. Não foi utilizado o Canvas nem criado um agente personalizado com skill. A skill de planilhas orientou a inspeção dos dados; ela não constitui o segundo caminho opcional do curso. O projeto não afirma uma comparação entre ferramentas que não foi executada.
