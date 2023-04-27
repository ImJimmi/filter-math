# The Beautifully Simple Complex Maths of Digital Filters

Filters are by far the most common effect used across the audio industry today – whether you’re mastering a hit record or dubbing a wildlife documentary, you’ll likely have hundreds, if not thousands of filters in your processing chain - whether you know it or not!

Many of us have a rough idea of how these filters work – combining samples with previous samples scaled by some coefficients – but how does that actually work, where do these coefficients come from, and how hard is it to design our own custom filters?

## Impulse Responses

Digital signals are represented as a series of samples - we call this a _discrete-time_ signal. We can express a discrete-time signal as a function of _n_, where _n_ is the index of a sample from the signal. We represent the current sample being processed as _n=0_ and the previous sample as _n=-1_, and so on.

A system consisting of an input signal _x(n)_ and an output signal _y(n)_ has an _impulse response h(n)_ which is the correlation between the system's output and its input. In other words, _h(n)_ is a function applied to _x(n)_ to produce _y(n)_.

![Generic Difference Equation](assets/equations/generic-difference-equation.svg)

![Impulse Response](assets/equations/impulse-response.svg) [_Equation 1_]

For example, for a system with the difference equation:

![System 1 Difference Equation](assets/equations/system1-difference-equation.svg) [_System 1_]

Where _a<sub>0</sub>_ is a constant, we can calculate the system's impulse response using _Equation 1_:

![System 1 Impulse Response (non-simplified)](assets/equations/system1-impulse-response-nonsimplified.svg)

![System 1 Impulse Response](assets/equations/system1-impulse-response.svg)

Since the impulse response is simply a constant, we can deduce that this system is a gain effect.

### Impulse response of a filter

Filters operate in the frequency domain to either amplify or attenuate certain frequencies. Since frequency is a function of time (_f=1/T_) then in order to alter the frequency of a signal, a system must introduce an element of time to its impulse response.

For a system with the difference equation:

![System 2 Difference Equation](assets/equations/system2-difference-equation.svg) [_System 2_]

Where _a<sub>0</sub>_ and _a<sub>1</sub>_ are constants, _x(n)_ is the current input sample, and _x(n-1)_ is the previous input sample, we can again calculate the system's impulse response using _Equation 1_:

![System 2 Impulse Response (non-simplified)](assets/equations/system2-impulse-response-nonsimplified.svg)

![System 2 Impulse Response](assets/equations/system2-impulse-response.svg)

This doesn't tell us much about the system's frequency domain. We could pass some samples through the system to see what the output signal would look like, but what we're really interested in is the frequency response. To find this, we need to use the _Z-transform_.

## The Z-transform

The Z-transform converts a discrete-time signal into a _complex_ frequency domain representation. Given a series of samples, the Z-transform can tell us what the frequency content of that signal is, representing frequency using complex numbers.

### Representing frequency as a complex number

Frequency is normally represented using _real_ numbers measured in Hertz. However, the Z-transform operates in the _Z-domain_, meaning it uses _complex_ numbers to represent frequency.

To represent frequency as a complex number, we use the value _z_, which can be calculated for a given frequency _f_ as so:

![z Formula](assets/equations/z-formula.svg) [_Equation 2_]

