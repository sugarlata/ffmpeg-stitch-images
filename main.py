import os
import json





def main():

    with open('config.json') as f:
        config = json.load(f)

    command = config['ffmpeg-command'] % (
        'jpg',
        'output'
    )

    print(command)

    os.chdir("images/")
    os.system(command)


if __name__ == '__main__':

    main()
