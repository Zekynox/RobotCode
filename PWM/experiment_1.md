# PWM Experiment 1

The objective is to use an oscilloscope to see different duty cycle levels produced by the PWMBlink Python
code. To do this:

1. Dupont cables replaced the ribbon cable connected from the Yaboom Tank expansion board and the LED circuit board.
1. The Dupont cables connect to a breadboard to provide a "breakout" which the oscilloscope can access.
1. The software PWM frequency is set to 10hz - a reasonable value within the range viewable by the oscilloscope.
1. The oscilloscope is set to 1v / 1x scaling for voltage, DC coupling, and a 50ms time base to be able to see a few cycles.
1. The program is run with differing duty cycles (90, 60, and 20). The oscilloscope is momentarily switched to "AUTO" triggering then back to "NORM" to capture the new waveform.

## 90%

![90%](images/im1444.png)

## 60%

![60%](images/im1445.png)

## 20%

![20%](images/im1446.png)

## Breakout details

Tank, Dupont cable, jumpers, and oscilloscope probe connections

![Breadboard and wiring](images/im1447.png)

## Oscilloscope details

DSO oscilloscope settings

![Oscilloscope](images/im1448.png)
