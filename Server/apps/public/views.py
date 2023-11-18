from django.shortcuts import render
from Server.Core import Connector
from django.http import JsonResponse
import base64
from time import time_ns, time

#In order to send audio file as JSON response I need to encode it into base64.

#robo_nav = RPS()
program = Connector.connect()

"""
def robot_control(request): # deals with the functions that give control over client using js etc.
    if request.method == 'POST':
        if 'reset' in request.POST.keys():
            robo_nav.reset()
            return JsonResponse({})

        else:
            receiving_time, sending_time = float(time_ns()), float(request.POST['sendingTime'])*1000000

            time_difference = round((receiving_time - sending_time)/1000000)
            print(1, time_difference, sending_time, receiving_time)
            angle, distance = robo_nav.run(time_difference)

            data = {'Angle':angle, 'Distance':distance}
            # request contains the data from the robot. I need to process that with local info
            # and triangulate. A triangulation object! of course!

            return JsonResponse(data)

    else: return render(request, 'Robot.html')
"""



def dialogue(request): #deals with the dialogue/voice etc.
    command = request.POST['command']

    unprocessed_text, audio_ = program.react(command) #returns the dialogue and the audio address
    encoded_audio = base64.b64encode(open(audio_[0], 'rb').read())

    text = {
        "content": str(unprocessed_text).replace('],', ']\n\n'),
        "type": "string/dialogue",
        "language": "en-US",
        }

    audio = {
        "content": str(encoded_audio)[2:].replace("'", ''), # replacing the { b'   ' } in the b64 encoding.
        'name': audio_[1],
        "type": "audio/mpeg",
        "language": "en-US",
        }

    data = {'text': text, 'audio': audio}

    return JsonResponse(data)


def homepage(request):
    return render(request, 'Homepage.html')