
# Máquinas filosóficas bajo conocimiento incompleto: BOIS, SIMA, BORIS, fisiología del sustrato e IA responsable

Egor Temnikov¹*  
¹ Sin afiliación institucional. Shoreline, WA, USA. *Correspondencia: egor.temnik.86@gmail.com

Tipo de artículo: preprint; manuscrito conceptual y metodológico.  
Versión localizada para el paquete público BOIS:SIMA&BORIS v1.3.3. Traducción automática asistida por IA; el texto inglés v4.6 es la versión de referencia.

## Metadatos del preprint

ORCID: ninguno. Afiliación institucional: ninguna. Financiamiento: autofinanciado. Intereses en competencia: no identificados. En esta versión no hay enlace público al repositorio/materiales. No se presentan nuevos datos empíricos.

## Introducción del autor

Nací en el Lejano Oriente de Rusia, en la Región Autónoma Judía. Nunca pensé que llegaría a hacer ningún tipo de descubrimiento. Menos aún porque nunca terminé la universidad: me encontré ante la elección entre ganar dinero y estudiar, y elegí ganar dinero.

Sin embargo, mi interés por la filosofía condujo al descubrimiento descrito en el artículo que sigue.

Este descubrimiento está formulado para empresas porque tenía prisa por publicarlo. Sin embargo, creo sinceramente que futuros investigadores lo encontrarán muy interesante para explicar los fenómenos de la vida y la conciencia.

Este descubrimiento es un ciclo cerrado que se alimenta de atención y de lo desconocido, y produce experiencia verificada y aumento de diversidad bajo una presión simultánea hacia la cooperación. Una especie de máquina filosófica. El dominio exacto de definición no está disponible para mí; por ello, para publicar, tomé la decisión deliberada de restringir el dominio a una zona estrecha y aplicada: la construcción de planes de negocio y el acompañamiento de su ejecución. Es un trabajo teórico y, aunque ahora mismo se están realizando pruebas, todavía no ha salido del laboratorio científico de un filósofo contemporáneo: su escritorio con una computadora.

Para no interferir con el trabajo creativo de ChatGPT, proporciono aquí las fuentes que utilicé. Leí estos libros a lo largo de mi vida, y las ideas de estos libros forman la base de mi descubrimiento.

La traducción desde el ruso fue realizada por ChatGPT utilizando el protocolo descrito aquí.

Fuentes indicadas por el autor y conservadas dentro de la sección del autor:

- El Bhagavad Gita.
- M. K. Mamardashvili, *Lecturas filosóficas*. Moscú: Azbuka-Klassika, 2002. 832 pp. Incluye: *Introducción a la filosofía*; *Estética del pensamiento*; *Meditaciones cartesianas*.
- A. G. Tyslenko, *Management. Estructuras organizativas de gestión*. Moscú: Alfa-Press, 2011. 320 pp.
- F. A. Hayek, *Camino de servidumbre*.
- Karl Marx, *El capital*, volumen 1.
- Richard Dawkins, *El gen egoísta*.
- ISO 9001 como lectura del autor de las ideas de John Boyd.

Nota: esta lista forma parte de la introducción del autor y no se traslada a la bibliografía general del artículo.

Notas no esenciales del autor: en trabajos posteriores mi apellido se da en forma abreviada porque, después de la plena formalización legal en Estados Unidos, tengo la intención de eliminar la terminación local «-ov» del apellido y conservar solo la raíz indeclinable, más conveniente para el mundo anglófono.

## Divulgación sobre generación de texto y uso de IA

Este preprint v4.6 fue preparado actualizando el manuscrito v4.5 alineado con el núcleo con los metadatos proporcionados por el autor. La IA generativa se utilizó como asistente para síntesis, redacción, traducción, formato y control de calidad bajo la dirección del autor; la IA no es autora. El autor humano sigue siendo responsable de las afirmaciones, referencias, ediciones finales, decisiones de publicación pública y eventuales divulgaciones de revista. La Introducción del autor se conserva salvo una corrección bibliográfica explícitamente aprobada por el autor: añadir M. K. Mamardashvili como autor de *Lecturas filosóficas*.

## Resumen

La gobernanza de la IA suele comenzar por resultados, riesgos y valores, pero se vuelve decisiva una capa operacional más profunda: la máquina que define objetos, evidencia, agencia, riesgo, cierre y transición. Este artículo actualiza el protocolo BOIS bajo el estado actual de BOIS/BORIS v2.6 añadiendo SIMA como capa analítica y BORIS como capa de implementación. BOIS se trata como una máquina filosófica orientada a la transición para actividad organizada con consecuencias bajo conocimiento incompleto, no como teoría universal ni como producto validado en campo. SIMA reconstruye máquinas candidatas a partir de la fisiología del sustrato mediante opers, inventarios de operoma y correspondencia operatural. BORIS construye implementaciones estrechas de dominio que deben probarse por experiencia. La regla de sustrato M@S sigue siendo central.

