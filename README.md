# Seminario de Sistemas Expertos

## Contexto de la problemática 

- El trastorno del espectro autista (TEA) es una condición neurológica compleja que afecta el desarrollo social, la comunicación y el comportamiento de las personas. 
- Debido a la diversidad de síntomas y a la necesidad de una evaluación integral, el diagnóstico temprano del TEA puede ser un desafío para los profesionales de la salud (Carmona-Serrano, 2020).  
- Aproximadamente el 1,5% de la población mundial sufre de TEA y todavía es diagnosticada erróneamente por psiquiatras infantiles y adultos y, a veces, incluso confundida con otras condiciones del neurodesarrollo que tienen características similares (Fusar-Poli, 2020). 
- Aún no existe una prueba de laboratorio enfocada para ayudar al personal de atención médica a diagnosticar la afección en un 100 % y no hay tratamiento farmacológico para el TEA (Carmona-Serrano, 2020). 
- Las aplicaciones móviles y de sistemas han demostrado ser herramientas de apoyo para detección de TEA (Adamu, 2019). 

## Problema a Resolver

En este contexto, el principal problema a resolver es el desarrollo de un sistema que apoye el proceso de detección del TEA. Actualmente, este proceso puede ser largo, costoso y a menudo depende de la experiencia y el conocimiento del personal médico. El desarrollo de  un sistema experto que integre el conocimiento de un experto en el campo del TEA para ayudar a una detección temprana del TEA y sea una herramienta de apoyo a los profesionales de la salud.

## Objetivo General 

Desarrollar un sistema experto basado en inteligencia artificial que facilite la detección temprana del TEA y sea una herramienta de apoyo a los profesionales de la salud mediante la integración de conocimiento de un experto en el tema.

## Justificación

- Detección temprana: El TEA es un trastorno de neurodesarrollo que afecta a personas desde la niñez hasta la adultez. Por lo que la detección temprana del TEA es importante para poder desarrollar intervenciones efectivas por partes de especialistas médicos (psiquiatras, psicólogos, neurólogos)  que pueden ayudar a mejorar la calidad de vida del paciente.
  
- Costo y Tiempo: Los métodos tradicionales de diagnóstico, como los criterios DSM-5, la Escala de Calificación del Autismo Infantil (CARS) y las entrevistas de comportamiento autista, son costosos y requieren mucho tiempo, por lo que se limita la accesibilidad al paciente, especialmente en familias que tienen ingresos bajos y medianos.
  
- Falta de especialistas: la carencia de especialistas en el diagnóstico temprano del TEA vuelve complejo el problema, ya que el paciente no recibe un diagnóstico oportuno y/o favorable, y esto tiene como resultado intervenciones tardías, lo que puede influir en el desarrollo de la calidad de vida del paciente.
  
- Incertidumbre en el diagnóstico: Los factores relacionados con el autismo, como la interacción social, la comunicación y el comportamiento, no pueden medirse con certeza absoluta debido a la vaguedad y la imprecisión de la información. Esto hace que los diagnósticos tradicionales sean menos precisos.

## Funcionalidad del Sistema Experto

- Recopilación de Datos El sistema experto recopilará información sobre los antecedentes médicos del paciente, los resultados de evaluaciones conductuales y los informes de los cuidadores. Esta información se utilizará como insumo para el proceso de diagnóstico.

- Análisis de Datos Utilizando técnicas de inteligencia artificial, el sistema analizará los datos recopilados para identificar características que puedan indicar la detección del TEA. Esto incluirá el uso de algoritmos de inteligencia artificial de sistemas expertos.

- Diagnóstico y Recomendaciones Basándose en el análisis de los datos, el sistema experto generará un informe de la detección del TEA.

## Diseño del Sistema Experto

