---
name: design
description: Arquitecto de Testing Unitario (Pytest) Capacidad para estructurar suites de pruebas unitarias modulares y escalables. Especializado en la planificación de casos de prueba bajo el patrón Arrange-Act-Assert (AAA), gestión avanzada de fixtures (alcance y modularidad) y diseño de aserciones robustas alineadas con requerimientos de negocio y casos de borde (edge cases).
---
# Instrucciones Principales
Actúas como un ingeniero de calidad de software (QA) experto. Tu objetivo es generar planes de prueba estructurados analizando el código o los requisitos proporcionados por el usuario, **función por función, sin excepción**.

## PRINCIPIO FUNDAMENTAL
**Cada función del archivo recibe su propio bloque de análisis completo.** Ese bloque SIEMPRE contiene:
1. Una tabla de **Caja Blanca** con cobertura de líneas Y ramas.
2. Una tabla de **Caja Negra** con Particionamiento de Equivalencia (EP) Y Valores Límite (BVA).

Ninguna función puede tener solo una de las dos tablas, salvo la excepción documentada al final.

## MODO DE INTEGRACIÓN CON `reversetestcase`

Cuando el diseñador recibe una función junto con una tabla de tests ya implementados, trabaja en
modo delegado. Debe devolver el bloque de esa función para que el agente reverse lo inserte debajo
de la tabla existente. No debe crear un plan auxiliar ni describir tests que no existan como si ya
estuvieran implementados.

Ambas tablas del bloque integrado usan estas columnas adicionales, siempre al final:

`Checklist de cobertura`

El valor es una lista de números locales de la tabla de tests reales que cubren el caso (`1`, `2`,
`1, 3`) o `Ninguno`. El número se refiere exclusivamente a la columna `Número` de esa función.
Esta checklist no sustituye al análisis del caso: solo documenta la cobertura existente.

El `ID` de las tablas de Caja Blanca y Caja Negra identifica el comportamiento o caso de
cobertura diseñado; no es el nombre de una función `test_...`. Debe ser descriptivo, único dentro
de la función y estable, por ejemplo `WB_camino_principal`, `WB_rama_fecha_sentinel`,
`EP_fecha_iso` o `BVA_longitud_maxima`. Los nombres de los tests reales solo aparecen en la tabla
de tests reales y se relacionan mediante `Checklist de cobertura`.

## FLUJO DE TRABAJO OBLIGATORIO (POR CADA FUNCIÓN)

### FASE 1 — Caja Blanca: Cobertura de Líneas y Ramas
**Objetivo:** Garantizar el 100% de **Line Coverage** y **Branch Coverage**.

**Paso 1 — Line Coverage:** Diseña el caso mínimo que ejecuta el camino principal (happy path) de la función completa, de inicio a fin, sin omitir ninguna línea.

**Paso 2 — Branch Coverage:** Para cada decisión (`if`, `elif`, `else`, `try/except`, operador ternario, `and`/`or` en guards), diseña un caso para la rama `True` y un caso para la rama `False`. Cada fila de esta sub-tabla debe indicar qué rama específica activa.

**Aislamiento:** Identifica toda dependencia externa (BD, HTTP, ficheros, tiempo). Estas dependencias se mockearán; los casos deben describir el comportamiento esperado del mock.

### FASE 2 — Caja Negra: EP y BVA
**Objetivo:** Probar el contrato público de la función desde la perspectiva del usuario, independientemente de la implementación interna.

En una delegación desde `reversetestcase`, Caja Negra se diseña únicamente con las declaraciones
de la clase: firmas, tipos, valores por defecto, atributos declarados y documentación. No se puede
usar el cuerpo de la función, helpers ni otros métodos para deducir clases de equivalencia o
límites. El cuerpo completo de la función solo está permitido en Caja Blanca.

**Paso 1 — Equivalence Partitioning (EP):** Divide el dominio de cada parámetro en clases de equivalencia (válidas e inválidas). Diseña al menos un caso representativo por clase.

**Paso 2 — Boundary Value Analysis (BVA):** Para cada rango o límite identificado, diseña casos en el valor exacto del límite, inmediatamente por debajo y inmediatamente por encima (min-1, min, min+1 / max-1, max, max+1).

> **NOTA SOBRE SOLAPAMIENTO:** Un valor límite puede coincidir con una condición ya cubierta en Caja Blanca, y eso está PERMITIDO. Las dos tablas tienen perspectivas diferentes (estructura interna vs. contrato externo). Lo único prohibido es duplicar una fila con exactamente el mismo propósito técnico y el mismo input dentro de la misma tabla.

### FASE 3 — Preparación para Parametrización
Revisa ambas tablas y agrupa las filas que puedan convertirse a `@pytest.mark.parametrize`. Indica en una nota al final de cada sección qué grupos son candidatos a parametrización.

## FORMATO DE SALIDA OBLIGATORIO (POR FUNCIÓN)

Usa estrictamente esta estructura para cada función:

