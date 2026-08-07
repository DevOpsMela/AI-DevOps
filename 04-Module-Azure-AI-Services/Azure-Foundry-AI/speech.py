"""
For more samples please visit https://github.com/Azure-Samples/cognitive-services-speech-sdk
"""

import azure.cognitiveservices.speech as speechsdk

endpoint_url = "https://devops-openai-fdry.cognitiveservices.azure.com/"

from urllib.parse import urlparse

parsed = urlparse(endpoint_url)
base_endpoint = f"{parsed.scheme}://{parsed.netloc}"

speech_key = ""
speech_config = speechsdk.SpeechConfig(subscription=speech_key, endpoint=base_endpoint)
speech_config.speech_synthesis_voice_name = "en-US-Ava:DragonHDLatestNeural"

# use the default speaker as audio output.
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

text = "Hello, Rohit! What are you doing today?"

result = speech_synthesizer.speak_text_async(text).get()
# Check result
if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesized for text [{}]".format(text))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error details: {}".format(cancellation_details.error_details))
