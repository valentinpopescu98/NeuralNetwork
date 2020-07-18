import tensorflow as tf
import matplotlib.pyplot as plt

"""Forma de test aleasa din setul de date x_test."""
sablon=1

"""Setul de date MNIST (Modified National Institute of Standards and Technology database),
care contine imagini de 28x28 pixeli cu cifre scrise de mana de la 0 la 9 folosite la antrenare."""
mnist = tf.keras.datasets.mnist

"""Incarca imaginile din pachetul MNIST."""
(x_train, y_train), (x_test, y_test) = mnist.load_data()

"""Se normalizeaza ca valori in intervalul [0, 1)."""
x_train=tf.keras.utils.normalize(x_train, axis=1)
x_test=tf.keras.utils.normalize(x_test, axis=1)

"""Se afiseaza valoarea tensor-ului formei de test alese."""
print(x_test[sablon])

"""Se afiseaza imaginea formei de test alese."""
plt.imshow(x_test[sablon], cmap=plt.cm.binary)
plt.show()