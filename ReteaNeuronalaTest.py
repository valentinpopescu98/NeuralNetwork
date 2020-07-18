import tensorflow as tf
import numpy as np

"""Forma de test aleasa din setul de date x_test."""
sablon=1000

"""Setul de date MNIST (Modified National Institute of Standards and Technology database),
care contine imagini de 28x28 pixeli cu cifre scrise de mana de la 0 la 9 folosite la antrenare."""
mnist = tf.keras.datasets.mnist

"""Incarca imaginile din pachetul MNIST."""
(x_train, y_train), (x_test, y_test) = mnist.load_data()

"""Se normalizeaza ca valori in intervalul [0, 1)."""
x_train=tf.keras.utils.normalize(x_train, axis=1)
x_test=tf.keras.utils.normalize(x_test, axis=1)

"""Se incarca modelul de pe hard-disk."""
model_antrenat = tf.keras.models.load_model('recunoastere_cifre.model')

"""Se verifica lista cu toate formele de test si se printeaza valoarea formei de test alese."""
testare = model_antrenat.predict([x_test])
print("Cifra este: "+str(np.argmax(testare[sablon])))