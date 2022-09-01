# Emission-Tomography-Application
This application allows you to upload seismic data such as gathers, travel times, sources' coordinates and tensor moments(you can also add them by hand or use the default ones). This data is used for coherent summation with different parameters:
1. window size
2. discretization step
3. current sample
4. current gather(It also has information about receivers' coordinates)
5. current travel times
6. curent sources coordinates
7. current tensor moments(tensor moments that are checked are used in calculations)

The result of coherent summation shows in 4 charts and 1 table:
1. upper right chart shows gather and travel times curve that gives a maximum amplitude after summation at the current moment of time 
2. upper left chart shows coherent semblance at the current moment of time
3. lower left chart shows detect function and vertical line at the current moment of time
4. lower right chart shows beachball for tensor moment that gives a maximum amplitude after summation at the current moment of time 
5. the table consist of 6 tensor moment's components, location info, and the current moment of time in miliseconds
![image](https://user-images.githubusercontent.com/89336202/187969508-dd40d7b5-f50c-4586-bace-4e11c7abacb5.png)
![image](https://user-images.githubusercontent.com/89336202/187969615-65c54d2f-04b6-43d9-bac7-55a1aa7fea17.png)
