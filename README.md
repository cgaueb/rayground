# [Rayground.com](https://www.rayground.com)

<p style='text-align: justify;'>
Rayground is a web-based framework for rapid prototyping of algorithms based on the ray tracing paradigm. Its main goal is to help develop, test and share self contained modules that showcase a particular method or technique. 
This work aims to demystify ray tracing fundamentals while relying on the established GLSL shading language for code development and the underlying WebGL pipeline for its hidden execution model. It is intended for people who are already familiar with the basics of computer graphics theory and shader-based programming. A detailed documentation of the Rayground's programming interface is available <a href="https://www.rayground.com/documentation"> on-site </a>, coupled with  many demo and tutorial projects, in order tο ease the way of newcomers.
</p>

![Image description](Figures/teaser.jpg)
**Teaser.** Rayground logo illuminated and shaded with a simple path tracer implementation. Rayground project link can be found <a href="https://www.rayground.com/view/WwBwf-k639U"> here </a>.

## Description

Rayground aims to demystify raytracing fundamentals, by providing a well-defined WebGL-based programmable graphics pipeline of configurable distinct raytracing stages coupled with a simple scene description format. The graphical user interface of Rayground is designed to have two discrete parts, the _preview window_ and the _shader editor_, similar to the layout of 
<a href="https://www.shadertoy.com/"> ShaderToy</a>, which many shader developers are already familiar with (Fig. 1). Visual feedback is interactively provided in the WebGL rendering context of the preview canvas, while the user performs live source code modifications. Rayground  follows a  programmable GPU-accelerated ray-tracing pipeline in order to give developers direct and flexible control of five ray tracing stages through a simple, high-level shader-based programming model. Thus, the shader editor  consists  of  five  tabs,  corresponding  to  five  customisableshader stage, namely _Scene_, _Generate_, _Hit_, _Miss_ and _PostProcess_.

![Image description](Figures/gui.jpg)
**Figure 1.** (Left) The Rayground interface, with the _preview window_ and the _shader editor_, showing the _Generate_ stage. (Middle and Right) _Hit_ and _Miss_ event shaders for the same project, where the Cornell Box scene is rendered using a simple path tracer. Complete implementation details can be found 
<a href="https://www.rayground.com/view/dExaQa67tqI"> here </a>.


## Prerequisites

Rayground is open, cross-platform, and available to everyone. It does not rely on any browser plugins and thus runs on any platform that has a modern standards compliant browser. Specifically, the website runs only on WebGL2-enabled browsers and requires the `EXT_color_buffer_float` extension. 

## Aim

The goal of this github account is twofold: 
- Inform the active users what new [features](https://github.com/cgaueb/rayground/projects) are coming in the next version(s) of the website.
- Offer accessibility for bug reporting, enhancements or feature [requests](https://github.com/cgaueb/rayground/issues).


## Research

**Motivation**. The advent of mass-produced, consumer grade hardware with raytracing acceleration capabilities has significantly boosted the interest of the graphics community and has led to the introduction of related methods to interactive applications, thus demonstrating its wide applicability to students. Unfortunately, this turn of interest to ray-tracing-based techniques is not sufficiently backed by proper educational tools to assist students in becoming familiar with the basic concepts and help them become practically engaged in building their own projects. Moreover, modern low-level graphics APIs, either dedicated to ray tracing like NVIDIA OptiX or supporting it, such as Microsoft DirectX 12 and Khronos Group Vulkan, pose high entry barriers to students and require a very daunting and long learning process, riddled with many distracting technicalities.

**Idea**. In [VGV+20], Rayground is used as an online, interactive education tool for richer in-class teaching and gradual self-study by providing a convenient introduction into practical ray tracing. In this work, an extensive discussion is offered describing how both undergraduate (Fig. 2) and postgraduate (Fig. 3) computer graphics theoretical lectures and laboratory sessions can be enhanced by Rayground, in order to achieve a broad understanding of the underlying concepts. For more details please refer to the original manuscript provided below.

**[VGV+20]** Vitsas N., Gkaravelis A., Vasilakis A. A., Vardis A., Papaioannou G., '_Rayground: An Online Educational Tool for Ray Tracing_'. In Eurographics 2020 - Education Papers (2020), The Eurographics Association.<br/><br/>
<a href="https://abasilak.github.io/papers/conferences/eg2020edu/paper.pdf">
<img alt="author's version pdf" src="Figures\pdf.png" width="100">
</a>
<a href="https://abasilak.github.io/papers/conferences/eg2020edu/presentation.pdf">
<img alt="EG presentation" src="Figures\pptx.png" width="100"> (TBD)
</a>

**Figures.**

![Image description](Figures/lab1.jpg)
**Figure 2.** Output of the first (a-c) and second (d) undergraduatelab sessions. 
a) <a href="https://www.rayground.com/view/WmVHCgz0qss"> Unlit shading of supported primitives. </a>
b) <a href="https://www.rayground.com/view/7_Pl0NIBFdQ"> Cornell Box using normal vector colouring </a> and 
c) <a href="https://www.rayground.com/view/H-Ve5hrVPug"> Lambertian shading</a>.
d) <a href="https://www.rayground.com/view/LYnWPJNFuPU"> Whitted-style ray tracing</a>.

