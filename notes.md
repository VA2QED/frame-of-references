# Frame of Reference project script and notes

###### This file serves to allow for visualisation before coding the animations, please place your pictures in ./assets/notes/

## Introduction

Hello everyone, in this video we are going to attempt to explain the concept of a reference frame.

```python
class SelfIntroduction(Scene):
	def construct(self):
		# Title and names    
        self.play(Write(Title))
        self.wait()
        self.play(Write(Names))
```

First of all, a reference frame is composed of an origin and methods of describing the position of an object relative to the origin. A frame of reference seeks to systematically answer the question of where something is in space.

```python
class ReferenceFrameDefWords(Scene):
    # Write A reference frame is composed of an **origin** and 
    # methods of describing the **position** of an **object**
    # **relative** to the **origin**
```

As an example, this point can be described by saying it is a certain units of distance horizontally and a certain distance vertically away from the origin. This is known as a Cartesian coordinate system. By the way, in mathematics and physics, the textual description can be abstracted with a set of coordinates for simplicity.

```python
class ReferenceFrameDef(GraphingScene):
    def construct(self):
        # draw graph
        # draw a point on the graph and move it around
        # write "the object is (distance) away from the origin in the x 
        # direaction and (distance) away from the origin in the y  
        # direction" 
        # transform that text into coordinates
```



For the purposes of this video, we are only going to explain what is known as inertial reference frames. Inertial reference frames are frames of references in which itself is not experiencing a force, or "pushes and pulls".

```python
class ReferenceFrameNoAcceleration(GraphingScene):
    def construct(self):
        # draw a graph that is sitting on a graph
        # somehow, that is not moving
```

- this probably needs more rigorous definitions