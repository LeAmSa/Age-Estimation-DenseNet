from tensorflow.keras.applications.densenet import DenseNet201
from tensorflow.keras.layers import Dense, Dropout, GlobalAveragePooling2D
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam

#7, 4 e 2 for the experiments
CLASSES = 4

base_model = DenseNet201(weights='imagenet', include_top=False, input_shape = (200,200,3))

x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dropout(0.5)(x)
predictions = Dense(CLASSES, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=predictions)

#training all the layers
for layer in base_model.layers:
  layer.trainable = True

#model compiling  
model.compile(optimizer=optimizers.Adam(lr=0.0001), loss='categorical_crossentropy', metrics=['acc'])