# Frame of Reference project script and notes

###### This file serves to allow for visualisation before coding the animations, please place your pictures in ./assets/notes/

## Outline

*In this project, instead of defining the concepts right from the beginning and demonstrating them, I believe that it is more fit to introduce a few different problems. The problems will be disagreements between different observers on the different properties of an object, each representing a part of the reference frame that needs to be implemented, then at the very end the solutions of these problems will be assembled together into the definition of the reference frame.*

* Situation 1: 
  * Settings: Stationary observers and an oriented object.
  * Problem: How do the observers come to an agreement with each other about the orientation and position of the object.
  * Solution: introduce an universal origin and a direction system [a compass] that allows both observers to *convert* their own reference frames [centred at their origin] into a **shared** reference frame. 
* Situation 2:
  * [To be added]

## ~~Introduction~~

*As previously mentioned, I prefer to define reference frame at the **end** of the presentation instead of the beginning, so I'm scrapping the introduction at the moment - as we gradually introduce the concepts we will re-use this part to cover the left-overs and sum up in the end.*

~~Hello everyone, in this video we would like to explain the concept of a reference frame, in the context of physics and motion.~~

```python
class SelfIntroduction(Scene)
```

~~First and foremost, a reference frame is "assigned" an origin. Consequently, various methods and equipment are utlised in order to describe the position and orientation of an object, relative to this origin. In essnse, a frame of reference seeks to systematically answer the question of *where* something is in time and space. Also please note that for this video, the observer is placed at the origin for ease. An observer can also be a certain distance away from the origin.~~

```python
class ReferenceFrameDefWords(Scene)
```

~~As an example, the positon of this moving green point can be described by saying it is a at a position of x from the origin's x axis and a position of y from the origin's y axis, of course assuming that the right direction indicates motion in the positive direction. This is known as a Cartesian coordinate system, which you may have encountered in math class.~~

```python
class ReferenceFrameExample(Scene)
```

~~For the purposes of this video, we are only going to discuss inertial reference frames. So, what is an *inetial* frame of reference? An Inertial reference frame is one that either does not move or moves at a constant speed, with zero acceleration, without changing direction.  An isolated object in this refernce frame would not experience any forces, or "pushes and pulls". For example, if your reference frame is a car moving at a constant velocity, then that is an inertial reference frame. However, a car that is speeding up, slowing down or making a turn (i.e : changing direction) is not considered an inertial reference frame.~~

```python
class InertialReferenceFrameDisclaimer(Scene)
```



## Perception of position or orientation

### Orientation

>  [Removed the mention to reference frames] Let us introduce the problem before creating the concepts. Instead of introducing the observers first, it is more optimal to introduce the subject of the discussion - the object. Introducing it first allows the audience to look at the object and come up with their own judgment before the observers' perspectives are presented.
>
> TODO: it is better to replace the object with something else, be it a car or an arrow that has an orientation associated with it instead of a triangle (directions can be confused if you use a simple shape). 

**Let us say that we have an object, facing this way.**

*Animation: create and rotate object.*

> Introducing the observers. I strongly prefer to not use my name. 
>
> TODO: We also prefer to use simpler names instead of our real names as they are easier to process. Naming observers also face the challenge of labelling the observers and having to reinforce the names throughout the presentation as they can be forgotten. Possible candidates can be the classic *Alice and Bob* or colour-coded observers *Blue and Orange* for example.
>
> Instead of directly saying reference frames, we indirectly indicate their position and orientation.

**And we have two observers, [Top Observer] and [Bottom Observer] facing each other on the opposite end of the screen.** 

*Animation: create and show the observers.*

*Animation: shake the observers (or use some construction on the shape of the observer) to demonstrate their directions.*

> Using using Cartesian coordinate systems and sign conventions is a bit too unreasonable - and you are establishing another reference frame (sneakily) by introducing a separate coordinate system, and that's a no-go.

> Instead of describing the situation in an "observer" tone, ask questions to try to have some engagement with the audience.

**So, which way is the object facing?**

> As mentioned earlier - using a shape makes describing the directions more difficult. 
>
> We are also separating orientation and position since asking them together can force too much information to be processed at once.
>
> We then present the perspectives on the directions.

*Animation: darken bottom observer and potentially zoom in as we introduce the perspective of the top observer.*

*Animation: show the "axis" of the top observer. Show all 4 directions and label them "front, back, left, right".*

**[Top Observer] would say that the object is facing their left.**

*Animation: extend (emphasise) and potentially brighten the "left" arrow and stretch the object to show the congruency in their orientation.*

*Animation: hide the "axis" of the top observer.*

*Animation: brighten the bottom observer as we exit the perspective of the top observer.*

> Present the perspectives of bottom observer.

*Animation: darken top observer and potentially zoom in as we introduce the perspective of the bottom observer.*

*Animation: show the "axis" of the bottom observer. Show all 4 directions and label them "front, back, left, right".*

**[Bottom Observer] would say that the object is facing their right.** 

*Animation: extend (emphasise) and potentially brighten the "right" arrow and stretch the object to show the congruency in their orientation.*

*Animation: hide the "axis" of the bottom observer.*

*Animation: brighten the bottom observer as we exit the perspective of the bottom observer.*

> Then present the conflict between the observers - they do not have an agreement on the orientation of the object.

**So which way is the object facing? There can be only one, right?**

*Animation: shake or stretch the object to emphasise its direction.*

