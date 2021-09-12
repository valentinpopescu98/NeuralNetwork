# NeuralNetworkKeras
OCR application using neural networks developed in Python using Keras.


To run this project follow the next steps:

1. Run "ReteaNeuronalaAntrenament.py" which is the training app for the NN.
Feel free to change the activation functions, loss function, optimizer, metrics, dataset or epochs number.
After you're done with the change, run it, so that it will train the model and save it after training to the disk.
This app also does a test on the NN by a chosen metric. I chose by accuracy, so that after the training, 
it shows you what percentage of all the test images does it predict correctly.

2. Run "ReteaNeuronalaTest.py", the test app for the NN.
This app loads the saved model at the previous step and makes a prediction based on the state of an image's input neurons tensor.
The prediction actually returns another tensor with the output neurons activations,
so I chose to print to the console only the highest value (the correct label) for visibility purposes.

3. Run "AfisareTensorSiImagine.py", the app that literally shows you whatever image from the dataset you want.
If you want to see if the NN actually did the corret prediction, you can use this app.
For ease of use, I added a variable named "sablon" in this app and the "ReteaNeuronalaTest.py" app,
so that you don't have to edit through all the code when you want to predict another image.
You just number it whatever you want, number it in the "ReteaNeuronalaTest.py" app the same number and compare them, to see if it worked.

You can interchange step 2 and 3, it doesn't matter, as the evaluation of the prediction is made by the user.

This project was developed using TensorFlow 2.2.

Thank you for using my OCR project!