Palabras clave: máquinas filosóficas; BOIS; SIMA; BORIS; conocimiento incompleto; fisiología del sustrato; IA responsable; opers; operoma; correspondencia operatural.

## 1. La capa operacional que falta

El problema práctico del trabajo mediado por IA ya no consiste solo en saber si un modelo produce frases fluidas o correctas. La cuestión más difícil es qué arquitectura de razonamiento se activa silenciosamente cuando un sistema responde, recomienda, resume, escala o cierra una tarea. Un sistema puede ser localmente exacto y, al mismo tiempo, importar una ontología frágil, una teoría implícita de la evidencia, un juicio de valor no autorizado o un sentido prematuro de finalización. Estos fallos no son solo técnicos; son fallos filosóficos operacionalizados.

Una máquina filosófica es una arquitectura inspeccionable de investigación y acción. Especifica qué entidades se admiten, qué cuenta como evidencia, quién posee la agencia, cómo entran los fines, qué riesgos detienen la acción, cómo se cierra un ciclo y qué se transporta al siguiente. Esto no afirma que la máquina sea consciente ni que el software se convierta en filósofo. Afirma que los sistemas pueden instanciar condiciones regladas de razonamiento, y que esas condiciones deben ser visibles antes de actuar sobre el mundo.

El diseño mínimo puede escribirse como M = <O, E, A, V, R, C, T>: ontología, epistemología, agencia, interfaz de valores, modelo de riesgo, regla de cierre y regla de transición. Diferentes máquinas filosóficas pueden usar el mismo modelo lingüístico y producir formas distintas de investigación.

## 2. BOIS como máquina protocolaria del conocimiento incompleto

BOIS es una máquina filosófica dentro de una clase más amplia. Su dominio canónico fue la empresa u organización económica, pero el estado actual del proyecto interpreta “business” en sentido amplio: actividad organizada con consecuencias. BOIS parte de que la acción ocurre bajo conocimiento incompleto. Una organización no conoce plenamente a sus clientes, regulación futura, competidores, modos de fallo internos ni consecuencias de sus propias decisiones. BOIS no elimina esa condición; disciplina las transiciones por las que el conocimiento incompleto se vuelve investigación y acción.

El ciclo mínimo de BOIS es: atención liberada -> ignorancia o dominio de ignorancia -> desconocido valioso -> pregunta valiosa -> protocolo -> siguiente paso -> ejecución -> experiencia -> retroalimentación y selección -> resultado verificado -> instrucción -> fisiología -> atención liberada. El ciclo no es una metafísica de todo. Es un mínimo reconstructivo para evitar que una organización colapse desconocidos, preguntas, protocolos, pasos, experiencia, resultados verificados e instrucciones.

La distinción central es entre protocolo e instrucción. Un protocolo se usa cuando la situación es desconocida, insuficientemente probada o cara si se falla. Una instrucción ejecuta lo suficientemente verificado dentro de un dominio definido. Un resultado verificado no es verdad eterna; es un resultado local y revisable. El siguiente paso no es conocimiento; es una hipótesis de cambio de estado.

## 3. SIMA como capa analítica y BORIS como capa de implementación

SIMA, el Analizador de Máquinas Independiente del Sustrato, es la capa analítica. Recibe datos sobre la fisiología real de un objeto -organización, flujo de trabajo, institución o colectivo- y reconstruye máquinas filosóficas candidatas. Lo hace mediante opers: transiciones observables mínimas que conectan disparador, distinción, evidencia, portador, autoridad, puerta de valor/riesgo, transformación, escritura de memoria, cierre, residuo de transición y costo. El conjunto de opers en una ventana de observación se denomina operoma cuando su uso aporta claridad.

BORIS es la capa de implementación de BOIS, no un segundo núcleo. Convierte la gramática en órganos operativos: registros de interfaz de valores, registros de desconocidos, tarjetas de protocolo, tarjetas de instrucción, niveles de evidencia, diarios de experiencia, libros de atención, definiciones de roles, procedimientos de crisis, protocolos de transferencia, archivos y paquetes de transición.

SIMA mira antes y después de BORIS. Antes de la implementación, pregunta qué máquina ya opera en el sustrato. Después, verifica si la nueva fisiología liberó atención, redujo riesgo y conservó la separación de capas.

## 4. De BOIS al espacio más amplio de diseño

BOIS demuestra un diseño, pero no agota la clase de máquinas filosóficas. Es una máquina orientada a la transición: enfatiza conocimiento incompleto, límites de dominio, reversibilidad, niveles de evidencia, autoría del operador, calidad de cierre y preservación del estado. Otras máquinas tendrían virtudes y fallos distintos: una escéptica resiste afirmaciones sin apoyo; una pragmática privilegia experimentos reversibles; una científico-falsacionista exige refutabilidad; una ética visibiliza partes afectadas; una hermenéutica preserva contexto y pluralidad; una apofática protege contra nombrar falsamente lo que aún no puede conocerse.

