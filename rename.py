import os


def main(ext="jpg"):

    os.chdir('images')
    files = [(os.getcwd(), x) for x in os.listdir() if x[-3:] == 'jpg']

    for x, file_tuple in enumerate(files):
        cwd = file_tuple[0]
        old_fn = file_tuple[1]
        new_fn = "%05d.jpg" % x

        old_file = os.path.join(cwd, old_fn)
        new_file = os.path.join(cwd, new_fn)

        os.rename(old_file, new_file)






if __name__ == '__main__':

    main()