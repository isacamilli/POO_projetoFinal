# Documento de Visão

## Sistema de assistência para vestuário

### Histórico da Revisão

|  Data  | Versão | Descrição | Autor |
|:-------|:-------|:----------|:------|
| 28/01/2025 |  **`1.00`** | Versão Inicial  | Gustavo Tavares e Isabella Camilli |

### 1. Objetivo do Projeto

O projeto **Cloud Wear** tem como objetivo fornecer uma solução eficiente e prática para a criação de combinações de roupas de acordo com a temperatura de um local selecionado.

### 2. Descrição do Problema

|         __        | __   |
|:------------------|:-----|
| **_O problema_**    | Dificuldades para escolher roupas adequadas ao clima, criar combinações bonitas e condizentes com a atual situação climática de uma cidade. |
| **_afetando_**      | Pessoas com rotinas agitadas, profissionais, estudantes e qualquer um que tenha um guarda-roupa grande, mas dificuldade em escolher combinações, otimizar o tempo e planejar o que vestir. |
| **_cujo impacto é_**| Perda de tempo na escolha de roupas, aumento da indecisão, frustração com a falta de combinações eficientes e, muitas vezes, um guarda-roupa subutilizado ou mal aproveitado. |
| **_uma boa solução seria_** | Fornecer sugestões utilizando as peças do guarda-roupa do usuário de acordo com o clima da cidade selecionada, organizar o guarda-roupa dando visão das peças que o usuário possui. |

### 3. Descrição dos Usuários

| Nome | Descrição | Responsabilidades |
|:---  |:--- |:--- |
| Administrador  | Gerencia as configurações do sistema. | Mantém o cadastro dos usuários e de roupas cadastradas; Realiza ajustes no sistema; Tem acesso a sugestões de melhorias deixadas pelos usuários. |
| Cliente | Realiza as atividades relacionadas ao gerenciamento do guarda-roupa e geração de combinações. | Gerenciamento do guarda-roupa; Gerar combinações de roupas; Pode logar no sistema; Pontua erros sobre o sistema para os administradores. |

### 4. Descrição do Ambiente dos Usuários

No cotidiano, muitas pessoas enfrentam dificuldades para escolher rapidamente o que vestir, especialmente profissionais, estudantes ou quem possui um guarda-roupa grande. O processo de selecionar roupas adequadas para o dia a dia pode ser demorado e, muitas vezes, pouco eficiente.

Atualmente, a maioria das pessoas precisa escolher suas combinações de forma manual, o que consome tempo e energia. Para pessoas com rotinas agitadas, isso pode se tornar um desafio constante.

A ideia central da aplicação é permitir que os usuários registrem suas roupas digitais e gerem combinações de roupas com base na temperatura da cidade escolhida. Isso proporciona uma maneira mais ágil e prática de planejar o que vestir, economizando tempo e tornando a escolha de roupas mais eficiente.

### 5. Principais Necessidades dos Usuários

Para empresas e profissionais, a necessidade é divulgar sua disponibilidade de atendimentos para viabilizar, de forma mais eficiente, o atendimento dos seus clientes.

Para os clientes, as necessidades são encontrar profissionais e empresas prestadoras de serviços e agendar atendimentos com eles de acordo com as disponibilidades de tempo dos envolvidos.

### 6. Alternativas Concorrentes

As alternativas concorrentes geralmente se concentram em organização de looks manuais ou recomendação de peças individuais. A proposta desta aplicação é oferecer uma solução simples e acessível para a escolha de combinações de roupas, considerando tanto o guarda-roupa do usuário quanto a temperatura da cidade selecionada.

### 7. Visão Geral do Produto

Em resumo, o Sistema de assistência para vestuário, o Cloud Wear, tem por objetivo ajudar os usuários com uma rotina muito agitada, ou quem tem muitas peças de roupa no guarda-roupa, a montar combinações de roupas que combinem entre si e que sejam eficientes na questão climática, pois o sistema escolherá uma combinação usando as peças cadastradas do usuário e também com base no clima da cidade selecionada pelo usuário.

### 8. Requisitos Funcionais

| Código | Nome | Descrição |
|:---  |:--- |:--- |
| RF01 | Entrar no sistema | Usuários devem logar no sistema para acessar as funcionalidades relacionadas ao gerenciamento do guarda-roupa e geração de combinação de peças. |
| RF02 | Sair do sistema | Os usuários podem sair do sistema. |
| RF03 | Editar perfil | Podem editar as informações do seu perfil como (nome, foto e descrição). |
| RF04 | Cadastro de guarda-roupa | O usuário pode cadastrar seu guarda roupas. |
| RF05 | Visualizar roupas | Os usuários podem visualizar as roupas cadastradas. |
| RF06 | Gerenciamento do guarda-roupa | Usuários logados no sistema podem adicionar ou remover roupas do guarda roupas. |
| RF07 | Pontuar erros do sistema | Os usuários podem apontar erros no sistema que serão enviados aos admins. |
| RF08 | Ler erros apontados | Os admins podem ler erros do sistema apontados pelos usuários e retornar uma resposta. |
| RF09 | Manter cadastro de roupas | Os admins guardam o cadastro do guarda roupas dos usuários. |
| RF10 | Manter cadastro de clientes | Os admins guardam o cadastro de cada cliente. |

### 9. Requisitos Não-funcionais

| Código | Nome | Descrição | Categoria | Classificação |
|:---  |:--- |:--- |:--- |:--- |
| RNF01 | Sistema Web | A aplicação deve ser um site. | Arquitetura | Obrigatório |
| RNF02 | Dados pessoais | Os clientes não devem visualizar dados de outros clientes (roupas cadastradas na conta de outros clientes, por exemplo). | Privacidade | Obrigatório |
