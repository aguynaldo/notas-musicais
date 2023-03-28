
![Logo do projeto](assets/logo.png){ width=300 .center }

# Notas Musicais

Notas Musicais é um CLI para ajudar na formação de escalas e acordes.

Temos dois comandos disponíveis: `acordes`, `escalas`
## Como usar?

### Escalas

Você pode chamar as escalas via linha de comando. Por exemplo:

Retornando os graus e as notas correspondentes a essa escala.

```bash
poetry run notas-musicais escala

┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ C │ D  │ E   │ F  │ G │ A  │ B   │
└───┴────┴─────┴────┴───┴────┴─────┘
```

#### Alteração na escala

O primeiro parâmetro do CLI é a tônica da escala ue deseja exibir. Desta forma, você pode alterar a escala retornada:

```bash
poetry run notas-musicas escala F#

┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ F#│ G# │ A#  │ B  │ C#│ D# │ F   │
└───┴────┴─────┴────┴───┴────┴─────┘
```

#### Alteração na tonalidade

Você pode alterar a tonalidade retornada da escala também. Esse é o segundo parâmetro do CLI é a tônica da escala ue deseja exibir. Desta forma, :

```bash
poetry run notas-musicas escala D# menor

┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ D#│ F  │ F#  │ G# │ A#│ B  │ C#  │
└───┴────┴─────┴────┴───┴────┴─────┘

```

### Acordes

Uso básico

```bash
poetry run notas-musicais acorde
┏━━━┳━━━━━┳━━━┓
┃ I ┃ III ┃ V ┃
┡━━━╇━━━━━╇━━━┩
│ C │ E   │ G │
└───┴─────┴───┘
```

#### Variações na cifra

```bash
poetry run notas-musicais acorde c+
┏━━━┳━━━━━┳━━━━┓
┃ I ┃ III ┃ V+ ┃
┡━━━╇━━━━━╇━━━━┩
│ C │ E   │ G# │
└───┴─────┴────┘
```

## Mais informações sobre o CLI

Para descobrir outras opções, você pode usar a flag `--help`

```bash
poetry run notas-musicais --help.
```