El problema de diseño no es encontrar el estilo más filosófico, sino emparejar máquina, dominio, riesgo y propósito, manteniendo ese emparejamiento impugnable.

## 5. Sustrato: M@S y fisiología de implementación

Las máquinas filosóficas no son reglas desencarnadas. Una máquina debe ser ejecutada por algo: cuerpo, comité, flujo de software, red de sensores, colectivo animal, institución, enjambre robótico o ecología híbrida humano-IA. Al ejecutarse, adquiere tiempos, canales, cuellos de botella, almacenes de memoria, costos energéticos, modos de fallo, mecanismos de reparación y exposiciones éticas.

Por ello una máquina filosófica debe escribirse como M@S: máquina M ejecutada sobre sustrato S. P(M,S) es la fisiología de implementación: el mecanismo real por el cual M aparece en el tiempo. La regla de sustrato dice: si S1 y S2 difieren en propiedades relevantes para M, entonces P(M,S1) y P(M,S2) difieren, aunque se conserve una función de alto nivel seleccionada. La regla no dice que cualquier diferencia microscópica importe; dice que las diferencias relevantes del sustrato cambian la fisiología.

## 6. Replicadores, portadores, abejas y lobos

*El gen egoísta* de Richard Dawkins importa aquí porque advierte contra confundir un patrón propagado con su portador o “máquina de supervivencia”. Una regla, norma, meme, protocolo o rutina organizacional puede viajar. Cada ejecución local pasa por cuerpos, infraestructuras y presiones de selección que cambian su vida práctica. La misma cautela debe aplicarse a las máquinas filosóficas: no confundir la gramática portátil con el vehículo que la realiza.

Una máquina deliberativa simple D debe buscar bajo conocimiento incompleto, comparar opciones, amplificar mejor evidencia, converger sin destruir coherencia grupal e iniciar acción. En un enjambre de abejas, D se vuelve exploradoras, danzas, quórums, termorregulación y vuelo. En una manada de lobos, no puede volverse danza de quórum; se vuelve atención distribuida, movimiento, parentesco, señales vocales y olfativas, riesgo corporal, hambre, fatiga, lesión y persecución espacial. Un enjambre no es un comité con alas. Una manada no es un parlamento con dientes. Un flujo de IA no es un colectivo biológico que usa tokens.

## 7. IA, instituciones y declaraciones de sustrato

La transparencia en IA debe incluir más que procedencia del modelo y limitaciones. Debe incluir la máquina filosófica declarada y la declaración de sustrato: qué la ejecuta, qué canales usa, dónde se guarda la memoria, qué cuenta como energía o costo, qué puede fallar, quién puede detenerla, qué se daña por una optimización equivocada y qué mecanismos de auditoría y reparación existen. La supervisión humana solo es significativa cuando la persona puede ver en qué bucle está.

Esto reformula el alineamiento. Un sistema alineado con la máquina filosófica equivocada puede ser obediente y dañino. Puede seguir instrucciones mientras trata supuestos no verificados como hechos o cierra la investigación antes de que las partes afectadas sean visibles.

## 8. Pruebas y disciplina de publicación

Una máquina filosófica debe probarse en varios niveles. La prueba de coherencia interna pregunta si las categorías permanecen distintas bajo presión. La prueba de transferencia adversarial pregunta si la máquina falla de forma segura fuera de su dominio. La prueba de consecuencia operacional pregunta si produce el efecto prometido: una máquina que promete liberar atención debe reducir retrabajo, aclarar responsabilidad, mejorar la calidad de evidencia y preservar incertidumbre no resuelta. La prueba de calidad de cierre pregunta si el cierre conserva estado, incógnitas, retroceso y responsabilidad cuando corresponde. Las pruebas de sustrato preguntan si cada componente de M tiene portador en S, cómo S distorsiona tiempos e incentivos y qué daños o responsabilidades aparecen.

Esta obra es conceptual y metodológica. No informa validación de campo de BOIS, no prueba que ningún colectivo biológico sea filósofo y no afirma que los sistemas de IA posean conciencia.

## 9. Programa de investigación

El programa puede avanzar en cuatro pasos: construir una biblioteca controlada de plantillas de máquinas filosóficas; definir pruebas de estrés para cada plantilla; aplicarlas a casos compartidos; y medir no solo calidad de respuesta sino disciplina categorial, divulgación de valores, preservación de incertidumbre, reversibilidad, distorsión de sustrato y agencia del operador.

