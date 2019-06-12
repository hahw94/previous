# MNIST-Decoder

<h2> Leaky-relu </h2>

![캡처](https://user-images.githubusercontent.com/49590432/59349208-08727980-8d54-11e9-96bf-77f272a368b1.PNG)
<p>In this code, I use Leaky relu for better optimize</p>


![111111111](https://user-images.githubusercontent.com/49590432/59329493-f845a480-8d29-11e9-965e-43d61e062811.PNG)<br><br>


![2222222222](https://user-images.githubusercontent.com/49590432/59329497-fa0f6800-8d29-11e9-8519-80875f0d619b.PNG)<br><br>


<h2><center>Put some noise in image</center></h2>

![noise](https://user-images.githubusercontent.com/49590432/59329513-0398d000-8d2a-11e9-8391-4f412df71cc5.png)<br><br>
<p>
  <h4> Using this code made some noise in image</h4> 
  
temp_img = mnist.test.images[2]<br>
temp_noisy_img = temp_img + 1 * np.random.randn(*temp_img.shape)<br>

plt.imshow(temp_noisy_img.reshape(28,28), cmap='gray')<br>
</p>
<br><br><br>
<h2>Result & Comparison</h2>

![비교](https://user-images.githubusercontent.com/49590432/59348927-5fc41a00-8d53-11e9-882f-80649adf4427.png)

<h3> - upper image is Input image & bottom image is Output image - </h3>

<br><br>

![original](https://user-images.githubusercontent.com/49590432/59329521-08f61a80-8d2a-11e9-9e58-bdebab86f5f4.png)

<h3> - original image -</h3>

<br><br><br><br><br><br><br>


![3333](https://user-images.githubusercontent.com/49590432/59332729-e10ab500-8d31-11e9-9250-5c6401fc2642.PNG)


<h2>Process of deep learning and Result of Accuracy by using trained neural network</h2>
Period: 0001 cost = 2.635733213<br>
Period: 0011 cost = 0.730518100<br>
Period: 0021 cost = 0.616208915<br>
Period: 0031 cost = 0.553452830<br>
Period: 0041 cost = 0.506920440<br>
Period: 0050 cost = 0.452219454<br>
Accuracy: 0.942
