from matplotlib.widgets import Slider
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import os
import csv
import time
from scipy.io import wavfile


matplotlib.use("TkAgg")


# **************************variaables*****************************
fig1=0
graph1, graph2, graph3="","",""
title1, title2, title3="","",""
no_channel =1
hide1,hide2,hide3= FALSE,FALSE,FALSE
stop1,stop2,stop3, stop_all1= FALSE,FALSE,FALSE, FALSE
pause1, pause2, pause3, pause_all1= FALSE, FALSE, FALSE, FALSE
count1,count2, count3=0,0,0
i1,i2,i3=0,0,0
zoom1, zoom2, zoom3=10,10,10
x_axis1, x_axis2, x_axis3 = [0], [0], [0]
data1, data2, data3 = [0], [0], [0]
data1r, data2r, data3r = FALSE, FALSE, FALSE
# **************************Methods********************************


def initialize_root(title, icon_path, size):
    # making main widget
    root = Tk()
    # set title for the widget
    root.title(title)
    # put icon on the title bar
    root.iconbitmap(icon_path)
    # set the size of the widget
    root.geometry(size)
    return root

def menu_bar(root):
    # create a toplevel menu
    menubar1 = Menu(root)
    # display the menu
    root.config(menu=menubar1)
    return menubar1


def open_file(channel_number, graph):
    global main_root, x_axis1, x_axis2, x_axis3, data1, data2, data3, title1, title2, title3
    main_root.filename = filedialog.askopenfilename(initialdir="E:/", title="select a file", filetypes=(("csv files", "* .csv"), ("png files", "* .png")))
    file_path, file_extension = os.path.splitext(main_root.filename)
    base = os.path.basename(file_path)
    if file_extension == ".csv":
        if channel_number ==1:
            title1 =os.path.splitext(base)[0]
            x_axis1, data1 = read_csv(main_root.filename)
            signal_view(x_axis1, data1, graph, title1,"yellow")
        if channel_number ==2:
            title2 =os.path.splitext(base)[0]
            x_axis2, data2 = read_csv(main_root.filename)
            signal_view(x_axis2, data2, graph, title2,"green")
        if channel_number ==3:
            title3 =os.path.splitext(base)[0]
            x_axis3, data3 = read_csv(main_root.filename)
            signal_view(x_axis3, data3, graph, title3,"red")
    elif file_extension == ".txt":
        if channel_number == 1:
            title1 =os.path.splitext(base)[0]
            x_axis1, data1 = read_txt(main_root.filename)
            signal_view(x_axis1, data1, graph, title1, "yellow")
        if channel_number == 2:
            title2 = os.path.splitext(base)[0]
            x_axis2, data2 = read_txt(main_root.filename)
            signal_view(x_axis2, data2, graph, title2,"green")
        if channel_number == 3:
            title3 = os.path.splitext(base)[0]
            x_axis3, data3 = read_txt(main_root.filename)
            signal_view(x_axis3, data3, graph, title3,"red")
    elif file_extension == ".wav":
        if channel_number == 1:
            title1 =os.path.splitext(base)[0]
            x_axis1, data1 = read_wav(main_root.filename)
            signal_view(x_axis1, data1, graph, title1,"yellow")
        if channel_number == 2:
            title2 = os.path.splitext(base)[0]
            x_axis2, data2 = read_wav(main_root.filename)
            signal_view(x_axis2, data2, graph, title2, "green")
        if channel_number == 3:
            title3 = os.path.splitext(base)[0]
            x_axis3, data3 = read_wav(main_root.filename)
            signal_view(x_axis3, data3, graph, title3, "red")
    else:
        messagebox.showerror("error message", "not supported format")


def read_wav(path):
    sample_rate, y_axis = wavfile.read(path)
    x_axis = np.linspace(0, 200, len(y_axis))
    return x_axis, y_axis


def read_txt(path):
    y_axis = np.loadtxt(path)
    x_axis = np.linspace(0, 200, len(y_axis))
    return x_axis, y_axis


def read_csv(path):
    r = open (path, 'r')
    reader = csv.reader(r)
    y_axis = []
    for row in reader:
        y_axis.append(float(row[0]))
    x_axis = np.linspace(0, 200, len(y_axis))
    return x_axis, y_axis


