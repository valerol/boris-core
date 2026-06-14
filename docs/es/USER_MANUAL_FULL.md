# Manual de usuario completo

Paquete público BOIS:SIMA&BORIS v1.4.3 con paridad estricta de idiomas de la ONU y BORIS EGO v1.0.

Este paquete proporciona un analizador SIMA local y sin red, más documentación para el uso humano de BOIS/BORIS. Las salidas son reconstrucciones candidatas, no verdad final ni validación de campo.

Una persona revisora debe definir el dominio, la interfaz de valores, el riesgo aceptable y las condiciones de parada.

No use este paquete para gobernanza coercitiva autónoma, decisiones médicas/jurídicas/financieras/militares ni control institucional oculto.

## Flujo de trabajo

1. Defina el dominio D y la interfaz de valores V.
2. Declare el sustrato S: unidades, canales, memoria, costes, modos de fallo y autoridad de parada.
3. Añada observaciones como opers: disparador, distinción, evidencia, portador, autoridad, puerta de valor/riesgo, transformación, escritura de memoria, señal de cierre, residuo de transición, coste y confianza.
4. Ejecute validación y análisis.
5. Trate M=<O,E,A,V,R,C,T> como una reconstrucción candidata.
6. Revise las señales de riesgo.
7. Ejecute una prueba de experiencia antes de crear instrucciones BORIS locales.
8. Conserve la ruta de reversión y las condiciones de parada.

## Comandos

```bash
python -m bois_sima_boris docs --lang es
python -m bois_sima_boris validate examples/example_local_workflow.json
python -m bois_sima_boris analyze examples/example_local_workflow.json --out analysis.json --md analysis.md
python -m bois_sima_boris self-check --root .
python -m pytest
```

## Núcleo activo y paridad lingüística

El paquete completo admite árabe, chino, inglés, francés, ruso y español sin idioma público preferente. Use `BORIS_EGO_LAYER.md` para la capa EGO activa y `../../core/ACTIVE_CORE_REFERENCE_v1_4_8.md` para todos los espejos del núcleo.

## Límites de uso

Este es un paquete público experimental. No lo use como gobernador independiente, sustituto de expertos de dominio ni prueba de conciencia de máquina. Todo paso del análisis a la instrucción requiere revisión humana, límites de aplicabilidad y señales de parada.
