
## 🎮 Especificação do Jogo: "Aventura em Família"

Esta é a base que define o que vamos construir. Ela é pensada para ser modular: começamos simples e adicionamos "poderes" ao código conforme avançamos.

### 1. Visão Geral

* **Gênero:** Plataforma 2D (Side-scroller).
* **Objetivo:** O jogador deve coletar itens (ex: moedas ou cristais) e chegar ao final do mapa (uma porta ou bandeira) sem cair em buracos ou tocar em "obstáculos perigosos".
* **Público-alvo:** Nós mesmos! O foco é a diversão no processo.

### 2. Mecânicas Principais

* **Movimentação:** Esquerda, Direita e Pulo (Física básica de gravidade).
* **Colisão:** Interação com o solo e plataformas criadas no Tiled.
* **Câmera:** A câmera deve seguir o jogador conforme ele avança pelo cenário.

### 3. Pilha Tecnológica (The "Antigravity" Stack)

* **Linguagem:** Python 3 (Interpretada, feedback instantâneo).
* **Engine:** `arcade` (Biblioteca moderna, focada em Python 3.x, com ótimo suporte a Sprites e Mapas).
* **Editor de Mapas:** Tiled (.tmx).
* **Arte:** Pixel Art (Sprites de 32x32 ou 64x64 pixels).

### 4. Divisão de Tarefas

* **Pai (Tech Lead):** Implementar a lógica de gravidade, carregamento de mapas e sistema de colisão.
* **Filho (Game Designer & Artist):** Desenhar o personagem e inimigos, criar os níveis no Tiled e definir a velocidade/pulo do herói.

---

## 🛠️ TODO: O Que Instalar no Windows

Siga esta ordem para garantir que tudo funcione perfeitamente. Se decidir usar o **WSL**, os comandos de `pip` são os mesmos, mas recomendo rodar a interface gráfica direto no Windows para evitar dores de cabeça com drivers de vídeo (X11/Wayland) no início.

### 1. Python & IDE

* [ ] **Instalar Python 3.11 ou superior:** Baixe em [python.org](https://www.python.org/). *Importante: Marque a opção "Add Python to PATH" no instalador.*
* [ ] **Instalar VS Code:** O melhor editor para Python.
* [ ] **Extensão Python no VS Code:** Procure por "Python" da Microsoft na aba de extensões.

### 2. A Engine (Arcade)

Abra o seu terminal (CMD ou PowerShell) e digite:

* [ ] `pip install arcade`
* *(Opcional)* `pip install arcade[dev]` (para ferramentas extras de desenvolvimento).

### 3. Ferramentas de Design

* [ ] **Tiled Map Editor:** Baixe em [mapeditor.org](https://www.mapeditor.org/). É aqui que seu filho vai "desenhar" as fases como se fosse um quebra-cabeça.
* [ ] **Piskel (Offline ou Online):** Para criar os desenhos (.png). Se preferir algo mais robusto, instale o **Pixelorama** (via Steam ou Itch.io).

### 4. Preparação da Pasta do Projeto

Crie uma estrutura simples para manter o foco:

```text
meu_jogo/
├── assets/         <-- Onde ficam os desenhos (.png) e sons
├── maps/           <-- Onde ficam os arquivos do Tiled (.tmx)
└── main.py         <-- O código mágico do Python

```

---

### Próximos Passos

Agora que o plano está traçado, o próximo passo é o **"Primeiro Contato"**.
