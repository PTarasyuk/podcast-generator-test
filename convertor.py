import os
import yaml
import eyed3
import time


# Get all audio files in the audio folder
def get_audio_files():
    audio_files = []
    for file in os.listdir('audio'):
        if file.endswith('.mp3'):
            # Load the audio file using eyed3
            audio_file = eyed3.load(os.path.join('audio', file))
            comments = ''
            # Get all comments in the audio file
            if audio_file.tag.comments:
                for comment in audio_file.tag.comments:
                    comments += comment.text
            # Get the duration of the audio file
            duration = time.strftime('%H:%M:%S', time.gmtime(audio_file.info.time_secs))
            # Get the size of the audio file
            size = os.path.getsize(os.path.join('audio', file))
            size_str = '{:,}'.format(size)
            # Add the audio file information to the list
            audio_files.append({
                'title': audio_file.tag.title,
                'descriptions': comments,
                'file': '/audio/' + file,
                'duration': duration,
                'length': size_str
            })
    return audio_files

# Convert the audio files to yaml
def convert_to_yaml():
    data = get_audio_files()
    yaml_data = yaml.dump(data, sort_keys=False)
    # Write the yaml data to a file
    with open('episodes.yaml', 'w') as file:
        file.write(yaml_data)

convert_to_yaml()