![Image description](Figures/lab2.jpg)
**Figure 3.** Output of the graduate lab session tasks. 
a) <a href="https://www.rayground.com/view/RuVlw5EAs9A"> Ambient occlusion</a>.
b) <a href="https://www.rayground.com/view/feYfjVF3fXM"> Unidirectional path tracer using importance sampling</a>.
c) <a href="https://www.rayground.com/view/KIemz357k5A"> Comparison of BRDF versus light importance sampling</a>.
d) <a href="https://www.rayground.com/view/WfC8cSyuX6Y"> Volumetric rendering</a>.


## Example Projects

### <a href="https://raytracing.github.io/books/RayTracingInOneWeekend.html"> 1. Ray Tracing in One Weekend </a> 

![Image description](Figures/rtiow.png)

#### Rayground links

<a href="https://www.rayground.com/view/_UfKcxB3gas"> Chapter 4  - Rays, a Simple Camera, and Background </a> by <a href="https://www.rayground.com/users/abasilak"> abasilak </a> </br>
<a href="https://www.rayground.com/view/sRK1FhKNKc0"> Chapter 5  - Adding a Sphere </a> by <a href="https://www.rayground.com/users/abasilak"> abasilak </a> </br>
<a href="https://www.rayground.com/view/A5ACqnpz3M4"> Chapter 6  - Surface Normals and Multiple Objects </a> by <a href="https://www.rayground.com/users/abasilak"> abasilak </a>  </br>
<a href="https://www.rayground.com/view/lNwc6PhzGHQ"> Chapter 7  - Antialiasing </a> by <a href="https://www.rayground.com/users/abasilak"> abasilak </a> </br>
<a href="https://www.rayground.com/view/-o_deCr290Y"> Chapter 8  - Diffuse Materials </a> by <a href="https://www.rayground.com/users/abasilak"> abasilak </a> </br>
<a href="https://www.rayground.com/view/1vUO9oRPNQU"> Chapter 9  - Metal </a> by <a href="https://www.rayground.com/users/abasilak"> abasilak </a> </br>
<a href="https://www.rayground.com/view/tdUZeZ29Y2I"> Chapter 10 - Dielectrics </a> by <a href="https://www.rayground.com/users/abasilak"> abasilak </a> </br>
<a href="https://www.rayground.com/view/NSGnYLZjYqc"> Chapter 11 - Positionable Camera </a> by <a href="https://www.rayground.com/users/abasilak"> abasilak </a> </br>
<a href="https://www.rayground.com/view/1cdXcNivq58"> Chapter 12 - Defocus Blur </a> by <a href="https://www.rayground.com/users/abasilak"> abasilak </a> </br>
<a href="https://www.rayground.com/view/2hucHmtxldY"> Chapter 13 - Where Next? </a> by <a href="https://www.rayground.com/users/abasilak"> abasilak </a> </br>

### <a href="https://raytracing.github.io/books/RayTracingTheNextWeek.html"> 2. Ray Tracing the Next Week </a> 

![Image description](Figures/rttnw.png)

#### Rayground links

<a href="https://www.rayground.com/view/szTlW7Tb7Nk"> Chapter 4  - Solid Textures </a> by <a href="https://www.rayground.com/users/abasilak"> abasilak </a> </br>
<a href="https://www.rayground.com/view/9xM4xAb6KJ4"> Chapter 5  - Perlin Noise </a> by <a href="https://www.rayground.com/users/abasilak"> abasilak </a> </br>
<a href="https://www.rayground.com/view/Ag2PFM0Ww-U"> Chapter 6  - Image Texture Mapping </a> by <a href="https://www.rayground.com/users/abasilak"> abasilak </a> </br>
<a href="https://www.rayground.com/view/DPPp6Gb5ZZg"> Chapter 7  - Rectangles and Lights </a> by <a href="https://www.rayground.com/users/abasilak"> abasilak </a> </br>
<a href="https://www.rayground.com/view/elkPNzPc5qA"> Chapter 8  - Instances </a> by <a href="https://www.rayground.com/users/abasilak"> abasilak </a> </br>
<a href="https://www.rayground.com/view/bKLY3YWRzPg"> Chapter 9  - Volumes </a> by <a href="https://www.rayground.com/users/abasilak"> abasilak </a> </br>

### <a href="https://dl.acm.org/doi/abs/10.1145/1198555.1198743"> 3. Whitted Ray Tracing </a> 

![Image description](Figures/whitted.png)

#### Rayground links

<a href="https://www.rayground.com/view/LYnWPJNFuPU"> Whitted </a> by 
<a href="https://www.rayground.com/users/Vineek"> Vineek </a> </br>

### <a href="https://dl.acm.org/doi/abs/10.1145/1198555.1198743"> 4. Ambient Occlusion </a> 

![Image description](Figures/ao.png)

#### Rayground links

<a href="https://www.rayground.com/view/RuVlw5EAs9A"> Ambient Occlusion
 </a> by 
<a href="https://www.rayground.com/users/Agkar"> Agkar </a> </br>