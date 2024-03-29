# PWM Mysteries Explained

The images from this passage come from [Pulse Width Modulation for Dummies](https://youngkin.github.io/post/pulsewidthmodulationraspberrypi/) by Rich Youngkin and [Introduction To PWM: How Pulse Width Modulation Works](https://www.kompulsa.com/introduction-pwm-pulse-width-modulation-works/) by Nicholas Brown, both very good information sources

![PWM diagram](images/PWMPulsePeriod.png)
from [Pulse Width Modulation for Dummies](https://youngkin.github.io/post/pulsewidthmodulationraspberrypi/) by Rich Youngkin

## What is PWM?

&nbsp;&nbsp;&nbsp; Pulse Width modulation (PWM) is a digital substitute to an analog signal (such as resistors and transistors) that uses just the amount of energy that a device actually needs to run at the power you want it to. PWM is a way more effective alternative to resistors and transistors because in the use of a resistor or transistor, if the resistor is set to 50%, the other 50% left over simply turns into heat and is wasted. (Note that this could be useful in some cases, but most of the time we really don't want our computers heating up and wasting more energy.)

&nbsp;&nbsp;&nbsp; PWM, instead of resiting the power it doesn't want the electronic device to take, it simply turns on and off _VERY_ quickly (**VERY** quickly, like, thousands of times per second, very quickly. This is how the device receiving the power works at) so that the computer only gives the amount of power for the "ON" part of your period and the device receives only the "ON" power.

&nbsp;&nbsp;&nbsp; Another great thing about PWM is that it is variable, and not static like a normal resistor is. This means that you can set the length of your Pulse Width to controlling amounts of power entering your device through duty cycle through the programs on your computer. You could set the Pulse Width to 50%, and that would give you about 50% power (when it pulses, it pulses with 50% of it's time "ON" and 50% of it time "OFF", if you gave it 75% duty cycle, it would be "ON" for 75% of it's time and "OFF" for 25%)

Most of the time PWM Signals are represented in square waves, as seen below.
The high part of the wave would be the "ON", and the low part would be the "OFF". The higher the percentage you put in, the longer the top part will be, and the shorter the bottom part will be.

![PWM waves](https://i0.wp.com/www.kompulsa.com/wp-content/uploads/2017/04/PWM-Square-Wave-50-Duty-Cycle.png?ssl=1)
50% wave duty cycle from [Introduction To PWM: How Pulse Width Modulation Works](https://www.kompulsa.com/introduction-pwm-pulse-width-modulation-works/) by Nicholas Brown

## Experiment

Wanting to see what PWM actually looks like? See [this experiment](experiment_1.md) using a Yahboom Tank.