*Animation: show and shake question marks above the observers.*

> Here, present a hint to the solution: there is no disagreement.

**Now you may have realised the two observers are talking about the same direction, they just call it differently.**

*Animation: show the "axis" of the observers again and stretch the arms to show that they are facing the same direction.*

> Then introduce an universal direction system, the compass always points at the same direction.

**Then how can the two observers [use their names here instead] come to an agreement? They decide to look for something that they can both have, and found a compass. **

*Animation: hide the observers and the object to introduce the compass.*

*Animation: Show a compass. [This may be a bit difficult to make, but a circle and two triangles with a smaller circle in the centre will do the trick.] Then shake it while keeping the arrows facing the same direction.*

> Specify that the compass always points at the same direction to clear up any potential confusion and make sure that people realise that this system can be shared.

**The compass always points to the same direction, no matter of where you put it and how you rotate it. **

*Note: for this instance, the compass will have its red arrow always pointing **right** as that will be the direction of the object.*

*Animation: hide the compass (make it fade away).*

*Animation: show the observers and the object again.*

**The two observers [use their names here instead] decided to each take a compass and take a look at the object again.**

*Animation: give each observer a compass.*

> Ask the same question again, though the question did not change, the observers have now been equipped the same tool to measure the direction, therefore the response would be different.

**So which way, is the object facing?**

*Animation: show the "axis" of both observers, but still label them with "left right" directions.*

**This time, they decide to use their compass.**

> Demonstrate that the use of the compass makes a difference in the observations.

*Animation: change the "right" axis of both observers to be **red**, and replace the labels with "north, south, west, east".*

**The object is facing north.**

*Animation: extend and brighten the north axis of **both** observers and then stretch the object to show the congruency in their orientation.*

> Explicitly state the conclusion of the experience for people who have not realised.

**By choosing to use the compass as their common reference in their directions, the two observers come to an agreement with the direction of the object.**

> In case *you* haven't realised, based on the raw information here, you should know why I am separating direction and position now.

*Animation: hide the axis of both observers.*

### Position

> After the first problem is resolved, introduce the second one. 

**Now that they [use the observers' names here] have come to an agreement with the direction, they begun thinking about a new question.**

**Where is the object?**





![position and orientation](./assets/notes/orientation-and-position.png)

## Relative motion
### TitleScreen
say nothing 
### DemonstrationOfRelativeMotion
```python
# Adding number line
self.play(ShowCreation(number_line))
self.add(label)
self.wait()
```
To demonstrate relative motion, let's say that the red eye, as a stationary observer is asked to describe the motion of a ball inside the car relative to a number line.

```python
# Adding stationary object
self.add(stationary_observer)
self.wait()
# adding car and positon label
self.play(ShowCreation(car))
self.play(ShowCreation(ball))
self.play(ShowCreation(position_label), ShowCreation(position_number))
self.wait()
```



On this car, the blue eye is also asked to observe the motion of the same ball. 

```python
# adding moving observer
self.add(moving_observer)
self.wait()
```



Imagine that we have trapped the blue eye in a car with one way mirrors and it does not know that the car is moving at a constant velocity relative to the number line. Also, let's say that the car and the object was already moving at a constant speed when the animation starts, meaning that there is no acceleration to begin with. Let's hit unpause and see the car move.

 ```python
# Playing animation
self.play(MoveAlongPath(car, moving_car_path), rate_func=linear, run_time=4)
self.wait()
 ```

### StationaryPerspective

```python
# adding number line
self.play(ShowCreation(number_line))
self.add(label)
self.wait()
```

When we ask the stationary observer the path of motion of the ball, it will say that the ball has moved from the position -4 to the position of 7 on the number line. 

```python
# adding ball, brace and the number for the ball's position
self.play(ShowCreation(ball), ShowCreation(brace_to_ball), ShowCreation(ball_position))
self.add(stationary_observer)
self.wait()
```



### MovingPerspectiveHideNumberLine

However, when we ask the observer in the moving car about its experiences a box, it will first complain about being stuck inside a box without any knowledge of the outside and say that the ball is stationary relative to it. 

To help understand the observer in the car's perspective better, I'm going to move the camera along with the car, and remove the number line. I'm going to start moving now.  

```python
# adding number line
self.play(ShowCreation(number_line))
self.add(label)
self.wait()
# zooming in
self.play(self.camera_frame.animate.scale(0.5).move_to(ball))
# adding ball and observer
self.play(ShowCreation(ball))
self.add(moving_observer)
self.wait()
# moving camera
self.camera_frame.add_updater(lambda d: d.move_to(ball.get_center()))
# If you are reading this code, think about why I didn't need to animate the ball moving
# removing number line
self.remove(number_line)
self.wait(4)  # this is the amount of time that the movement would usually take
self.play(Restore(self.camera_frame))
self.wait()
```



What? You can't tell if the ball, car and the observer are moving or not? Exactly. This is exactly what the observer in the car sees as well. The car is moving at a constant velocity so nothing inside the car experiences any accelerations. The observer only knows that the ball is stationary relative to it. 

### OwnReferenceFrame

```python
self.play(ShowCreation(number_line), Write(label))
self.play(FadeIn(moving_observer), ShowCreation(ball))
self.wait()
```



In fact, the observer that is in the moving car is not in the same reference frame as the stationary observer, as demonstrated beforehand, this creates a disagreement between the measurements of the position and change of position of the ball.



