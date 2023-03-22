![Logo do projeto](assets/logo.png){ width=300 .center }

# Notas Musicais

## Como usar?

Você pode chamar as escalas via linha de comando. Por exemplo:
```bash
poetry run escalas
```

Retornando os graus e as notas correspondentes a essa escala.
```
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ C │ D  │ E   │ F  │ G │ A  │ B   │
└───┴────┴─────┴────┴───┴────┴─────┘
```

### Alteração na escala

O primeiro parâmetro do CLI é a tônica da escala ue deseja exibir. Desta forma, você pode alterar a escala retornada:
```bash
poetry run escalas F#

```

### Alteração na tonalidade

Você pode alterar a tonalidade retornada da escala também. Esse é o segundo parâmetro do CLI é a tônica da escala ue deseja exibir. Desta forma, :
```bash
poetry run escalas F# maior

```

## Mais informações sobre o CLI

Para descobrir outras opções, você pode usar a flag `--help`