from EmotionDetection.emotion_detection import emotion_detector

# Define the text to analyze
text_to_analyze = "I hate working long hours."

# Run the detection
result = emotion_detector(text_to_analyze)

# Display the results

print(f"Input: {text_to_analyze}")
print(f"Output: {result}")
