<h1 align = "center">Fourier Epicycle</h1>



## Contents

* [Introduction](#introduction)
* [Prerequisites](#prerequisites)
* [Usage](#usage)
* [Numerical Technique](#numerical-technique)
* [Code Structure](#code-structure)
* [Examples](#examples)
* [References](#references)



## Introduction

This project is a Fourier Epicycle generator based on numerical algorithms, i.e. Fourier Transform, interpolation, etc.

Drawing with time-axis is visualized as follows.

<img src="https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Fourier-Epicycle/intro-1.jpg" width="200"><img src="https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Fourier-Epicycle/intro-2.jpg" width="200">

And Fourier Transform parameter `order` ( ~ number of epicycles ) controls the precision of drawing.

<img src="https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Fourier-Epicycle/intro-3.jpg" width="200"><img src="https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Fourier-Epicycle/intro-4.jpg" width="200"><img src="https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Fourier-Epicycle/intro-5.jpg" width="200">

( More in [References](#references) )



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

  The definitions are as follows, in general, integer ![k](https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Fourier-Epicycle/k.png) is theoretically infinite.
  
  ![equation-1](https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Fourier-Epicycle/equation-1.png)
  
  Integer ![j](https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Fourier-Epicycle/j.png), used as an index, is also the number of cycles of the ![j](https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Fourier-Epicycle/j.png)-th exponential term in interval ![I](https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Fourier-Epicycle/I.png), and the parameter ![a_j](https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Fourier-Epicycle/a_j.png) could be calculated by
  
  ![equation-2](https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Fourier-Epicycle/equation-2.png)
  
  ( In this project, we set  ![tinI](https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Fourier-Epicycle/tinI.png) )

  By this, we can decompose a periodic function into the sum of exponential terms, and thus implementing FFT helps constructing code.

  

* #### Fast Fourier Transform

  Fourier transform is a mathematical transform that decomposes functions depending on time into functions depending on temporal frequency, such as the expression of a musical chord in terms of the volumes and frequencies of its constituent notes.

  When ![f(t)](https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Fourier-Epicycle/f(t).png) is a complex valued periodic function of real variable t (stands for time), we can implementing the Discrete/Fast Fourier Transform on it, ![f](https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Fourier-Epicycle/f.png) will be an array of complex numbers, where ![f(t)](https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Fourier-Epicycle/f(t).png) corresponds to the complex number information at time t, and ![f(t)](https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Fourier-Epicycle/f(t).png) can also be interpreted as the point of the drawing at time t, as for why (how to represent a 2-D image information with one complex number), we'll show it soon.

  Suppose ![f](https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Fourier-Epicycle/f.png) array is ![farray](https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Fourier-Epicycle/farray.png), ![N](https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Fourier-Epicycle/N.png) is the number of the sampling points.
  
  ![equation-3](https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Fourier-Epicycle/equation-3.png)
  
  And Fourier Transform tells,
  
  ![equation-4](https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Fourier-Epicycle/equation-4.png)
  
  
* #### Interpolation

  DFT is easy to implement but not so efficient, while power-2 FFT is relatively efficient but limited, for it only works when the number of sampling points is power of two.

  So how to solve this problem? Actually it's almost impossible to get ![N=2^n](https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Fourier-Epicycle/N=2^n.png), we use interpolations, in this project, linear interpolation & periodic cubic spline interpolation are implemented, because the complex function ![f](https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Fourier-Epicycle/f.png) is periodic and the distance between each two sampling points won't be so long.

  

* #### 2-D information

  This is trivial, just converted 2-D coordinates ![(x,y)](https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Fourier-Epicycle/(x,y).png) into one complex number like ![x+iy](https://github.com/Tequila-Sunrise/Image-Hosting/blob/main/Fourier-Epicycle/x+iy.png).



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

[![example](https://github.com/Tequila-Sunrise/Fourier-Epicycle/blob/main/example/bird/fourier-epicycle.gif)](https://github.com/Tequila-Sunrise/Fourier-Epicycle/blob/main/example/bird/fourier-epicycle.mp4)



## References

1. [Fourier series videos by 3B1B](https://www.youtube.com/watch?v=r6sGWTCMz2k) my motivation for this project

2. [Fourier Transform videos by 3B1B](https://www.youtube.com/watch?v=spUNpyF58BY) beautiful understanding on Fourier Transform

3. [An Interactive Introduction to Fourier Transforms](https://www.jezzamon.com/fourier/index.html) helps a lot


