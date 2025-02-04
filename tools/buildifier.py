# Required: go install github.com/bazelbuild/buildtools/buildifier@latest
import glob
import os


TARGETS = [
    'WORKSPACE',
    'BUILD',
    'tabio/**/BUILD',
    'tools/**/BUILD',
]


def main():
    project_root = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
    for target in TARGETS:
        for f in glob.glob(os.path.join(project_root, target), recursive=True):
            cmd = F'buildifier {f}'
            print(cmd)
            os.system(cmd)


if __name__ == '__main__':
    main()
