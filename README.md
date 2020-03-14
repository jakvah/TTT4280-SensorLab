## TTT4280 -  Sensorer og instrumentering, lab

Kode til alle 4 labber i faget TTT4280, sensorer og instrumentering.

```adc_sampler.c``` kjøres på RaspberryPi for å sample data fra ADCene i sensorsystemet. 

```buggesmatteland.py``` inneholder matterelaterte funksjoner som brukes i de ulike labbene og annet snadder.

```importdata.py``` importerer data fra ```.bin``` filene ```adc_sampler.c``` returnerer. Takk til big biceps bro Kjeka.

```lab1.py```, ```lab2.py```,```lab3.py```,```lab4.py``` er filene til hver enkelt lab. Hovedsaklig bare masse plots av beregninger på data gjort i ```buggesmatteland.py```