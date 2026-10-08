# Plan Inverso — `calculadora/reverseplan_TestCalcular`

Archivo de test analizado: [tests/test_calculadora.py](../../test_calculadora.py)

Archivo bajo prueba: [src/calculadora.py](../../../src/calculadora.py)

## Inventario de Funciones Cubiertas (1 función detectada)(6 tests detectados)
1. `calcular` (6 tests)

## Funciones sin cobertura
- Ninguna — todas las funciones definidas en el archivo fuente tienen al menos un test.

## Función 1: `calcular`

### Tests reales

| Número | ID del test | Descripción | Input | Expected Output |
|---:|---|---|---|---|
| 1 | [test_suma](../../test_calculadora.py#L13) | Comprueba que la operación de suma devuelve el resultado esperado. | `numero1=1`, `numero2=2`, `operacion='+'` | Devuelve `3`. |
| 2 | [test_resta](../../test_calculadora.py#L18) | Comprueba que la operación de resta devuelve el resultado esperado. | `numero1=5`, `numero2=3`, `operacion='-'` | Devuelve `2`. |
| 3 | [test_multiplicacion](../../test_calculadora.py#L23) | Comprueba que la operación de multiplicación devuelve el resultado esperado. | `numero1=4`, `numero2=3`, `operacion='*'` | Devuelve `12`. |
| 4 | [test_division](../../test_calculadora.py#L28) | Comprueba que la operación de división devuelve el resultado esperado. | `numero1=10`, `numero2=2`, `operacion='/'` | Devuelve `5.0`. |
| 5 | [test_operacion_invalida](../../test_calculadora.py#L33) | Comprueba que un símbolo no reconocido provoca una excepción. | `numero1=10`, `numero2=5`, `operacion='x'` | Lanza `ValueError`. No verifica el mensaje. |
| 6 | [test_raizcuadrada](../../test_calculadora.py#L37) | Comprueba que la raíz cuadrada usa el primer operando y devuelve el resultado esperado. | `numero1=16`, `numero2=0`, `operacion='√'` | Devuelve `4`. |

### CAJA BLANCA — Cobertura de Líneas y Ramas

| ID | Descripción | Tipo | Condición / Línea | Input | Expected Output | Checklist de cobertura |
|---|---|---|---|---|---|---|
| WB_inicializacion_respuesta | Ejecuta la inicialización de `respuesta` antes del `match`. | Line Coverage | Línea 2 | Cualquier llamada válida | La función continúa hasta devolver el resultado de la operación. | 1, 2, 3, 4, 6 |
| WB_rama_suma | Activa el caso de suma. | Branch CASE | Línea 4, `operacion='+'` | `1, 2, '+'` | `3` | 1 |
| WB_rama_resta | Activa el caso de resta. | Branch CASE | Línea 6, `operacion='-'` | `5, 3, '-'` | `2` | 2 |
| WB_rama_multiplicacion | Activa el caso de multiplicación. | Branch CASE | Línea 8, `operacion='*'` | `4, 3, '*'` | `12` | 3 |
| WB_rama_division | Activa el caso de división. | Branch CASE | Línea 10, `operacion='/'` | `10, 2, '/'` | `5.0` | 4 |
| WB_rama_potencia | Activa el caso de potencia. | Branch CASE | Línea 12, `operacion='**'` | `2, 3, '**'` | `8` | Ninguno |
| WB_rama_division_entera | Activa el caso de división entera. | Branch CASE | Línea 14, `operacion='//'` | `7, 2, '//'` | `3` | Ninguno |
| WB_rama_modulo | Activa el caso de módulo. | Branch CASE | Línea 16, `operacion='%'` | `7, 3, '%'` | `1` | Ninguno |
| WB_rama_raiz_cuadrada | Activa el caso de raíz cuadrada. | Branch CASE | Línea 18, `operacion='√'` | `16, 0, '√'` | `4.0`, equivalente numéricamente a `4` | 6 |
| WB_rama_cubo | Activa el caso de cubo. | Branch CASE | Línea 20, `operacion='c'` | `3, 0, 'c'` | `27` | Ninguno |
| WB_rama_raiz_cubica | Activa el caso de raíz cúbica con el símbolo principal. | Branch CASE | Línea 22, `operacion='√3'` | `27, 0, '√3'` | Aproximadamente `3` | Ninguno |
| WB_rama_raiz_cubica_alternativa | Activa el caso alternativo de raíz cúbica. | Branch CASE | Línea 24, `operacion='cbrt'` | `27, 0, 'cbrt'` | Aproximadamente `3` | Ninguno |
| WB_rama_valor_absoluto | Activa el caso de valor absoluto. | Branch CASE | Línea 26, `operacion='abs'` | `-5, 0, 'abs'` | `5` | Ninguno |
| WB_rama_negacion | Activa el caso de negación. | Branch CASE | Línea 28, `operacion='neg'` | `5, 0, 'neg'` | `-5` | Ninguno |
| WB_rama_logaritmo_natural | Activa el caso de logaritmo natural. | Branch CASE | Líneas 30-32, `operacion='ln'` | `1, 0, 'ln'` | `0.0` | Ninguno |
| WB_rama_operacion_invalida | Activa el caso comodín para un símbolo no reconocido. | Branch DEFAULT | Línea 34 | `10, 5, 'x'` | Lanza `ValueError`. | 5 |
| WB_retorno | Comprueba el retorno final después del `match`. | Line Coverage | Línea 36 | Operación reconocida | Devuelve el valor calculado. | 1, 2, 3, 4, 6 |

### CAJA NEGRA — EP y Valores Límite

La firma declara tres parámetros (`numero1`, `numero2`, `operacion`), pero no declara tipos, rangos, valores permitidos ni documentación contractual. Las clases siguientes se basan únicamente en esa interfaz pública y distinguen los casos observados en los tests de los casos aún no implementados.

| ID | Descripción | Técnica | Clase / Límite | Input | Expected Output | Checklist de cobertura |
|---|---|---|---|---|---|---|
| EP_tres_argumentos | Usa la aridad declarada por la firma. | EP válida | Tres argumentos posicionales | `1, 2, '+'` | Resultado calculado sin error. | 1 |
| EP_operacion_reconocida | Usa un valor de operación aceptado por el comportamiento observado. | EP válida | Símbolo de operación reconocido | `5, 3, '-'` | `2` | 2 |
| EP_operacion_no_reconocida | Usa un valor de operación que no pertenece al conjunto aceptado por la función. | EP inválida | Símbolo no reconocido | `10, 5, 'x'` | `ValueError` | 5 |
| EP_operando_numerico | Usa operandos numéricos ordinarios. | EP válida | Operandos numéricos | `4, 3, '*'` | `12` | 3 |
| EP_operando_no_numerico | Comprueba el comportamiento con un tipo de operando no declarado en la firma. | EP no documentada | Cadena, `None` u otro tipo no numérico | Entrada no implementada en los tests actuales | Debe definirse el contrato; no hay resultado esperado verificable en el test existente. | Ninguno |
| BVA_divisor_cero | Comprueba el límite natural del divisor para las operaciones `/`, `//` y `%`. | BVA límite | `numero2=0` | Entrada no implementada en los tests actuales | Debe definirse si se espera `ZeroDivisionError` u otro comportamiento. | Ninguno |
| BVA_numero_cero | Comprueba el valor cero del primer operando en operaciones que lo admiten. | BVA límite | `numero1=0` | Entrada no implementada en los tests actuales | Debe definirse el resultado esperado por operación. | Ninguno |
| BVA_dominio_logaritmo | Comprueba el límite del dominio matemático del logaritmo natural. | BVA límite | `numero1=0` y valores negativos | Entrada no implementada en los tests actuales | Debe definirse el error esperado. | Ninguno |

### Mejoras sugeridas — `calcular`
- Faltan por crear: tests para `**`, `//`, `%`, `c`, `√3`, `cbrt`, `abs`, `neg` y `ln`; cada uno debe comprobar el valor devuelto. También faltan casos de divisor cero para `/`, `//` y `%`, dominio inválido de `ln`, operandos negativos en raíces y operandos no numéricos.
- Ya está cubierto: los tests 1, 2, 3 y 4 cubren suma, resta, multiplicación y división; el 5 cubre la excepción del caso comodín; el 6 cubre la rama de raíz cuadrada. Todos comprueban el valor, salvo la excepción, que solo comprueba el tipo.
- Sobran o se pueden eliminar: no hay tests redundantes entre sí. Mantendría los seis porque cada uno representa una operación o el error de operación inválida.
- Cobertura parcial: `test_operacion_invalida` no verifica el mensaje de `ValueError`; `test_raizcuadrada` usa `numero2=0`, pero no demuestra que se ignore ese argumento ni cubre entradas negativas. Las operaciones cubiertas solo tienen un ejemplo y no prueban límites o tipos inválidos.

### Posible parametrización — `calcular`
- Parametrizaría [test_suma](../../test_calculadora.py#L13), [test_resta](../../test_calculadora.py#L18), [test_multiplicacion](../../test_calculadora.py#L23) y [test_division](../../test_calculadora.py#L28), porque comparten la misma preparación, llamada y aserción del valor; cambiarían `numero1`, `numero2`, `operacion` y el resultado esperado.
- Mantendría separado [test_operacion_invalida](../../test_calculadora.py#L33), porque verifica una excepción en lugar de un valor, y [test_raizcuadrada](../../test_calculadora.py#L37), porque usa una operación unaria con semántica distinta.

## CHECKLIST DE INTEGRIDAD

=======================
Total funciones con test en inventario : 1
Funciones con tabla de tests reales      : 1 → debe ser 1
Funciones con tabla Caja Blanca          : 1 → debe ser 1
Funciones con tabla Caja Negra           : 1 → debe ser 1
Funciones con bloque designer integrado : 1 → debe ser 1
Funciones con sección de Mejoras        : 1 → debe ser 1
Funciones completas en auditoría        : 1 → debe ser 1
Estado: ✅ COMPLETO

## Orden de Prioridad de Testing

| Orden | Función | Qué haría | Por qué |
|---:|---|---|---|
| 1 | `calcular` | Ampliar tests ahora | Concentra toda la lógica de negocio, tiene 15 ramas de operación y varias excepciones matemáticas posibles. La cobertura actual solo alcanza 6 ramas. |

Atacaría primero `calcular`, ampliando las ramas sin cobertura y los dominios inválidos porque cualquier regresión afecta a toda la calculadora. No hay getters, setters ni delegaciones triviales que dejar para después, y no dejaría esta función sin pruebas adicionales mientras sigan descubiertas las operaciones implementadas.
