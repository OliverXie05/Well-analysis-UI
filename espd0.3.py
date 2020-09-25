# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 15:55:49 2020

@author: xyf11
"""
from fluidcalc import *
from inflowcurve import *
import math
import pandas as pd
from tkinter import ttk, filedialog
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.pyplot
try:
    import tkinter as tk
    from tkinter import messagebox

except:
    import Tkinter as tk
    import tkMessageBox as messagebox
import pygubu
from tkinter import *
from tkinter.ttk import *
from ttkthemes import themed_tk as tkh
class MyApplication(object):

    def __init__(self, master):
        global uss_uo
        global uss_sim
        global uss_rm
        uss_uo = 1
        uss_sim = 0
        uss_rm = 0
        global v_a
        v_a = 0
        global gr
        gr = 0
        global use_c7
        use_c7 = 1
        global ugc
        ugc = 0
        global gc_ugc
        gc_ugc = 0
        global ci
        global pi
        global zi
        ci = 1
        pi = 1
        zi = 1
        builder = pygubu.Builder()
        builder.add_from_file('espd0.3.ui')
        self.mainwindow = builder.get_object('EspdPlus')
        global sec_counter
        global ifsec
        ifsec = 0
        sec_counter = 0
        global eq_counter
        global ifeq
        ifeq = 0
        eq_counter = 0
        global vogel
        vogel = 2
        self.notebook = builder.get_object('espd')
        self.flowline = builder.get_object('Flowline_3')
        flowline = builder.get_object('Flowline_3')
        notebook = builder.get_object('espd')
        self.fblank = builder.get_object('fblank')
        fblank = builder.get_object('fblank')
        self.forget = builder.get_object('forget')
        self.recover = builder.get_object('recover')
        self.tree = builder.get_object('tree')

#WellInfo
        self.cname = builder.get_object('cname_en')
        self.wname = builder.get_object('wname_en')
        self.fname = builder.get_object('fname_en')
        self.rname = builder.get_object('rname_en')
        self.loc = builder.get_object('loc_en')
        self.aname = builder.get_object('aname_en')
        self.notes = builder.get_object('notes_text')
        
#Tubulars
        self.cas = builder.get_object('casingt')
        self.tub = builder.get_object('tubingt')
        self.shr = builder.get_object('shroudt')
        self.sec_en = builder.get_object('secondary')
        self.wellbore = builder.get_object('wc_c')
        self.perforation = builder.get_object('perforation')
        self.perfunit = builder.get_object('top_c')
        self.secdepth = builder.get_object('secondary')
        self.depunit = builder.get_object('depth_c')
        self.temp = builder.get_object('rtemp')
        self.tempunit = builder.get_object('rtempunit')
        self.wellbore.configure(values = ['None Calculated', 'MONO modified (1986)', 'MONA (1986)','Mukherjee && Brill (1983)','Beggs && Brill (1973)'])
#Flowline
        self.pipe = builder.get_object('pipet')
        self.choke = builder.get_object('choket')
        self.datatemp = builder.get_object('datatemp')
        self.datatempunit = builder.get_object('datatemp_unit')
        self.datapre = builder.get_object('datapre')
        self.datapreunit = builder.get_object('datapre_unit')
        self.pcorrelation = builder.get_object('correlationbox')
        self.ccorrelation = builder.get_object('correlationbox_9')
        self.speheat = builder.get_object('speheat')
        self.heatunit = builder.get_object('heatunit')
        self.elev = builder.get_object('elev')
        self.pcorrelation.configure(values = ['Beggs && Brill','Beggs. Brill && Minami','Dukler','Gomez','MONA','MONA Modified','Mukherjee && Brill','Xiao e al Mechanistic','None Calculated'])
        self.ccorrelation.configure(values = ['No choke calculated','Perkins (1993) Critical & Subcritical','Ashford & Pierce (1975) Critical & Subcritical	','Sachdeva et. Al. (1986) Critical & Subcritical','API14B (1974) Subcritical only','Baxendell (1961) Critical only','Ros (1960) Critical only','Gilbert (1954) Critical only','Achong Critical only'])
#Fluid tab 1
        self.gore = builder.get_object('gore')
        self.goru = builder.get_object('gor_unit')
        self.glre = builder.get_object('glre')
        self.glru = builder.get_object('glr_unit')
        self.floge = builder.get_object('floge')
        self.flogu = builder.get_object('flogu')
        self.flsge = builder.get_object('flsge')
        self.flwge = builder.get_object('flwge')
        self.flwce = builder.get_object('flwce')
        self.flwcu = builder.get_object('flwcu')
        self.flgice = builder.get_object('flgice')
        self.flgicu = builder.get_object('flgicu')
        self.flgihe = builder.get_object('flgihe')
        self.flgihu = builder.get_object('flgihu')
        self.flgine = builder.get_object('flgine')
        self.flginu = builder.get_object('flginu')
        self.flcmrsu = builder.get_object('flcmrsu')
        self.flcmovu = builder.get_object('flcmovu')
        self.flcmwvu = builder.get_object('flcmwvu')
        self.flcmgvu = builder.get_object('flcmgvu')
        self.flcmowmu = builder.get_object('flcmowmu')
        self.flcmzfu = builder.get_object('flcmzfu')
        self.flscte = builder.get_object('flscte')
        self.flsctu = builder.get_object('flsctu')
        self.flscpe = builder.get_object('flscpe')
        self.flscpu = builder.get_object('flscpu')
#Fluid tab 2
        self.tte = builder.get_object('pvt_tte')
        self.ttu = builder.get_object('pvt_ttu')
        self.pu = builder.get_object('pvt_pu')
        self.sgu = builder.get_object('pvt_sgu')
        self.u = builder.get_object('pvt_u')
        self.ofu = builder.get_object('pvt_ofu')
        self.ovu = builder.get_object('pvt_ovu')
        self.gvu = builder.get_object('pvt_gvu')
        self.gfu = builder.get_object('pvt_gfu')
        self.fltree = builder.get_object('pvt_tree')
        data = [
            ('1'),
            ('2','', '','','',''),
            ('3','', '','','',''),
            ('4','', '','','',''),
            ('5','', '','','',''),
            ('6','', '','','',''),
            ('7','', '','','',''),
            ('8'),
            ('9'),
            ('10'),
            ('11'),
            ('12'),
            ('13'),
            ('14'),
            ('15'),
            ('16')
            ]
        for d in data:
            self.fltree.insert('', tk.END, values=d)
#Fluid tab 3
        self.c1e = builder.get_object('gc_c1e')
        self.c1u = builder.get_object('gc_c1u')
        self.o2e = builder.get_object('gc_o2e')
        self.o2u = builder.get_object('gc_o2u')
        self.gte = builder.get_object('gc_gte')
        self.gtu = builder.get_object('gc_gtu')
        self.c2e = builder.get_object('gc_c2e')
        self.c2u = builder.get_object('gc_c2u')
        self.h2e = builder.get_object('gc_h2e')
        self.h2u = builder.get_object('gc_h2u')
        self.c3e = builder.get_object('gc_c3e')
        self.c3u = builder.get_object('gc_c3u')
        self.hee = builder.get_object('gc_hee')
        self.heu = builder.get_object('gc_heu')
        self.ic4e = builder.get_object('gc_ic4e')
        self.ic4u = builder.get_object('gc_ic4u')
        self.h2oe = builder.get_object('gc_h2oe')
        self.h2ou = builder.get_object('gc_h2ou')
        self.nc4e = builder.get_object('gc_nc4e')
        self.nc4u = builder.get_object('gc_nc4u')
        self.n2e = builder.get_object('gc_n2e')
        self.n2u = builder.get_object('gc_n2u')
        self.ic5e = builder.get_object('gc_ic5e')
        self.ic5u = builder.get_object('gc_ic5u')
        self.co2e = builder.get_object('gc_co2e')
        self.co2u = builder.get_object('gc_co2u')
        self.nc5e = builder.get_object('gc_nc5e')
        self.nc5u = builder.get_object('gc_nc5u')
        self.h2se = builder.get_object('gc_h2se')
        self.h2su = builder.get_object('gc_h2su')
        self.c6e = builder.get_object('gc_c6e')
        self.c6u = builder.get_object('gc_c6u')
        self.c7pe = builder.get_object('gc_c7pe')
        self.c7pu = builder.get_object('gc_c7pu')
        self.c8e = builder.get_object('gc_c8e')
        self.c8u = builder.get_object('gc_c8u')
        self.c9e = builder.get_object('gc_c9e')
        self.c9u = builder.get_object('gc_c9u')
        self.c10e = builder.get_object('gc_c10e')
        self.c10u = builder.get_object('gc_c10u')
        self.gcmw = builder.get_object('gc_mw')
        self.gcsg = builder.get_object('gc_c7sg')
#inflow
        self.ipfrout= builder.get_object('ipfrout_11')
        self.index= builder.get_object('index_13')
        self.constunit = builder.get_object('const_unit_5')
        self.const = builder.get_object('const_5')
        self.stacondc= builder.get_object('stacond_16_20')
        self.bhpc = builder.get_object('bhp_6_10')
        self.bhpcunit = builder.get_object('bhp_unit_6_10')
        self.cpc = builder.get_object('cp_7_11')
        self.cpcunit = builder.get_object('cp_unit_7_11')
        self.flc= builder.get_object('fl_8_12')
        self.flcunit = builder.get_object('fl_unit_8_12')
        self.stacond= builder.get_object('stacond_16')
        self.bhp = builder.get_object('bhp_6')
        self.bhpunit = builder.get_object('bhp_unit_6')
        self.cp = builder.get_object('cp_7')
        self.cpunit = builder.get_object('cp_unit_7')
        self.fl= builder.get_object('fl_8')
        self.flunit = builder.get_object('fl_unit_8')
        self.fr = builder.get_object('fluidrate_13')
        self.frc = builder.get_object('fluidratec_13')
        self.vstacond = builder.get_object('stacond_16_20_24')
        self.bhpv = builder.get_object('bhp_6_10_14')
        self.bhpvunit = builder.get_object('bhp_unit_6_10_14')
        self.cpv = builder.get_object('cp_7_11_15')
        self.cpvunit = builder.get_object('cp_unit_7_11_15')
        self.flv= builder.get_object('fl_8_12_16')
        self.flvunit = builder.get_object('fl_unit_8_12_16')
        self.wc = builder.get_object('watercute')
        self.wcu = builder.get_object('watercutc')
        self.const = builder.get_object('const_5')
        self.calc1 = builder.get_object('fluidrate')
        self.calc2 = builder.get_object('bhp_6_10')
        self.calc3 = builder.get_object('cp_7_11')
        self.calc4 = builder.get_object('fl_8_12')
        self.calc5 = builder.get_object('ipfr6_17_19')
        self.calc6 = builder.get_object('ipfr7_18_20')
        self.ifcalc= builder.get_object('index_13')
        self.fr1 = builder.get_object('fluidrate_13')
        self.cp1 = builder.get_object('cp_7_11_15')
        self.fl1 = builder.get_object('fl_8_12_16')
        self.fr2 = builder.get_object('fluidrate')
        self.cp2 = builder.get_object('cp_7_11')
        self.fl2 = builder.get_object('fl_8_12')
        self.bhp2 = builder.get_object('bhp_6_10')
        self.calc7 =builder.get_object('pi8_15')
        self.calc8 = builder.get_object('pi9_16')
        self.calc9 = builder.get_object('ipfr6_17_19_22')
        self.calc0 = builder.get_object('ipfr7_18_20_23')
        self.fr3 = builder.get_object('fluidrate')
        self.cp3 = builder.get_object('cp_7_11')
        self.fl3 = builder.get_object('fl_8_12')
        self.bhp3 = builder.get_object('bhp_6_10') 
 #pump design
        self.dout= builder.get_object('dout')
        self.pd = builder.get_object('pd')
        self.pdc = builder.get_object('pdc')
        self.tfr = builder.get_object('tfr')
        self.tfrc = builder.get_object('tfrc')
        self.pic= builder.get_object('index')
        self.ipe = builder.get_object('ipe')
        self.ipeu= builder.get_object('ipe_unit')
        self.fop = builder.get_object('fop')
        self.fopu = builder.get_object('fopunit')
        self.fle = builder.get_object('fle')
        self.fleu = builder.get_object('fleunit')
        self.tdhunit= builder.get_object('tdhunit')
        self.casing= builder.get_object('casing')
        self.casingu= builder.get_object('casingunit')
        self.tubing= builder.get_object('tubing_1')
        self.tubingu= builder.get_object('tubingunit')
        self.flcout= builder.get_object('flc')
        self.pvcuout= builder.get_object('pvcu')
        self.fope = builder.get_object('fope')
#Deviation Surey
        self.fcontainer = builder.get_object('fcontainer')
        fcontainer = builder.get_object('fcontainer')
        self.figure = fig = Figure(figsize=(4, 4), dpi=100)
        fig.subplots_adjust(left = 0.2)
        self.canvas = canvas = FigureCanvasTkAgg(fig, master=fcontainer)
        canvas.get_tk_widget().pack()
        self.toolbar = NavigationToolbar2Tk(canvas, fcontainer)
        self.toolbar.update()
        canvas._tkcanvas.pack()
        self.mta = builder.get_object('mta')
        
        builder.connect_callbacks(self)
        tree = builder.get_object('tree')
        tree.insert('', 'end',text='- Well Name')
        tree.insert('', 'end',text='    - Well Info')
        tree.insert('', 'end',text='    - Tubulars')
        tree.insert('', 'end',text='    - Deviation Survey')
        tree.insert('', 'end',text='    - Flowline')
        tree.insert('', 'end',text='          - Data')
        tree.insert('', 'end',text='          - Elevation')
        tree.insert('', 'end',text='    - Fluid')
        tree.insert('', 'end',text='          - Fluid Data')
        tree.insert('', 'end',text='          - PVT Calibration')
        tree.insert('', 'end',text='          - Gas Composition')
        tree.insert('', 'end',text='    - Inflow')
        tree.insert('', 'end',text='    - Pump Design')
        tree.insert('', 'end',text='    - Equipment')
        tree.insert('', 'end',text='          - Pump Selection')
        tree.insert('', 'end',text='          - Motor Selection')
        tree.insert('', 'end',text='          - Cable Selection')
        tree.insert('', 'end',text='          - Separator Selection')
        tree.insert('', 'end',text='          - Surface Selection')
        tree.insert('', 'end',text='          - Summary')
        tree.insert('', 'end',text='    - Sensitivity')
    
        def Curtree(self):
            #a = str((tree.get(tree.selection())))
            #print(tree.selection)
            #print(a)
            curItem = tree.focus()
            #print(curItem)
            go_tab = tree.item(curItem)['text']
            #print (tree.item(curItem)['text'])
            if 'Well Info' in go_tab:
                notebook.select(tab_id = 0)
            elif 'Tubulars' in go_tab:
                notebook.select(tab_id = 1)
            elif 'Deviation Survey' in go_tab:
                notebook.select(tab_id = 2)
            elif 'Flowline' in go_tab:
                notebook.select(tab_id = 3)
            elif 'Fluid' in go_tab and 'Data' not in go_tab:
                notebook.select(tab_id = 4)
            elif 'Inflow' in go_tab:
                notebook.select(tab_id = 5)
            elif 'Pump Design' in go_tab:
                notebook.select(tab_id = 6)
            elif 'Equipment' in go_tab and 'Surface' not in go_tab:
                notebook.select(tab_id = 7)
            elif 'Sensitivity' in go_tab:
                notebook.select(tab_id = 8)
            elif 'Data' in go_tab and 'Fluid' not in go_tab:
                notebook.select(tab_id = 3)
                flowline.select(tab_id = 0)
            elif 'Elevation' in go_tab:
                notebook.select(tab_id = 3)
                flowline.select(tab_id = 1)
            elif 'Fluid Data' in go_tab:
                notebook.select(tab_id = 4)
                fblank.select(tab_id = 0)
            elif 'PVT Calibration' in go_tab:
                notebook.select(tab_id = 4)
                fblank.select(tab_id = 1)
            elif 'Gas Composition' in go_tab:
                notebook.select(tab_id = 4)
                fblank.select(tab_id = 2)
            
        tree.bind('<<TreeviewSelect>>',Curtree)
        
        testl = builder.get_object('test')
        def show_range(self):
            testl.config(text='change the value')
        def show_range1(self):
            #f=Foo(5)
            testl.config(text='123')
            #print (f.foobar(7))
            #testl.config(text=f.foobar(7))
        self.cname.bind('<Button-1>', show_range)
        self.wname.bind('<Button-1>', show_range1)
        
        def Curtab(self):

            curtab = notebook.tab(notebook.select(), "text")
            #curtab = notebook.select()
            #print(curtab)
            if 'Well Info' in curtab:
                tree.focus(item = 'I002')
                tree.selection_set('I002')
                #print('check')
            elif 'Tubulars' in curtab:
                tree.focus(item = 'I003')
                tree.selection_set('I003')
            elif 'Deviation Survey' in curtab:
                tree.focus(item = 'I004')
                tree.selection_set('I004')
            elif 'Flowline' in curtab:
                tree.focus(item = 'I005')
                tree.selection_set('I005')
            elif 'Fluid' in curtab:
                tree.focus(item = 'I008')
                tree.selection_set('I008')
            elif 'Inflow' in curtab:
                tree.focus(item = 'I00C')
                tree.selection_set('I00C')
            elif 'Pump Design' in curtab:
                tree.focus(item = 'I00D')
                tree.selection_set('I00D')
            elif 'Equipment' in curtab and 'Surface' not in curtab:
                tree.focus(item = 'I00E')
                tree.selection_set('I00E')
            elif 'Sensitivity' in curtab:
                tree.focus(item = 'I014')
                tree.selection_set('I014')
        notebook.bind('<<NotebookTabChanged>>',Curtab)
        def Curtab1(self):
            curtab1 = flowline.tab(flowline.select(), "text")
            if 'Data' in curtab1:
                tree.focus(item = 'I006')
                tree.selection_set('I006')
                #print('check')
            elif 'Elevation' in curtab1:
                tree.focus(item = 'I007')
                tree.selection_set('I007')
        flowline.bind('<<NotebookTabChanged>>',Curtab1)
        def Curtab2(self):
            curtab2 = fblank.tab(fblank.select(), "text")
            if 'Fluid Data' in curtab2:
                tree.focus(item = 'I009')
                tree.selection_set('I009')
                #print('check')
            elif 'PVT Calibration' in curtab2:
                tree.focus(item = 'I00A')
                tree.selection_set('I00A')
            elif 'Gas Composition' in curtab2:
                tree.focus(item = 'I00B')
                tree.selection_set('I00B')
        fblank.bind('<<NotebookTabChanged>>',Curtab2)
        data = [
            ('1'),
            ('2','', '','','',''),
            ('3','', '','','',''),
            ('4','', '','','',''),
            ('5','', '','','',''),
            ('6','', '','','',''),
            ('7','', '','','',''),
            ('8'),
            ('9'),
            ('10'),
            ('11'),
            ('12'),
            ('13'),
            ('14'),
            ('15'),
            ('16')
            ]
        for d in data:
            self.cas.insert('', tk.END, values=d)
            self.tub.insert('', tk.END, values=d)
            self.shr.insert('', tk.END, values=d)
            self.pipe.insert('', tk.END, values=d)
            self.choke.insert('', tk.END, values=d)
            self.elev.insert('', tk.END, values=d)       
            self.mta.insert('', tk.END, values=d)  
    
        # Add some data to the treeview
#        listbox= builder.get_object('odid')
#        #frame= self.builder.get_object('Tubulars')
#        file2 = open("casingodid.txt","r") 
#        data1 = "1.050        0.824"
#        listbox.insert("end",data1)
#        while (file2.readline()):
#            data=file2.readline()
#            listbox.insert("end",data)
#        self.logBox = builder.get_object('odid')
#        self.yscrollbar = builder.get_object('ODID_scroll')
#        self.logBox['yscrollcommand'] = self.yscrollbar.set
#        self.yscrollbar['command'] = self.logBox.yview
#        def CurSelet(self):
#            global value
#            value=str((listbox.get(listbox.curselection())))
#            print (value)
#        def insert(self):
#            global value
#            plz =  builder.get_object('od1')
#            abc = ('','', '',value,'','')
#            plz.replace('1.0',0,values=abc)
#            print('test',value)
#        listbox.bind('<<ListboxSelect>>',CurSelet)

#        
#        listbox1= builder.get_object('sizenid')
#        file2 = open("pipesizeid.txt","r") 
#        data1 = "0.50     0.622"
#        listbox1.insert("end",data1)
#        while (file2.readline()):
#            data=file2.readline()
#            listbox1.insert("end",data)
#        self.logBox1 = builder.get_object('sizenid')
#        self.yscrollbar1 = builder.get_object('sizeid_scroll')
#        self.logBox1['yscrollcommand'] = self.yscrollbar1.set
#        self.yscrollbar1['command'] = self.logBox1.yview
#        listbox2= builder.get_object('chokeid_1')
#        file1 = open("chokeid.txt","r") 
#        while (file1.readline()):
#            data=file1.readline()
#            listbox2.insert("end",data)
#        self.logBox2 = builder.get_object('chokeid_1')
#        self.yscrollbar2 = builder.get_object('sizeid_scroll_7')
#
#        self.logBox2['yscrollcommand'] = self.yscrollbar2.set
#        self.yscrollbar2['command'] = self.logBox2.yview
#        def CurSelet1(self):
#            global value1
#            value1=str((listbox1.get(listbox1.curselection())))
#            print (value1[-7:-1])
#
#        listbox1.bind('<<ListboxSelect>>',CurSelet1)
#        def CurSelet2(self):
#            value2=str((listbox2.get(listbox2.curselection())))
#            print (value2)
#        listbox2.bind('<<ListboxSelect>>',CurSelet2)        
        
     
    def run(self):
        self.mainwindow.mainloop()
    def on_forget(self):
        self.tree.grid_forget()
        self.notebook.grid(padx = 5)
        self.forget.grid_forget()
    def on_recover(self):
        self.notebook.grid(padx = 210)
        self.tree.grid(row = 1, column = 0,sticky = 'nw')
        self.forget.grid(row = 1, column = 0, sticky = 'sw', padx = 200, ipady = 5)
    def on_vd(self):
        global v_a
        v_a = 0
    def on_angle(self):
        global v_a
        v_a = 1
    def on_ecc(self):
#        result = espd_eccas.eccas()
#        print(result)
        builder2 = pygubu.Builder()
        builder2.add_from_file('editabletv.ui')
        self.top3 = tk.Toplevel(self.mainwindow)
        frame3 = builder2.get_object('ec', self.top3)
        #callbacks = {}
        builder2.connect_callbacks(self)
        self.eccas = builder2.get_object('eccas')
        eccas = builder2.get_object('eccas')
        data = []
        data1 = "1.050        0.824     1.20"
        data += [(str(1),data1[0:5],data1[13:18],data1[-7:-1])]
        filepath = 'newcasing.txt'
        with open(filepath) as fp:
            line = fp.readline()
            cnt = 1
            while line:
               line = fp.readline()
               #print(line)
               cnt += 1
               data += [(str(cnt),line[0:5],line[13:18],line[-7:-1])]
        fp.close()
        #print(data)
        for d in data:
            self.eccas.insert('', tk.END, values=d)
        def Curtree(self):
            #a = str((tree.get(tree.selection())))
            #print(tree.selection)
            #print(a)
            curItem = eccas.focus()
            #print(curItem)
            go_tab = eccas.item(curItem)['values']
            #print(go_tab[2],go_tab[3])
            global result
            result = [go_tab[1],go_tab[2]]
            #print(result)
        eccas.bind('<<TreeviewSelect>>',Curtree)
    def on_ect(self):
#        result = espd_eccas.eccas()
#        print(result)
        builder2 = pygubu.Builder()
        builder2.add_from_file('editabletv.ui')
        self.top3 = tk.Toplevel(self.mainwindow)
        frame3 = builder2.get_object('ec', self.top3)
        #callbacks = {}
        builder2.connect_callbacks(self)
        self.ectub = builder2.get_object('ectub')
        ectub = builder2.get_object('ectub')
        ec_nb = builder2.get_object('ec_nb')
        ec_nb.select(tab_id = 1)
        data = []
        data1 = "0.50     0.622     40 "
        data += [(str(1),data1[0:5],data1[9:16],data1[-3:-1])]
        filepath = 'pipesizeid.txt'
        with open(filepath) as fp:
            line = fp.readline()
            cnt = 1
            while line:
               line = fp.readline()
               #print(line)
               cnt += 1
               data += [(str(cnt),line[0:5],line[9:16],line[-3:-1])]
        fp.close()
        #print(data)
        for d in data:
            self.ectub.insert('', tk.END, values=d)
        def Curtree(self):
            #a = str((tree.get(tree.selection())))
            #print(tree.selection)
            #print(a)
            curItem = ectub.focus()
            #print(curItem)
            go_tab = ectub.item(curItem)['values']
            #print(go_tab[2],go_tab[3])
            global result_tub
            result_tub = [go_tab[1],go_tab[2]]
            #print(result)
        ectub.bind('<<TreeviewSelect>>',Curtree)
    def on_ecpipe(self):
#        result = espd_eccas.eccas()
#        print(result)
        builder2 = pygubu.Builder()
        builder2.add_from_file('editabletv.ui')
        self.top3 = tk.Toplevel(self.mainwindow)
        frame3 = builder2.get_object('ec', self.top3)
        #callbacks = {}
        builder2.connect_callbacks(self)
        self.ecp = builder2.get_object('ecp')
        ecp = builder2.get_object('ecp')
        ec_nb = builder2.get_object('ec_nb')
        ec_nb.select(tab_id = 2)
        data = []
        data1 = "0.50     0.622     40 "
        data += [(str(1),data1[0:5],data1[9:16],data1[-3:-1])]
        filepath = 'pipesizeid.txt'
        with open(filepath) as fp:
            line = fp.readline()
            cnt = 1
            while line:
               line = fp.readline()
               #print(line)
               cnt += 1
               data += [(str(cnt),line[0:5],line[9:16],line[-3:-1])]
        fp.close()
        #print(data)
        for d in data:
            self.ecp.insert('', tk.END, values=d)
        def Curtree(self):
            #a = str((tree.get(tree.selection())))
            #print(tree.selection)
            #print(a)
            curItem = ecp.focus()
            #print(curItem)
            go_tab = ecp.item(curItem)['values']
            #print(go_tab[2],go_tab[3])
            global result_p
            result_p = [go_tab[2]]
            #print(result)
        ecp.bind('<<TreeviewSelect>>',Curtree)
    def on_ecchoke(self):
#        result = espd_eccas.eccas()
#        print(result)
        builder2 = pygubu.Builder()
        builder2.add_from_file('editabletv.ui')
        self.top3 = tk.Toplevel(self.mainwindow)
        frame3 = builder2.get_object('ec', self.top3)
        #callbacks = {}
        builder2.connect_callbacks(self)
        self.ecch = builder2.get_object('ecch')
        ecch = builder2.get_object('ecch')
        ec_nb = builder2.get_object('ec_nb')
        ec_nb.select(tab_id = 3)
        data = []
        #data1 = "0.50     0.622     40 "
        #data += [(str(1),data1[0:5],data1[9:16],data1[-3:-1])]
        filepath = 'chokeid.txt'
        with open(filepath) as fp:
            line = fp.readline()
            cnt = 0
            while line:
               line = fp.readline()
               #print(line)
               cnt += 1
               data += [(str(cnt),line[0:3])]
        fp.close()
        #print(data)
        for d in data:
            self.ecch.insert('', tk.END, values=d)
        def Curtree(self):
            #a = str((tree.get(tree.selection())))
            #print(tree.selection)
            #print(a)
            curItem = ecch.focus()
            #print(curItem)
            go_tab = ecch.item(curItem)['values']
            #print(go_tab[2],go_tab[3])
            global result_ch
            result_ch = [go_tab[1]]
            #print(result)
        ecch.bind('<<TreeviewSelect>>',Curtree)
    def on_ecc_ok(self):
            self.top3.destroy()
            global result
            #print(result)
            self.cas.set(self.cas.focus(), column = '#4',value =  result[0])
            self.cas.set(self.cas.focus(), column = '#5',value =  result[1])
    def on_ecc_cancel(self):
        #self.top3.destroy()
        #self.eccas.selection()
        if len(self.eccas.selection()) > 0:
            self.eccas.selection_remove(self.eccas.selection()[0])
    def on_ect_ok(self):
            self.top3.destroy()
            global result_tub
            #print(result)
            self.tub.set(self.tub.focus(), column = '#4',value =  result_tub[0])
            self.tub.set(self.tub.focus(), column = '#5',value =  result_tub[1])
    def on_ect_cancel(self):
        #self.top3.destroy()
        #self.eccas.selection()
        if len(self.ectub.selection()) > 0:
            self.ectub.selection_remove(self.ectub.selection()[0])
    def on_ecp_ok(self):
            self.top3.destroy()
            global result_p
            #print(result)
            self.pipe.set(self.pipe.focus(), column = '#3',value =  result_p[0])
    def on_ecp_cancel(self):
        #self.top3.destroy()
        #self.eccas.selection()
        if len(self.ecp.selection()) > 0:
            self.ecp.selection_remove(self.ecp.selection()[0])
    def on_ecch_ok(self):
            self.top3.destroy()
            global result_ch
            #print(result)
            self.choke.set(self.choke.focus(), column = '#3',value =  result_ch[0])
    def on_ecch_cancel(self):
        #self.top3.destroy()
        #self.eccas.selection()
        if len(self.ecch.selection()) > 0:
            self.ecch.selection_remove(self.ecch.selection()[0])
    def on_sec(self):
        global ifsec
        global sec_counter

        if (sec_counter%2) == 0:
            ifsec = 1
            self.sec_en.configure(state='normal')
        else:
            ifsec =0
            self.sec_en.configure(state='disabled')
        sec_counter = sec_counter +1
    def on_eq(self):
        global ifeq
        global eq_counter
        if (eq_counter%2) == 0:
            ifeq = 1
        else:
            ifeq =0
        eq_counter = eq_counter +1
    def on_next5(self):
        self.dout_out = self.dout.cget("text")
        if self.dout_out =='Pump Depth':
            
            self.pd_out = self.pd.get()
            
            self.pdc_out = self.pdc.get()
        elif self.dout_out =='Total Fluid Rate':
            
            self.tfr_out = self.tfr.get()
            
            self.tfrc_out = self.tfrc.get()
        
        self.pic_out = self.pic.cget("text")
        if self.pic_out =='Intake Pressure':
            
            self.ipe_out = self.ipe.get()
            
            self.ipeu_out = self.ipeu.get()
        elif self.pic_out =='Flow Over Pump':
            
            self.fop_out = self.fop.get()
            
            self.fopu_out = self.fopu.get()
        elif self.pic_out =='Fluid Level':
            
            self.fle_out = self.fle.get()
            
            self.fleu_out = self.fleu.get()
        
        self.tdhunit_out = self.tdhunit.get()
        
        self.casing_out = self.casing.get()
        
        self.casingu_out = self.casingu.get()
        
        self.tubing_out = self.tubing.get()
        
        self.tubingu_out = self.tubingu.get()
        
        self.flcout_out = self.flcout.get()
        
        self.pvcuout_out = self.pvcuout.get()
        self.notebook.select(tab_id = 7)
        #global root1
        #root1.destroy()
        #espd_Flowline.flowline()
        #notebook = self.builder.get_object('perforation')
        #notebook.select(tab_id)
    def on_next0(self):
        self.company_name_out = self.cname.get()
        self.well_name_out = self.wname.get()
        self.field_name_out = self.fname.get()
        self.reservoir_name_out = self.rname.get()
        self.location_out = self.loc.get()
        self.analyst_name_out = self.aname.get()
        self.notes_out = self.notes.get("1.0","end")
        self.notebook.select(tab_id = 1)
    def on_next1(self):
        self.wellbore_out = self.wellbore.get()

        self.perforation_out = self.perforation.get()

        self.perfunit_out = self.perfunit.get()
        if (sec_counter%2) == 0:
            
            self.secdepth_out = self.secdepth.get()
            
            self.depunit_out = self.depunit.get()
        
        self.temp_out = self.temp.get()
        
        self.tempunit_out = self.tempunit.get()
        self.notebook.select(tab_id = 2)
    def on_next2(self):

        self.notebook.select(tab_id = 3)
    def on_next3(self):
        self.datatemp_out = self.datatemp.get()

        self.datatempunit_out = self.datatempunit.get()
        
        self.datapre_out = self.datapre.get()
        
        self.datapreunit_out = self.datapreunit.get()
        
        self.pcorrelation_out = self.pcorrelation.get()
        
        self.ccorrelation_out = self.ccorrelation.get()

        self.speheat_out = self.speheat.get()
        
        self.heatunit_out = self.heatunit.get()
        self.notebook.select(tab_id = 4)
        self.fblank.select(tab_id = 0)
    def on_next3_1(self):
        self.datatemp_out = self.datatemp.get()

        self.datatempunit_out = self.datatempunit.get()
        
        self.datapre_out = self.datapre.get()
        
        self.datapreunit_out = self.datapreunit.get()
        
        self.pcorrelation_out = self.pcorrelation.get()
        
        self.ccorrelation_out = self.ccorrelation.get()

        self.speheat_out = self.speheat.get()
        
        self.heatunit_out = self.heatunit.get()
        self.flowline.select(tab_id = 1)
    def on_next4(self):
        if self.ipfrout == 'Calculated by Productivity Index':
            
            self.index_out = self.index.cget("text")
            if self.index_out == 'Constant':
                
                self.const_out = self.const.get()
                
                self.constunit_out = self.constunit.get()
                
                self.stacondc_out = self.stacondc.cget("text")
            if self.index_out == 'Calculate':
                if self.stacondc_out == 'Bottom Hole Pressure':
                    
                    self.bhpc_out = self.bhpc.get()
                    
                    self.bhpcunit_out = self.bhpcunit.get()
                elif self.stacondc_out == 'Casting Pressure':
                    
                    self.cpc_out = self.cpc.get()
                    
                    self.cpcunit_out = self.cpcunit.get()
                    
                    self.flc_out = self.flc.get()
                    
                    self.flcunit_out = self.flcunit.get()
        
        self.stacond_out = self.stacond.cget("text")
        if self.stacond_out == 'Bottom Hole Pressure':
            
            self.bhp_out = self.bhp.get()
            
            self.bhpunit_out = self.bhpunit.get()
        elif self.stacond_out == 'Casting Pressure':
            
            self.cp_out = self.cp.get()
            
            self.cpunit_out = self.cpunit.get()
            
            self.fl_out = self.fl.get()
            
            self.flunit_out = self.flunit.get()
        if self.ipfrout == 'Calculated by Vogel' or self.ipfrout == 'Calculated by Vogel Corrected for Water Cut':
            
            self.fr_out = self.fr.get()
            
            self.frc_out = self.frc.get()
            
            self.vstacond_out = self.vstacond.cget("text")
            if self.vstacond_out == 'Bottom Hole Pressure':
                
                self.bhpv_out = self.bhpv.get()
                
                self.bhpvunit_out = self.bhpvunit.get()
            elif self.vstacond_out == 'Casting Pressure':
                
                self.cpv_out = self.cpv.get()
                
                self.cpvunit_out = self.cpvunit.get()
                
                self.flv_out = self.flv.get()
                
                self.flvunit_out = self.flvunit.get()
        if self.ipfrout == 'Calculated by Vogel Corrected for Water Cut':
            
            self.wc_out = self.wc.get()
            
            self.wcu_out = self.wcu.get()
        self.notebook.select(tab_id = 6)
    def on_back1(self):
        self.notebook.select(tab_id = 0)
    def on_back2(self):
        self.notebook.select(tab_id = 1)
    def on_back3(self):
        self.notebook.select(tab_id = 2)
    def on_back3_1(self):
        self.flowline.select(tab_id = 0)
    def on_back4(self):
        self.notebook.select(tab_id = 4)
        self.fblank.select(tab_id = 2)
    def on_back5(self):
        self.notebook.select(tab_id = 5)
    def on_ok0(self):
        self.company_name_out = self.cname.get()
        self.well_name_out = self.wname.get()
        self.field_name_out = self.fname.get()
        self.reservoir_name_out = self.rname.get()
        self.location_out = self.loc.get()
        self.analyst_name_out = self.aname.get()
        self.notes_out = self.notes.get("1.0","end")
    def on_ok1(self):
        self.wellbore_out = self.wellbore.get()

        self.perforation_out = self.perforation.get()

        self.perfunit_out = self.perfunit.get()
        if (sec_counter%2) == 0:
            
            self.secdepth_out = self.secdepth.get()
            
            self.depunit_out = self.depunit.get()
        
        self.temp_out = self.temp.get()
        
        self.tempunit_out = self.tempunit.get()
    def on_ok2(self):
        a = True
    def on_ok3(self):
        self.datatemp_out = self.datatemp.get()

        self.datatempunit_out = self.datatempunit.get()
        
        self.datapre_out = self.datapre.get()
        
        self.datapreunit_out = self.datapreunit.get()
        
        self.pcorrelation_out = self.pcorrelation.get()
        
        self.ccorrelation_out = self.ccorrelation.get()

        self.speheat_out = self.speheat.get()
        
        self.heatunit_out = self.heatunit.get()  
    def on_ok4(self):
        if self.ipfrout == 'Calculated by Productivity Index':
            
            self.index_out = self.index.cget("text")
            if self.index_out == 'Constant':
                
                self.const_out = self.const.get()
                
                self.constunit_out = self.constunit.get()
                
                self.stacondc_out = self.stacondc.cget("text")
            if self.index_out == 'Calculate':
                if self.stacondc_out == 'Bottom Hole Pressure':
                    
                    self.bhpc_out = self.bhpc.get()
                    
                    self.bhpcunit_out = self.bhpcunit.get()
                elif self.stacondc_out == 'Casting Pressure':
                    
                    self.cpc_out = self.cpc.get()
                    
                    self.cpcunit_out = self.cpcunit.get()
                    
                    self.flc_out = self.flc.get()
                    
                    self.flcunit_out = self.flcunit.get()
        
        self.stacond_out = self.stacond.cget("text")
        if self.stacond_out == 'Bottom Hole Pressure':
            
            self.bhp_out = self.bhp.get()
            
            self.bhpunit_out = self.bhpunit.get()
        elif self.stacond_out == 'Casting Pressure':
            
            self.cp_out = self.cp.get()
            
            self.cpunit_out = self.cpunit.get()
            
            self.fl_out = self.fl.get()
            
            self.flunit_out = self.flunit.get()
        if self.ipfrout == 'Calculated by Vogel' or self.ipfrout == 'Calculated by Vogel Corrected for Water Cut':
            
            self.fr_out = self.fr.get()
            
            self.frc_out = self.frc.get()
            
            self.vstacond_out = self.vstacond.cget("text")
            if self.vstacond_out == 'Bottom Hole Pressure':
                
                self.bhpv_out = self.bhpv.get()
                
                self.bhpvunit_out = self.bhpvunit.get()
            elif self.vstacond_out == 'Casting Pressure':
                
                self.cpv_out = self.cpv.get()
                
                self.cpvunit_out = self.cpvunit.get()
                
                self.flv_out = self.flv.get()
                
                self.flvunit_out = self.flvunit.get()
        if self.ipfrout == 'Calculated by Vogel Corrected for Water Cut':
            
            self.wc_out = self.wc.get()
            
            self.wcu_out = self.wcu.get()
    def on_ok5(self):
        self.dout_out = self.dout.cget("text")
        if self.dout_out =='Pump Depth':
            
            self.pd_out = self.pd.get()
            
            self.pdc_out = self.pdc.get()
        elif self.dout_out =='Total Fluid Rate':
            
            self.tfr_out = self.tfr.get()
            
            self.tfrc_out = self.tfrc.get()
        
        self.pic_out = self.pic.cget("text")
        if self.pic_out =='Intake Pressure':
            
            self.ipe_out = self.ipe.get()
            
            self.ipeu_out = self.ipeu.get()
        elif self.pic_out =='Flow Over Pump':
            
            self.fop_out = self.fop.get()
            
            self.fopu_out = self.fopu.get()
        elif self.pic_out =='Fluid Level':
            
            self.fle_out = self.fle.get()
            
            self.fleu_out = self.fleu.get()
        
        self.tdhunit_out = self.tdhunit.get()
        
        self.casing_out = self.casing.get()
        
        self.casingu_out = self.casingu.get()
        
        self.tubing_out = self.tubing.get()
        
        self.tubingu_out = self.tubingu.get()
        
        self.flcout_out = self.flcout.get()
        
        self.pvcuout_out = self.pvcuout.get()
    def on_cancel0(self):
        self.cname.delete(0, 'end')
        self.wname.delete(0, 'end')
        self.fname.delete(0, 'end')
        self.rname.delete(0, 'end')
        self.loc.delete(0, 'end')
        self.aname.delete(0, 'end')
        self.notes.delete('1.0', END)
        #global cancel0
        #cancel0 = True
    def on_cancel1(self):
        #global cancel1
        #cancel1 = True
        self.perforation.delete(0, 'end')
        self.sec_en.delete(0, 'end')
        self.temp.delete(0, 'end')
        self.cas.delete(*self.cas.get_children())
        self.tub.delete(*self.tub.get_children())
        self.shr.delete(*self.shr.get_children())
        data = [
            ('1'),
            ('2','', '','','',''),
            ('3','', '','','',''),
            ('4','', '','','',''),
            ('5','', '','','',''),
            ('6','', '','','',''),
            ('7','', '','','',''),
            ('8'),
            ('9'),
            ('10'),
            ('11'),
            ('12'),
            ('13'),
            ('14'),
            ('15'),
            ('16')
            ]
        for d in data:
            self.cas.insert('', tk.END, values=d)
            self.tub.insert('', tk.END, values=d)
            self.shr.insert('', tk.END, values=d)
    def on_cancel2(self):
        #global cancel2
        #cancel2 = True
       
        self.mta.delete(*self.mta.get_children())
        data = [
            ('1'),
            ('2','', '','','',''),
            ('3','', '','','',''),
            ('4','', '','','',''),
            ('5','', '','','',''),
            ('6','', '','','',''),
            ('7','', '','','',''),
            ('8'),
            ('9'),
            ('10'),
            ('11'),
            ('12'),
            ('13'),
            ('14'),
            ('15'),
            ('16')
            ]
        for d in data:
            self.mta.insert('', tk.END, values=d)
        self.canvas.draw()
        #self.cname.delete(0, 'end')
    def on_cancel3(self):
        #global cancel3
        #cancel3 = True
        self.datatemp.delete(0, 'end')
        self.datapre.delete(0, 'end')
        self.speheat.delete(0, 'end')
        self.pipe.delete(*self.pipe.get_children())
        self.choke.delete(*self.choke.get_children())
        self.elev.delete(*self.elev.get_children())
        data = [
            ('1'),
            ('2','', '','','',''),
            ('3','', '','','',''),
            ('4','', '','','',''),
            ('5','', '','','',''),
            ('6','', '','','',''),
            ('7','', '','','',''),
            ('8'),
            ('9'),
            ('10'),
            ('11'),
            ('12'),
            ('13'),
            ('14'),
            ('15'),
            ('16')
            ]
        for d in data:
            self.pipe.insert('', tk.END, values=d)
            self.choke.insert('', tk.END, values=d)
            self.elev.insert('', tk.END, values=d)
    def on_cancel4(self):
        #global cancel4
        #cancel4 = True
        self.const.delete(0, 'end')
        self.calc1.delete(0, 'end')
        self.bhpc.delete(0, 'end')
        self.cpc.delete(0, 'end')
        self.flc.delete(0, 'end')
        self.bhp.delete(0, 'end')
        self.cp.delete(0, 'end')
        self.fl.delete(0, 'end')
        self.fr.delete(0, 'end')
        self.bhpv.delete(0, 'end')
        self.cpv.delete(0, 'end')
        self.flv.delete(0, 'end')
        self.wc.delete(0, 'end')
    def on_cancel5(self):
        #global cancel5
        #cancel5 = True
        self.tfr.delete(0, 'end')
        self.pd.delete(0, 'end')
        self.ipe.delete(0, 'end')
        self.fope.delete(0, 'end')
        self.fle.delete(0, 'end')
        self.casing.delete(0, 'end')
        self.tubing.delete(0, 'end')
#    def on_in(self):
#        global value
#        tree1 =  self.builder.get_object('bttm')
#        tree1.insert('', 'end',values=value)
     
    def on_row_edit(self, event):
        # Get the column id and item id of the cell
        # that is going to be edited
        
        col, item = self.cas.get_event_info()


        # Allow edition only if allow_edit variable is checked
        
            # Define the widget editor to be used to edit the column value
        #if self.allow.get() == True:
        if col in ('bttm','td','rou1',):
                self.cas.inplace_entry(col, item)
    def on_row_edit1(self, event):

        col1, item1 = self.tub.get_event_info()
        #if self.allow.get() == True:
        if col1 in ('bttm_4','td_%','rou1_8',):
                self.tub.inplace_entry(col1, item1)
    def on_row_edit2(self, event):
        col2, item2 = self.shr.get_event_info()
        #if self.allow.get() == True:
        if col2 in ('bttm_9','td_10','rou1_13',):
                self.shr.inplace_entry(col2, item2)
    def on_row_edit3(self, event):
        col3, item3 = self.elev.get_event_info()
        if col3 in ('ewd','eaz',):
                self.elev.inplace_entry(col3, item3)
    def on_row_edit4(self, event):
        # Get the column id and item id of the cell
        # that is going to be edited
        col4, item4 = self.pipe.get_event_info()
        if col4 in ('wd','rou','dc',):
                self.pipe.inplace_entry(col4, item4)
    def on_row_edit5(self, event):
        col5, item5 = self.choke.get_event_info()
        if col5 in ('wd1','rou1','dc1',):
                self.choke.inplace_entry(col5, item5)

    def on_row_edit6(self, event):
        col6, item6 = self.mta.get_event_info()
        if col6 in ('md','tvd','ang',):
                self.mta.inplace_entry(col6, item6)
    def on_const(self):
        global vogel
        if vogel ==0:
            
            self.const.configure(state='normal')
            
            self.calc1.configure(state='disabled')
            
            self.calc2.configure(state='disabled')
            
            self.calc3.configure(state='disabled')
            
            self.calc4.configure(state='disabled')
            
            self.calc5.configure(state='disabled')
            
            self.calc6.configure(state='disabled')
    def on_calc(self):
        global vogel
        if vogel ==0:
            #const = self.builder.get_object('const_5')
            self.const.configure(state='disabled')
            #calc1 = self.builder.get_object('fluidrate')
            self.calc1.configure(state='normal')
            #calc2 = self.builder.get_object('bhp_6_10')
            #calc2.configure(state='normal')
            #calc3 = self.builder.get_object('cp_7_11')
            self.calc3.configure(state='normal')
            #calc4 = self.builder.get_object('fl_8_12')
            self.calc4.configure(state='normal')
            #calc5 = self.builder.get_object('ipfr6_17_19')
            self.calc5.configure(state='normal')
            #calc6 = self.builder.get_object('ipfr7_18_20')
            self.calc6.configure(state='normal')
    def on_bhp(self):
        
        self.bhp.configure(state='normal')
        #cp = self.builder.get_object('cp_7')
        self.cp.configure(state='disabled')
        #fl = self.builder.get_object('fl_8')
        self.fl.configure(state='disabled')
    def on_cp(self):
        #bhp = self.builder.get_object('bhp_6')
        self.bhp.configure(state='disabled')
        #cp = self.builder.get_object('cp_7')
        self.cp.configure(state='normal')
        #fl = self.builder.get_object('fl_8')
        self.fl.configure(state='normal')
    def on_bhpc(self):
        global vogel
        
        ifcalc = self.ifcalc.cget("text")
        if ifcalc == 'Calculate'and vogel ==0:
            #bhpc = self.builder.get_object('bhp_6_10')
            self.bhpc.configure(state='normal')
            #cpc = self.builder.get_object('cp_7_11')
            self.cpc.configure(state='disabled')
            #self.flc = self.builder.get_object('fl_8_12')
            self.flc.configure(state='disabled')
    def on_cpc(self):
        global vogel
        #ifcalc= self.builder.get_object('index_13')
        ifcalc = self.ifcalc.cget("text")
        if ifcalc == 'Calculate'and vogel ==0:
            #bhpc = self.builder.get_object('bhp_6_10')
            self.bhpc.configure(state='disabled')
            #cpc = self.builder.get_object('cp_7_11')
            self.cpc.configure(state='normal')   
            #flc = self.builder.get_object('fl_8_12')
            self.flc.configure(state='normal')
    def on_vogel(self):
        global vogel
        vogel = 1
        
        self.fr1.configure(state='normal')   
        
        self.cp1.configure(state='normal')   
        
        self.fl1.configure(state='normal') 
        
        self.fr2.configure(state='disabled')   
        
        self.cp2.configure(state='disabled')   
        
        self.fl2.configure(state='disabled')
        
        self.bhp2.configure(state='disabled')
        
        self.wc.configure(state='disabled')
        #const = self.builder.get_object('const_5')
        self.const.configure(state='disabled')
        #calc5 = self.builder.get_object('ipfr6_17_19')
        self.calc5.configure(state='disabled')
        #calc6 = self.builder.get_object('ipfr7_18_20')
        self.calc6.configure(state='disabled')
        
        self.calc7.configure(state='disabled')
        
        self.calc8.configure(state='disabled')
        
        self.calc9.configure(state='normal')
        
        self.calc0.configure(state='normal')
    def on_bhpv(self):
            global vogel
            if vogel ==1:
                #bhpv = self.builder.get_object('bhp_6_10_14')
                self.bhpv.configure(state='normal')
                #cpv = self.builder.get_object('cp_7_11_15')
                self.cpv.configure(state='disabled')
                #flv = self.builder.get_object('fl_8_12_16')
                self.flv.configure(state='disabled')
    def on_cpv(self):
            global vogel
            if vogel ==1:
                #bhpv = self.builder.get_object('bhp_6_10_14')
                self.bhpv.configure(state='disabled')
                #cpv = self.builder.get_object('cp_7_11_15')
                self.cpv.configure(state='normal') 
                #flv = self.builder.get_object('fl_8_12_16')
                self.flv.configure(state='normal')
    def on_calcpi(self):
        global vogel
        vogel =0
        #fr1 = self.builder.get_object('fluidrate')
        self.fr2.configure(state='normal')   
        #cp1 = self.builder.get_object('cp_7_11')
        self.cp2.configure(state='normal')   
        #fl1 = self.builder.get_object('fl_8_12')
        self.fl2.configure(state='normal')
       # fr2 = self.builder.get_object('fluidrate_13')
        self.fr.configure(state='disabled')   
        #cp2 = self.builder.get_object('cp_7_11_15')
        self.cpv.configure(state='disabled')   
        #fl2 = self.builder.get_object('fl_8_12_16')
        self.flv.configure(state='disabled') 
        #bhp2 = self.builder.get_object('bhp_6_10_14')
        self.bhpv.configure(state='disabled')
        #wc = self.builder.get_object('watercute')
        self.wc.configure(state='disabled')
        #calc5 = self.builder.get_object('ipfr6_17_19')
        self.calc5.configure(state='normal')
        #calc6 = self.builder.get_object('ipfr7_18_20')
        self.calc6.configure(state='normal')
        #calc7 = self.builder.get_object('pi8_15')
        self.calc7.configure(state='normal')
        #calc8 = self.builder.get_object('pi9_16')
        self.calc8.configure(state='normal')
        #calc9 = self.builder.get_object('ipfr6_17_19_22')
        self.calc9.configure(state='disabled')
        #calc0 = self.builder.get_object('ipfr7_18_20_23')
        self.calc0.configure(state='disabled')

    def on_vogelwc(self):
        global vogel
        vogel = 1
        #wc = self.builder.get_object('watercute')
        self.wc.configure(state='normal')
        #fr1 = self.builder.get_object('fluidrate_13')
        self.fr1.configure(state='normal')   
        #cp1 = self.builder.get_object('cp_7_11_15')
        self.cp1.configure(state='normal')   
        #fl1 = self.builder.get_object('fl_8_12_16')
        self.fl1.configure(state='normal') 
        #fr2 = self.builder.get_object('fluidrate')
        self.fr2.configure(state='disabled')   
        #cp2 = self.builder.get_object('cp_7_11')
        self.cp2.configure(state='disabled')   
        #fl2 = self.builder.get_object('fl_8_12')
        self.fl2.configure(state='disabled')
        #bhp2 = self.builder.get_object('bhp_6_10')
        self.bhp2.configure(state='disabled')
        #const = self.builder.get_object('const_5')
        self.const.configure(state='disabled')
        #calc9 = self.builder.get_object('ipfr6_17_19_22')
        self.calc9.configure(state='normal')
        #calc0 = self.builder.get_object('ipfr7_18_20_23')
        self.calc0.configure(state='normal')
        #calc5 = self.builder.get_object('ipfr6_17_19')
        self.calc5.configure(state='disabled')
        #calc6 = self.builder.get_object('ipfr7_18_20')
        self.calc6.configure(state='disabled')
        #calc7 = self.builder.get_object('pi8_15')
        self.calc7.configure(state='disabled')
        #calc8 = self.builder.get_object('pi9_16')
        self.calc8.configure(state='disabled')
    def on_data(self):
        global vogel
        vogel = 2
        #fr2 = self.builder.get_object('fluidrate_13')
        self.fr1.configure(state='disabled')   
        #cp2 = self.builder.get_object('cp_7_11_15')
        self.cp1.configure(state='disabled')   
        #fl2 = self.builder.get_object('fl_8_12_16')
        self.fl1.configure(state='disabled') 
        #bhp2 = self.builder.get_object('bhp_6_10_14')
        self.bhp2.configure(state='disabled')
        #wc = self.builder.get_object('watercute')
        self.wc.configure(state='disabled')
        
        self.fr3.configure(state='disabled')   
        
        self.cp3.configure(state='disabled')   
        
        self.fl3.configure(state='disabled')
        
        self.bhpv.configure(state='disabled')
        #calc9 = self.builder.get_object('ipfr6_17_19_22')
        self.calc9.configure(state='disabled')
        #calc0 = self.builder.get_object('ipfr7_18_20_23')
        self.calc0.configure(state='disabled')
        #calc5 = self.builder.get_object('ipfr6_17_19')
        self.calc5.configure(state='disabled')
        #calc6 = self.builder.get_object('ipfr7_18_20')
        self.calc6.configure(state='disabled')
        #calc7 = self.builder.get_object('pi8_15')
        self.calc7.configure(state='disabled')
       # calc8 = self.builder.get_object('pi9_16')
        self.calc8.configure(state='disabled')
        
    def on_tfr(self):
        #tfr = self.builder.get_object('tfr')
        self.tfr.configure(state='disabled')
        #pd = self.builder.get_object('pd')
        self.pd.configure(state='normal')
    def on_pic(self):
        #tfr = self.builder.get_object('tfr')
        self.tfr.configure(state='disabled')
        #pd = self.builder.get_object('pd')
        self.pd.configure(state='disabled')
    def on_pd(self):
        #tfr = self.builder.get_object('tfr')
        self.tfr.configure(state='normal')
        #pd = self.builder.get_object('pd')
        self.pd.configure(state='disabled')
    def on_fl(self):
        #ipe = self.builder.get_object('ipe')
        self.ipe.configure(state='disabled')
        
        self.fope.configure(state='disabled')
        #fle = self.builder.get_object('fle')
        self.fle.configure(state='normal')
    def on_fop(self):
        #ipe = self.builder.get_object('ipe')
        self.ipe.configure(state='disabled')
        #fop = self.builder.get_object('fope')
        self.fope.configure(state='normal')
        #fle = self.builder.get_object('fle')
        self.fle.configure(state='disabled')
    def on_ip(self):
        #ipe = self.builder.get_object('ipe')
        self.ipe.configure(state='normal')
        #fope = self.builder.get_object('fope')
        self.fope.configure(state='disabled')
        #fle = self.builder.get_object('fle')
        self.fle.configure(state='disabled')
    def on_ds_calc(self):
        test = []
        result = []
        write_data = []
        xvalue = []
        global dsdata
        global v_a
        if v_a == 0:
            for i in range(0,int(len(dsdata)/3)):
        	    test +=[(float(dsdata[i*3]),float(dsdata[i*3+1]),0,0)]
            for i in range(0,len(test)):
	            if test[i][0] == test[i][1]:
		            HD = 0
		            angle = 0
		            temp = test[i][0]
		            result += [(test[i][0],test[i][1],0,0)]
	            else:
		            angle = math.acos((test[i][1]-test[i-1][1])/(test[i][0]-test[i-1][0]))
		            sin = math.sin(angle)
		            angle = math.degrees(angle)
		            HD = (test[i][0]-test[i-1][0])*sin+result[i-1][2]
		            result +=[(test[i][0],test[i][1],HD,angle)]
            result +=[(0,0,0,0)]
            #print(result)
            self.mta.delete(*self.mta.get_children())
            for i in range(0,len(test)):
                write_data += [(str(i+1),result[i][0],result[i][1],result[i+1][3])]
        else:
            for i in range(0,int(len(dsdata)/3)):
                test +=[(float(dsdata[i*3]),0,0,float(dsdata[(i)*3+2]))]
            #print(test)
            result += [(test[0][0],test[0][0],0,test[0][3])]
            for i in range(1,len(test)):
                    angled = math.radians(test[i-1][3])
                    TVD = math.cos(angled)*(test[i][0]-test[i-1][0]) + result[i-1][1]
                    HD = (test[i][0]-test[i-1][0])*math.sin(angled) + result[i-1][2]
                    result +=[(test[i][0],TVD,HD,test[i][3])]
            self.mta.delete(*self.mta.get_children())
            #write_data += [(str(1),result[0][0],result[0][1],0)]
            #print(result)
            result +=[(0,0,0,0)]
            for i in range(0,len(test)):
                write_data += [(str(i+1),result[i][0],result[i][1],result[i][3])]
        for d in write_data:
            self.mta.insert('', tk.END, values=d)
        a = self.figure.add_subplot(111)
        result.pop()
        for i in range(0,len(result)):
        	xvalue += [result[i][2]]
        #print(xvalue)
        maxx = max(xvalue)
        a.set_xlim([0,round(maxx,-3)])
        a.set_ylim([10000,0])
        a.set_ylabel('TVD (ft)')
        a.set_xlabel('Horizontal displacement (ft)')

        tempx = []
        tempy = []
        
        for item in result:
        	tempx += [item[2]]
        	tempy += [item[1]]
        a.plot(tempx,tempy,'-o')
        self.canvas.draw()
    def on_use_c7(self):
        global use_c7
        if use_c7 == 1:
            self.gcmw.configure(state = 'normal')
            self.gcsg.configure(state = 'normal')
            self.c8e.configure(state = 'disabled')
            self.c8u.configure(state = 'disabled')
            self.c9e.configure(state = 'disabled')
            self.c9u.configure(state = 'disabled')
            self.c10e.configure(state = 'disabled')
            self.c10u.configure(state = 'disabled')
            use_c7 = 0
        else:
            self.gcmw.configure(state = 'disabled')
            self.gcsg.configure(state = 'disabled')
            self.c8e.configure(state = 'normal')
            self.c8u.configure(state = 'normal')
            self.c9e.configure(state = 'normal')
            self.c9u.configure(state = 'normal')
            self.c10e.configure(state = 'normal')
            self.c10u.configure(state = 'normal')
            use_c7 = 1
    def on_gc_ugc(self):
        global ugc
        if ugc == 0:
            ugc = 1
        else:
            ugc = 0
    def on_pvt_iff(self):
            filename = filedialog.askopenfilename(initialdir=".")
            self.infile = open(filename, "r")
            #self.infile = io.TextIOWrapper(self.infile, encoding='utf8', newline='')
            df = pd.read_excel(self.infile.name)
            dfin = []
            self.fltree.delete(*self.fltree.get_children())
            for i in range(0,len(df['Pressure'])):
                dfin += [(str(i+1),df['Pressure'][i],df['Soln GOR'][i],df['Oil FVF'][i],df['Oil Visc'][i],df['Gas Visc'][i],df['Gas FVF'][i],df['Z Factor'][i])]
            #dfin += [(str(i+1),int(str(df['Pressure'][i])[:8]),int(str(df['Soln GOR'][i])[:8]),int(str(df['Oil FVF'][i])[:8]),int(str(df['Oil Visc'][i])[:8]),int(str(df['Gas Visc'][i])[:8]),int(str(df['Gas FVF'][i])[:8]),int(str(df['Z Factor'][i])[:8]))]
            for d in dfin:
                self.fltree.insert('', tk.END, values=d)
    def on_ds_import(self):
            global v_a
            global dsdata
            dsdata = []
            filename = filedialog.askopenfilename(initialdir=".")
            self.infile = open(filename, "r")
            #self.infile = io.TextIOWrapper(self.infile, encoding='utf8', newline='')
            #print(self.infile.name)
            with open(self.infile.name, 'r') as myfile:
                txt_file=myfile.read().replace('\n', '')
            for word in txt_file.split():
                if word.isalpha() == False:
                    
                    dsdata += [word]
            #print(len(dsdata))
            #print(dsdata)
            write_data = []
            if v_a == 0:
                self.mta.delete(*self.mta.get_children())
                for i in range(0,int(len(dsdata)/3)):
                    write_data += [(str(i+1),dsdata[i*3],dsdata[i*3+1],'')]
            else:
                self.mta.delete(*self.mta.get_children())
                for i in range(0,int(len(dsdata)/3)):
                    write_data += [(str(i+1),dsdata[i*3],'',dsdata[i*3+2])]
            for d in write_data:
                self.mta.insert('', tk.END, values=d)
            #print(txt_file)
    def on_gor(self):
        global gr
        self.glre.configure(state = 'disabled')
        self.gore.configure(state = 'normal')
        gr = 1
    def on_glr(self):
        global gr
        self.glre.configure(state = 'normal')
        self.gore.configure(state = 'disabled')
        gr = 0
    def on_gcnext(self):
        self.c1e_out = self.c1e.get()
        self.c1u_out = self.c1u.get()
        self.o2e_out = self.o2e.get()
        self.o2u_out = self.o2u.get()
        self.gte_out = self.gte.get()
        self.gtu_out = self.gtu.get()
        self.c2e_out = self.c2e.get()
        self.c2u_out = self.c2u.get()
        self.h2e_out = self.h2e.get()
        self.h2u_out = self.h2u.get()
        self.c3e_out = self.c3e.get()
        self.c3u_out = self.c3u.get()
        self.hee_out = self.hee.get()
        self.heu_out = self.heu.get()
        self.ic4e_out = self.ic4e.get()
        self.ic4e_out = self.ic4u.get()
        self.h2oe_out = self.h2oe.get()
        self.h2ou_out = self.h2ou.get()
        self.nc4e_out = self.nc4e.get()
        self.nc4u_out = self.nc4u.get()
        self.n2e_out = self.n2e.get()
        self.n2u_out = self.n2u.get()
        self.ic5e_out = self.ic5e.get()
        self.ic5u_out = self.ic5u.get()
        self.co2e_out = self.co2e.get()
        self.co2u_out = self.co2u.get()
        self.nc5e_out = self.nc5e.get()
        self.nc5u_out = self.nc5u.get()
        self.h2se_out = self.h2se.get()
        self.h2su_out = self.h2su.get()
        self.c6e_out = self.c6e.get()
        self.c6u_out = self.c6u.get()
        self.c7pe_out = self.c7pe.get()
        self.c7pu_out = self.c7pu.get()
        self.c8e_out = self.c8e.get()
        self.c8u_out = self.c8u.get()
        self.c9e_out = self.c9e.get()
        self.c9u_out = self.c9u.get()
        self.c10e_out = self.c10e.get()
        self.c10u_out = self.c10u.get()
        self.gcmw_out = self.gcmw.get()
        self.gcsg_out = self.gcsg.get()
        self.notebook.select(tab_id = 5)
    def on_pvtnext(self):
        self.tte_out = self.tte.get()
        self.ttu_out = self.ttu.get()
        self.pu_out = self.pu.get()
        self.sgu_out = self.sgu.get()
        self.ofu_out = self.ofu.get()
        self.ovu_out = self.ovu.get()
        self.gvu_out = self.gvu.get()
        self.gfu_out = self.gfu.get()
        self.fblank.select(tab_id = 2)
    def on_flnext(self):
        global gr
        if gr == 1:
            self.gore_out = self.gore.get()
            self.goru_out = self.goru.get()
        else:
            self.glre_out = self.glre.get()
            self.glru_out = self.glru.get()
        self.floge_out = self.floge.get()
        self.flogu_out = self.flogu.get()
        self.flsge_out = self.flsge.get()
        self.flwge_out = self.flwge.get()
        self.flwce_out = self.flwce.get()
        self.flwcu_out = self.flwcu.get()
        self.flgice_out = self.flgice.get()
        self.flgicu_out = self.flgicu.get()
        self.flgihe_out = self.flgihe.get()
        self.flgihu_out = self.flgihu.get()
        self.flgine_out = self.flgine.get()
        self.flginu_out = self.flginu.get()
        self.flcmrsu_out = self.flcmrsu.get()
        self.flcmovu_out = self.flcmovu.get()
        self.flcmwvu_out = self.flcmwvu.get()
        self.flcmgvu_out = self.flcmgvu.get()
        self.flcmowmu_out = self.flcmowmu.get()
        self.flcmzfu_out = self.flcmzfu.get()
        self.flscte_out = self.flscte.get()
        self.flsctu_out = self.flsctu.get()
        self.flscpe_out = self.flscpe.get()
        self.flscpu_out = self.flscpu.get()
        self.fblank.select(tab_id = 1)
    def on_flback(self):
        self.notebook.select(tab_id = 3)
        self.flowline.select(tab_id = 1)
    def on_gcback(self):
        self.fblank.select(tab_id = 1)
    def on_pvtback(self):
        self.fblank.select(tab_id = 0)
    def on_gcsave(self):
        self.c1e_out = self.c1e.get()
        self.c1u_out = self.c1u.get()
        self.o2e_out = self.o2e.get()
        self.o2u_out = self.o2u.get()
        self.gte_out = self.gte.get()
        self.gtu_out = self.gtu.get()
        self.c2e_out = self.c2e.get()
        self.c2u_out = self.c2u.get()
        self.h2e_out = self.h2e.get()
        self.h2u_out = self.h2u.get()
        self.c3e_out = self.c3e.get()
        self.c3u_out = self.c3u.get()
        self.hee_out = self.hee.get()
        self.heu_out = self.heu.get()
        self.ic4e_out = self.ic4e.get()
        self.ic4e_out = self.ic4u.get()
        self.h2oe_out = self.h2oe.get()
        self.h2ou_out = self.h2ou.get()
        self.nc4e_out = self.nc4e.get()
        self.nc4u_out = self.nc4u.get()
        self.n2e_out = self.n2e.get()
        self.n2u_out = self.n2u.get()
        self.ic5e_out = self.ic5e.get()
        self.ic5u_out = self.ic5u.get()
        self.co2e_out = self.co2e.get()
        self.co2u_out = self.co2u.get()
        self.nc5e_out = self.nc5e.get()
        self.nc5u_out = self.nc5u.get()
        self.h2se_out = self.h2se.get()
        self.h2su_out = self.h2su.get()
        self.c6e_out = self.c6e.get()
        self.c6u_out = self.c6u.get()
        self.c7pe_out = self.c7pe.get()
        self.c7pu_out = self.c7pu.get()
        self.c8e_out = self.c8e.get()
        self.c8u_out = self.c8u.get()
        self.c9e_out = self.c9e.get()
        self.c9u_out = self.c9u.get()
        self.c10e_out = self.c10e.get()
        self.c10u_out = self.c10u.get()
        self.gcmw_out = self.gcmw.get()
        self.gcsg_out = self.gcsg.get()
    def on_pvtsave(self):
        self.tte_out = self.tte.get()
        self.ttu_out = self.ttu.get()
        self.pu_out = self.pu.get()
        self.sgu_out = self.sgu.get()
        self.ofu_out = self.ofu.get()
        self.ovu_out = self.ovu.get()
        self.gvu_out = self.gvu.get()
        self.gfu_out = self.gfu.get()
    def on_flsave(self):
        global gr
        if gr == 1:
            self.gore_out = self.gore.get()
            self.goru_out = self.goru.get()
        else:
            self.glre_out = self.glre.get()
            self.glru_out = self.glru.get()
        self.floge_out = self.floge.get()
        self.flogu_out = self.flogu.get()
        self.flsge_out = self.flsge.get()
        self.flwge_out = self.flwge.get()
        self.flwce_out = self.flwce.get()
        self.flwcu_out = self.flwcu.get()
        self.flgice_out = self.flgice.get()
        self.flgicu_out = self.flgicu.get()
        self.flgihe_out = self.flgihe.get()
        self.flgihu_out = self.flgihu.get()
        self.flgine_out = self.flgine.get()
        self.flginu_out = self.flginu.get()
        self.flcmrsu_out = self.flcmrsu.get()
        self.flcmovu_out = self.flcmovu.get()
        self.flcmwvu_out = self.flcmwvu.get()
        self.flcmgvu_out = self.flcmgvu.get()
        self.flcmowmu_out = self.flcmowmu.get()
        self.flcmzfu_out = self.flcmzfu.get()
        self.flscte_out = self.flscte.get()
        self.flsctu_out = self.flsctu.get()
        self.flscpe_out = self.flscpe.get()
        self.flscpu_out = self.flscpu.get()
    def on_gcclear(self):
        self.c1e.delete(0, 'end')
        self.c1u.delete(0, 'end')
        self.o2e.delete(0, 'end')
        self.o2u.delete(0, 'end')
        self.gte.delete(0, 'end')
        self.gtu.delete(0, 'end')
        self.c2e.delete(0, 'end')
        self.c2u.delete(0, 'end')
        self.h2e.delete(0, 'end')
        self.h2u.delete(0, 'end')
        self.c3e.delete(0, 'end')
        self.c3u.delete(0, 'end')
        self.hee.delete(0, 'end')
        self.heu.delete(0, 'end')
        self.ic4e.delete(0, 'end')
        self.ic4u.delete(0, 'end')
        self.h2oe.delete(0, 'end')
        self.h2ou.delete(0, 'end')
        self.nc4e.delete(0, 'end')
        self.nc4u.delete(0, 'end')
        self.n2e.delete(0, 'end')
        self.n2u.delete(0, 'end')
        self.ic5e.delete(0, 'end')
        self.ic5u.delete(0, 'end')
        self.co2e.delete(0, 'end')
        self.co2u.delete(0, 'end')
        self.nc5e.delete(0, 'end')
        self.nc5u.delete(0, 'end')
        self.h2se.delete(0, 'end')
        self.h2su.delete(0, 'end')
        self.c6e.delete(0, 'end')
        self.c6u.delete(0, 'end')
        self.c7pe.delete(0, 'end')
        self.c7pu.delete(0, 'end')
        self.c8e.delete(0, 'end')
        self.c8u.delete(0, 'end')
        self.c9e.delete(0, 'end')
        self.c9u.delete(0, 'end')
        self.c10e.delete(0, 'end')
        self.c10u.delete(0, 'end')
        self.gcmw.delete(0, 'end')
        self.gcsg.delete(0, 'end')
    def on_pvtclear(self):
        self.tte.delete(0, 'end')
        self.ttu.delete(0, 'end')
        self.pu.delete(0, 'end')
        self.sgu.delete(0, 'end')
        self.ofu.delete(0, 'end')
        self.ovu.delete(0, 'end')
        self.gvu.delete(0, 'end')
        self.gfu.delete(0, 'end')
        self.fltree.delete(*self.fltree.get_children())
        data = [
            ('1'),
            ('2','', '','','',''),
            ('3','', '','','',''),
            ('4','', '','','',''),
            ('5','', '','','',''),
            ('6','', '','','',''),
            ('7','', '','','',''),
            ('8'),
            ('9'),
            ('10'),
            ('11'),
            ('12'),
            ('13'),
            ('14'),
            ('15'),
            ('16')
            ]
        for d in data:
            self.fltree.insert('', tk.END, values=d)
    def on_flclear(self):
        self.gore.delete(0, 'end')
        self.goru.delete(0, 'end')
        self.glre.delete(0, 'end')
        self.glru.delete(0, 'end')
        self.floge.delete(0, 'end')
        self.flogu.delete(0, 'end')
        self.flsge.delete(0, 'end')
        self.flwge.delete(0, 'end')
        self.flwce.delete(0, 'end')
        self.flwcu.delete(0, 'end')
        self.flgice.delete(0, 'end')
        self.flgicu.delete(0, 'end')
        self.flgihe.delete(0, 'end')
        self.flgihu.delete(0, 'end')
        self.flgine.delete(0, 'end')
        self.flginu.delete(0, 'end')
        self.flcmrsu.delete(0, 'end')
        self.flcmovu.delete(0, 'end')
        self.flcmwvu.delete(0, 'end')
        self.flcmgvu.delete(0, 'end')
        self.flcmowmu.delete(0, 'end')
        self.flcmzfu.delete(0, 'end')
        self.flscte.delete(0, 'end')
        self.flsctu.delete(0, 'end')
        self.flscpe.delete(0, 'end')
        self.flscpu.delete(0, 'end')
    def on_row_edit7(self,event):
        col7, item7 = self.fltree.get_event_info()
        if col7 in ('pvt_pre','pvt_sg','pvt_of','pvt_ov','pvt_gv','pvt_gf','pvt_zf',):
                self.fltree.inplace_entry(col7, item7)
    def on_gc_ugc(self):
        global gc_ugc
        if gc_ugc ==0:
            gc_ugc = 1
            self.c1e.configure(state = 'normal')
            self.c1u.configure(state = 'normal')
            self.o2e.configure(state = 'normal')
            self.o2u.configure(state = 'normal')
            self.gte.configure(state = 'normal')
            self.gtu.configure(state = 'normal')
            self.c2e.configure(state = 'normal')
            self.c2u.configure(state = 'normal')
            self.h2e.configure(state = 'normal')
            self.h2u.configure(state = 'normal')
            self.c3e.configure(state = 'normal')
            self.c3u.configure(state = 'normal')
            self.hee.configure(state = 'normal')
            self.heu.configure(state = 'normal')
            self.ic4e.configure(state = 'normal')
            self.ic4u.configure(state = 'normal')
            self.h2oe.configure(state = 'normal')
            self.h2ou.configure(state = 'normal')
            self.nc4e.configure(state = 'normal')
            self.nc4u.configure(state = 'normal')
            self.n2e.configure(state = 'normal')
            self.n2u.configure(state = 'normal')
            self.ic5e.configure(state = 'normal')
            self.ic5u.configure(state = 'normal')
            self.co2e.configure(state = 'normal')
            self.co2u.configure(state = 'normal')
            self.nc5e.configure(state = 'normal')
            self.nc5u.configure(state = 'normal')
            self.h2se.configure(state = 'normal')
            self.h2su.configure(state = 'normal')
            self.c6e.configure(state = 'normal')
            self.c6u.configure(state = 'normal')
            self.c7pe.configure(state = 'normal')
            self.c7pu.configure(state = 'normal')
            self.c8e.configure(state = 'normal')
            self.c8u.configure(state = 'normal')
            self.c9e.configure(state = 'normal')
            self.c9u.configure(state = 'normal')
            self.c10e.configure(state = 'normal')
            self.c10u.configure(state = 'normal')
        else:
            gc_ugc = 0
            self.c1e.configure(state = 'disabled')
            self.c1u.configure(state = 'disabled')
            self.o2e.configure(state = 'disabled')
            self.o2u.configure(state = 'disabled')
            self.gte.configure(state = 'disabled')
            self.gtu.configure(state = 'disabled')
            self.c2e.configure(state = 'disabled')
            self.c2u.configure(state = 'disabled')
            self.h2e.configure(state = 'disabled')
            self.h2u.configure(state = 'disabled')
            self.c3e.configure(state = 'disabled')
            self.c3u.configure(state = 'disabled')
            self.hee.configure(state = 'disabled')
            self.heu.configure(state = 'disabled')
            self.ic4e.configure(state = 'disabled')
            self.ic4u.configure(state = 'disabled')
            self.h2oe.configure(state = 'disabled')
            self.h2ou.configure(state = 'disabled')
            self.nc4e.configure(state = 'disabled')
            self.nc4u.configure(state = 'disabled')
            self.n2e.configure(state = 'disabled')
            self.n2u.configure(state = 'disabled')
            self.ic5e.configure(state = 'disabled')
            self.ic5u.configure(state = 'disabled')
            self.co2e.configure(state = 'disabled')
            self.co2u.configure(state = 'disabled')
            self.nc5e.configure(state = 'disabled')
            self.nc5u.configure(state = 'disabled')
            self.h2se.configure(state = 'disabled')
            self.h2su.configure(state = 'disabled')
            self.c6e.configure(state = 'disabled')
            self.c6u.configure(state = 'disabled')
            self.c7pe.configure(state = 'disabled')
            self.c7pu.configure(state = 'disabled')
            self.c8e.configure(state = 'disabled')
            self.c8u.configure(state = 'disabled')
            self.c9e.configure(state = 'disabled')
            self.c9u.configure(state = 'disabled')
            self.c10e.configure(state = 'disabled')
            self.c10u.configure(state = 'disabled')
    def on_op_des(self):
        builder3 = pygubu.Builder()
        builder3.add_from_file('editabletv.ui')
        self.top4 = tk.Toplevel(self.mainwindow)
        frame3 = builder3.get_object('setting', self.top4)
        #callbacks = {}
        builder3.connect_callbacks(self)
#Default Setting
        self.gsnse = builder3.get_object('des_gsnse')
        self.gssfe = builder3.get_object('des_gssfe')
        self.gsnsu = builder3.get_object('des_gsnsu')
        self.gsnsu.current(0)
        self.gssfu = builder3.get_object('des_gssfu')
        self.gssfu.current(0)
        self.des_fpoge = builder3.get_object('des_fpoge')
        self.des_fpogu = builder3.get_object('des_fpogu')
        self.des_fpogu.current(0)
        self.des_fpsgge = builder3.get_object('des_fpsgge')
        self.des_fpsgwe = builder3.get_object('des_fpsgwe')
        self.des_dfe = builder3.get_object('des_dfe')
        self.tcd_odu = builder3.get_object('tcd_odu')
        self.tcd_odu.current(0)
        self.tcd_idu = builder3.get_object('tcd_idu')
        self.tcd_idu.current(0)
        self.tcd_wtu = builder3.get_object('tcd_wtu')
        self.tcd_wtu.current(0)
        self.tcd_ru = builder3.get_object('tcd_ru')
        self.tcd_ru.current(0)
        self.tcd_tode = builder3.get_object('tcd_tode')
        self.tcd_tide = builder3.get_object('tcd_tide')
        self.tcd_twte = builder3.get_object('tcd_twte')
        self.tcd_tre = builder3.get_object('tcd_tre')
        self.tcd_code = builder3.get_object('tcd_code')
        self.tcd_cide = builder3.get_object('tcd_cide')
        self.tcd_cwte = builder3.get_object('tcd_cwte')
        self.tcd_cre = builder3.get_object('tcd_cre')
    def on_uss_so(self):
        global uss_uo
        global uss_sim
        global uss_rm
        uss_uo = 1
        uss_sim = 0
        uss_rm = 0
    def on_uss_sim(self):
        global uss_uo
        global uss_sim
        global uss_rm
        uss_uo = 0
        uss_sim = 1
        uss_rm = 0
    def on_uss_rm(self):
        global uss_uo
        global uss_sim
        global uss_rm
        uss_uo = 0
        uss_sim = 0
        uss_rm = 1
    def on_des_ok(self):
        self.gsnse = self.gsnse.get()
        self.gssfe = self.gssfe.get()
        self.gsnsu = self.gsnsu.get()
        self.gssfu = self.gssfu.get()
        self.des_fpoge = self.des_fpoge.get()
        self.des_fpogu = self.des_fpogu.get()
        self.des_fpsgge = self.des_fpsgge.get()
        self.des_fpsgwe = self.des_fpsgwe.get()
        self.des_dfe = self.des_dfe.get()
        self.tcd_odu = self.tcd_odu.get()
        self.tcd_idu = self.tcd_idu.get()
        self.tcd_wtu = self.tcd_wtu.get()
        self.tcd_ru = self.tcd_ru.get()
        self.tcd_tode = self.tcd_tode.get()
        self.tcd_tide = self.tcd_tide.get()
        self.tcd_twte = self.tcd_twte .get()
        self.tcd_tre = self.tcd_tre.get()
        self.tcd_code = self.tcd_code.get()
        self.tcd_cide = self.tcd_cide.get()
        self.tcd_cwte = self.tcd_cwte.get()
        self.tcd_cre  = self.tcd_cre.get()
        self.top4.destroy()
        self.floge.insert(0,self.des_fpoge)
        self.flogu.set(self.des_fpogu)
        self.flsge.insert(0,self.des_fpsgge)
        self.flwge.insert(0,self.des_fpsgwe)
    def on_des_cancel(self):
        self.top4.destroy()
    def on_report(self):
        if(self.flcmrsu_out == 'VazquezAndBeggs'):
            self.flcmrsu_out = 'VASQUEZ_BEGGS'
        #print(self.flcmrsu_out,float(self.floge_out),float(self.flsge_out),float(self.flwce_out),float(self.gore_out),float(self.datatemp_out),float(self.flscpe_out),float(self.flscte_out),float(self.flgine_out),float(self.flgice_out),float(self.flgihe_out))
        BubblePnt = dFlBubblePnt(self.flcmrsu_out,float(self.floge_out),float(self.flsge_out),float(self.flwce_out),float(self.gore_out),float(self.datatemp_out),float(self.flscpe_out),float(self.flscte_out),float(self.flgine_out),float(self.flgice_out),float(self.flgihe_out))
        print(BubblePnt)
if __name__ == '__main__':
#def NewWell():
        global root1
        root1 = tkh.ThemedTk()
        root1.title('EspdPlus')
        root1.get_themes()
        #root1.set_theme("arc")
        #app1 = MyApplication(root1)
        app1 = MyApplication(root1)
        app1.run()