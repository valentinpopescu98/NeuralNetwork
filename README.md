# NeuralNetworkFromScratch
Simple neural network developed in python from scratch, no ML libraries.
This is a project written in romanian language. Feel free to edit my code and create an english version.


To run this project follow the next steps:

1. Run "EditorSabloaneAntrenament.py" and create one or more patterns for the Neural Network to learn.
It should create a file named "sabloane antrenament.txt" which contains the pixel values (1/0) of the training patterns.
Generally, the more patterns you add, the better the NN trains.

2. Run "ReteaNeuronalaAntrenament.py" which is the training app for the NN.
It should create a file named "ponderi.txt" which contains the weights after the training finishes.
The NN works by training until the gradient descends down to a certain threshold. Feel free to change the threshold or run it for a fixed number of epochs.

3. Run "EditorSabloaneTest.py" and choose a test pattern for the NN to make a prediction.
It should create a file named "sabloane test.txt" which contains the pixel values (1/0) of the test pattern.
This app works by making a test per run. If you try to add another pattern over the existing one, the app will overwrite the old pattern with the new one.
If you want, you can edit the app to allow more than one prediction, but you have to edit the app at the next step too,
so it will be able to make a prediction on more than one pattern.

4. Run "ReteaNeuronalaTest.py", the test app for the NN.
This app works by getting the state of each pixel from the "sabloane text.txt" file and calculate the activations of the output neurons,
thus returning the values for each one of them. It prints the highest activation which is likely the correct label for the OCR project,
whereas the NN uses 10 labels for each number from 0-9.


Thank you for using my OCR project!
