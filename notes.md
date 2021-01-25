# Frame of Reference project script and notes

###### This file serves to allow for visualisation before coding the animations, please place your pictures in ./assets/notes/

## Introduction

Hello everyone, in this video we are going to attempt to explain the concept of a reference frame.

```python
class SelfIntroduction(Scene)
```



First of all, a reference frame is composed of an origin and methods of describing the position and orientation of an object relative to the origin. A frame of reference seeks to systematically answer the question of where something is in space. 

```python
class ReferenceFrameDefWords(Scene)
```

Also please note that we are assuming that the observer is at the origin for ease. An observer can also be anywhere in space relative to the origin/

```python
class ObserverCanBeAnywhere(VectorScene)
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

## Relative motion

To demonstrate relative motion, let's say that the red eye, as a stationary observer is asked to describe the motion of a ball inside the car relative to a number line. On this car, the blue eye is also asked to observe the motion of the same ball. Imagine that we have trapped the blue eye in a car with one way mirrors and it does not know that the car is moving at a constant velocity relative to the number line. Also, let's say that the car is moving at a constant velocity and that the object was already moving at a constant speed when it starts to move. Let's hit unpause and see the car move.

When we ask the stationary observer the path of motion of the ball, it will say that the ball has moved from the position -4 to the position of 7 on the number line.



However, when we ask the observer in the moving car about its experiences a box, it will first complain about being stuck inside a box without any knowledge of the outside and say that the ball is stationary relative to it. 

To help understand the observer in the car's perspective better, I'm going to move the camera along with the car, and remove the number line. I'm going to start moving now. 

What? Nothing's moving? Exactly. This is exactly what the observer in the car sees as well. The car is moving at a constant velocity so nothing inside the car experiences any accelerations. The observer only knows that the ball is stationary relative to it. Thus, it has no idea that it, along with the ball is moving relative to a number line at a constant velocity as well.