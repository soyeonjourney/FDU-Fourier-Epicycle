<h1 align = "center">Fourier Epicycle</h1>



## Contents

* [Introduction](#introduction)
* [Prerequisites](#prerequisites)
* [Usage](#usage)
* 



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

     * `fft`: using built-in FFT
     * `mydft`: using DFT
     * `myfft`: using linear interpolation & power-2 FFT
     * `myfftplus`: using cubic interpolation & power-2 FFT

   * `Save file type` <string>: mp4 or gif file, mp4 is recommended

4. Start generating:

   > Generating animation ...
   >
   > (with a progress bar here)
   >
   > Generating gif file successfully!

5. Finally see your output at `/output/`