def signal_view(x, data,graph, file_name, color):
    global zoom1, zoom2, zoom3,count1, count2, count3, data1r, data2r, data3r
    graph.clear()
    graph.set_facecolor("black")
    graph.grid(True, linewidth=0.5, color='white', linestyle='-')
    graph.plot(x, data, color, label=color)
    graph.title.set_text(file_name)
    graph.title.set_color("white")
    graph.set_ylim([np.amin(data) - (0.1 * np.amax(data)), np.amax(data) + (0.1 * np.amax(data))])
    graph.set_xlim([0, 10])
    canvas.draw()
    if np.array_equal(graph,graph1):
        zoom1 =10
        count1 =0
    elif np.array_equal(graph,graph2):
        zoom2 = 10
        count2 =0
    else:
        zoom3 =10
        count3 = 0
    if np.array_equal(data,data1):
        data1r = TRUE
    if np.array_equal(data,data2):
        data2r = TRUE
    if np.array_equal(data,data3):
        data3r = TRUE


def add_channel():
    global no_channel, graph1, graph2, graph3, graph4, graph5, fig1, canvas
    if no_channel == 1:
        fig1.clear()
        graph1 = fig1.add_subplot(211)
        graph1.title.set_text(title1)
        graph1.title.set_color("white")
        graph1.set_facecolor("black")
        graph1.grid(True, linewidth=0.5, color='white', linestyle='-')
        graph1.set_xlim([0, zoom1])
        if data1r == FALSE:
            graph1.set_ylim([0,10])
        else:
            graph1.set_ylim([np.amin(data1) - (0.1 * np.amax(data1)), np.amax(data1) + (0.1 * np.amax(data1))])
            graph1.plot(x_axis1,data1,'yellow', label="yellow")
        graph1.tick_params(axis="y", colors="white")
        graph1.tick_params(axis="x", colors="white")
        graph1.spines['bottom'].set_color('white')
        graph1.spines['left'].set_color('white')
        graph1.spines['right'].set_color('white')
        graph1.spines['top'].set_color('white')
        graph2 = fig1.add_subplot(212)
        graph2.title.set_text(title2)
        graph2.title.set_color("white")
        graph2.set_facecolor("black")
        graph2.grid(True, linewidth=0.5, color='white', linestyle='-')
        graph2.set_xlim([0, zoom2])
        if data2r == FALSE:
            graph2.set_ylim([0, 10])
        else:
            graph2.set_ylim([np.amin(data2) - (0.1 * np.amax(data2)), np.amax(data2) + (0.1 * np.amax(data2))])
            graph2.plot(x_axis2,data2,'green', label="green")
        graph2.tick_params(axis="y", colors="white")
        graph2.tick_params(axis="x", colors="white")
        graph2.spines['bottom'].set_color('white')
        graph2.spines['left'].set_color('white')
        graph2.spines['right'].set_color('white')
        graph2.spines['top'].set_color('white')
        no_channel = 2
    elif no_channel == 2:
        fig1.clear()
        graph1 = fig1.add_subplot(311)
        graph1.title.set_text(title1)
        graph1.title.set_color("white")
        graph1.set_facecolor("black")
        graph1.grid(True, linewidth=0.5, color='white', linestyle='-')
        graph1.set_xlim([0, zoom1])
        if data1r == FALSE:
            graph1.set_ylim([0, 10])
        else:
            graph1.set_ylim([np.amin(data1) - (0.1 * np.amax(data1)), np.amax(data1) + (0.1 * np.amax(data1))])
            graph1.plot(x_axis1,data1,'yellow', label="yellow")
        graph1.tick_params(axis="y", colors="white")
        graph1.tick_params(axis="x", colors="white")
        graph1.spines['bottom'].set_color('white')
        graph1.spines['left'].set_color('white')
        graph1.spines['right'].set_color('white')
        graph1.spines['top'].set_color('white')
        graph2 = fig1.add_subplot(312)
        graph2.title.set_text(title2)
        graph2.title.set_color("white")
        graph2.title.set_text(title2)
        graph2.title.set_color("white")
        graph2.set_facecolor("black")
        graph2.grid(True, linewidth=0.5, color='white', linestyle='-')
        graph2.set_xlim([0, zoom2])
        if data2r == FALSE:
            graph2.set_ylim([0, 10])
        else:
            graph2.set_ylim([np.amin(data2) - (0.1 * np.amax(data2)), np.amax(data2) + (0.1 * np.amax(data2))])
            graph2.plot(x_axis2,data2,'green', label="green")
        graph2.tick_params(axis="y", colors="white")
        graph2.tick_params(axis="x", colors="white")
        graph2.spines['bottom'].set_color('white')
        graph2.spines['left'].set_color('white')
        graph2.spines['right'].set_color('white')
        graph2.spines['top'].set_color('white')
        graph3 = fig1.add_subplot(313)
        graph3.set_facecolor("black")
        graph3.grid(True, linewidth=0.5, color='white', linestyle='-')
        graph3.set_xlim([0, zoom3])
        if data3r == FALSE:
            graph3.set_ylim([0, 10])
        else:
            graph3.set_ylim([np.amin(data3) - (0.1 * np.amax(data3)), np.amax(data3) + (0.1 * np.amax(data3))])
            graph3.plot(x_axis3,data3,'red', label="red")
        graph3.tick_params(axis="y", colors="white")
        graph3.tick_params(axis="x", colors="white")
        graph3.spines['bottom'].set_color('white')
        graph3.spines['left'].set_color('white')
        graph3.spines['right'].set_color('white')
        graph3.spines['top'].set_color('white')
        no_channel =3
    canvas.draw()


