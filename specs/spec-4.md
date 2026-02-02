# Especificação do Jogo: "Aventura em Família" (Versão 4.0)

Esta é a especificação definitiva do projeto, consolidando todas as funcionalidades implementadas do protótipo até a versão final com Chefões e IA Avançada.

## 1. Visão Geral
* **Gênero:** Plataforma 2D (Side-scroller).
* **Objetivo:** Explorar mapas, coletar moedas, sobreviver a perigos, derrotar o Chefão e alcançar o Troféu de ouro.
* **Tecnologia:** Python 3.11+ e Biblioteca `arcade` 3.0+.

## 2. Personagens e IA
### 2.1 O Jogador (`Player`)
* **Movimentação:** Setas ou WASD. Pulo com Espaço/Cima.
* **Mecânica de Ataque:** Elimina inimigos e causa dano ao Boss pulando sobre eles (colisão vertical negativa).
* **Reset:** Retorna ao início da fase se tocar em espinhos, cair no buraco ou ser atingido lateralmente por inimigos.

### 2.2 Inimigos Comuns (`Enemy`)
* **Comportamento:** Persegue o jogador horizontalmente.
* **IA de Patrulha:** Ao colidir com paredes ou espinhos, inverte a direção por 60 quadros (1 segundo) antes de voltar a perseguir.

### 2.3 O Chefão (`Boss`)
* **HP:** 3 pontos de vida.
* **Ativação:** Só se move quando o jogador entra em um raio de 400 pixels.
* **Velocidade:** Superior aos inimigos comuns.
* **Knockback:** Ao ser atingido, empurra o jogador para cima e para o lado oposto.

## 3. Estrutura do Mundo (Tiled Map)
O jogo utiliza arquivos `.tmx` localizados na pasta `maps/`, com as seguintes camadas obrigatórias:
* `Platforms`: Blocos de colisão sólida.
* `Coins`: Itens coletáveis para pontuação.
* `Hazards`: Espinhos que matam o jogador ao tocar.
* `enemy`: Sprites de inimigos comuns.
* `boss`: Sprite do Chefão da fase.
* `goal`: Troféu final. **Importante:** Fica invisível e inativo até que todos os bosses sejam derrotados.

## 4. Fluxo de Jogo
* **Menu Principal:** Tela inicial com título e comando de início.
* **Progressão:** Carregamento automático de fases seguindo o padrão `level_1.tmx`, `level_2.tmx`, etc.
* **Freeze de Vitória:** Ao tocar no troféu, o jogo pausa todas as movimentações (congelamento) até que o jogador pressione ENTER.
* **Loop Final:** Após a última fase, o jogador é parabenizado e retorna ao menu principal.

## 5. Configurações Técnicas (`src/constants.py`)
Todas as variáveis críticas de jogabilidade estão centralizadas:
* Gravidade e velocidades (pulo/movimento).
* Dimensões da tela.
* Atributos do Boss (HP, knockback).
* Mensagens de interface.
