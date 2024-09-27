**Nature-Inspired Algorithms to Optimize the Base Station Location Allocation Problem**

**Project Overview**

This project focuses on optimizing the placement of base stations in urban and rural areas using nature-inspired algorithms, specifically the Genetic Algorithm (GA). The goal is to minimize costs while ensuring comprehensive coverage and meeting connectivity demands. The project covers three neighborhoods in Istanbul: Basibuyuk, Resadiye, and Tepeustu, each with unique characteristics to test the adaptability and efficiency of the proposed solution.

**Project Features**

Neighborhood Selection: Three different neighborhoods were chosen to evaluate the algorithm under varying conditions.

Data Collection and Preprocessing: Street data, including geographical coordinates, population distribution, and demand, were collected and processed.

Genetic Algorithm Implementation: The GA is used to generate an initial population of potential base station configurations, refined through selection, crossover, and mutation processes.

Fitness Evaluation: Each configuration is evaluated based on coverage, demand fulfillment, and cost, incorporating penalties for unmet demand and excess base stations.

Experimental Studies: Multiple tests were conducted with varying mutation rates and generations to analyze the performance of the GA.

Visualization: The final results are visualized using mapping libraries to illustrate coverage and base station locations.

**Technologies Used**

Programming Language: Python

**Libraries:**

Selenium: For web scraping street data.

Folium: For visualizing the results on interactive maps.

Tools: Visual Studio Code (VSCode) for development.



**System Architecture**

The project is structured into several layers:

Data Processing Layer: Responsible for reading, preprocessing, and normalizing the data.

Algorithm Execution Layer: Implements the Genetic Algorithm, including population generation, fitness evaluation, and new generation creation.

Visualization Layer: Displays the placement of base stations and the coverage provided using interactive maps.

User Interface: Console-based UI for configuring the algorithm parameters and viewing results.

**Results and Discussion**

The Genetic Algorithm effectively optimized the base station placement, achieving near-optimal solutions consistently across different neighborhoods. The algorithm demonstrated significant cost savings, enhanced coverage, and scalability to diverse geographic settings.

This project showcases the potential of nature-inspired algorithms, particularly the Genetic Algorithm, in solving complex real-world problems related to telecommunications infrastructure. The results provide a strong foundation for further research and practical implementation.

**Acknowledgements**

We would like to thank our advisor, Asst. Prof. Fatma Corut Ergin, for her guidance and support throughout the project. Special thanks to the Department of Computer Engineering at Marmara University for providing the resources and knowledge required for this project.