def play_sig(ch):
    global stop1,stop2, stop3 ,pause1 ,pause2, pause3, i1, i2, i3, x_axis1, x_axis2, x_axis3, data1, data2, data3
    if ch == 1:
        for i1 in range(i1, 200):
            if stop1 == TRUE:
                i1 = 0
                stop1 = FALSE
                return 0
            if ch != 1:
              return 0
            elif pause1 == FALSE and ch == 1:
                graph1.clear()
                graph1.set_facecolor("black")
                graph1.grid(True, linewidth=0.5, color='white', linestyle='-')
                graph1.title.set_text(title1)
                graph1.title.set_color("white")
                x_axis1 = np.linspace(0 - i1, 200 - i1, len(data1))
                graph1.set_xlim([0, zoom1])
                graph1.plot(x_axis1, data1, 'yellow', label="yellow")
                canvas.draw()
                main_root.update()
                time.sleep(0.05)
            else:
                pause1 = FALSE
                return 0
    if ch == 2:
        for i2 in range(i2, 200):
            if stop2 == TRUE:
                i2 = 0
                stop2 = FALSE
                return 0
            if ch != 2:
             return 0
            elif pause2 == FALSE and ch == 2:
                graph2.clear()
                graph2.set_facecolor("black")
                graph2.grid(True, linewidth=0.5, color='white', linestyle='-')
                graph2.title.set_text(title2)
                graph2.title.set_color("white")
                x_axis2 = np.linspace(0 - i2, 200 - i2, len(data2))
                graph2.set_xlim([0, zoom2])
                graph2.plot(x_axis2, data2, 'yellow', label="yellow")
                canvas.draw()
                main_root.update()
                time.sleep(0.05)
            else:
                pause2 = FALSE
                return 0
    if ch == 3:
        for i3 in range(i3, 200):
            if stop3 == TRUE:
                i3 = 0
                stop3 = FALSE
                return 0
            if ch != 3:
                return 0
            elif pause3 == FALSE and ch == 3:
                graph3.clear()
                graph3.set_facecolor("black")
                graph3.grid(True, linewidth=0.5, color='white', linestyle='-')
                graph3.title.set_text(title3)
                graph3.title.set_color("white")
                x_axis3 = np.linspace(0 - i3, 200 - i3, len(data3))
                graph3.set_xlim([0,zoom3])
                graph3.plot(x_axis3, data3, 'red', label="red")
                canvas.draw()
                main_root.update()
                time.sleep(0.05)
            else:
                pause3 = FALSE
                return 0


def pause_sig(ch):
    global pause1, pause2, pause3
    if ch == 1 :
        pause1 = TRUE
    if ch == 2 :
        pause2 = TRUE
    if ch == 3 :
        pause3 = TRUE


