import pandas as pd

def read_file():
    # df = pd.read_csv("results.txt",sep='%10.4g' * 7, header=None)
    # print(df.head(1))
    with open("results.txt", "r") as file:
        lines = file.readlines()
        for l in lines:
            print(l)
            out = l.split('')
            for s in out:
                print('entrance:' +s )
            exit()


def main():
    read_file()


if __name__ == '__main__':
    main()
