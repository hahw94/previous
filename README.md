# aeiou

<h3>1. Indexing input data</h3>

<p> Each text file has 1.5 million data. it consist of 75 people's data so 20,000 data for one person</p>

![screencapture-localhost-8888-notebooks-OneDrive-edy-Python-Machine-learning-for-everyone-aeiou-working-place-aeiou-data-ipynb-2019-06-16-22_11_49](https://user-images.githubusercontent.com/49590432/59564613-e5add100-9083-11e9-9239-d9f78c15c4fd.png)

![130만 20만 사진](https://user-images.githubusercontent.com/49590432/59564543-09244c00-9083-11e9-81d5-e4426cd61a8d.PNG)

<br><br><br>

<h3>2. Make array for training and testing (for onehot method)</h3>

<p> For using one hot method, I made array for testing(50 people) and training(325 people)
  <br><br>
  
  - Set the target value like this 
  <ul>
    <li> a data : 0</li>
    <li> e data : 1</li>
    <li> i data : 2</li>
    <li> o data : 3 </li>
    <li>u data : 4</li>
  </ul>
</p>

![screencapture-localhost-8888-notebooks-OneDrive-edy-Python-Machine-learning-for-everyone-aeiou-working-place-aeiou-data-ipynb-2019-06-16-22_18_51](https://user-images.githubusercontent.com/49590432/59564697-ea26b980-9084-11e9-8a17-6e44941b0c74.png)


![65 one hot method](https://user-images.githubusercontent.com/49590432/59564542-09244c00-9083-11e9-9ac6-a7f9f00b3cd1.PNG)


![10 one hot method](https://user-images.githubusercontent.com/49590432/59564541-09244c00-9083-11e9-8358-28b57dc5dcb4.PNG)

<br><br><br>

<h3>3. Indexing and reshape for train</h3>

![makes inputdata by reshape 50 40](https://user-images.githubusercontent.com/49590432/59564544-09bce280-9083-11e9-8722-1d841843b09a.PNG)


<br><br><br>

<h3>4-1. Training process</h3>

![screencapture-localhost-8888-notebooks-OneDrive-edy-Python-Machine-learning-for-everyone-aeiou-working-place-aeiou-data-ipynb-2019-06-16-22_25_01](https://user-images.githubusercontent.com/49590432/59564767-c44de480-9085-11e9-84ed-c369db1799d5.png)

![pooling proceed](https://user-images.githubusercontent.com/49590432/59564540-088bb580-9083-11e9-837f-bcd1ef7a7219.PNG)

<br><br><br>

<h3>4-2. Training process</h3>

![screencapture-localhost-8888-notebooks-OneDrive-edy-Python-Machine-learning-for-everyone-aeiou-working-place-aeiou-data-ipynb-2019-06-16-22_27_57](https://user-images.githubusercontent.com/49590432/59564799-17c03280-9086-11e9-81d6-033be2b47451.png)


![outputdata](https://user-images.githubusercontent.com/49590432/59564545-09bce280-9083-11e9-9bf4-6e4f8a01395c.PNG)

<br><br><br>

<h3>5. Result</h3>

<p> When I test to using logits Neural Network, I could got 100% maximum accuracy </p>

![result](https://user-images.githubusercontent.com/49590432/59564813-52c26600-9086-11e9-9b69-07cb30069de9.PNG)
