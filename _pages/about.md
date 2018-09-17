---
permalink: /
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I hope to contribute to our understanding of how we can  map abstract high-level descriptions of algorithms into efficient custom hardware. To date my research has led me to develop tools that aim to make high-level synthesis of FPGA digital circuits easier, faster, and more reliable.

PushPush
=====
Currently I am working on developing PushPush, a tool that makes linking hardware and software functions as easy as linking software objects together.
We have developed a higher-order system-level type system that enables functions to be passed as parameters between functions executing in both hardware and software. This enables some novel designs to be efficiently constructed.
For example: systems where the `main()` function is specified in hardware not software, or giving functions executing in hardware the ability to make software based OS system calls such as `printf()`. 

Reliable FPGA Computation
===========================
FPGA-based applications working in extreme environments, such as satellites in low-earth orbit, or safety critical applications, such as autonmous vehicles, need to be designed in such a way that they are resillient to errors.
However in general, off-the-shelf FPGA devices are highly sensitive to errors in their configuration memory, with bit-flips causing unwanted reconfigurations.
My research in this area focusses on a few things:
* __[Automatic protection]__: Protecting FPGA designs is a tedious and error-prone task. My aim is to build tools that automatically provide circuit protection (at a higher-abstraction level) than current tools.
* __[Selective protection]__: By statically analysing high-level descriptions of applications, such as an input to a high-level synthesis tool, it is easier for us to extract the _"important portions"_ of the application compared to at a lower abstraction level, such as the hardware description. Using this information we can then automatically protect only the identified portions, reducing the expensive area and power overheads that typically inflict protection strategies. 
* __[Testing time]__: Testing complex FPGA circuits against faults is a lengthy time consuming process. I have worked on tools and infrastructure to accelerate this process, improving test converage and testing times.

Working in this area has also lead to me becoming an experimenter of the European Space Agency OPS-SAT project, an experimental research platform being sent into low-earth orbit. My work will investigate the resilliency of modern commercial reconfigurable SoC devices in the harsh environment of space. FPGA circuits constructed via my tools will be executing on the on-board commercial FPGA reconfigurable SoC devices during flight. 

Helper Circuits for High-Level Synthesis
=========================================
High-level synthesis optimisations often require a static analysis of the input so that they can determine runtime behaviours, such as memory access patterns or loop dependencies, they can then use this information to generate more efficient circuits.
However, for dynamic applications, such as those which walk dynamic data structures, static analysis-based approaches often fall flat. 
I am interested in addressing this gap by developing tools that can construct _helper circuits_ that execute along side the main circuit in a support role. These helper circuits are built using application specific knowledge extracted from the semantics of the input source and are included in the generated hardware.
Research in this direction has led me to develop helper circuit-based high-level synthesis optimisations that can:
* __[protect control-flow]__ by detecting any incorrect branch the exact cycle it occurs
* __[prefetch data]__ by running ahead of the main circuit, fetching the data it requires, and storing it locally just before it is needed.  
* __[predict dynamic schedules]__ by running ahead and constantly updating a dynamically improving worst-case execution time upper-bound for high-level synthesis generated applications. 
