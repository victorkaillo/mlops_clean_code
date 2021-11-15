# Princípios de código limpo para Data Science e aprendizado de máquina
Autores:
Júlia Guardiani e
Víctor Kaillo


Data:
Nov. 2021

Dsiciplimna: PROJETO DE SISTEMAS BASEADOS EM APRENDIZADO DE MÁQUINA - T01


Professor: Ivanovitch Medeiros Dantas da Silva


# Um resumo da solução para o projeto guiado: [Exploring eBay Car Sales Data](https://app.dataquest.io/c/54/m/294/guided-project%3A-exploring-ebay-car-sales-data/)
  O arquivo []() contém um Jupyter Notebook que é nossa implementação do projeto guiado. Trabalhando com um conjunto de dados de carros usados do eBay Kleinanzeigen, uma seção de classificados do site alemão do eBay. O conjunto de dados foi originalmente alterado e carregado no Kaggle pelo usuário orgesleka. O conjunto de dados original não está mais disponível no Kaggle, mas você pode encontrá-lo em [Data Society: used cars data](https://data.world/data-society/used-cars-data). O objetivo deste projeto é limpar os dados e analisar as listagens de carros usados incluídas. Nesse ínterim, familiarizamo-nos com alguns dos benefícios exclusivos que o notebook jupyter oferece para pandas.
  
# Clean Code no projeto guiado
Aproveitando o estudo do projeto guiado para exemplificar e aprender melhor como utilizar as regras do clean code com a ajuda de quatro ferramentas, pycodestyle, pylint, autopep8 e nbQA para automatizar/checar o código. A seguir, um exemplo real utilizando o pylint no projeto guiado.

## Pylint
Seguindo o estilo recomendado pelo PEP 8, o pylint verifica bugs e otimiza a qualidade do código fonte para a linguagem de programação Python. Ao utilizar a ferramenta, não obtemos o retorno do código analisado, mas uma verificação de erros segundo as recomendações de estilo e uma nota gerada automaticamente segundo os erros. A primeira execução do código pelo pylint está mostrada logo abaixo, com nota negativa de -1.40. 
OBS: para chamar a ferramate: pylint exemplo.py


	PS C:\Users\julia\mlops_clean_code> pylint trabalho_01_cleancode.py
	trabalho_01_cleancode.py:10:0: C0301: Line too long (229/100) (line-too-long)
	trabalho_01_cleancode.py:14:0: C0301: Line too long (125/100) (line-too-long)
	trabalho_01_cleancode.py:73:84: C0303: Trailing whitespace (trailing-whitespace)
	trabalho_01_cleancode.py:88:75: C0303: Trailing whitespace (trailing-whitespace)
	trabalho_01_cleancode.py:126:102: C0303: Trailing whitespace (trailing-whitespace)
	trabalho_01_cleancode.py:126:0: C0301: Line too long (102/100) (line-too-long)
	trabalho_01_cleancode.py:186:0: C0301: Line too long (255/100) (line-too-long)
	trabalho_01_cleancode.py:9:0: W0105: String statement has no effect (pointless-string-statement)
	trabalho_01_cleancode.py:40:0: C0413: Import "import pandas as pd" should be placed at the top of the module (wrong-import-position)   
	trabalho_01_cleancode.py:41:0: C0413: Import "import numpy as np" should be placed at the top of the module (wrong-import-position)
	trabalho_01_cleancode.py:42:0: C0413: Import "import requests" should be placed at the top of the module (wrong-import-position)
	trabalho_01_cleancode.py:43:0: C0413: Import "import io" should be placed at the top of the module (wrong-import-position)
	trabalho_01_cleancode.py:47:0: C0103: Constant name "url" doesn't conform to UPPER_CASE naming style (invalid-name)
	trabalho_01_cleancode.py:51:0: E1101: Instance of 'TextFileReader' has no 'head' member; maybe 'read'? (no-member)
	trabalho_01_cleancode.py:55:16: E1101: Instance of 'TextFileReader' has no 'columns' member (no-member)
	trabalho_01_cleancode.py:60:0: E1101: Instance of 'TextFileReader' has no 'rename' member (no-member)
	trabalho_01_cleancode.py:64:0: E1101: Instance of 'TextFileReader' has no 'head' member; maybe 'read'? (no-member)
	trabalho_01_cleancode.py:68:0: E1101: Instance of 'TextFileReader' has no 'describe' member (no-member)
	trabalho_01_cleancode.py:71:0: W0105: String statement has no effect (pointless-string-statement)
	trabalho_01_cleancode.py:84:0: E1101: Instance of 'TextFileReader' has no 'rename' member (no-member)
	trabalho_01_cleancode.py:85:0: E1136: Value 'autos' is unsubscriptable (unsubscriptable-object)
	trabalho_01_cleancode.py:90:8: E1136: Value 'autos' is unsubscriptable (unsubscriptable-object)
	trabalho_01_cleancode.py:90:14: E1136: Value 'autos' is unsubscriptable (unsubscriptable-object)
	trabalho_01_cleancode.py:128:0: W0106: Expression "(~autos['registration_year'].between(1930, 2016)).sum() / autos.shape[0]" is assigned to nothing (expression-not-assigned)
	trabalho_01_cleancode.py:143:0: W0104: Statement seems to have no effect (pointless-statement)
	trabalho_01_cleancode.py:182:0: W0104: Statement seems to have no effect (pointless-statement)
	trabalho_01_cleancode.py:185:0: W0105: String statement has no effect (pointless-string-statement)
	trabalho_01_cleancode.py:41:0: W0611: Unused numpy imported as np (unused-import)
	trabalho_01_cleancode.py:43:0: C0411: standard import "import io" should be placed before "import pandas as pd" (wrong-import-order)
	-------------------------------------------------------------------
	Your code has been rated at -1.40/10 


Em alguma linhas, quando usávamos o ".head()" ou o próprio data frame para selecionar uma coluna específica, o pylint não reconhece a correção gerando um erro de " Value 'autos' is unsubscriptable (unsubscriptable-object)". Após conferir em algumas documentações vimos que era uma falha de reconhecimento. Por isso, desativamos a ferramenta pylint em algumas linhas de código. Mesmo realizando as correções sugeridas pelo pylint não foi possível conseguir uma nota acima dos 9,5 como recomendado pelo professor, pois se a mensagem  “ Value 'autos' is unsubscriptable (unsubscriptable-object)” fosse realizada como sugerida pelo pylint o código ficaria errado, nao satisfazendo a proposta inicial do projeto guiado. 


	PS C:\Users\julia\mlops_clean_code> pylint trabalho_01_cleancode.py
	************* Module trabalho_01_cleancode
	trabalho_01_cleancode.py:45:8: E1136: Value 'autos' is unsubscriptable (unsubscriptable-object)
	trabalho_01_cleancode.py:45:14: E1136: Value 'autos' is unsubscriptable (unsubscriptable-object)

	------------------------------------------------------------------
	Your code has been rated at 7.96/10 (previous run: 7.96/10, +0.00)

O código a seguir é um comentário para cancelar alguma linha da correção específica:

	#pylint: disable=E1101



