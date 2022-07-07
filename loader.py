import numpy as np
import os
import pandas as pd
import tensorflow as tf



class Create_datasets:
    
    def __init__(self,train, eval, dev):
        self.train_names = train
        self.eval_names = eval
        self.dev_names = dev
        self.load_train()
    
    def get_spectogram(self, wav_file):

        # An integer scalar Tensor. The window length in samples.
        frame_length = 256
        # An integer scalar Tensor. The number of samples to step.
        frame_step = 160
        # An integer scalar Tensor. The size of the FFT to apply.
        # If not provided, uses the smallest power of 2 enclosing frame_length.
        fft_length = 384

        file = tf.io.read_file(wav_file+".wav")
    # 2. Decode the wav file
        audio, _ = tf.audio.decode_wav(file)
        audio = tf.squeeze(audio, axis=-1)
        audio = audio.numpy()
        return audio

    def load_train(self):
        dir = os.path.join(os.path.abspath("."),"rodigits")
        with open(os.path.join(dir,self.train_names),"r") as f:
            train_files = f.read().split("\n")
        for i in train_files:
            try:
                voice = os.path.join(dir,i)
                spectogram = self.get_spectogram(voice)
                print(type(spectogram))
            except Exception as e:
                print(str(e))
                continue
            
