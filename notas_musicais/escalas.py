NOTAS = 'C C# D D# E F F# G G# A A# B'.split()
ESCALAS = {'maior': (0, 2, 4, 5, 7, 9, 11)}


def escalas(tonica: str, tonalidade: str) -> dict[str, list[str]]:
    """
    Gera uma escala a partir de uma nota tônica e uma tonalidade.

    Parameters:
        tonica: Nota que representa a tônica da escala.
        tonalidade: Tonalidade da escala.

    Returns:
        Um dicionário com as notas da escalas e os respectivos graus.

    Examples:
        >>> escalas('C', 'maior')
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> escalas('A', 'maior')
        {'notas': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

    Todo:
        * Permitir que o usuário informe a escala em maiúsculo ou não. 'A' ou 'a'.
    """
    intervalos = ESCALAS[tonalidade]
    tonica_pos = NOTAS.index(tonica)   # type: ignore
    temp = []

    for intervalo in intervalos:
        nota = (tonica_pos + intervalo) % 12
        temp.append(NOTAS[nota])

    return {'notas': temp, 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
