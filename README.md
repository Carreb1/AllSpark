# Projeto AllSpark - CubeSat

Bem-vindo ao repositório oficial do **Projeto AllSpark**, uma iniciativa do grupo **TOPUS - Projetos Aeroespaciais**. Este projeto é um esforço colaborativo de estudantes voltado ao aprendizado e desenvolvimento prático no campo de CubeSats.

O principal objetivo do projeto é consolidar conhecimento sobre sistemas embarcados, engenharia aeroespacial, processamento de dados e integração de sistemas, documentando cada etapa do desenvolvimento.

## Estrutura do Repositório

O repositório está estruturado para refletir os dois principais módulos do projeto: **Controle do Satélite** e **Payload**. Abaixo, você encontrará a descrição das principais pastas:

### Pastas Principais
- **/docs:** Documentação geral do projeto, incluindo arquitetura do sistema, notas técnicas e referências.
- **/common:** Recursos compartilhados entre o controle do satélite e o payload:
  - **/libraries:** Bibliotecas comuns utilizadas por ambos os módulos.
  - **/configs:** Arquivos de configuração gerais.
  - **/tests:** Testes de integração entre os módulos.

### Eletronica(`/eletronica`)
Reúne os arquivos e códigos relacionados à eletronica do cubeset como controle do satélite e sistemas de telemetria.
- **/src:** Código-fonte para eletronica do satélite, incluindo drivers e utilitários.
- **/hardware:** Esquemáticos, layouts de PCB e lista de componentes para o controle.
- **/simulations:** Modelos e simulações voltadas ao controle do satélite.

### Payload (`/payload`)
Focado no algoritmo de visão computacional embarcado e hardware relacionado.
- **/src:** Código-fonte do algoritmo de visão computacional e utilitários.
- **/hardware:** Esquemáticos, layouts de PCB e lista de componentes do payload.
- **/simulations:** Simulações e validação do algoritmo de visão computacional.
