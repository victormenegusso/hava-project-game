# Especificação do Jogo: "Aventura em Família" (Versão 3.0)

Esta versão consolida as implementações das Fases 1 a 5 e estabelece as bases para o sistema de Boss e IA avançada.

## 1. Visão Geral
* **Gênero:** Plataforma 2D (Side-scroller).
* **Objetivo:** Coletar moedas, derrotar inimigos e o Chefão, e chegar ao troféu final.
* **Tecnologia:** Python 3.11 + Biblioteca `arcade`.

## 2. Inimigos e Chefão (Boss)
### 2.1 Inimigos Comuns (`enemy`)
* **Comportamento:** Perseguem o jogador horizontalmente.
* **IA Avançada:** Invertem a direção (patrulha) ao colidir com paredes ou espinhos.
* **Derrota:** Pulando em cima.

### 2.2 Chefão (`boss`)
* **Atributos:** 3 pontos de vida (HP).
* **Comportamento:** Segue o jogador apenas quando ele entra em sua área de detecção. Move-se mais rápido que inimigos comuns.
* **Derrota:** 3 acertos pulando em cima. Cada acerto gera um impulso direcional no jogador.
* **Dependência:** O troféu de final de fase (`goal`) só aparece após o Boss ser derrotado.

## 3. Mecânicas de Jogo
* **Física:** `PhysicsEnginePlatformer` com gravidade ajustável e velocidades centralizadas.
* **Níveis:** Carregamento dinâmico de arquivos `level_*.tmx`.
* **Interface:** HUD com Score, Controles e Indicador de Fase.

## 4. Estrutura de Camadas (Tiled)
* `Platforms`: Colisão sólida.
* `Coins`: Coletáveis.
* `Hazards`: Perigos (espinhos).
* `enemy`: Inimigos comuns.
* `boss`: Camada específica para o Chefão.
* `goal`: Troféu final (condicional).