def stop_sig(ch):
    global stop1, stop2, stop3, x_axis1,x_axis2,x_axis3, data2 , data1, data3
    if ch == 1:
        x_axis1 = np.linspace(0, 200 , len(data1))
        graph1.clear()
        graph1.set_xlim([0, 10])
        graph1.set_facecolor("black")
        graph1.grid(True, linewidth=0.5, color='white', linestyle='-')
        graph1.title.set_text(title1)
        graph1.title.set_color("white")
        graph1.plot(x_axis1,data1,'yellow', label="yellow")
        canvas.draw()
        stop1 = TRUE
    if ch == 2:
        x_axis2 = np.linspace(0 , 200 , len(data2))
        graph2.clear()
        graph2.set_xlim([0, 10])
        graph2.set_facecolor("black")
        graph2.grid(True, linewidth=0.5, color='white', linestyle='-')
        graph2.title.set_text(title2)
        graph2.title.set_color("white")
        graph2.plot(x_axis2, data2, 'green', label="green")
        canvas.draw()
        stop2=TRUE
    if ch == 3:
        x_axis3 = np.linspace(0 , 200 , len(data3))
        graph3.clear()
        graph3.set_xlim([0, 10])
        graph3.set_facecolor("black")
        graph3.grid(True, linewidth=0.5, color='white', linestyle='-')
        graph3.title.set_text(title3)
        graph3.title.set_color("white")
        graph3.plot(x_axis3, data3, 'red', label="red")
        canvas.draw()
        stop3 = TRUE


def channel(x):
    global hide1, hide2, hide3, data1, data2, data3
    if x ==1 :
        if hide1 == FALSE:
            graph1.clear()
            graph1.grid(True, linewidth=0.5, color='white', linestyle='-')
            graph1.set_xlim([0, 10])
            if data1r == FALSE:
                graph1.set_ylim([0,10])
            else:
                graph1.set_ylim([np.amin(data1)-(0.1*np.amax(data1)), np.amax(data1)+(0.1*np.amax(data1))])
            hide1 = TRUE
        else:
            graph1.plot(x_axis1,data1,'yellow', label="yellow")
            graph1.title.set_text(title1)
            graph1.title.set_color("white")
            hide1 = FALSE
    elif x ==2:
        if hide2 == FALSE:
            graph2.clear()
            graph2.grid(True, linewidth=0.5, color='white', linestyle='-')
            graph2.set_xlim([0, 10])
            if data2r ==FALSE:
                graph2.set_ylim([0,10])
            else:
                graph2.set_ylim([np.amin(data2) - (0.1 * np.amax(data2)), np.amax(data2) + (0.1 * np.amax(data2))])
            hide2 = TRUE
        else:
            graph2.plot(x_axis2,data2,'green', label="green")
            graph2.title.set_text(title2)
            graph2.title.set_color("white")
            hide2 = FALSE
    else:
        if hide3 == FALSE:
            graph3.clear()
            graph3.grid(True, linewidth=0.5, color='white', linestyle='-')
            graph3.set_xlim([0, 10])
            if data3r == FALSE:
                graph3.set_ylim([0,10])
            else:
                graph3.set_ylim([np.amin(data3) - (0.1 * np.amax(data3)), np.amax(data3) + (0.1 * np.amax(data3))])
            hide3 = TRUE
        else:
            graph3.plot(x_axis3,data3,'red', label="red")
            graph3.title.set_text(title3)
            graph3.title.set_color("white")
            hide3 = FALSE
    canvas.draw()

def clear_sig(channel_number):
    global data1, data2, data3, zoom1, zoom2, zoom3, count1, count2, count3, data1r, data2r, data3r
    if channel_number == 1:
        data1 = 0
        data1r = FALSE
        graph1.clear()
        graph1.set_facecolor("black")
        graph1.grid(True, linewidth=0.5, color='white', linestyle='-')
        graph1.set_ylim([0,10])
        graph1.set_xlim([0, 10])
        zoom1 = 10
        count1 = 0
    elif channel_number == 2:
        data2 = 0
        data2r = FALSE
        graph2.clear()
        graph2.set_facecolor("black")
        graph2.grid(True, linewidth=0.5, color='white', linestyle='-')
        graph2.set_ylim([0,10])
        graph2.set_xlim([0, 10])
        zoom2 = 0
        count2 =0
    else:
        data3 = 0
        data3r = FALSE
        graph3.clear()
        graph3.set_facecolor("black")
        graph3.grid(True, linewidth=0.5, color='white', linestyle='-')
        graph3.set_ylim([0,10])
        graph3.set_xlim([0, 10])
        zoom3 =0
        count3 =0
    canvas.draw()

