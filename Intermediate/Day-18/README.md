# Day 18 - Turtle & the Graphical User Interface (GUI)

## Project: Hirst Painting

This project consists of two main components: color extraction from a reference image using the `colorgram` library and generating a 
Hirst-style painting using the extracted color palette.


### Color Extraction:

- The first part of the project involves extracting colors from a reference image using the colorgram library. This process captures a selection of colors from the reference image, which is essential for replicating the color palette of a real Hirst painting accurately.
- The extract_rgb function is utilized to extract RGB values from each color in the color palette, providing a structured representation of the colors in the form of tuples.
- The extracted color palette is stored in a list for later use in generating the painting.

### Painting Generation:

- The second part of the project focuses on generating a Hirst-style painting using the extracted color palette.
The turtle module in Python is employed to create a canvas for the painting. A turtle object, representing the paintbrush, is used to draw dots of varying colors on the canvas.
- The color_list obtained from the color extraction process serves as the color palette for the painting. Random colors from this palette are chosen for each dot to create an abstract and visually appealing composition.
- The painting is constructed by iteratively placing rows of dots on the canvas, creating a grid-like pattern reminiscent of Hirst's signature style.

## Result

![image](https://github.com/cristobalgrau/100-days-of-python/assets/119089907/2c5dcaf7-c487-4bd6-846d-5c76091f5755)
