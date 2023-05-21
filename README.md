O projeto DATA_GAMES trata arquivos em excel retirados de um banco de dados em cloud, a fim de servir para análises e geração de insigths.

Etapas:

1 - separador.py gera um novo arquivo csv separado por ;

2 - linhas_em_branco.py deleta todas as linhas em branco encontradas no dataset

2 - transformador.py transforma strings em int subistituindo o "k" por 3 zeros.

OBS: Sempre que o dataset passa por uma função python neste projeto, é gerado um novo arquivo com a função aplicada e mantido o original caso sejam necesários eventuais "hold back".

Como executar? 
O projeto pode ser clonado para a sua máquina local e aberto o arquivo .pbix que é o dashboard em power bi ou acessar o link do dashboard disponível na net em:

"https://app.powerbi.com/view?r=eyJrIjoiZDJiNTI5NWEtZGJlNC00NmMzLThkMGQtYzk1ZGI4MGY0NzEyIiwidCI6ImE5M2YyOTk3LTRjNGMtNDk2ZS05OTk5LTZkNTEzY2Y1ODFjZiJ9"

Não esqueça de retirar as aspas.