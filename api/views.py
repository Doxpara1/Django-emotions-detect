from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer

from textblob import TextBlob
from nrclex import NRCLex



class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


    def detect_emotions(self, text):
        # Analyze basic sentiment using TextBlob
        blob = TextBlob(text)
        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)

        # Analyze emotions using NRC Emotion Lexicon
        emotion = NRCLex(text)
        emotion_scores = emotion.raw_emotion_scores

        if not emotion_scores:
            emotion_summary = "No strong emotion detected."
            dominant_emotion = None
        else:
            # Find dominant emotion
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)
            emotion_summary = f"The dominant emotion is **{dominant_emotion}** with contributing emotions: " + \
                            ", ".join([f"{k} ({v})" for k, v in emotion_scores.items()])

        self.result = dominant_emotion
        return self.result


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Extract x, y as strings (convert if needed)
        x = str(serializer.validated_data['sentence'])

        # passing the value to function
        emotions =  self.detect_emotions(x)
        instance = serializer.save(emotions=emotions)
        output_serializer = self.get_serializer(instance)
        headers = self.get_success_headers(output_serializer.data)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED, headers=headers)