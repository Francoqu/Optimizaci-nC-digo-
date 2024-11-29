# Optimización de Cálculo de Números Primos

Este repositorio contiene dos implementaciones para calcular los números primos menores a un número \(n\): una versión inicial y una versión optimizada utilizando la técnica de la Criba de Eratóstenes. Este proyecto demuestra cómo las técnicas algorítmicas pueden mejorar significativamente la eficiencia del código.



## Descripción

El objetivo principal de este proyecto es encontrar números primos menores a \(n\), comparando el rendimiento de dos enfoques:

1. **Código Original:**  
   - Una implementación básica que utiliza bucles anidados para verificar la primalidad de cada número.  
   - Este enfoque tiene una complejidad \(O(n^2)\), lo que lo hace ineficiente para entradas grandes.  

2. **Código Optimizado:**  
   - Implementa la **Criba de Eratóstenes**, un algoritmo eficiente para encontrar números primos.  
   - Este enfoque utiliza una lista booleana para marcar múltiplos y reduce operaciones redundantes, logrando una complejidad de \(O(n \log \log n)\).

