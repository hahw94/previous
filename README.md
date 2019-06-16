# ising-model

<h4>1. Make randomly spin </h4><br>

<p> - By this code we can get N*M arrray, value is radomly +1 or -1</p>

![111111111111](https://user-images.githubusercontent.com/49590432/59559347-ff2d2980-903f-11e9-944b-916252a53948.PNG)

![array 77](https://user-images.githubusercontent.com/49590432/59559285-92fdf600-903e-11e9-9df4-6fa47bf3de38.PNG)

<br><br><br>

<h4>2. Make randomly spin field</h4><br>

<p>  
  - make some image from function 'image.fromarray' and using 'random_spin' function that we made,     then we can get some image like this
</p>

![222222222222222](https://user-images.githubusercontent.com/49590432/59559348-00f6ed00-9040-11e9-97df-483959b846c2.PNG)


![spin field(2)](https://user-images.githubusercontent.com/49590432/59559286-95605000-903e-11e9-894e-220c13b07345.PNG)

<br><br><br>

<h4>3. Make ising_process and ising_update function </h4><br>

<p>
   - 'ising_process'  is for processing ising model,  N*M layer, it is proceed order by skip 2 spaces
</p>

<p>
   - 'ising_update' is for updating ising model, it is decide what will be next, total은 i((n-1) ~ (n+1) divided by N and j(m-1) through(m+1) divided by M.

Furthermore, if these values are positive, there is no change in the spin, but they are less than zero or equal to zero.

If the exp (-dE * beta) is greater than a random number, the condition of the field changes (and therefore *(-1)).
</p>


![444444](https://user-images.githubusercontent.com/49590432/59559349-03f1dd80-9040-11e9-8868-7c0521c7b597.PNG)

![55555555555](https://user-images.githubusercontent.com/49590432/59559350-05230a80-9040-11e9-8e44-67508e1fa833.PNG)

<br><br><br>

<h4>4. Append ising_process image and make sequence image </h4><br>

<p>
   - By this function we can show successive changes of ising model. Use an interact tool from the ipywidgets library. We've introduced a way to see visually using frame.
</p>

![6666666666](https://user-images.githubusercontent.com/49590432/59559351-05bba100-9040-11e9-9875-d3260235d9c9.PNG)


![3333](https://user-images.githubusercontent.com/49590432/59559287-972a1380-903e-11e9-8df2-90b3c640817a.PNG)




<br><br><br>

<h4>5. Creating an image sequence using </h4><br>

<p>
  - Create a random spin field plot called images.

Add ising_process to this picture to add multiple pictures

Then you print out the image using the function you created above as follows:

You can view the changing ising_model.

</p>

![777777777777777](https://user-images.githubusercontent.com/49590432/59559352-06ecce00-9040-11e9-85ca-317579c86414.PNG)


![result](https://user-images.githubusercontent.com/49590432/59559288-985b4080-903e-11e9-9c6e-fbfae417a9f1.PNG)
