## Comparador de PDF

# Descrição

Este projeto consiste em uma aplicação web desenvolvida em Django, que oferece funcionalidades específicas para a visualização e processamento de informações contidas em arquivos PDF. A aplicação possui páginas dedicadas a diferentes entidades, como eventos e processamentos, e oferece a capacidade de comparar informações entre dois arquivos PDF.

---

## Pré-requisitos

Certifique-se de ter o Python e o Django instalados em seu ambiente

### Funcionalidades

#### Página Inicial

A página inicial apresenta links para diferentes seções da aplicação:

- **/home/:** Página inicial.
- **/white/:** Visualização específica para "WHITE".
- **/sucden-rs/:** Visualização específica para "SUCDEN RS".
- **/sucden-pd/:** Visualização específica para "SUCDEN PD".
- **/sucafina/:** Visualização específica para "SUCAFINA".
- **/veloso/:** Visualização específica para "VELOSO".
- **/mercon/:** Visualização específica para "MERCON".

#### Página de Login

- **/login/:** Página de login.

#### Processamento de Arquivos PDF

- **/processar/:** Página para upload de arquivos PDF.
  - Campos para upload de arquivos "ARQUIVO PROCAFE" e "ARQUIVO MERCON".
  - Botão "PROCESSAR" para iniciar o processamento.
  - Exibição dos resultados em tempo real na área de resultados.

### Tecnologias Utilizadas

- Django
- Bootstrap
- jQuery

