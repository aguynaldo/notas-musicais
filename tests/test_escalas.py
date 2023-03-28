"""
AAA - 3A - A3

Arrange - Act - Asserts!
Arrumar - Agir - Garantir!
"""
from pytest import mark, raises

from notas_musicais.escalas import ESCALAS, NOTAS, escala


def test_deve_funcionar_com_notas_minusculas():
    # Arrumar
    tonica = 'c'
    tonalidade = 'maior'

    # Act
    result = escala(tonica, tonalidade)

    # Assert
    assert result


def test_deve_retornar_um_erro_dizendo_que_a_nota_nao_existe():
    tonica = 'X'
    tonalildade = 'maior'

    mensagem_de_erro = f'Essa nota não existe, tente uma dessas {NOTAS}'

    with raises(ValueError) as error:
        escala(tonica, tonalildade)

    assert mensagem_de_erro == error.value.args[0]


def test_deve_retornar_um_erro_dizendo_que_a_escala_nao_existe():
    tonica = 'c'
    tonilidade = 'tonalidade'

    mensagem_de_erro = (
        'Essa escala não existe ou não foi implementada. '
        f'Tente uma dessas {list(ESCALAS.keys())}'
    )

    with raises(KeyError) as error:
        escala(tonica, tonilidade)

    assert mensagem_de_erro == error.value.args[0]


@mark.parametrize(
    # Arrange
    'tonica,tonalidade,esperado',
    [
        ('C', 'maior', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
        ('C#', 'maior', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']),
        ('F', 'maior', ['F', 'G', 'A', 'A#', 'C', 'D', 'E']),
        ('C', 'menor', ['C', 'D', 'D#', 'F', 'G', 'G#', 'A#']),
        ('C#', 'menor', ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B']),
        ('F', 'menor', ['F', 'G', 'G#', 'A#', 'C', 'C#', 'D#']),
    ],
)
def test_deve_retornar_as_notas_corretas(tonica, tonalidade, esperado):
    # Act
    resultado = escala(tonica, tonalidade)

    # Assert
    assert resultado['notas'] == esperado


def test_deve_retornar_os_sete_graus():
    # Arrange
    tonica = 'c'
    tonalidade = 'maior'
    esperado = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']

    # Act
    resultado = escala(tonica, tonalidade)

    # Assert
    assert resultado['graus'] == esperado
