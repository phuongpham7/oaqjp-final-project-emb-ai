import requests
import json

def emotion_detector(text_to_analyze):
    # config url and header
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # construct the payload
    payload = {"raw_document": {"text": text_to_analyze}}

    # send the POST request to the service
    response = requests.post(url, json=payload, headers=header)

    # convert the response text into a dictionary
    dictionary_response = json.loads(response.text)

    # extract the emotion scores
    emotions = dictionary_response['emotionPredictions'][0]['emotion']

    # assign each score
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    # find the dominant emotion
    emotion_list = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotion_list, key=emotion_list.get)

    # construct the output
    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }

    # return the formated result
    return result