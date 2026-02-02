# Aventura em Família 🎮

Um jogo de plataforma 2D vibrante e desafiador construído com **Python** e a biblioteca **Arcade**.

## 📖 Sobre o Jogo
Em "Aventura em Família", você controla um herói em busca de moedas e glória. Enfrente inimigos com IA inteligente, supere obstáculos fatais e derrote o grande Chefão para desbloquear a passagem para o próximo nível.

## 🚀 Funcionalidades
- **IA Avançada**: Inimigos que patrulham e perseguem o jogador.
- **Batalhas de Boss**: Chefões com múltiplas vidas e mecânicas de knockback.
- **Mapas Dinâmicos**: Suporte a múltiplos níveis criados no Tiled Editor.
- **Design Moderno**: Interface polida com HUD e menu principal.
- **Configuração Centralizada**: Ajuste facilmente a física do jogo em um único arquivo de constantes.

## 🛠️ Instalação e Execução

### Pré-requisitos
- Python 3.11 ou superior.
- Arcade 3.0.0+.

### Como Jogar
1. Instale as dependências:
   ```bash
   pip install arcade
   ```
2. Execute o jogo:
   ```bash
   python main.py
   ```

## 📂 Estrutura do Projeto
```text
hava-project-game/
├── main.py              # Ponto de entrada do jogo
├── src/
│   ├── constants.py     # Configurações globais
│   ├── entities/        # Jogador, Inimigos e Boss
│   └── views/           # Telas de Menu e Jogo
├── maps/                # Arquivos Tiled (.tmx)
├── assets/              # Imagens e Sons
└── specs/               # Especificações detalhadas (v1 a v4)
```

## 🎮 Controles
- **Setas / WASD**: Movimentação e Pulo.
- **Espaço**: Pulo.
- **Enter**: Avançar entre fases e menus.

---
Desenvolvido com ❤️ para a diversão de toda a família, por Victor e Heitor
