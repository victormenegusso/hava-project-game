# Especificação do Jogo: "Aventura em Família" (Versão 2.0)

Esta é a versão atualizada das especificações, incluindo detalhes técnicos descobertos e implementados durante as Fases 1 a 4.

## 1. Visão Geral
* **Gênero:** Plataforma 2D (Side-scroller).
* **Objetivo:** Coletar itens (moedas) e chegar ao final do mapa.
* **Tecnologia:** Python 3.11 + Biblioteca `arcade` (Versão 3.0+).

## 2. Estrutura do Projeto
```text
hava-project-game/
├── main.py             # Entrada: Inicializa a janela e a GameView
├── src/
│   ├── constants.py    # Globais: SCREEN_WIDTH/HEIGHT (1024x768), Título
│   ├── entities/
│   │   └── player.py   # Classe Player (herda de arcade.Sprite)
│   └── views/
│       └── game_view.py # Lógica principal do loop de jogo
├── assets/
│   └── images/         # Sprites (.png). Transparência tratada via script.
├── maps/               # Mapas Tiled (.tmx) e tilesets
└── process_assets.py   # Script utilitário para redimensionar/limpar assets
```

## 3. Detalhes Técnicos de Implementação

### 3.1. Mapa e Física
* **Ferramenta:** Tiled Map Editor.
* **Formato:** `.tmx` (XML), Ortogonal, Tiles 32x32px.
* **Camadas (Layers):**
    * `Platforms`: Blocos sólidos (chão, paredes). Usados pela PhysicsEngine.
    * `Coins`: Colecionáveis.
* **Física:** `arcade.PhysicsEnginePlatformer` com gravidade (0.5).
* **Otimização:** `use_spatial_hash=True` ativado para camadas de colisão.

### 3.2. Câmera
* **Tipo:** `arcade.camera.Camera2D`.
* **Lógica de Centralização:**
    * A posição da câmera define o canto inferior esquerdo da viewport.
    * Cálculo: `Posição = Player.center - (Screen / 2)`.
    * **Clamping:** A posição nunca é menor que (0,0) para não mostrar o "vazio" à esquerda/baixo.

### 3.3. Interface (UI)
* **Renderização:** Desenhada diretamente no `on_draw` usando coordenadas de mundo corrigidas.
* **Posição:** Relativa à âncora da câmera (`camera.position.x + offset`).
* **Motivo:** O uso de múltiplas câmeras apresentou instabilidade na versão atual da biblioteca, optou-se por cálculo manual de coordenadas world-space.

### 3.4. Assets (Pipeline)
* **Geração:** Imagens geradas por IA.
* **Processamento:** Scripts em Python (`process_assets.py`) são usados para:
    1. Redimensionar (Player: 64px, Coin: 32px, Tiles: 128px/tile).
    2. Remover fundo branco (transformar em transparente).

## 4. Estado Atual (Fim da Fase 4)
* [x] Janela e Loop funcionando.
* [x] Personagem anda e pula com física.
* [x] Mapa carrega e colide.
* [x] Câmera segue o personagem corretamente.
* [x] Moedas são coletáveis e contam pontos.
* [x] UI de pontos segue a tela.

## 5. Próximos Passos
* **Fase 5:** Implementar "Hazards" (Espinhos/Buracos) e tela de Game Over.
* **Fase 6:** Menu Principal e fluxo de jogo completo.
