# Plano de Desenvolvimento: Aventura em Família

Este documento descreve o roteiro de desenvolvimento para o jogo de plataforma, dividido em fases para facilitar a implementação e testes progressivos.

## 1. Estrutura do Projeto

A estrutura de diretórios foi definida para equilibrar organização e simplicidade:

```text
hava-project-game/
├── main.py             # Ponto de entrada do jogo (Entry Point)
├── plains/             # Documentação e planos
├── src/                # Código fonte modular
│   ├── __init__.py
│   ├── constants.py    # Configurações globais (Tamanho da tela, Cores, etc.)
│   ├── entities/       # Lógica de entidades (Player, Inimigos)
│   │   ├── __init__.py
│   │   └── player.py
│   └── views/          # Diferentes telas do jogo
│       ├── __init__.py
│       ├── game_view.py
│       └── menu_view.py
├── assets/             # Recursos visuais e sonoros
│   ├── images/
│   └── sounds/
└── maps/               # Arquivos de mapa do Tiled (.tmx)
```

## 2. Faseamento de Desenvolvimento

O desenvolvimento será realizado em 6 fases incrementais. Ao final de cada fase, tere mos um componente funcional testável.

### Fase 1: Fundação (Hello World)
**Objetivo:** Configurar o ambiente e abrir uma janela vazia do jogo usando a nova estrutura.
- [x] Criar estrutura de pastas.
- [x] Criar `src/constants.py` com configurações básicas (Largura, Altura, Título).
- [x] Implementar `src/views/game_view.py` com uma classe básica herdando de `arcade.View`.
- [x] Implementar `main.py` para carregar a `GameView` e iniciar a janela.
- **Teste:** Rodar `main.py` e ver uma janela preta (ou com cor de fundo) que não fecha sozinha.

### Fase 2: O Herói (Movimentação e Física)
**Objetivo:** Colocar o personagem na tela e fazê-lo se mover e pular.
- [x] Adicionar um sprite de placeholder para o Player em `assets/images`.
- [x] Criar `src/entities/player.py` herdando de `arcade.Sprite`.
- [x] Implementar física simples em `src/views/game_view.py` (Gravidade).
- [x] Implementar controles de teclado (Setas/WASD + Espaço).
- **Teste:** O personagem cai, anda para os lados e pula. (Ainda sem chão, ele vai cair infinitamente se não tiver um limite).

### Fase 3: O Mundo (Mapas com Tiled)
**Objetivo:** Carregar um mapa criado no Tiled e fazer o personagem colidir com o chão.
- [x] Criar um mapa simples no Tiled (`maps/level_1.tmx`) com uma camada de colisão.
- [x] Implementar carregamento de mapa em `src/views/game_view.py`.
- [x] Implementar `arcade.PhysicsEnginePlatformer` para gerenciar colisões Player-Mundo.
- [x] Implementar Câmera (`arcade.Camera`) para seguir o jogador.
- **Teste:** O personagem anda sobre o chão desenhado no Tiled e a câmera o segue.

### Fase 4: Colecionáveis e Objetivos
**Objetivo:** Dar um propósito ao jogo (pegar moedas e chegar ao fim).
- [x] Adicionar camada de "Moedas" no mapa Tiled.
- [x] Adicionar lógica de detecção de colisão entre Player e Moedas (remover moeda ao tocar).
- [x] Adicionar contador de pontuação na tela.
- [x] Teste: Jogador coleta moedas, elas somem e o placar aumenta.

### Fase 5: Perigos e Game Over
**Objetivo:** Adicionar desafio (buracos e inimigos).
- [ ] Adicionar camada de "Perigo" (espetos, lava) ou buracos no mapa.
- [ ] Implementar lógica de morte (resetar posição ou ir para tela de Game Over).
- [ ] (Opcional) Adicionar inimigo simples que anda de um lado para o outro.
- **Teste:** Jogador "morre" ao cair no buraco ou tocar em perigos.

### Fase 6: Polimento e Fluxo
**Objetivo:** Menu Inicial e transições.
- [x] Criar `src/views/menu_view.py` (Tela de "Press Start").
- [x] Conectar Menu -> Jogo -> Game Over -> Menu.
- [x] Adicionar sons básicos (pulo, coleta).
- [x] Teste: Jogo completo com ciclo de início, meio e fim.

## 3. Próximos Passos Imediatos

Iniciar a **Fase 1: Fundação**.
