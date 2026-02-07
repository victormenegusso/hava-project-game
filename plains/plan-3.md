# Plano de Implementação - Inimigos Avançados e Chefão (V3.0) [CONCLUÍDO]

Este plano descreve a implementação de IA de patrulha para inimigos, o sistema de Chefão (Boss) e a lógica de aparição condicional do troféu.

## User Review Required

> [!IMPORTANT]
> O Chefão exigirá 3 acertos para ser derrotado. Cada acerto empurrará o jogador em uma direção oposta para evitar múltiplos acertos acidentais imediatos.
> O troféu final permanecerá invisível e sem colisão até que todos os Chefões presentes no mapa sejam eliminados.

## Proposed Changes

### 1. Constantes e Assets
#### [MODIFY] [constants.py](file:///c:/Users/victo/OneDrive/Documentos/workspace/hava-project-game/src/constants.py)
- Adicionar `BOSS_SPEED`.
- Adicionar `BOSS_HEALTH` (valor padrão 3).
- Adicionar `BOSS_KNOCKBACK_X` e `BOSS_KNOCKBACK_Y`.

#### [NEW] [generate_boss_sprite.py](file:///c:/Users/victo/OneDrive/Documentos/workspace/hava-project-game/generate_boss_sprite.py)
- Script para gerar o sprite do Boss (baseado no player, mas maior e em cor diferente).

### 2. Entidades (IA e Boss)
#### [MODIFY] [enemy.py](file:///c:/Users/victo/OneDrive/Documentos/workspace/hava-project-game/src/entities/enemy.py)
- Implementar detecção de colisão com paredes e spikes.
- Alterar comportamento de perseguição para incluir inversão de marcha (patrulha) em obstáculos.

#### [NEW] [boss.py](file:///c:/Users/victo/OneDrive/Documentos/workspace/hava-project-game/src/entities/boss.py)
- Criar classe `Boss` que herda de `Enemy`.
- Adicionar atributo `health`.
- Implementar lógica de ativação (só persegue quando o player está próximo).

### 3. Lógica de Jogo (GameView)
#### [MODIFY] [game_view.py](file:///c:/Users/victo/OneDrive/Documentos/workspace/hava-project-game/src/views/game_view.py)
- Adicionar suporte para a camada `boss`.
- Implementar sistema de dano no Boss.
- Implementar lógica de visibilidade do `goal` (troféu) baseada na lista de sprites da camada `boss`.

## Verification Plan

### Manual Verification
1. **Passo 1: Patrulha**: Observar inimigos comuns batendo em paredes/spikes e mudando de direção.
2. **Passo 2: Ativação do Boss**: Verificar se o Boss ignora o player até este se aproximar.
3. **Passo 3: Luta contra o Boss**: Acertar o Boss 3 vezes e validar o efeito de "knockback" (empurrão).
4. **Passo 4: Troféu**: Confirmar que o troféu não aparece/não funciona enquanto o Boss estiver vivo.
