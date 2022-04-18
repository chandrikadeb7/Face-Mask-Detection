#This is training code for age detection model
#Currently, mean ablsoute error value is about ±30 age which is so big

# Also, the problem that I faced with the Github is uploading age_gender.csv file to master branch because it was almost 199 mb.
# And github says I should upload via Github LFS which is not possible with my laptop(Error is "fatal: cannot exec 'git-lfs': Bad CPU type in executable")
# Then I just shared age_gender.csv file on Google Drive. The Link is:
AGE_CSV = "https://drive.google.com/file/d/1iuWUN-Cy_wynFTnhOv4OfJkOG80o3NOf/view?usp=sharing"


#Import libraries
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn import model_selection

#This is CNN model
def sequential_model():
	my_model = tf.keras.Sequential()
	my_model.add(tf.keras.layers.InputLayer(input_shape=(48,48,1)))
	my_model.add(tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
	my_model.add(tf.keras.layers.BatchNormalization())
	my_model.add(tf.keras.layers.MaxPooling2D((2, 2)))
	my_model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu'))
	my_model.add(tf.keras.layers.MaxPooling2D((2, 2)))
	my_model.add(tf.keras.layers.Conv2D(128, (3, 3), activation='relu'))
	my_model.add(tf.keras.layers.MaxPooling2D((2, 2)))
	my_model.add(tf.keras.layers.Conv2D(256, (3, 3), activation='relu'))
	my_model.add(tf.keras.layers.MaxPooling2D((2, 2)))
	my_model.add(tf.keras.layers.Flatten())
	my_model.add(tf.keras.layers.Dense(64, activation='relu'))
	my_model.add(tf.keras.layers.Dropout(rate=0.5))
	my_model.add(tf.keras.layers.Dense(1, activation='relu'))
	return my_model

def pixel_to_array(column_name):
	data[column_name] = data[column_name].apply(lambda each: np.array(each.split(), dtype = "float32"))
	image_3D = np.array(data[column_name].tolist())
	image_3D= image_3D.reshape(image_3D.shape[0],48,48,1)
	return image_3D

#Path for csv file
PATH = "age_gender.csv"

#Reading csv file with pandas
print("Reading data...")
data = pd.read_csv(PATH)
print(data.head(10))
print("Data printed successfully!")

data.pixels = np.asarray(data.pixels)

#We need to convert pixels to array and reshape it to 3d array
image = pixel_to_array("pixels")

age = data.age

train_X, test_X, train_y, test_y = model_selection.train_test_split(image, age,test_size = 0.30)

model = sequential_model()

model.compile(optimizer='sgd',loss='mean_squared_error')

history = model.fit(train_X, train_y, epochs = 10)

print("Final test result is: " + str(model.evaluate(test_X,test_y)[1]) + " mean absloute error")
