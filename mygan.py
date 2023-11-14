import tensorflow as tf
from keras import layers
from keras.initializers import RandomNormal
init = RandomNormal(mean=0.0, stddev=0.02, seed=23)
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

MAPS = 128
noise_dim = 128

def make_generator():
    seed = tf.keras.Input(shape=((noise_dim,)))
    label = tf.keras.Input(shape=((1,)))
    x = layers.Embedding(120, 120, input_length=1, name='emb')(label)
    x = layers.Flatten()(x)
    x = layers.concatenate([seed, x])
    x = layers.Dense(4 * 4 * MAPS * 8, use_bias=False)(x)
    x = layers.Reshape((4, 4, MAPS * 8))(x)
    x = layers.BatchNormalization()(x)
    x = layers.ReLU()(x)

    x = layers.Conv2DTranspose(MAPS * 4, (5, 5), strides=(2, 2), padding='same', kernel_initializer=init,
                               use_bias=False)(x)
    x = layers.BatchNormalization()(x)
    x = layers.ReLU()(x)

    x = layers.Conv2DTranspose(MAPS * 2, (5, 5), strides=(2, 2), padding='same', kernel_initializer=init,
                               use_bias=False)(x)
    x = layers.BatchNormalization()(x)
    x = layers.ReLU()(x)

    x = layers.Conv2DTranspose(MAPS, (5, 5), strides=(2, 2), padding='same', kernel_initializer=init, use_bias=False)(x)
    x = layers.BatchNormalization()(x)
    x = layers.ReLU()(x)

    x = layers.Conv2DTranspose(3, (5, 5), strides=(2, 2), padding='same', kernel_initializer=init, use_bias=False,
                               activation='tanh')(x)

    model = tf.keras.Model(inputs=[seed, label], outputs=x)
    model.load_weights(filepath='./generator_w.h5')
    return model


generator = make_generator()


def generate_latent_points(latent_dim, n_samples):
    return tf.random.truncated_normal((n_samples,latent_dim))


def genarate_100_dogs(index):
    seed = generate_latent_points(noise_dim, 100)
    labs = tf.cast(120*tf.random.uniform((100,1)),tf.int8)
    predictions = generator([seed,labs], training=False)
    # plt.figure(figsize=(20,20))
    # plt.subplots_adjust(wspace=0,hspace=0)
    # for k in range(100):
    #     plt.subplot(10,10,k+1)
    #     plt.imshow( (predictions[k,:,:,:]+1.)/2. )
    #     plt.axis('off')
    # plt.show()
    p = predictions[index]
    p = 255 * ((np.array(p) + 1.) / 2.)
    img = Image.fromarray(p[:, :, :].astype('uint8'))
    return img
