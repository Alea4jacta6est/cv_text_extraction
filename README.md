# Information Extraction from png pictures

This is a demo of approaches that extract objects from images. The first version of this app is able to extract textual data from driving license and save it as an excel file / demonstrate results in a simple user interface

## How to run this app?

Using Docker:

`docker build . -t "cv:v1"`

`docker run -p 4200:4200 "cv:v1"`

By default you can access the app here: http://localhost:4200/