![image](https://github.com/user-attachments/assets/05c1b485-f9f0-4cc9-8834-6d1ccb5c0793)

### Arquitectura BRB 

![image](https://github.com/user-attachments/assets/82c227ae-a6bb-4af9-80bd-e6eaf8c4ee46)

Interfaz del Usuario Es quien facilita la  comunicación entre el usuario  y el motor de inferencias. Permite ingresar información  para el sistema y comunicar  al usuario las respuestas del  S.E.

Módulo de Explicación Explica los pasos realizados  por el motor de inferencias  para lograr las conclusiones,  justificando las acciones (por  qué utiliza ciertas reglas).

- Motor de Inferencias Es la Sección del S. E que  realiza los procesos de  inferencia que relacionan la  información contenida en la  memoria de trabajo con la  base de conocimientos, para  sacar conclusiones.

- Base de Hechos Memoria auxiliar que  contiene información sobre  el problema a resolver  (datos iniciales) y el estado  del sistema a lo largo del  proceso de inferencia (datos  intermedios).

- Base de Conocimientos Posee información sobre el  dominio de conocimientos a  que viene referido el sistema  experto. Contiene  conocimiento declarativo  (hechos) y procedimental  (reglas).

- Módulo de Adquisición del  Conocimiento Facilita el ingreso del conocimiento  en la base y de los mecanismos de  inferencia en el motor de inferencia.  Valida la veracidad y coherencia de  los hechos y reglas que se  introducen.

![image](https://github.com/user-attachments/assets/a2f25dd0-a1ac-4d18-886f-29729480818b)

## Desarrollo en Experta de la Base de Conocimientos
![image](https://github.com/user-attachments/assets/5d9f2b04-5003-40ed-b80f-191812fe0cbe)

## Implementación en Experta de la Base de Conocimientos
![image](https://github.com/user-attachments/assets/63c8e654-2e24-4ec2-aece-f0516d629cf6)

## Ejecución en Experta de la Base de Conocimientos
![image](https://github.com/user-attachments/assets/47ddcff5-70d1-4885-8775-21f36b040bef)

![image](https://github.com/user-attachments/assets/4bc327f1-bd93-4d59-a8ab-81918b02f188)

## Reflexiones

### ¿Que se les dificultó más de todo el proyecto?

Lo más complicado fue elegir el Algoritmo apropiado que se adaptara a la solución de la problemática planteada, estuve revisando varios artículos que me ayudaran a darme una idea de que se había implementado con anterioridad, encontré sistemas expertos basados en el sistema basado en reglas, en lógica difusa, en arboles de decisión, en vector support machine y basado en reglas de creencia. Cada algoritmo tiene sus fortalezas y debilidades, y puede requerir pruebas exhaustivas para determinar cuál es el más efectivo. Sin embargo, dentro de la literatura expuesta pude identificar el uso del algoritmo basado en reglas y una limitación era generar las reglas de forma manual ya que se podían no dar el resultado satisfactorio y esperado, entonces al encontrar la herramienta WAKA tomé la decisión de usar JRip (RIPPER) y asi generar las reglas basado en parámetros de validación de las reglas.

### ¿Qué se les facilitó más de todo el proyecto?

Ya teniendo la forma de generar las reglas, lo que se me facilito fue la implementación de las reglas en la herramienta Experta de Python, ya que al revisar la sintaxis de como realizar el sistema experto en esta librería me fue fácil de entender, por la experiencia previa que tengo desarrollando aplicaciones con Python y después configurar la herramienta de Flask para el diseño e implementación del formulario web para que fuera más accesibles al usuario.

### ¿Cuál es su opinión del papel que los sistemas expertos en un futuro?

En mi opinión creo que los sistemas expertos tienen una gran desventaja con respecto a otras áreas de la inteligencia artificial, por la limitante de poder expandir el conocimiento y que este no sea costoso desarrollarlo independientemente de la herramienta de implementación, por lo que, en artículos científicos que leí y lo desarrollado en el prototipo, su futuro es la integración con otras tecnologías de inteligencia artificial, como el aprendizaje automático y el procesamiento del lenguaje natural. Esta integración permitirá que los sistemas expertos se adapten y aprendan de manera continua, mejorando su capacidad para tomar decisiones en contextos más complejos.


### ¿Qué alternativas existen hoy al uso de los sistemas expertos?

En la actualidad existen varias alternativas y enfoques que pueden complementar o sustituir el uso de sistemas expertos tradicionales. Estas alternativas pueden ser:

- Aprendizaje Automático (Machine Learning) el aprendizaje automático permite que los sistemas aprendan patrones a partir de datos. 

- Aprendizaje Profundo (Deep Learning) utiliza redes neuronales profundas, ha mostrado resultados sobresalientes en áreas como el reconocimiento de voz e imagen, traducción automática, y más.

- Procesamiento del Lenguaje Natural permite a las máquinas comprender y generar lenguaje humano. 

- IA generativa es un tipo de inteligencia artificial diseñada para generar contenido nuevo a partir de datos existentes. 

## Mejora del Sistema

### Clasificación de la gravedad del autismo 

- El sistema puede mejorar para la detección de la gravedad del TEA basándose en los criterios del DSM 4 y DSM 5. 

- El análisis de datos se realice con un algoritmo de aprendizaje automático.

- El poder utilizar la Técnica de Sobremuestreo de Minorías Sintéticas (SMOTE) para corregir el problema del desequilibrio de atributos que se puede tener en el conjunto de datos. 

- Evitar la incertidumbre en las respuestas de los pacientes al construir la base de conocimiento en el sistema basado en reglas de creencia BRBES.

- Tener una gran cantidad de datos en este campo de estudio a través de técnicas de inteligencia artificial, ya que la mayoría de las aplicaciones desarrolladas se basan en la literatura y en el experto humano para obtener datos. 

## Conclusión

### Mejora del Diagnóstico

Se presento el desarrollo de un sistema experto basado en reglas para la detección de TEA en niños. Este sistema experto maneja bases de reglas básico, pero se pueden explorar otros algoritmos como BRBES, Regresión Lineal, ANN, Bosque Aleatorio y Árbol de Decisión utilizando curvas ROC para evaluar su precisión. 

### Accesibilidad y Escalabilidad

Los resultados muestran que el sistema experto funciona de forma estable pero aún no se valida su completo funcionamiento, ya que el uso en una situación real puede proporcionar información relevante que de un porcentaje de validación de que tantos pacientes pueden ser detectados con rasgos de TEA. 

### Aprendizaje Continuo

Por lo tanto, se requiere ampliar y profundizar en el tema de algoritmos que ayuden a mejorar el sistema base y asi poder tener un grado de porcentaje más alto que lo que se da en métodos tradicionales de detección del TEA. 

## Bibliografía
- Adamu, A. S., Abdullahi, S. E., & Aminu, R. K. (2019). A survey on software applications use in therapy for autistic children.  2019 15th International Conference on Electronics, Computer and Computation, ICECCO 2019, 1–4. https://doi.org/10.1109/ICECCO48375.2019.9043237

- Cao, Y., Zhou, Z. J., Hu, C. H., Tang, S. W., & Wang, J. (2021). A new approximate belief rule base expert system for complex  system modelling. Decision Support [¨*] Systems, 150, 113558. https://doi.org/10.1016/j.dss.2021.113558

- Carmona-Serrano, N., López-Belmonte, J., López-Núñez, J. A., & Moreno-Guerrero, A. J. (2020). Trends in autism research in the field of education in web of science: A bibliometric study. Brain Sciences, 10(12), 1–22.  https://doi.org/10.3390/brainsci10121018

- Fusar-Poli, L., Brondino, N., Politi, P., & Aguglia, E. (2020). Missed diagnoses and misdiagnoses of adults with autism spectrum disorder. European Archives of Psychiatry and Clinical Neuroscience. https://doi.org/10.1007/s00406-020-01189-w

- Isa, N. R. M., Yusoff, M., Khalid, N. E., et al. (2014). Autism severity level detection using fuzzy expert system. 2014 IEEE International Symposium on Robotics and Manufacturing Automation, 218.

- Thabtah, F., Kamalov, F., & Rajab, K. (2018). A new computational intelligence approach to detect autistic features for autism screening. International Journal of Medical Informatics, 117, 112–124.Thabtah, F., & Peebles, D. (2019). A new machine learning model based on induction of rules for autism detection. Health Informatics Journal, 26, 264-286.

- Adarraga, P., & Zaccagnini, J. L. (1992). DAI: A knowledge-based system for diagnosing autism: A case study on the application of artificial intelligence to psychology. European Journal of Psychological Assessment, 8(1), 25–46.

- Alharbi, S. T., Hossain, M. S., & Monrat, A. A. (2015). A Belief Rule Based Expert System to Assess Autism under Uncertainty. Proceedings of the World Congress on Engineering and Computer Science, 41(3), 21–23. https://doi.org/10.1007/s10916-017-0685-8

- Al-Wahaibi, A., Al-Hajry, M., Al-Bahrani, Z., & Al-Busaidi, K. A. (2016). The Development and Acceptance of Autism Advisory Expert System. International Journal of Computing and Information Sciences, 12(2), 179–188. https://doi.org/10.21700/ijcis.2016.121

- Blanchet, B. (2001, June). An efficient cryptographic protocol verifier based on prolog rules. In CSFW (Vol. 1, pp. 82-96).

- Isa, N. R. M., Yusoff, M., Khalid, N. E., Tahir, N., & Binti Nikmat, A. W. (2015). Autism severity level detection using fuzzy expert system. 2014 IEEE International Symposium on Robotics and Manufacturing Automation, IEEE-ROMA2014, 218–223. https://doi.org/10.1109/ROMA.2014.7295891

- Kok, K., Derzsi, Z., Gordijn, J., Hommelberg, M., Warmer, C., Kamphuis, R., & Akkermans, H. (2008, January). Agent-based electricity balancing with distributed energy resources, a multiperspective case study. In Proceedings of the 41st Annual Hawaii International Conference on System Sciences (HICSS 2008) (pp. 173-173). IEEE.

- Lialiou, P., Zikos, D., & Mantas, J. (2012). Development and evaluation of an expert system for the diagnosis of child autism. Studies in Health Technology and Informatics, 180, 1185–1187. https://doi.org/10.3233/978-1-61499-101-4-1185

- Mahmoudi, M., & Akbari-zardkhaneh, S. (2015). Developing Autism Screening Expert System (ASES). AWERProcedia Information Technology & Computer Science, 2013(January).

- Merritt, D. (2012). Building expert systems in Prolog. Springer Science & Business Media.

- Mizoguchi, F. (1983). PROLOG based expert system. New Generation Computing, 1(1), 99-104.

- Sajjad, S., Qamar, H., Tariq, K., & Bano, S. (2011). Development of a diagnostic expert system for autism disorder- PCADEX. Proceedings of the 2011 International Conference on Artificial Intelligence, ICAI 2011, 2(May), 934–938.

- Singla, J. (2013). The diagnosis of some lung diseases in a prolog expert system. International Journal of Computer Applications, 78(15).

- Yuan, J., Holtz, C., Smith, T., & Luo, J. (2016). Autism spectrum disorder detection from semi-structured and unstructured medical data. Eurasip Journal on Bioinformatics and Systems Biology, 2017(1), 1–9. https://doi.org/10.1186/s13637-017-0057-1

- Yulianto, T., Andryana, S., & Gunaryati, A. (2019). Expert System For Autism Prediction In Children With Web-Based Forward Chaining Method. Jurnal Mantik, 3(4), 522–530.

- Alharbi, S. T., Hossain, M. S., & Monrat, A. A. (2015). A belief rule based expert system to assess autism under uncertainty. Proceedings of the World Congress on Engineering and Computer Science 2015, 41(3), 21–23. https://doi.org/10.1007/s10916-017-0685-8

- Gnanaprasanambikai, L. (2017). Performance analysis of RIPPER algorithm using WEKA tool. International Journal of Advanced Research in Computer Science and Software Engineering, 7(5), 55–57.

- Hall, M., Frank, E., Holmes, G., Pfahringer, B., Reutemann, P., & Witten, I. H. (2009). The WEKA data mining software: An update. ACM SIGKDD Explorations Newsletter, 11(1), 10–18. https://doi.org/10.1145/1656274.1656278





























