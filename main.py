# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import matplotlib.pyplot as plt

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    fileName = "2409_2021_04_16.json"
    dataArray = []
    file = open('./testdata/' + fileName, 'r')
    lines = file.readlines()
    for line in lines:
        if line.find(',') != -1:
            dataArray.append(float(line.split(',')[3]) )

    plt.plot(list(reversed(dataArray)))
    plt.ylabel('price')
    plt.show()

    file.close()
