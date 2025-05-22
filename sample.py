from textblob import TextBlob
from nrclex import NRCLex

# def detect_emotions(text):
#     # Analyze basic sentiment using TextBlob
#     blob = TextBlob(text)
#     polarity = round(blob.sentiment.polarity, 2)
#     subjectivity = round(blob.sentiment.subjectivity, 2)

#     # Analyze emotions using NRC Emotion Lexicon
#     emotion = NRCLex(text)
#     emotion_scores = emotion.raw_emotion_scores

#     if not emotion_scores:
#         emotion_summary = "No strong emotion detected."
#         dominant_emotion = None
#     else:
#         # Find dominant emotion
#         dominant_emotion = max(emotion_scores, key=emotion_scores.get)
#         emotion_summary = f"The dominant emotion is **{dominant_emotion}** with contributing emotions: " + \
#                           ", ".join([f"{k} ({v})" for k, v in emotion_scores.items()])

#     return {
#         "text": text,
#         "polarity": polarity,
#         "subjectivity": subjectivity,
#         "dominant_emotion": dominant_emotion,
#         "emotion_scores": emotion_scores,
#         "summary": emotion_summary
#     }

# result = detect_emotions("This boy is waiting for the bus.")
# print(result["dominant_emotion"])



def detect_emotions(text):
    blob = TextBlob(text)
    polarity = round(blob.sentiment.polarity, 2)
    subjectivity = round(blob.sentiment.subjectivity, 2)

    emotion = NRCLex(text)
    emotion_scores = emotion.raw_emotion_scores

    if not emotion_scores:
        dominant_emotion = None
    else:
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    return dominant_emotion


print(detect_emotions("this is bad"))