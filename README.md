# Projeto de Geração de Energia Solar em Organizações Militares de Saúde (OMS)

Este projeto desenvolve um modelo analítico aproximado que permite auxiliar na escolha das primeiras Organizações Militares de Saúde (OMS) onde serão implementadas usinas fotovoltaicas e das possíveis soluções a serem adotadas, a depender do perfil em que as unidades se encaixam.

## Descrição

O código faz uma análise para determinar o equipamento apropriado e a área necessária para a instalação de painéis solares em vários hospitais militares brasileiros, com o objetivo de reduzir seus custos de energia. A análise é baseada em diversos fatores, incluindo a demanda média de energia do hospital, as horas de pico de sol por dia e o consumo médio de energia.

## Funcionalidades

1. O código começa lendo um arquivo CSV que contém os dados de entrada para a análise.
2. Para cada hospital, é criado um objeto Cliente que contém as características relevantes do hospital.
3. Para cada Cliente, o código determina o inversor adequado e o painel solar a ser usado.
4. O código calcula o número de painéis solares necessários e a área total necessária para a instalação.
5. Os resultados são adicionados a um novo arquivo CSV para análise posterior.

## Como usar

1. Clone o repositório
2. Certifique-se de ter Python instalado em sua máquina, bem como as bibliotecas pandas e numpy.
3. Execute o arquivo `main.py` através do terminal usando o comando `python main.py`.
4. O script lerá os dados do arquivo `VMHospitais.csv` e escreverá os resultados no arquivo `VMHospitais_with_areas.csv`.

## Dependências

- Python
- pandas
- numpy

## Contribuições

Este projeto está aberto a contribuições. Sinta-se à vontade para abrir um issue ou fazer um pull request.

## Licença

Este projeto está licenciado sob a licença MIT.