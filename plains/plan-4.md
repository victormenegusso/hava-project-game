# Plano de Implementação: Animação do Personagem (plan-4.md)

Este documento detalha o plano para implementar animações no personagem principal, conforme a Especificação 4.0.

## 1. Objetivos
- Adicionar estados de animação: Idle (parado), Walking (andando), Jumping (pulando) e Falling (caindo).
- Implementar inversão horizontal (espelhamento) baseada na direção do movimento.
- Gerar assets via IA para manter a consistência visual.

## 2. Assets a serem Gerados
Recomendamos um ciclo de 4 frames para caminhada para um equilíbrio entre fluidez e simplicidade.
- `player_idle.png`
- `player_walk_1.png`, `player_walk_2.png`, `player_walk_3.png`, `player_walk_4.png`
- `player_jump.png`
- `player_fall.png`

## 3. Implementação Técnica
A lógica será encapsulada na classe `Player` (em `src/entities/player.py`), estendendo as funcionalidades do `arcade.Sprite`.

### Estrutura da Classe Player:
- **Atributos de Textura:** Listas para armazenar as texturas de caminhada, idle, pulo e queda.
- **Controle de Estado:** Variáveis para rastrear a face atual (esquerda/direita) e o índice do frame da animação.
- **Método `update_animation`:**
  - Lógica para detectar se o personagem está no ar (`change_y != 0`) e se está subindo ou descendo.
  - Lógica para detectar movimento horizontal (`change_x != 0`) e alternar frames de caminhada.
  - Lógica para inverter texturas usando o método `flip_left_right()` do objeto `Texture` (Necessário para Arcade 3.x).
  - Uso de placeholders (`player_idle.png`, etc.) até que os assets reais sejam gerados.

## 4. Integração
- O `GameView` em `on_update` continuará chamando `self.physics_engine.update()`.
- Como o `Player` será um `arcade.Sprite`, o Arcade chamará automaticamente `update_animation` se adicionarmos o player a uma `Scene`.

## 5. Cronograma
1. **Fase 1:** Geração e processamento de imagens por IA.
2. **Fase 2:** Atualização da classe `Player` com carregamento de texturas.
3. **Fase 3:** Implementação da lógica de troca de estados em `update_animation`.
4. **Fase 4:** Testes e ajustes de velocidade de animação.
