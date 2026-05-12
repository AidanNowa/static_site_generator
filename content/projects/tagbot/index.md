# TAGBOT — Autonomous Tag-Playing Robot

A robotics project from my Master's program at Boston University (EC545 — Embedded and Real-Time Systems). TAGBOT is an autonomous robot that plays the game of tag with real people outdoors, using computer vision and LiDAR for perception and a finite state machine for control.

## The Idea

Most indoor robotics projects keep kids sitting at a screen. TAGBOT was designed to bring STEM learning outside — robots that move, react, and compete physically with players in the real world.

## How It Works

The system runs on a Yahboom ROSMASTER X3 robot (Jetson Nano, RGB-D camera, 2D LiDAR) with two custom ROS packages:

**Color Detector** subscribes to the robot's RGB and depth camera feeds, finds red-colored targets in the image, filters out small noise contours, and publishes the distance and angle to the nearest target as a ROS topic.

**Controller** implements a three-state finite state machine:

- _Search_ — robot moves forward scanning for targets
- _Chase_ — robot aligns to the target angle and closes distance
- _Avoid_ — overrides chase to steer away from walls and obstacles detected by LiDAR

LiDAR coverage is split into left, front, and right zones across a 320-degree field of view. When obstacles are too close in all three zones simultaneously, the robot backs up before rotating to a new heading.

## Tech Stack

- **ROS1 Melodic** on Ubuntu 18.04
- **Python** — color detection and control logic
- **C++** — lower-level node implementations
- **UPPAAL** — formal state machine verification

## Results

The system successfully chased and tagged players in outdoor testing. Color-based detection proved more reliable than YOLO-style neural network detectors for our ground-level camera angle, though it was susceptible to false positives on red objects in the environment.

[View on GitHub](https://github.com/AidanNowa/EC545_TAGBOT)

[Back to Home](/)
