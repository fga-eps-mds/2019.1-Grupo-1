---
layout: post
title: Plano de gerenciamento de riscos
tags: datelhamento riscos documento eps
category: Gerencia
---
|Data   |Versão   |Descrição   |Autor   |
|---|---|---|---|
|05/04/2019   | 1.0  |Criação do documento   | Lucas Vitor |
|09/04/2019   | 1.1  |Refatoração do documento | Lucas Vitor |
|25/04/2019   | 1.2  |Refatoração do documento | Lucas Vitor |


## 1. Introdução

<p align="justify">O plano de gerenciamento de riscos tem por objetivo a identificação, análise e planejamento de medidas para os possíveis riscos que o projeto pode enfrentar. Este documento se torna imprescindível, pois a partir dele riscos que podem causar consequências graves são identificados e resolvidos ou mitigados.</p>
<!--more-->

## 2. Análise Quantitativa

<p align="justify">A análise quantitativa tem por objetivo a priorização e categorização dos riscos de acordo com 2 métricas: probabilidade, chances de um risco ocorrer; impacto, o quanto o risco impacta no projeto.</p>

### 2.1. Probabilidade

|Probabilidade|Intervalo|Peso|
|:-:|:-:|:-:|
|Muito baixa|0 a 15|1|
|Baixa|16 a 35|2|
|Média|36 a 50|3|
|Alta|51 a 65|4|
|Muito alta|65 a 100|5|

### 2.2. Impacto

|Impacto|Descrição|Peso|
|:-:|:-:|:-:|
|Muito baixo|Pouco expressivo|1|
|Baixo|Pouco impacto|2|
|Médio|Impacto médio|3|
|Alto|Grande impacto|4|
|Muito alto|Impacto impede o procedimento do projeto|5|

### 2.3. Prioridade

<p align="justify">Se baseando com no impacto e na probabilidade é calculada a prioridade dos riscos. O que determina a urgência com que medidas devem ser tomadas para mitigar ou resolver um risco que pode impedir o projeto.</p>

|I/P|Muito baixa|Baixa|Média|Alta|Muito alta|
|:-:|:-:|:-:|:-:|:-:|:-:|
|**Muito baixo**|1|2|3|4|5|
|**Baixo**|2|4|6|8|10|
|**Médio**|3|6|9|12|15|
|**Alto**|4|8|12|16|20|
|**Muito alto**|5|10|15|20|25|

#### 2.3.1. Nível de Prioridade

|Prioridade|Intervalo|
|:-:|:-:|
|Muito baixo|1 a 5|
|Baixo|6 a 10|
|Médio|11 a 15|
|Alto|16 a 20|
|Muito alto|21 a 25|

## 3. Estrutura Analítica de Riscos

<p align="justify">Esta estrutura, também conhecida como EAR, é responsável por agrupar as possíveis causas dos riscos, o que facilita o tratamento e reconhecimento de riscos do projeto, facilitando o processo de mitigação dos riscos.</p>
<p align="justify">Os riscos podem ser classificados de acordo com várias categorias. <b>Técnico</b>, que são riscos associados à tecnologia, requisitos  e qualidade. <b>Externo</b>, são riscos relativos ao cliente, mercado ou ambiente. <b>Organizacional</b>, são relacioandos à priorização e recursos do projeto. <b>Gerência</b>, são relativos à estimativa, planejamento, controle e comunicação.</p>

## 4. Identificação dos Riscos

<p align="justify">O processo de identificação de riscos se utilizou de identificação de riscos atráves da comparação análoga - método que se utiliza de experiências anteriores e similares para facilitar a concepção e identificação comum em projetos do gênero. </p>

## 5. Documentação dos Riscos e Ações

| Risco  | Ação Preventiva  | Ação Reativa  | Categoria | Probabilidade | Impacto | Prioridade |
|---|---|---|---|---|---|---|
| Dificuldades da equipe com as novas tecnologias inseridas  |Seleção de alunos experientes para aplicação de treinamento. |Realização de treinamento sobre tecnologias.   | Técnico | 4 | 5 | 20 |
|Divergência de horários entre membros da equipe   |Elaboração de quadro de horários disponíveis da cada membro da equipe. |Planejamento de de pareamento por sprint baseado na disponibilidade dos integrantes por meio do quadro de disponibilidade. | Gerência | 4 | 3 | 12 | 
|Desistência da disciplina. |Estimular a máxima participação dos membros da equipe |Redistribuir tarefas de forma que não ocorra sobrecarga para nenhum dos membros do grupo e que o grupo consiga interagir da melhor maneira possível. | Gerência | 2 | 5 |10 |
|Alteração do escopo |Documentar e refinar de forma constante os requisitos |Planejar corretamente a sprint e se manter atualizado quanto às novas funcionalidades que serão adicionadas ao bot | Gerência | 5 | 4 | 20 |
|Alteração das tecnologias |Definir de forma conscisa o escopo do projeto   |Planejar corretamente a sprint e se manter atualizado quanto às novas funcionalidades que serão adicionadas ao bot | Técnico | 4 | 5 | 20 |
|Presença dos membros durante Daily e reunião de planejamento |Definir datas, horários e locais que sejam acessíveis a todos. |Manter o time sempre alinhado quanto às decisões tomadas.|  Gerência | 4 | 3 | 12 |
| Falta de cliente real |Utilização de ferramentas que ajudem a levantar requisitos |Utilização de dados levantados por usuários que sejam o público alvo do projeto. | Externo | 5 | 2 | 10 |
|Dependência entre as atividades  |Priorização das atividades |Planejar Sprints de forma a evitar o excesso de dependências entras as issues | Organizacional | 3 | 3 | 9 |
|Baixa produtividade dos integrantes do grupo |Motivação  da equipe quanto a criação do projeto através de reuniões constantes |Gamificação do projeto para reintegração de membros desmotivados | Gerência | 3 | 5 | 15 |
|Dificuldade de comunicação entre os membros do grupo |Elaborar e seguir plano de comunicações |Reuniões presenciais com a equipe para tomada de decisões | Gerência | 3 | 4 | 12 |

## 6. Bibliografia

> [Detalhamento de Riscos da equipe do Receita Mais](https://github.com/fga-eps-mds/2017.2-Receita-Mais/wiki/Detalhamento-dos-Riscos)

> [Detalhamento de Riscos da equipe do HubCare](https://github.com/fga-eps-mds/2019.1-hubcare-docs/tree/master/docs/project-risk-management/risk-management-list)

> [Detalhamento de Riscos da equipe do MaisMonitoria](https://fga-eps-mds.github.io/2019.1-MaisMonitoria/docs/plano-riscos)

> PMI. Um guia do conhecimento em gerenciamento de projetos. Guia PMBOK 6a. ed. - EUA: Project Management Institute, 2017.