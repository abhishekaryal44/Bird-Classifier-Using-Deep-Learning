import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import os

# Disable GPU usage
tf.config.set_visible_devices([], 'GPU')


# # Provide the path to your saved model
print("Current working directory:", os.getcwd())

model_path = 'home/bird_classification_model.h5'
model = load_model(model_path)


class_labels=['Abbott’s Babbler',
 'Black Bittern',
 'Blue-eared Kingfisher',
 'Blue-naped Pitta',
 'Broad-billed Warbler',
 'Cheer Pheasant',
 'Chestnut Munia',
 'Cinereous Vulture',
 'Golden Babbler',
 'Goulds Shortwing ',
 'Great Bittern',
 'Great Hornbill',
 'Great Slaty Woodpecker',
 'Ibisbill',
 'Indian Courser',
 'Indian Grassbird',
 'Indian Nightjar',
 'Knob-billed Duck',
 'Northern Pintail',
 'Painted Stork',
 'Purple Cochoa',
 'Red-headed Trogon',
 'Red-headed Vulture ',
 'Red-necked Falcon',
 'Ruby-cheeked Sunbird',
 'Rusty-fronted',
 'Saker Falcon',
 'Silver-eared Mesia',
 'Slaty-legged Crake',
 'Spot-bellied Eagle Owl',
 'Sultan Tit',
 'Swamp Francolin ',
 'Tawny-bellied Babbler',
 'Thick-billed Green Pigeon ',
 'White-throated Bulbul',
 'White-throated Bushchat',
 'Yellow-rumped Honeyguide',
 'Yellow-vented Warbler']

# class_labels=['Abbott’s Babbler Malacocincla abbotti',
#  'Black Bittern (Dupetor flavicollis)',
#  'Blue-eared Kingfisher Alcedo meninting',
#  'Blue-naped Pitta Pitta nipalensis',
#  'Broad-billed Warbler Tickellia hodgsoni',
#  'Cheer Pheasant (Catreus wallichii)',
#  'Chestnut Munia Lonchura atricapilla',
#  'Cinereous Vulture Aegypius monachus',
#  'Golden Babbler Stachyris chrysaea',
#  'Goulds Shortwing Brachypteryx stellata',
#  'Great Bittern Botaurus stellaris',
#  'Great Hornbill (Buceros bicornis)',
#  'Great Slaty Woodpecker Mulleripicus pulverulentus',
#  'Ibisbill Ibidorhyncha struthersii',
#  'Indian Courser Cursorius coromandelicus',
#  'Indian Grassbird - Graminicola bengalensis',
#  'Indian Nightjar Caprimulgus asiaticus',
#  'Knob-billed Duck Sarkidiornis melanotos',
#  'Northern Pintail Anas acuta',
#  'Painted Stork Mycteria leucocephala',
#  'Purple Cochoa Cochoa purpurea',
#  'Red-headed Trogon Harpactes erythrocephalus',
#  'Red-headed Vulture Sarcogyps calvus',
#  'Red-necked Falcon Falco chicquera',
#  'Ruby-cheeked Sunbird Anthreptes singalensis',
#  'Rusty-fronted Barwing Actinodura egertoni',
#  'Saker Falcon Falco cherrug',
#  'Silver-eared Mesia Leiothrix argentauris',
#  'Slaty-legged Crake Rallina eurizonoides',
#  'Spot-bellied Eagle Owl Bubo nipalensis',
#  'Sultan Tit Melanochlora sultanea',
#  'Swamp Francolin Francolinus gularis',
#  'Tawny-bellied Babbler Dumetia hyperythra',
#  'Thick-billed Green Pigeon Treron curvirostra',
#  'White-throated Bulbul Alophoixus flaveolus',
#  'White-throated Bushchat Saxicola insignis',
#  'Yellow-rumped Honeyguide - Indicator xanthonotus',
#  'Yellow-vented Warbler Phylloscopus cantator']


from PIL import Image

def predictClassLabel(image):
    # Load and preprocess the image
    img = Image.open(image)
    img = img.resize((224, 224))  # Adjust the size based on your model's input size

    # Convert the image to an array
    img_array = np.array(img) / 255.0  # Normalize pixel values to be between 0 and 1
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    # Make predictions
    predictions = model.predict(img_array)

    # Assuming predictions is a one-hot encoded array, find the predicted class index
    predicted_class_index = np.argmax(predictions)

    # Print the predicted class label (replace 'class_labels' with your actual class labels)
    predicted_class_label = class_labels[predicted_class_index]
    print("Predicted Class Label:", predicted_class_label)
    return predicted_class_label

#to prevent the model loading when I am learning an API i have commented the above code with a dummy function

# the following code is just a dummy
# def predictClassLabel(image):
#     return "Dummy text"

