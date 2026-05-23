

# Mouse Gesture Recognition using Pygame

Using Pygame and basic vector calculations to identify shapes drawn by the user.

This project tracks the mouse movement of the user and attempts to identify shapes such as horizontal lines, vertical lines, triangles, rectangles, and circles using geometric heuristics instead of machine learning.

---

## Features

- Horizontal line detection
- Vertical line detection
- Diagonal line detection
- Triangle recognition
- Rectangle recognition
- Basic circle detection
- Mouse input smoothing / noise filtering
- Corner grouping using distance thresholds

---

## How It Works

The program works by analyzing mouse movement as a sequence of points and applying specific conditions for each shape.

- **Horizontal Line** — the total change along the y-axis is minimal (small hand jitters are ignored)
- **Vertical Line** — the total change along the x-axis is minimal
- **Diagonal Line** — both x and y values change significantly
- **Detecting Corners** — rapid directional changes are detected using the dot product of vectors, and shapes are assigned based on the number of detected corners

### Detection Pipeline

1. Mouse positions are continuously sampled.
2. Direction vectors are generated between nearby points.
3. Dot products are used to calculate angles between vectors.
4. Large directional changes are treated as corners.
5. Nearby corners are grouped together to reduce duplicate detections.
6. Shapes are classified based on:
   - corner count
   - movement direction
   - start/end point distance

---

## Technologies Used

- Python
- Pygame
- Vector mathematics
- Basic computational geometry

---

## Running the Project

### Install Dependencies

```bash
pip install pygame
```

### Run

```bash
python mouse_draw.py
```

---

## Current Limitations

- Circle detection is still experimental
- Detection accuracy depends on drawing speed and drawing accuracy
- Very noisy input can produce false corners
- Complex gestures are not yet supported
- Shape classification currently relies on heuristic thresholds

---

## Future Improvements

- Radius-based circle detection
- Better corner clustering
- Gesture smoothing
- Gesture-controlled gameplay integration
- OpenCV experimentation
- Machine learning-based gesture classification

---

## Project Goal

This project started as an experiment to better understand:

- vector math
- gesture recognition
- computational geometry
- event-driven programming with Pygame
- mouse input processing

The final goal is to integrate the recognition software with OpenCV for an interactive game system.

---

## Demo
<img width="1612" height="541" alt="image" src="https://github.com/user-attachments/assets/558ac906-c215-4022-a45e-8b426a0789b0" />
<img width="782" height="297" alt="image" src="https://github.com/user-attachments/assets/679e2d00-f531-4551-bb28-991f83c40084" />