def quit1():
    main_root.destroy()

def zoom_in():
    global zoom1, zoom2, zoom3, count1, count2, count3
    if no_channel == 1:
        if zoom1 > 3:
            graph1.set_xlim([0, zoom1-3])
            zoom1 = zoom1-3
            count1= count1-1
    if no_channel == 2:
        if zoom2 >3:
            graph1.set_xlim([0, zoom1-3])
            graph2.set_xlim([0, zoom2-3])
            zoom1 = zoom1 - 3
            zoom2 = zoom2 -3
            count1 = count1 -1
            count2 = count2 -1
        elif zoom2 < 3 and zoom1 >3:
            graph1.set_xlim([0, zoom1 - 3])
            zoom1 = zoom1 - 3
            count1 = count1 -1

    if no_channel == 3:
        if zoom3 >3:
            graph1.set_xlim([0, zoom1 - 3])
            graph2.set_xlim([0, zoom2 - 3])
            graph3.set_xlim([0, zoom3 -3])
            zoom1 = zoom1 -3
            zoom2 = zoom2  -3
            zoom3 = zoom3 -3
            count1 = count1 -1
            count2 = count2 -1
            count3 = count3 -1
        elif zoom3<3 and zoom2 >3 and zoom1>3:
            graph1.set_xlim([0, zoom1 - 3])
            graph2.set_xlim([0, zoom2 - 3])
            zoom1 = zoom1 - 3
            zoom2 = zoom2 - 3
            count1 = count1 - 1
            count2 = count2 - 1
        elif zoom3 <3 and zoom2<3 and zoom1>3:
            graph1.set_xlim([0, zoom1 - 3])
            zoom1 = zoom1 - 3
            count1 = count1 - 1
    canvas.draw()

def zoom_out():
    global zoom1, zoom2, zoom3, count1, count2, count3
    if no_channel == 1:
        graph1.set_xlim([0, zoom1 + 3])
        zoom1 = zoom1+3
        count1 = count1 +1
    if no_channel == 2:
        graph1.set_xlim([0, zoom1 + 3])
        graph2.set_xlim([0, zoom2 + 3])
        zoom1 = zoom1+3
        zoom2= zoom2 +3
        count1 = count1 +1
        count2 = count2 +1
    if no_channel == 3:
        graph1.set_xlim([0, zoom1 + 3])
        graph2.set_xlim([0, zoom2 + 3])
        graph3.set_xlim([0, zoom3 + 3])
        zoom1 = zoom1 + 3
        zoom2 = zoom2 + 3
        zoom3 = zoom3 +3
        count1 = count1 +1
        count2 = count2+1
        count3 = count3+1
    canvas.draw()


def pan_right():
    global zoom1, zoom2, zoom3
    if no_channel == 1:
        if  zoom1 < 200:
            graph1.set_xlim([(zoom1-10-(count1*3))+1, zoom1 + 1])
            zoom1 = zoom1+1
    if no_channel ==2:
        if zoom1 < 200:
            graph1.set_xlim([(zoom1 -10 - (count1 * 3)) + 1, zoom1 + 1])
            graph2.set_xlim([(zoom2 -10 - (count2 * 3)) + 1, zoom2 + 1])
            zoom1 = zoom1 +1
            zoom2 = zoom2 +1
        elif zoom1 > 200 and zoom2 < 200:
            graph2.set_xlim([(zoom2-10 - (count2 * 3)) + 1, zoom2 + 1])
            zoom2 = zoom2 +1
    if no_channel ==3:
        if zoom1 < 200 :
            graph1.set_xlim([(zoom1-10 - (count1 * 3)) + 1, zoom1 + 1])
            graph2.set_xlim([(zoom2 -10- (count2 * 3)) + 1, zoom2 + 1])
            graph3.set_xlim([(zoom3 -10- (count3 * 3)) + 1, zoom3 + 1])
            zoom1 = zoom1 + 1
            zoom2 = zoom2 + 1
            zoom3 = zoom3 +1
        elif zoom1 >200 and zoom2 <200 and zoom3 <200:
            graph2.set_xlim([(zoom2-10 - (count2 * 3)) + 1, zoom2 + 1])
            graph3.set_xlim([(zoom3 -10 - (count3 * 3)) + 1, zoom3 + 1])
            zoom2 = zoom2 + 1
            zoom3 = zoom3 + 1
        elif zoom1 >200 and zoom2 >200 and zoom3 <200:
            graph3.set_xlim([(zoom3 -10-( count3 * 3)) + 1, zoom3 + 1])
            zoom3 = zoom3 +1
    canvas.draw()

