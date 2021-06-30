<h1 align = "center">Fourier Epicycle</h1>



## Contents

* [Introduction](#introduction)
* [Prerequisites](#prerequisites)
* [Usage](#usage)
* [Numerical Technique](#numerical-technique)
* [Code Structure](#code-structure)
* [Examples](#examples)
* [Further Reading](#further-reading)



## Introduction

This project is a Fourier Epicycle generator based on numerical algorithms like Fourier Transform, interpolation, etc.



## Prerequisites

Project is created with:

* Python version: 3.8
* numpy library version: 1.20.1
* scipy library version: 1.6.2
* pygame library version: 2.0.1
* matplotlib library version: 3.3.4
* tqdm library version: 4.59.0

Install requirements with:

```powershell
pip install -r requirements.txt
```



## Usage

1. Run `draw_epicycle_animation.py`

   > Draw image by yourself ? (y/n) 

2. Input 'y' for 'yes' and you can draw a new image by yourself, or 'n' for 'no' to continue with the previous image

   * Closed figure is recommended

   * Press 'Left Mouse Button' to record drawing points, 'R' to retry and 'Enter' to save

3. Then set parameters for Fourier Epicycle generator

   For example:

   > Max order: 20
   >
   > Fourier Transform type (fft/mydft/myfft/myfftplus): myfft
   >
   > Save file type (mp4/gif): mp4

   * `Max order` <integer n>: number of epicycles - 2*n, usually set 5-100

   * `Fourier Transform type` <string>:

     * `fft` : Use built-in FFT
     * `mydft `: Use DFT
     * `myfft` : Use linear interpolation & power-2 FFT
     * `myfftplus` : Use cubic interpolation & power-2 FFT

   * `Save file type` <string>: Generate mp4 or gif file, mp4 is recommended

4. Start generating:

   > Generating animation ...
   >
   > (with a progress bar here)
   >
   > Generating gif file successfully!

5. Finally see your output at `/output/`



## Numerical Technique

* #### Fourier Series

  The definitions are as follows, in general, integer $k$ is theoretically infinite.
  $$
  f(t) = (a_{-k} \cdot e^{i2\pi t\frac{-k}{N}}) + ... + (a_{-1} \cdot e^{i2\pi t\frac{-1}{N}}) +
        a_0 + (a_1 \cdot e^{i2\pi t\frac{1}{N}}) + ... + (a_k \cdot e^{i2\pi t\frac{k}{N}})
        = \sum_{j=-k}^k a_j \cdot e^{i2\pi t\frac{j}{N}}
  $$
  Integer $j$, used as an index, is also the number of cycles of the $j$-th exponential term in interval $I$, and the parameter $a_j$ could be calculated by
  $$
  a_j = \frac{1}{I} \int_I f(t) \cdot e^{i\frac{2\pi jt}{I}} dt
  $$
  ( In this project, we set  $t\in I=[0,1]$ )

  By this, we can decompose a periodic function into the sum of exponential terms, and thus implementing FFT helps constructing code.

  

* #### Fast Fourier Transform

  Fourier transform is a mathematical transform that decomposes functions depending on time into functions depending on temporal frequency, such as the expression of a musical chord in terms of the volumes and frequencies of its constituent notes.

  When $f(t)$ is a complex valued periodic function of real variable t (stands for time), we can implementing the Discrete/Fast Fourier Transform on it, $f$ will be an array of complex numbers, where $f(t)$ corresponds to the complex number information at time t, and $f(t)$ can also be interpreted as the point of the drawing at time t, as for why (how to represent a 2-D image information with one complex number), we'll show it soon.

  Suppose $f$ array is $[f(0),f(1),\dots,f(N-1)]$, $N$ is the number of the sampling points.
  $$
  c(j) = \sum_{n=0}^{N-1} f(n) \cdot e^{-i2\pi j\frac{n}{N}},\quad\quad j=0,1,\dots,N-1
  $$
  And Fourier Transform tells,
  $$
  f(n) = \frac{1}{N}\sum_{j=0}^{N-1} c(j) \cdot e^{i2\pi n\frac{j}{N}},\quad\quad n=0,1,\dots,N-1
  $$
  
* #### Interpolation

  DFT is easy to implement but not so efficient, while power-2 FFT is relatively efficient but limited, for it only works when the number of sampling points is power of two.

  So how to solve this problem? Actually it's almost impossible to get $N=2^n$, we use interpolations, in this project, linear interpolation & periodic cubic spline interpolation are implemented, because the complex function $f$ is periodic and the distance between each two sampling points won't be so long.

  

* #### 2-D information

  This is trivial, just converted 2-D coordinates $(x,y)$ into one complex number like $x+iy$.



## Code Structure

* `draw_it_yourself.py` : Drawing window implemented by pygame
* `utils.py` : Basic algorithms, including:

  * `coeffs_mydft` : Calculate Fourier Transform parameters by DFT
  * `coeffs_myfft` : Calculate Fourier Transform parameters by power-2 FFT with linear interpolation
  * `coeffs_myfft_plus` : Calculate Fourier Transform parameters by power-2 FFT with periodic cubic spline interpolation
  * `coeffs_fft` : Calculate Fourier Transform parameters by built-in FFT function
* `fourier_transform.py` : Return all coefficients of Fourier Transform
* `epicycle_frame.py` : Return all epicycle's track at frame time t
* `draw_epicycle_animation.py` : Main function to generate the animation



## Examples





## Further Reading

1. [Fourier series videos by 3B1B](https://www.youtube.com/watch?v=r6sGWTCMz2k) my motivation for this project
2. [Fourier Transform videos by 3B1B](https://www.youtube.com/watch?v=spUNpyF58BY) beautiful understanding on Fourier Transform
3. [An Interactive Introduction to Fourier Transforms](https://www.jezzamon.com/fourier/index.html) helps a lot

