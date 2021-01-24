# Frame of Reference project script and notes

###### This file serves to allow for visualisation before coding the animations, please place your pictures in ./assets/notes/

## Introduction

Hello everyone, in this video we are going to attempt to explain the concept of a reference frame.

```python
class SelfIntroduction(Scene)
```



First of all, a reference frame is composed of an origin and methods of describing the position and orientation of an object relative to the origin. A frame of reference seeks to systematically answer the question of where something is in time and space. Also please note that for this video, the observer is placed at the origin for ease. An observer can also be a certain distance away from the origin.

```python
class ReferenceFrameDefWords(Scene)
```



As an example, this moving green point can be described by saying it is a at a position of x from the origin's x axis and a position of y from the origin's y axis, of course assuming that the right direction indicates a positive . This is known as a Cartesian coordinate system.

```python
class ReferenceFrameExample(Scene)
```



For the purposes of this video, we are only going to explain what is known as inertial reference frames. Inertial reference frames are frames of references in which itself is not experiencing a force, or "pushes and pulls". For example, if your reference frame is a car moving at a constant velocity, then that is an inertial reference frame. However, a car that is speeding up or slowing down is not an inertial reference frame.

```python
class InertialReferenceFrameDisclaimer(Scene)
```





## Perception of position or orientation

First, let us discuss how a change of reference frames can affect the orientation and position of the object. As an example, let's say that there are two observers, Jerry and Ashmita with two different reference frames. Jerry's positive x direction and positive y direction are right and up relative to the screen and Ashmita's positive x direction and positive y direction are down and left relative to the screen. When asked to describe the position and orientation of the object, Jerry will say that the triangle is right side up and positioned to the right and up relative to his origin and Ashmita will say that the triangle is upside down and is positioned to the left and up of his reference frame.

![position and orientation](./assets/notes/orientation-and-position.png)