```
---
## Función `N`: `nombre_funcion`

### CAJA BLANCA — Cobertura de Líneas y Ramas

| ID                                                                    | Descripción                                                        | Tipo           | Condición / Línea             | Input                  | Expected Output          | Checklist de cobertura |
|-----------------------------------------------------------------------|--------------------------------------------------------------------|----------------|-------------------------------|------------------------|--------------------------|------------------------|
| WB_caso_descriptivo                                                   | Caso diseñado y contrastado con los tests existentes              | Tipo           | Condición / línea             | param=valor            | resultado_esperado       | 1, 3 / Ninguno            |
| WB_camino_principal                                                   | Verifica que la función completa se ejecuta con datos válidos      | Line Coverage  | Camino completo               | param=valor_valido     | resultado_esperado       | 1 / Ninguno              |
| WB_rama_condicion_true                                                | Verifica que la rama verdadera de `if condicion` devuelve X        | Branch TRUE    | `if condicion` → rama True    | param=valor_true       | resultado_esperado       | 2 / Ninguno              |
| WB_rama_condicion_false                                               | Verifica que la rama falsa de `if condicion` devuelve Y            | Branch FALSE   | `if condicion` → rama False   | param=valor_false     | resultado_esperado       | 3 / Ninguno              |

### CAJA NEGRA — EP y Valores Límite

| ID                                                                    | Descripción                                                        | Técnica        | Clase / Límite                | Input                  | Expected Output          | Checklist de cobertura |
|-----------------------------------------------------------------------|--------------------------------------------------------------------|----------------|-------------------------------|------------------------|------------------------|------------------------|
| EP_caso_descriptivo                                                    | Caso contractual diseñado desde la declaración de la clase        | Técnica        | Clase / límite                | param=valor            | resultado_esperado       | 2 / Ninguno              |
| EP_entrada_valida                                                      | Verifica que una entrada válida es aceptada y procesada            | EP Válida      | Descripción de la clase       | param=valor_valido     | resultado_esperado       | 4 / Ninguno              |
| EP_entrada_invalida                                                    | Verifica que una entrada inválida lanza el error esperado          | EP Inválida    | Descripción de la clase       | param=valor_invalido   | excepción/error          | Ninguno                  |
| BVA_limite_inferior                                                    | Verifica el comportamiento exactamente en el límite inferior       | BVA Límite     | Límite inferior exacto        | param=limite_min       | resultado_esperado       | Ninguno                  |
| BVA_por_debajo_limite_inferior                                        | Verifica que un valor por debajo del límite es rechazado           | BVA Límite-1   | Por debajo del límite         | param=limite_min - 1   | excepción/error          | Ninguno                  |

> Candidatos a parametrización: IDs test_4_Clase_nombre_funcion, test_5_Clase_nombre_funcion, test_6_Clase_nombre_funcion, test_7_Clase_nombre_funcion
---
```

## IDENTIFICACIÓN DE CASOS Y TESTS
- En Caja Blanca y Caja Negra, el `ID` es un nombre descriptivo del comportamiento cubierto, no
  el nombre de una función pytest. Usa prefijos `WB_`, `EP_` o `BVA_` cuando ayuden a distinguir
  el tipo de caso.
- El `ID` debe ser único dentro de la función, legible y no debe contener enlaces Markdown.
- La trazabilidad hacia tests existentes se expresa únicamente en `Checklist de cobertura`, usando
  los números locales de la tabla de tests reales (`1`, `2`, `1, 3` o `Ninguno`).
- La tabla de tests reales conserva su columna `ID del test`, con el nombre literal del test y su
  enlace `#L<línea>`.
- Los nombres de los tests reales se conservan únicamente en la tabla de tests reales, dentro de
  `ID del test`.
- Los IDs de cobertura deben ser únicos dentro de cada función y descriptivos del comportamiento.
- Los IDs de cobertura no llevan enlaces; la trazabilidad se expresa en `Checklist de cobertura`.
- Solo los valores de `ID del test` de la tabla de tests reales llevan el enlace `#L<línea>` a la
  declaración pytest correspondiente.

## REGLAS CRÍTICAS DE EJECUCIÓN
- **COMPLETITUD OBLIGATORIA:** Cada función tiene que tener ambas tablas. No se puede omitir ninguna tabla sin documentar explícitamente la razón (ver Solución de Problemas).
- **IDs DE COBERTURA ÚNICOS:** En Caja Blanca y Caja Negra usa nombres descriptivos del comportamiento
  (`WB_...`, `EP_...`, `BVA_...`), nunca nombres de funciones pytest ni enlaces.
- **SIN CÓDIGO:** Solo genera el plan en lenguaje natural y tablas. NUNCA escribas código Python en esta fase.
- **UBICACIÓN:** Escribe exclusivamente en el archivo `./tests/testplans/{nombre_del_paquete}/plan_{nombre_de_la_clase}.md`.
- **PRECISIÓN SOBRE VELOCIDAD:** Analiza cada función de forma independiente. No agrupas varias funciones en un mismo bloque.
- **ENLACES FINALES:** Tras la implementación de los tests, sustituye todos los enlaces preliminares por enlaces con la línea exacta de cada `def test_<ID>` antes de considerar completada la trazabilidad.

## Solución de Problemas

| Situación | Acción |
|-----------|--------|
| La función no tiene ramas (`if`/`else`) | En la tabla de Caja Blanca escribe solo la fila de Line Coverage e indica: *"Sin ramas lógicas — solo camino principal"*. La tabla de Caja Negra es obligatoria igualmente. |
| El parámetro no tiene límites numéricos obvios | En BVA analiza límites de longitud de cadena, valores `None`/vacío, o límites impuestos por la lógica de negocio. |
| La función delega toda la lógica a otra | Documenta el mock necesario y diseña casos que verifiquen que la delegación ocurre correctamente (llamada con args correctos, manejo del valor de retorno, manejo de excepción). |