def pan_left():
    global zoom1, zoom2, zoom3
    if no_channel == 1:
        if zoom1 < 200:
            graph1.set_xlim([(zoom1 -10-( count1 * 3)) - 1, zoom1 - 1])
            zoom1 = zoom1 - 1
    if no_channel == 2:
        if zoom1 < 200:
            graph1.set_xlim([(zoom1 -10- (count1 * 3)) - 1, zoom1 - 1])
            graph2.set_xlim([(zoom2 -10- (count2 * 3)) - 1, zoom2 - 1])
            zoom1 = zoom1 - 1
            zoom2 = zoom2 -1
        elif zoom1 > 200 and zoom2 < 200:
            graph2.set_xlim([(zoom2 -10- (count2 * 3)) - 1, zoom2 - 1])
            zoom2 = zoom2 - 1
    if no_channel == 3:
        if zoom1 < 200:
            graph1.set_xlim([(zoom1 -10- (count1 * 3)) - 1, zoom1 - 1])
            graph2.set_xlim([(zoom2 -10- (count2 * 3)) - 1, zoom2 - 1])
            graph3.set_xlim([(zoom3 -10- (count3 * 3)) - 1, zoom3 - 1])
            zoom1 = zoom1 - 1
            zoom2 = zoom2 - 1
            zoom3 = zoom3 - 1
        elif zoom1 > 200 and zoom2 < 200 and zoom3 < 200:
            graph2.set_xlim([(zoom2 -10- (count2 * 3)) - 1, zoom2 - 1])
            graph3.set_xlim([(zoom3 -10- (count3 * 3)) - 1, zoom3 - 1])
            zoom2 = zoom2 - 1
            zoom3 = zoom3 - 1
        elif zoom1 > 200 and zoom2 > 200 and zoom3 < 200:
            graph3.set_xlim([(zoom3 -10- (count3 * 3)) - 1, zoom3 - 1])
            zoom3 = zoom3 -1
    canvas.draw()


