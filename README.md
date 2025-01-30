# Projeto AllSpark - CubeSat

Bem-vindo ao repositório oficial do **Projeto AllSpark**, uma iniciativa do grupo **TOPUS - Projetos Aeroespaciais**. Este projeto é um esforço colaborativo de estudantes voltado ao aprendizado e desenvolvimento prático no campo de CubeSats.

## 📌 Descrição da Missão
O **Projeto AllSpark** tem como objetivo o desenvolvimento e operação de um **CubeSat 1U** para **análise de solo e terreno por meio de cor**, utilizando técnicas avançadas de **visão computacional embarcada**. O satélite será lançado na **região do interior de São Paulo** e operará a aproximadamente **1.5 km de altitude**. Ele captará imagens coloridas do solo, aplicando algoritmos de **processamento de imagem** para identificar padrões de solo e vegetação, além de destacar regiões de possível interesse.

O CubeSat será equipado com uma **câmera otimizada para capturas a 1.5 km de altitude**, com ajustes automáticos de exposição e filtros opcionais. O **processamento poderá ocorrer a bordo** por meio de uma **board embarcada** (**TORADEX** ou alternativas como Raspberry), sendo analisadas **redes neurais** para segmentação de cores e classificação do terreno. O sistema incluirá **módulos de comunicação, sensores auxiliares e memória adicional**. No software, serão implementadas **técnicas de visão computacional** para segmentação e análise de cor, com compressão eficiente para transmissão dos dados à estação terrestre.

O projeto busca consolidar conhecimento sobre **sistemas embarcados, engenharia aeroespacial e integração de sistemas**, documentando cada etapa do desenvolvimento para futuras aplicações e aprimoramento de tecnologias CubeSat.

---

## 📁 Estrutura do Repositório
O repositório está estruturado para refletir os dois principais módulos do projeto: **Controle do Satélite** e **Payload**.

### 📂 Pastas Principais
- **📄 /docs** – Documentação geral do projeto, incluindo arquitetura do sistema, notas técnicas e referências.
- **📂 /common** – Recursos compartilhados entre o controle do satélite e o payload:
  - **/libraries** – Bibliotecas comuns utilizadas por ambos os módulos.
  - **/configs** – Arquivos de configuração gerais.
  - **/tests** – Testes de integração entre os módulos.

---

### 📡 Eletrônica (`/eletronica`)
Reúne os arquivos e códigos relacionados à eletrônica do CubeSat, incluindo **controle do satélite** e **sistemas de telemetria**.
- **📂 /src** – Código-fonte para eletrônica do satélite, incluindo drivers e utilitários.
- **🔧 /hardware** – Esquemáticos, layouts de PCB e lista de componentes para o controle do satélite.
- **🛰️ /simulations** – Modelos e simulações voltadas ao controle do satélite.

---

### 🎯 Payload (`/payload`)
Focado no **algoritmo de visão computacional embarcado** e hardware relacionado.
- **📂 /src** – Código-fonte do algoritmo de visão computacional e utilitários.
- **🔧 /hardware** – Esquemáticos, layouts de PCB e lista de componentes do payload.
- **🖥️ /simulations** – Simulações e validação do algoritmo de visão computacional.

---

## ⚡ Principais Tecnologias Utilizadas
- **🖥️ Visão Computacional** – Algoritmos para segmentação de cor, análise de terreno e reconhecimento de padrões.
- **📡 Sistemas Embarcados** – Hardware de baixo consumo para processamento eficiente.
- **🛰️ Engenharia Aeroespacial** – Integração dos subsistemas em um CubeSat compacto.
- **📡 Telecomunicações** – Estratégias de transmissão eficiente de dados para a estação terrestre.

---

## 👥 Contribuição
Contribuições são bem-vindas! Caso tenha interesse em colaborar, siga os passos:
1. Faça um **fork** do repositório.
2. Crie uma nova branch para sua funcionalidade ou correção (`git checkout -b minha-feature`).
3. Faça um commit das alterações (`git commit -m "Adicionando nova funcionalidade"`).
4. Envie seu código (`git push origin minha-feature`).
5. Abra um **Pull Request** para revisão.
