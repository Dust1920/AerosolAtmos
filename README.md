# Modelo Atmosférico de Aerosoles. 


## Explicación del Repositorio

El repositorio posee los siguientes archivos relevantes, aparte del README.md que ahora estas leyendo. 
* books
* data
* fig_gamma
* fig_gamma2
* fig_gamma3
* fig_nu0
* AtmosModel.zip
* plots.py
* process_data.py
* process.py

Cabe aclarar que dentro del repositorio. 
  
## Introducción
Dentro del entorno atmosférico, cada proceso es influenciado por variables u otros proceso que aparentan ajenos. En nuestro caso exploraremos el ciclo del agua, principalmente dos de los procesos más importantes. 

* Condensación.
* Evaporación.

Exploraremos ambos procesos y como un elemento aparentemente externo como son las partículas de polvo, el polen, entre otros, interactuan con ellos. 

Estos antes mencionados se conocen como aerosoles. En este trabajo nos centraremos en los núcleos de condensación (CNN) y revisaremos como estos intervienen en el proceso de condensación.

A pesar que la mayor parte actualmente se generan por la contaminación del aire. Cabe mencionar que estos en si no son malos, ya que su ausencia causa un efecto similar al del abuso de los mismos. Una disminición considerable de la condensación, que en otras palabras disminuye la posibilidad de lluvias. 


## Modelo

En esta tesis, usaremos un modelo de ecuaciones diferenciales parciales aleatorias. 

$$
\partial_t (u) + \partial_x(f(u)) = b(t,z) + \eta(t,z),  
$$

donde $\eta(t,z)$ representa el ruido aleatorio. En nuestro caso usaremos una aproximación del movimiento browniano. 

$$
\eta(t,z) \approx W(t) \mathbf{i},
$$

En nuestro modelo estamos considerando un sistema de 5 variables, construido en función de las siguientes variables atmosféricas. 

* Velocidad vertical $w$ (m$\text{s}^{-1}$)
* Temperatura Potencial $\theta$ K
* Vapor de Agua $q_v$ (g$\text{kg}^{-1}$)
* Agua Líquida $q_r$ (g$\text{kg}^{-1}$)
* Nucleos de condensación $q_N$ (p$\text{cm}^{-3}$)

## Método Númerico

Para resolver el sistema de ecuaciones. Consideraremos condiciones inciales

$$
u_0(t,z) = [w_0(t,z),\theta_0(t,z),q_{v0}(t,z),q_{r0}(t,z),q_{N0}(t,z)]
$$
y condiciones de frontera tipo Dirichlet.
$$
u_{T}(t,z) = [w_T(t,z),\theta_T(t,z),q_{vT}(t,z),q_{rT}(t,z),q_{NT}(t,z)]
$$
,usaremos una versión modificada del método de Upwind, incorporando el método de Euler-Maruyama para considerar el ruido aleatorio y elementos adicionales al modelo como. 

* Perturbaciones. 
* Ajustes por Entropía.

## Conclusiones

Al comienzo del trabajo. Se esperaba corroborar el comportamiento de los CNN, cantidad excesiva o reducida apagaría de forma significativa 
Después de resolver el sistema, no logramos encontrar evidencia del comportamiento esperado. Se plantea algunos detalles dentro del modelo como posibles causas. 
1. Falló en el planteamiento. (Puede ser que nuestro hipótesis fuera falsa)
2. Problemas con el ruido aleatorio. (Estamos usando una aproximación del movimiento browniano)
3. Error en los parámetros. (Los parámetros que se utilizaron son extraídos de literatura, por lo tanto puede que bajo nuestras cirscuntancias no sean suficientes)
4. El ruido aleatorio. (El ruido aleatorio es una alternativa al flujo turbulento, entonces usar alternativas podría )