def play_all ():
    global stop_all1, pause_all1, i1, i2, i3, x_axis1, x_axis2, x_axis3, data1, data2, data3, zoom1, zoom2, zoom3, graph2, graph1, graph3
    for x in range(1, 200):
        i1=x
        i2=x
        i3=x
        if stop_all1 == TRUE:
            i1 ,i2, i3 = 0,0,0
            stop_all1 = FALSE
            return 0
        elif pause_all1 == FALSE and no_channel == 1:
            graph1.clear()
            graph1.set_facecolor("black")
            graph1.grid(True, linewidth=0.5, color='white', linestyle='-')
            graph1.title.set_text(title1)
            graph1.title.set_color("white")
            if data1r == TRUE:
                x_axis1 = np.linspace(0 - i1, 200 - i1, len(data1))
                graph1.set_xlim([0, zoom1])
                graph1.plot(x_axis1, data1, 'yellow', label="yellow")
            else :
                i1 = i1 -1
        elif pause_all1 == FALSE and no_channel ==2:
            graph1.clear()
            graph1.set_facecolor("black")
            graph1.grid(True, linewidth=0.5, color='white', linestyle='-')
            graph1.title.set_text(title1)
            graph1.title.set_color("white")
            graph2.clear()
            graph2.set_facecolor("black")
            graph2.grid(True, linewidth=0.5, color='white', linestyle='-')
            graph2.title.set_text(title2)
            graph2.title.set_color("white")
            if data1r == TRUE:
                x_axis1 = np.linspace(0 - i1, 200 - i1, len(data1))
                graph1.set_xlim([0, zoom1])
                graph1.plot(x_axis1, data1, 'yellow', label="yellow")
            else:
                i1 = i1 - 1
            if data2r == TRUE:
                x_axis2 = np.linspace(0 - i2, 200 - i2, len(data2))
                graph2.set_xlim([0, zoom2])
                graph2.plot(x_axis2, data2, 'yellow', label="yellow")
            else:
                i2 = i2 - 1
        elif pause_all1 == FALSE and no_channel == 3:
            graph1.clear()
            graph1.set_facecolor("black")
            graph1.grid(True, linewidth=0.5, color='white', linestyle='-')
            graph1.title.set_text(title1)
            graph1.title.set_color("white")
            graph2.clear()
            graph2.set_facecolor("black")
            graph2.grid(True, linewidth=0.5, color='white', linestyle='-')
            graph2.title.set_text(title2)
            graph2.title.set_color("white")
            graph3.clear()
            graph3.set_facecolor("black")
            graph3.grid(True, linewidth=0.5, color='white', linestyle='-')
            graph3.title.set_text(title3)
            graph3.title.set_color("white")
            if data1r == TRUE:
                x_axis1 = np.linspace(0 - i1, 200 - i1, len(data1))
                graph1.set_xlim([0, zoom1])
                graph1.plot(x_axis1, data1, 'yellow', label="yellow")
            else:
                i1 = i1 - 1
            if data2r == TRUE:
                x_axis2 = np.linspace(0 - i2, 200 - i2, len(data2))
                graph2.set_xlim([0, zoom2])
                graph2.plot(x_axis2, data2, 'yellow', label="yellow")
            else:
                i2 = i2 - 1
            if data3r == TRUE:
                x_axis3 = np.linspace(0 - i3, 200 - i3, len(data3))
                graph3.set_xlim([0, zoom3])
                graph3.plot(x_axis3, data3, 'yellow', label="yellow")
            else:
                i3 = i3 - 1
        else:
            pause_all1 = FALSE
            return 0
        canvas.draw()
        main_root.update()
        time.sleep(0.05)

def stop_all ():
    global x_axis1, x_axis2, x_axis3
    global stop_all1
    stop_all1 = TRUE
    graph1.clear()
    graph1.set_facecolor("black")
    graph1.grid(True, linewidth=0.5, color='white', linestyle='-')
    graph1.title.set_text(title1)
    graph1.title.set_color("white")
    graph1.set_xlim([0, zoom1])
    x_axis1 = np.linspace(0 - i1, 200 - i1, len(data1))
    graph1.plot(x_axis1, data1, 'yellow', label="yellow")
    graph2.clear()
    graph2.set_facecolor("black")
    graph2.grid(True, linewidth=0.5, color='white', linestyle='-')
    graph2.title.set_text(title2)
    graph2.title.set_color("white")
    graph2.set_xlim([0, zoom2])
    x_axis2 = np.linspace(0 - i2, 200 - i2, len(data2))
    graph2.plot(x_axis2, data2, 'green', label="green")
    graph3.clear()
    graph3.set_facecolor("black")
    graph3.grid(True, linewidth=0.5, color='white', linestyle='-')
    graph3.title.set_text(title3)
    graph3.title.set_color("white")
    graph3.set_xlim([0, zoom3])
    x_axis3 = np.linspace(0 - i3, 200 - i3, len(data3))
    graph3.plot(x_axis3, data3, 'red', label="red")
    canvas.draw()

def pause_all ():
    global pause_all1
    pause_all1 = TRUE

# ****************************APP***********************************************************************************************************

main_root = initialize_root("Signal Viewer","sv.ico",size="500x500")


# create a toplevel menu
menubar  = menu_bar(main_root)

# add file menu
fileMenu = Menu(menubar)
menubar.add_cascade(label="File", menu=fileMenu)

# make sub menu for open & clear
openMenu = Menu(fileMenu)
fileMenu.add_cascade(label="Open", menu= openMenu)
openMenu.add_command(label="CH1", command=lambda :open_file(1, graph1))
openMenu.add_command(label="CH2",command=lambda :open_file(2, graph2))
openMenu.add_command(label="CH3",command=lambda :open_file(3, graph3))

