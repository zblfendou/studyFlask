import numpy as np
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model


def extract_features(img_path):
    # 加载预训练的 VGG16 模型，不包含全连接层
    base_model = VGG16(weights='imagenet', include_top=False)
    model = Model(inputs=base_model.input, outputs=base_model.get_layer('block5_pool').output)

    # 加载并预处理图像
    img = image.load_img(img_path, target_size=(224, 224))
    img_data = image.img_to_array(img)
    img_data = np.expand_dims(img_data, axis=0)
    img_data = preprocess_input(img_data)

    # 提取特征
    features = model.predict(img_data)
    return features


def feature_similarity(img1_path, img2_path):
    # 提取两张图片的特征
    features1 = extract_features(img1_path)
    features2 = extract_features(img2_path)

    # 计算特征的余弦相似度
    similarity = np.dot(features1.flatten(), features2.flatten()) / (
                np.linalg.norm(features1) * np.linalg.norm(features2))
    return similarity


similarity_score = feature_similarity('static/1.jpeg', 'static/2.jpeg')
print(f"两张图片的特征相似度为: {similarity_score}")