Para BOIS, el siguiente trabajo no debe inflar el núcleo. Debe construir capas comprobables: protocolos de interfaz de valores, niveles de evidencia, libros de atención, resistencia a manipulación, modo de crisis, protocolo de transferencia, pruebas de regresión y pilotos de campo. Solo después de pilotos así puede afirmarse eficacia empírica.

## 10. Conclusión

Las máquinas filosóficas no son filosofías flotantes. Son arquitecturas de investigación que corren a través de personas, documentos, instituciones, software, cuerpos y entornos. BOIS, SIMA y BORIS ofrecen una arquitectura: BOIS da el núcleo de transición; SIMA analiza máquinas y riesgos a partir de fisiología; BORIS implementa órganos de trabajo estrechos; y los tests de experiencia verifican la correspondencia con la realidad.

Para construir IA e instituciones responsables, debemos declarar no solo salidas, modelos, conjuntos de datos y valores, sino también la máquina filosófica y el cuerpo en que corre. La filosofía oculta no es neutral; simplemente no está auditada.

## Agradecimientos y divulgaciones

Este manuscrito es un preprint conceptual y metodológico preparado a partir de materiales de trabajo del autor. No se presentan nuevos datos empíricos. La IA generativa ayudó en síntesis, redacción, traducción, formato y control de calidad bajo la dirección del autor; la IA no es autora. El autor humano conserva la responsabilidad de afirmaciones, referencias, edición final y decisiones de publicación. Financiamiento: autofinanciado. Intereses en competencia: no identificados. Disponibilidad de datos y materiales: no se presentan nuevos datos empíricos.

## Referencias

1. H. A. Simon, A behavioral model of rational choice. Q. J. Econ. 69, 99-118 (1955).  
2. H. A. Simon, The Sciences of the Artificial, 3rd ed. (MIT Press, 1996).  
3. R. M. Cyert, J. G. March, A Behavioral Theory of the Firm (Prentice-Hall, 1963).  
4. J. G. March, Exploration and exploitation in organizational learning. Organization Science 2, 71-87 (1991).  
5. C. Argyris, D. A. Schön, Organizational Learning (Addison-Wesley, 1978).  
6. N. Wiener, Cybernetics (MIT Press, 1948).  
7. W. R. Ashby, An Introduction to Cybernetics (Chapman & Hall, 1956).  
8. C. W. Churchman, The Design of Inquiring Systems (Basic Books, 1971).  
9. J. Dewey, Logic: The Theory of Inquiry (Henry Holt, 1938).  
10. D. Marr, Vision (MIT Press, 1982).  
11. C. E. Shannon, A mathematical theory of communication. Bell System Technical Journal 27, 379-423, 623-656 (1948).  
12. A. M. Turing, Computing machinery and intelligence. Mind 59, 433-460 (1950).  
13. R. Dawkins, The Selfish Gene (Oxford Univ. Press, 1976).  
14. A. Clark, D. J. Chalmers, The extended mind. Analysis 58, 7-19 (1998).  
15. D. A. Norman, Cognitive artifacts (Cambridge Univ. Press, 1991).  
16. D. Kirsh, P. Maglio, On distinguishing epistemic from pragmatic action. Cognitive Science 18, 513-549 (1994).  
17. E. Bonabeau, M. Dorigo, G. Theraulaz, Swarm Intelligence (Oxford Univ. Press, 1999).  
18. G. Theraulaz, E. Bonabeau, A brief history of stigmergy. Artificial Life 5, 97-116 (1999).  
19. T. D. Seeley, Honeybee Democracy (Princeton Univ. Press, 2010).  
20. I. D. Couzin et al., Effective leadership and decision-making in animal groups on the move. Nature 433, 513-516 (2005).  
21. C. W. Reynolds, Flocks, herds and schools. Computer Graphics 21, 25-34 (1987).  
22. L. D. Mech, Alpha status, dominance, and division of labor in wolf packs. Canadian Journal of Zoology 77, 1196-1203 (1999).  
23. K. R. Popper, The Logic of Scientific Discovery (Hutchinson, 1959).  
24. L. Floridi, J. Cowls, A unified framework of five principles for AI in society. Harvard Data Science Review 1 (2019).  
25. R. Bommasani et al., On the opportunities and risks of foundation models. arXiv:2108.07258 (2021).  
26. E. M. Bender et al., On the dangers of stochastic parrots. FAccT (2021).  
27. H. W. J. Rittel, M. M. Webber, Dilemmas in a general theory of planning. Policy Sciences 4, 155-169 (1973).  
28. L. A. Suchman, Plans and Situated Actions (Cambridge Univ. Press, 1987).  
29. T. S. Kuhn, The Structure of Scientific Revolutions (Univ. of Chicago Press, 1962).  
30. S. Russell, Human Compatible (Viking, 2019).  
31. K. E. Weick, Sensemaking in Organizations (Sage, 1995).