Where _e_ is [Euler's Number](https://en.wikipedia.org/wiki/E_(mathematical_constant)), _j_ is the [Imaginary Unit](https://en.wikipedia.org/wiki/Imaginary_unit) (usually depicted as _i_ in mathematics, but we like to use _j_ in computing so as not to be confused with `i` used for indexes), and _f<sub>s</sub>_ is the system's sample rate (AKA sampling frequency).

_Table 1_ shows how varying the value of _f_ changes the value of _z_, and the resultant [phase and magnitude](https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:complex/x9e81a4f98389efdf:complex-abs-angle/a/complex-number-absolute-value-and-angle-review) of _z_.

<!-- Using [Euler's Formula](https://en.wikipedia.org/wiki/Euler%27s_formula) we can see how _Equation 2_ is effectively taking a frequency and placing it somewhere around a circle on a complex number line. _Table 1_ shows the relationship between varying values of _f_, and the resultant value of _z_. -->

For a system with a sample rate _f<sub>s</sub>_ of 1Hz:

| _f_ | _z_         | Phase of _z_    | Magnitude of _z_ |
| --- | ----------- | --------------- | ---------------- |
| 0.0 | 1.0+0.0j    | 0<sup>O</sup>   | 1.0              |
| 0.1 | 0.81+0.59j  | 36<sup>O</sup>  | 1.0              |
| 0.2 | 0.31+0.95j  | 72<sup>O</sup>  | 1.0              |
| 0.3 | -0.31+0.95j | 108<sup>O</sup> | 1.0              |
| 0.4 | -0.81+0.59j | 144<sup>O</sup> | 1.0              |
| 0.5 | -1.0+0j     | 180<sup>O</sup> | 1.0              |

[_Table 1_]

From this, we can see that by representing frequencies as complex numbers we're effectively placing them around a circle on a complex number line because the _phase_ of _z_ changes with frequency, whereas the _magnitude_ stays the same. So whenever you see _z_, remember it's simply a representation of frequency, plotted around a circle (rather than along a flat axis).

See [Euler's Formula](https://en.wikipedia.org/wiki/Euler%27s_formula) for a more in-depth look into _Equation 2_ and how it relates to the trigonometric functions, and why it produces a circle.

### Converting discrete-time signals to complex frequency representations

Now that we understand _z_, we can take a look at the Z-transform:

![Z-Transform](assets/equations/z-transform.svg) [_Equation 3_]

Where _N_ is the number of samples in the discrete-time signal.

This tells us that in order to find the magnitude of the frequency response for a given value of _z_ (and thus for a given frequency) _X(z)_ we must sum each sample in the signal _x(n)_ multiplied by _z_ raised to _-n_.

Let's apply this to a simple sine wave. _Table 2_ shows the values of samples in a single cycle of a sine wave at 10Hz for a system with a sample rate _f<sub>s</sub>_ of 100Hz:

| _n_    | 0    | 1    | 2    | 3    | 4    | 5    | 6     | 7     | 8     | 9     |
| ------ | ---- | ---- | ---- | ---- | ---- | ---- | ----- | ----- | ----- | ----- |
| _x(n)_ | 0.00 | 0.59 | 0.95 | 0.95 | 0.59 | 0.00 | -0.59 | -0.95 | -0.95 | -0.59 |

[_Table 2_]

Using a frequency _f_ of 30Hz, we can use _Equation 2_ to calculate _z_ as _-0.31+0.95j_. Then, using _Table 2_ and our value for _z_, we can use _Equation 3_ to calculate the Z-transform of our system:

```
x = [0.00, 0.59, 0.95, 0.95, 0.59, 0.00, -0.59, -0.95, -0.95, -0.59]

X(z) = sum(
    x[0] * z^-0,
    x[1] * z^-1,
    ...
    x[8] * z^-8,
    x[9] * z^-9
)

X(z) = sum(
    0.00 + 0.00j,
    -0.18 - 0.56j,
    ...
    0.77+0.59j,
    0.18-0.56j
)

X(z) = 0.00 - 0.01j
```

By taking the magnitude of the resultant complex number, we get 0.01. Given that our system contains a sine wave at 10Hz, and we calculated the magnitude of the system's frequency response at 30Hz, it makes sense that the result was very low as there should be no content at that frequency.

Let's now do the same, but using a frequency _f_ of 10Hz, giving us a _z_ value of _0.81+0.59j_:

```
X(z) = sum(
    0.00 + 0.00j,
    0.48 - 0.35j,
    ...
    -0.29-0.90j,
    -0.48-0.35j
)

X(z) = 0.00-5.00j
```

This time, the magnitude of the resultant complex number is 5, proving that our system does in fact have a prevalent frequency at 10Hz.

### Frequency and phase responses

One of the really clever things about representing frequency as a complex number is that not only can we find the _frequency_ content of a discrete-time signal, but also it's _phase_ response. A system's phase response tells us how the phase of the signal passed through it is altered, which can give us an indication of what the frequency response may be like. However, in some systems such as an all-pass filter for example, the phase response gives us far more information that the frequency response alone as in such a system, the frequency response will be completely flat, while the phase response has a full 360-degree rotation of phase above the cutoff frequency.

The result of the Z-transform _X(z)_ can be split into its frequency and phases responses using the following two equations:

![Frequency Response](assets/equations/frequency-response.svg) [_Equation 4_]

![Phase Response](assets/equations/phase-response.svg) [_Equation 5_]

## Z-transform of an Impulse Response

We can apply the Z-transform to a system's impulse response to find that system's frequency & phase responses. Since the system's impulse response isn't a signal - merely a function applied to a signal - we can simplify the result of the Z-transform by only summing the terms of _n_ that appear in the impulse response.

Let's take the impulse response of our second example system - with the `x(n-1)` term:

![System 2 Impulse Response](assets/equations/system2-impulse-response.svg)

To find the Z-transform of this system's impulse response _H(z)_ we _could_ apply the Z-transform directly to _h(n)_, which would give us:

![System 2 Z-transform with n](assets/equations/system2-Z-transform-with-n.svg)

However, doing it this way we still have terms of _n_, meaning we'd have to apply a discrete-time signal to be able to calculate the system's response.

Instead, we should apply the Z-transform to each individual term of _n_ in the system's impulse response in order to calculate it's overall Z-transform. So for our example system, we need to apply the Z-transform to both _x(n)_ and _x(n-1)_, which gives us:

![System 2 Z-transform non-simplified](assets/equations/system2-z-transform-nonsimplified.svg)

![System 2 Z-transform](assets/equations/system2-z-transform.svg)

Now, not only have we removed all terms of _n_ from our equation for _H(z)_, we've also removed _X_ altogether! This tells us that our system's frequency and phase responses are independent of it's input (and it's output since there's also no _Y_) - perfect for a digital filter!

Now that we _finally_ have an equation to calculate the frequency response of our system, let's apply it to a few varying values of _f_ to see the shape of its response curve and so get an idea of what it might sound like!

Using a sample rate _f<sub>s</sub>=100Hz_, _a<sub>0</sub>=0.4_ and _a<sub>1</sub>=0.6_, _Table 3_ shows the frequency and phase responses of various values of _f_ from _0Hz_ to the Nyquist limit:

| _f_  | _z_             | _H(z)_          | _H(f)_ | _H(theta)_          |
| ---- | --------------- | --------------- | ------ | ------------------- |
| 0Hz  | _1.00 + 0.00j_  | _1.00 + 0.00j_  | 1.00   | 0.00<sup>O</sup>    |
| 10Hz | _0.81 + 0.59j_  | _0.89 - 0.35j_  | 0.95   | -21.72<sup>O</sup>  |
| 20Hz | _0.31 + 0.95j_  | _0.59 - 0.57j_  | 0.82   | -44.27<sup>O</sup>  |
| 30Hz | _-0.31 + 0.95j_ | _0.21 - 0.57j_  | 0.61   | -69.39<sup>O</sup>  |
| 40Hz | _-0.81 + 0.59j_ | _-0.09 - 0.35j_ | 0.36   | -103.61<sup>O</sup> |
| 50Hz | _-1.00 + 0.00j_ | _-0.20 + 0.00j_ | 0.20   | -180.00<sup>O</sup> |
