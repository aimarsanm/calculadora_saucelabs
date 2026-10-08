# Inventario global del proyecto

## Paquetes

| Paquete | Cantidad de clases |
|---|---:|
| `src` | 0 |

## Paquete: `src`

No se localizaron clases de produccion en este paquete.

### Funciones de produccion sin clase

| Funcion | Cantidad de tests | Tests que faltan por hacer | Tests que se pueden parametrizar | Tests que se pueden borrar |
|---|---:|---:|---:|---:|
| `calcular` | 6 | 13 | 4 | 0 |

Evidencia del reverse plan: sus tablas contienen 6 tests reales y 13 casos sin checklist de cobertura. La tabla de mejoras identifica 4 tests parametrizables y no identifica tests eliminables. No se encontro un plan normal (`*plan*.md` sin `reverseplan`) con cantidades adicionales.

## Tests

| Archivo | Clase de test | Cantidad de tests | Funciones ejercitadas |
|---|---|---:|---|
| [tests/test_calculadora.py](tests/test_calculadora.py) | `TestCalcular` | 6 | `calcular` |

Los seis tests llaman directamente a `calcular`: `test_suma`, `test_resta`, `test_multiplicacion`, `test_division`, `test_operacion_invalida` y `test_raizcuadrada`.

## Planes localizados

- Reverse plan: [tests/reversetestplans/calculadora/reverseplan_TestCalcular.md](tests/reversetestplans/calculadora/reverseplan_TestCalcular.md)
- Planes normales: ninguno.
- La busqueda de archivos `.md` cuyo nombre contiene `plan` o `reverseplan` termino sin encontrar planes normales adicionales.

## Limitaciones

- `calcular` es una funcion de nivel de modulo; por eso no existe una tabla de clase ni un resumen porcentual global de clase.
- El reverse plan no aporta un denominador separado para los indicadores de mejora. Los valores 13, 4 y 0 se obtienen respectivamente de los casos sin checklist, la seccion de parametrizacion y la seccion de eliminacion; no se calculan porcentajes por falta de ese denominador.
- Se excluyeron caches, artefactos generados, `.venv`, `htmlcov`, `.playwright-mcp` y `alembic/versions` cuando aplicaba.