# make sub menu for open & clear
clearMenu = Menu(fileMenu)
fileMenu.add_cascade(label="Clear", menu= clearMenu)
clearMenu.add_command(label="CH1", command=lambda :clear_sig(1))
clearMenu.add_command(label="CH2", command=lambda :clear_sig(2))
clearMenu.add_command(label="CH3", command=lambda :clear_sig(3))


fileMenu.add_command(label="Quit", command=quit1)




# add tool menu
toolMenu = Menu(menubar)
menubar.add_cascade(label="Tool", menu=toolMenu)
playMenu = Menu (toolMenu)
toolMenu.add_cascade(label="Play",menu=playMenu)
playMenu.add_command(label="CH1", command=lambda :play_sig(1))
playMenu.add_command(label="CH2", command=lambda :play_sig(2))
playMenu.add_command(label="CH3", command=lambda :play_sig(3))

pauseMenu = Menu (toolMenu)
toolMenu.add_cascade(label="Pause",menu=pauseMenu)
pauseMenu.add_command(label="CH1", command=lambda :pause_sig(1))
pauseMenu.add_command(label="CH2", command=lambda :pause_sig(2))
pauseMenu.add_command(label="CH3", command=lambda :pause_sig(3))

stopMenu = Menu (toolMenu)
toolMenu.add_cascade(label="Stop", menu=stopMenu)
stopMenu.add_command(label="CH1", command=lambda :stop_sig(1))
stopMenu.add_command(label="CH2", command=lambda :stop_sig(2))
stopMenu.add_command(label="CH3", command=lambda :stop_sig(3))







# add edit menu
editMenu = Menu(menubar)
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Language")
editMenu.add_command(label="Display mode")

# Create toolbar
toolbar = Frame(main_root, bg="grey")

# Create play button
play = Button(toolbar, text="Play", command = play_all)
play.grid(row=0, column=0)
# Create play button
pause = Button(toolbar, text="Pause",command =pause_all)
pause.grid(row=0, column=1)
# Create play button
stop = Button(toolbar, text="Stop", command = stop_all)
stop.grid(row=0, column=2)
# create button for add new channels
add = Button(toolbar, text="+", command=add_channel)
add.grid(row=0, column=3)
toolbar.pack(side=TOP, fill=X)

# Create play button
channel1 = Button(toolbar, text="Channel 1", command=lambda :channel(1))
channel1.grid(row=0, column=4)
# Create play button
channel2 = Button(toolbar, text="Channel 2", command=lambda :channel(2))
channel2.grid(row=0, column=5)
# Create play button
channel3 = Button(toolbar, text="Channel 3", command=lambda :channel(3))
channel3.grid(row=0, column=6)

zoomIn = Button(toolbar, text="zoom in", command=zoom_in)
zoomIn.grid(row=0, column=7)
zoomOut = Button(toolbar, text="zoom out", command=zoom_out)
zoomOut.grid(row=0, column=8)


panRight = Button(toolbar, text="pan right", command=pan_right)
panRight.grid(row=0, column=9)
panLeft = Button(toolbar, text="pan left", command=pan_left)
panLeft.grid(row=0, column=10)

# ***************************create figure and canvas*****************************
# Create figure to put graph on it
fig1 = Figure( dpi=100, facecolor="white", edgecolor="black")
fig1.set_facecolor("black")
graph1 = fig1.add_subplot(111)
graph1.set_facecolor("black")
graph1.grid(True, linewidth=0.5, color='white', linestyle='-')
graph1.set_xlim([0, 10])
graph1.set_ylim([0, 10])
graph1.tick_params(axis="y",colors="white" )
graph1.tick_params(axis="x",colors="white" )
graph1.spines['bottom'].set_color('white')
graph1.spines['left'].set_color('white')
graph1.spines['right'].set_color('white')
graph1.spines['top'].set_color('white')



# Create canvas widget to put figure on it
canvas = FigureCanvasTkAgg(fig1, master=main_root)
canvas.draw()
canvas.get_tk_widget().pack(side=BOTTOM, fill = BOTH,expand = TRUE)
main_root.mainloop()

