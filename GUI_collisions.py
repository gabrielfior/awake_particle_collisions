# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 00:11:09 2017

@author: gabrielfior
"""

#!/usr/bin/python
# -*- coding: iso-8859-1 -*-


#import matplotlib
#matplotlib.use('TkAgg')
import numpy as np
import Tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

from read_collisions import *
import plotly.plotly as py
from plotly.graph_objs import *

def randrange(n, vmin, vmax):
    '''
    Helper function to make an array of random numbers having shape (n, )
    with each number distributed Uniform(vmin, vmax).
    '''
    return (vmax - vmin)*np.random.rand(n) + vmin

class App:
    def __init__(self, master):
        # Create a container
        #frame = Tkinter.Frame(master)

        #############
        m = Tkinter.PanedWindow(orient=Tkinter.VERTICAL,height=500,width=500)
        m.pack(fill=Tkinter.BOTH, expand=1)

        top = Tkinter.Label(m)
        m.add(top)

        bottom = Tkinter.Label(m)
        m.add(bottom)
        ##############



        

        """
        fig = Figure()
        ax = fig.add_subplot(111)
        self.line, = ax.plot(range(10))

        self.canvas = FigureCanvasTkAgg(fig,master=master)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side='top', fill='none', expand=0.5)
        """
        df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
        trace1 = Scatter3d(
            x=df['year'][750:1500],
            y=df['continent'][750:1500],
            z=df['pop'][750:1500],
            text=df['country'][750:1500],
            mode='markers',
            marker=dict(
                sizemode='diameter',
                sizeref=750,
                size=df['gdpPercap'][750:1500],
                color = df['lifeExp'][750:1500],
                colorscale = 'Viridis',
                colorbar = dict(title = 'Life<br>Expectancy'),
                line=dict(color='rgb(140, 140, 170)')
            )
        )
        data=[trace1]
        layout=dict(height=800, width=800, title='Examining Population and Life Expectancy Over Time')
        self.fig=dict(data=data, layout=layout)
        py.iplot(self.fig)
        
        self.canvas = FigureCanvasTkAgg(self.fig,master=master)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side='top', fill='none', expand=0.5)
        self.ax.mouse_init()

        """
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        n = 100        
        
        for c, z1, zlow, zhigh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
            xs = randrange(n, 23, 32)
            ys = randrange(n, 0, 100)
            zs = randrange(n, zlow, zhigh)
            self.scatter = self.ax.scatter(xs, ys, zs, c=c, marker='o')        
        
        self.ax.set_xlabel('X Label')
        self.ax.set_ylabel('Y Label')
        self.ax.set_zlabel('Z Label')

        self.canvas = FigureCanvasTkAgg(self.fig,master=master)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side='top', fill='none', expand=0.5)
        self.ax.mouse_init()

        """
        # Create 2 buttons
        self.button_left = Tkinter.Button(m,text="< Decrease Slope",
                                        command=self.decrease)
        self.button_left.pack(side="left")
        self.button_right = Tkinter.Button(m,text="Plot from selections",
                                        command=self.plot_from_selection)
        self.button_right.pack(side="left")

        self.scrollbar = Tkinter.Scrollbar(m, orient=Tkinter.VERTICAL)
        self.listbox = Tkinter.Listbox(m,selectmode=Tkinter.MULTIPLE,
                                       yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        self.scrollbar.pack(side=Tkinter.RIGHT, fill='y')        
        self.listbox.pack()
        
        #Insert items in listbox
        list_tracks= return_tracks_with_second()
        #self.listbox.insert(Tkinter.END, "a list entry")
        
        #for item in ["one", "two", "three", "four"]:
        for item in list_tracks:            
            self.listbox.insert(Tkinter.END, item)



        ##############
        m.pack()

    def poll(self):
        now = self.list.curselection()
        if now != self.current:
            self.list_has_changed(now)
            self.current = now
        self.after(250, self.poll)

    def list_has_changed(self, selection):
        print "selection is", selection

    def backspace(event):
        event.widget.delete("%s-1c" % Tkinter.INSERT, Tkinter.INSERT)

    def decrease(self):
        x, y = self.line.get_data()
        self.line.set_ydata(y - 0.2 * x)
        self.canvas.draw()
        
    def OnPressEnter(self,event):
        self.labelVariable.set( self.entryVariable.get()+" (You pressed ENTER)" )


    def plot_from_selection(self):
        items = map(int, self.listbox.curselection())
        print items
        #plot all trajects

        ax = self.ax
        self.scatter.set_visible(False)         

        for item in items:
            pos_list_e,pos_list_gamma,pos_list_p=return_positions_track(int(item))
            array_e= np.array(pos_list_e)
            array_gamma= np.array(pos_list_e)                        
            array_proton= np.array(pos_list_e)                        
            #plot
            print 'clear fig'
            print array_e==[]
            print array_e.shape,array_e.shape[0]
            if array_e.shape[0]>0:
                ax.scatter(array_e[:,0], array_e[:,1], array_e[:,2], c='r', marker='*') 
            if array_gamma.shape[0]>0:
                ax.scatter(array_gamma[:,0], array_gamma[:,1], array_gamma[:,2], c='b', marker='o') 
            if array_proton.shape[0]>0:
                ax.scatter(array_proton[:,0], array_proton[:,1], array_proton[:,2], c='g', marker='*')             

        self.scatter.set_visible(True)         
            
        print 'done plot'

if __name__ == "__main__":
    root = Tkinter.Tk()
    root.geometry("500x580+600+400")
    app = App(root)
    root.mainloop()
