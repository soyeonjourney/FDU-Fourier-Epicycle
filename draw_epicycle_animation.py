import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import json
from tqdm import tqdm

from fourier_transform import FourierTransform
from epicycle_frame import EpicycleFrame
from draw_it_yourself import draw_it_yourself


# Draw it yourself
diy_or_not = input("Draw image by yourself ? (y/n) ")
if diy_or_not == 'y':
    draw_it_yourself()

# Show original sample points
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_axis_off()
ax.set_aspect('equal')  # To have symmetric axes

# Load coords
f = open('data/coords', 'r')
coords = json.load(f)
f.close()

x_list = [coord[0] for coord in coords]
x_list = x_list - np.mean(x_list)
y_list = [-coord[1] for coord in coords]
y_list = y_list - np.mean(y_list)
ax.plot(x_list, y_list)
xlim = plt.xlim()
ylim = plt.ylim()

plt.show(block=False)
plt.pause(3)
plt.close()

# Ask for settings
order = min(int(input("Max order: ")), int(np.ceil((len(coords)-1)/2)))
mode = input("Fourier Transform type (fft/mydft/myfft/myfftplus): ")
suffix = input("Save file type (mp4/gif): ")

# Compute fourier coeffients
ft = FourierTransform(x_list, y_list, order, mode=mode)

# Draw animation
fig, ax = plt.subplots()
ax.set_xlim(xlim[0]-100, xlim[1]+100)
ax.set_ylim(ylim[0]-100, ylim[1]+100)
ax.set_axis_off()
ax.set_aspect('equal')

# Frame params
original_drawing, = ax.plot([], [], '-', color='mediumaquamarine', linewidth=0.5)
circles = [ax.plot([], [], '-', color='pink', alpha=0.3, linewidth=0.75)[0] for i in range(-order, order+1)]
lines = [ax.plot([], [], '-', color='mediumpurple', alpha=0.7, linewidth=0.75)[0] for i in range(-order, order+1)]
paintbrush_x, paintbrush_y = [], []
drawing, = ax.plot([], [], '-', color='plum', linewidth=2)

# Generate animation
print("Generating animation ...")
frames = 3000
pbar = tqdm(total=frames, desc='Progress')  # Progress bar

# Draw frame at time t (t goes from 0 to 2*pi for complete cycle)
def generate_frame(k, ft, t_list):
    global pbar
    t = t_list[k]

    # Draw original image
    original_drawing.set_data(x_list, y_list)

    epicycle_frame = EpicycleFrame(ft, t)
    for i in range(-order, order+1):
        # Draw circles
        circles[i].set_data(*epicycle_frame.circles[i])
        # Draw lines
        lines[i].set_data(*epicycle_frame.lines[i])
    # Draw paintbrush
    paintbrush_x.append(epicycle_frame.paintbrush[0])
    paintbrush_y.append(epicycle_frame.paintbrush[1])
    drawing.set_data(paintbrush_x, paintbrush_y)

    # Update progress bar
    pbar.update(1)

# Generate mp4 / gif
t_list = np.linspace(0, 2*np.pi, num=frames)
anim = animation.FuncAnimation(fig, generate_frame, frames=frames, fargs=(ft, t_list), interval=1)

# Set up formatting for the video file
Writer = animation.writers['ffmpeg']
writer = Writer(fps=30, metadata=dict(artist='Tequila-Sunrise'), bitrate=7200)
anim.save('output/fourier-epicycle.'+suffix, writer=writer)

pbar.close()
print(f"Generating {suffix} file successfully!")
