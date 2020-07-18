import tensorflow as tf

"""Setul de date MNIST (Modified National Institute of Standards and Technology database),
care contine imagini de 28x28 pixeli cu cifre scrise de mana de la 0 la 9 folosite la antrenare."""
mnist = tf.keras.datasets.mnist

"""Incarca imaginile din pachetul MNIST."""
(x_train, y_train), (x_test, y_test) = mnist.load_data()

"""Se normalizeaza ca valori in intervalul [0, 1)."""
x_train=tf.keras.utils.normalize(x_train, axis=1)
x_test=tf.keras.utils.normalize(x_test, axis=1)

"""STRUCTURA RETELEI NEURONALE
    Strat intrare:  28x28 pixeli intrare, adica 784 pixeli, deci 784 neuroni intrare
    Strat ascuns 1: 128 neuroni; functia de transfer ReLU (rectified linear unit)
    Strat ascuns 2: 128 neuroni; functia de transfer ReLU (rectified linear unit)
    Strat iesire:   10 neuroni iesire; functia de transfer softmax"""
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dense(10, activation='softmax'))

"""Se configureaza modelul:
    Algoritmul de optimizare - Adam
    Functie de minimizare cost - entropie incrucisata categoric
    Modul de etalonare a erorii - dupa acuratete"""
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

"""Se antreneaza reteaua neuronala."""
model.fit(x_train, y_train, epochs=5)

"""Se verifica performanta modelului actual."""
val_loss, val_acc = model.evaluate(x_test, y_test)
print("Pierdere: "+str(val_loss))
print("Acuratete: "+str(val_acc))

"""Se salveaza modelul pe hard-disk."""
model.save('recunoastere_cifre.model')