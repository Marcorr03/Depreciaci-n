import tkinter as tk
from tkinter import ttk
import time
import json
import xml.etree.ElementTree as ET
import os

app= tk.Tk()
app.title("Depreciacion Activos")
app.geometry("1350x700")
Activo={}
ListaActivos={"Activos":[]}
Act_L={}
ListaAct_L={"Activos_L":[]}
Act_S={}
ListaAct_S={"Activos_S":[]}
sum=0

root=ET.Element("Activos")
class Activos:
    
    def mensaje (dato): 
        mensaje_label = ttk.Label(app, text=dato)
        mensaje_label.pack() 
        app.update()
        time.sleep(2)
        mensaje_label.destroy()
 
    def eliminar_todos_los_widgets():
        for widget in app.winfo_children():
            widget.destroy()
 
    def Pantalla_Activos():
        Activos.eliminar_todos_los_widgets()
        Activos_Lab=tk.Label(app,text="ACTIVOS  WENSOFT", font=("Arial",28))
        Activos_Lab.place(x=450,y=50)

        Identificador_Lab=tk.Label(app,text="Identificador",font=("Arial",14))
        Identificador_Lab.place(x=65,y=150,height=30,width=250)
        global Identificador_entry,Nombre_entry,Responsable_entry,VMonetario_entry, VMonetarioR_entry, VidaUtil_entry 
        Identificador_entry=tk.Entry(app,validate="key", validatecommand=(app.register(lambda char: char.isalnum( )), '%S'))
        Identificador_entry.place(x=350,y=150,height=30,width=250) 
        Nombre_Lab=tk.Label(app,text="Nombre del activo",font=("Arial",14))
        Nombre_Lab.place(x=90,y=225,height=30,width=250)
        Nombre_entry=tk.Entry(app,validate="key", validatecommand=(app.register(lambda char: char.isalpha()), '%S'))
        Nombre_entry.place(x=350,y=225,height=30,width=250)
        Responsable_Lab=tk.Label(app,text="Responsable",font=("Arial",14))
        Responsable_Lab.place(x=70,y=300,height=30,width=250)
        Responsable_entry=tk.Entry(app,)
        Responsable_entry.place(x=350,y=300,height=30,width=250)
        VMonetario_Lab=tk.Label(app,text="Valor monetario",font=("Arial",14))
        VMonetario_Lab.place(x=80,y=375,height=30,width=250)
        VMonetario_entry=tk.Entry(app,validate="key", validatecommand=(app.register(lambda char: char.isdigit()), '%S'))
        VMonetario_entry.place(x=350,y=375,height=30,width=250)
        VMonetarioR_Lab=tk.Label(app,text="Valor monetario rescate ",font=("Arial",14))
        VMonetarioR_Lab.place(x=115,y=450,height=30,width=250)
        VMonetarioR_entry=tk.Entry(app,validate="key", validatecommand=(app.register(lambda char: char.isdigit()), '%S'))
        VMonetarioR_entry.place(x=350,y=450,height=30,width=250)
        VidaUtil_Lab=tk.Label(app,text="Valor vida útil (años) ",font=("Arial",14))
        VidaUtil_Lab.place(x=100,y=525,height=30,width=250)
        VidaUtil_entry=tk.Entry(app,validate="key", validatecommand=(app.register(lambda char: char.isdigit()), '%S'))
        VidaUtil_entry.place(x=350,y=525,height=30,width=250)

        Bt_Ingresar=tk.Button(app,text="Ingresar",font=("Arial",15),command=Activos.InsertarActivos)
        Bt_Ingresar.place(x=900,y=200,height=50,width=150)
        Bt_Editar=tk.Button(app,text="Editar",font=("Arial",15),command=Activos.EditarActivos)
        Bt_Editar.place(x=900,y=250,height=50,width=150)
        Bt_Eliminar=tk.Button(app,text="Eliminar",font=("Arial",15),command=Activos.EliminarActivos)
        Bt_Eliminar.place(x=900,y=300,height=50,width=150)
        Bt_Consultar=tk.Button(app,text="Consultar",font=("Arial",15),command=Activos.ConsultarActivos)
        Bt_Consultar.place(x=900,y=350,height=50,width=150)
        Bt_Regresar=tk.Button(app,text="Regresar",font=("Arial",15),command=Activos.Menu)
        Bt_Regresar.place(x=1050,y=550,height=50,width=150)
            
         
    def Pantalla_Depreciacion():
        Activos.eliminar_todos_los_widgets() 
        global activo_dep_entry,Metodo_Dep_combo,Vh_entry,Vhr_entry,VU_entry 
        Depreciacion_A=tk.Label(app,text="CALCULO DEPRECIACION DE ACTIVOS", font=("Arial",28))
        Depreciacion_A.place(x=300,y=50)

        activo_dep=tk.Label(app, text="Identificador del activo",font=("Arial",12))
        activo_dep.place(x=50,y=150,height=30,width=200)
        activo_dep_entry=tk.Entry(app,validate="key", validatecommand=(app.register(lambda char: char.isalnum()), '%S'))
        activo_dep_entry.place(x=250,y=150,height=30,width=170)
        Metodo_Dep_lab=tk.Label(app, text="Metodo depreciacion",font=("Arial",12))
        Metodo_Dep_lab.place(x=45,y=200,height=30,width=200)
        Op_met=["Linea recta","Suma de los digitos"]
        Metodo_Dep_combo=ttk.Combobox(app,values=Op_met,font=("Arial",12))
        Metodo_Dep_combo.place(x=250,y=200,height=30,width=170)

        Vh=tk.Label(app,text="Valor Monetario", font=("Arial",9))
        Vh.place(x=6,y=300,height=20,width=250)
        Vh_entry=tk.Entry(app)
        Vh_entry.place(x=250,y=300,height=20,width=170)
        Vhr=tk.Label(app,text="Valor Monetario Rescate", font=("Arial",9))
        Vhr.place(x=32,y=350,height=20,width=250)
        Vhr_entry=tk.Entry(app)
        Vhr_entry.place(x=250,y=350,height=20,width=170)
        VU=tk.Label(app,text="Valor vida Util", font=("Arial",9))
        VU.place(x=1,y=400,height=20,width=250)
        VU_entry=tk.Entry(app)
        VU_entry.place(x=250,y=400,height=20,width=170)

        Bt_Consultar=tk.Button(app,text="Borrar datos",font=("Arial",15),command=Activos.Borrar_d_Calc)
        Bt_Consultar.place(x=620,y=560,height=50,width=150)
        Bt_Consultar=tk.Button(app,text="Consultar",font=("Arial",15),command=Activos.Calculodepreciaciones)
        Bt_Consultar.place(x=780,y=560,height=50,width=150)
        BT_Guardar_Dep=tk.Button(app,text="Guardar",font=("Arial",15),command=Activos.guardardepreciacion )
        BT_Guardar_Dep.place(x=940,y=560,height=50,width=150)
        Bt_Regresar=tk.Button(app,text="Regresar",font=("Arial",15),command=Activos.Menu)
        Bt_Regresar.place(x=1100,y=560,height=50,width=150)
   
    def Pantalla_linea_recta():  
        global Linea_R_Lab,TablaLinea,Act_L
        Linea_R_Lab=tk.Label(app,text="CALCULO LINEA RECTA", font=("Arial",18))
        Linea_R_Lab.place(x=670,y=200)

        TablaLinea=ttk.Treeview(app,columns=("V_Act", "Anos", "Dep_Anual","Dep_Acumulada", "V_libros"),show="headings")
        TablaLinea.heading("V_Act",text="Valor_Activo")
        TablaLinea.heading("Anos",text="Ano")
        TablaLinea.heading("Dep_Anual",text="Depreciacion Anual")
        TablaLinea.heading("Dep_Acumulada",text="Depreciacion Acumulada")
        TablaLinea.heading("V_libros",text="Valor en libros")
        
        TablaLinea.column("V_Act", width=150)
        TablaLinea.column("Anos", width=60)
        TablaLinea.column("Dep_Anual", width=150)
        TablaLinea.column("Dep_Acumulada", width=150)
        TablaLinea.column("V_libros", width=150) 
    
        for i in range(int(VU_entry.get()) + 1):
            if i == 0:
                Valor_Act=int(Vh_entry.get())
                Depre_A = 0
                Depre_Acu = 0
                VL = int(Vh_entry.get() )
            else:
                Valor_Act=int(Vh_entry.get())
                Depre_A = (int(Vh_entry.get())-int(Vhr_entry.get()) )/int(VU_entry.get())
                Depre_Acu = Depre_A * i
                VL = Valor_Act - Depre_Acu   
            Act_L= {"Valor_historico": Valor_Act,"Ano": i ,"Depreciacion_Anual":Depre_A, "Depreciacion_Acumulada":Depre_Acu,"Valor_libros":VL}       
             
            TablaLinea.insert("", tk.END, values=(Valor_Act ,i,Depre_A if i != 0 else '', Depre_Acu if i > 0 else '', VL))
            ListaAct_L["Activos_L"].extend([Act_L])
           
        TablaLinea.place(x=530,y=270) 
  
    def Pantalla_suma_digitos():  
        global Sum_entry,sum_LAB,TablaSuma,Sum_Lab,Act_S
        Sum_Lab=tk.Label(app,text="CALCULO SUMA DE DIGITOS", font=("Arial",18))
        Sum_Lab.place(x=650,y=200)
        sum_LAB=tk.Label(app,text="Suma de los años",font=("Arial",9))
        sum_LAB.place(x=52,y=450,height=20,width=170)
        Sum_entry=tk.Entry(app )
        Sum_entry.place(x=250,y=450,height=20,width=170)

        TablaSuma=ttk.Treeview(app,columns=("Anos","Valor_his" ,"Costo_D","S.D.A", "Imp.dep","Dep_Acumulada","V_librosS"),show="headings")
        TablaSuma.heading("Anos",text="Anos")
        TablaSuma.heading("Valor_his",text="Valor historico")
        TablaSuma.heading("Costo_D",text="Costo_Depreciable")
        TablaSuma.heading("S.D.A",text="s.d.a")
        TablaSuma.heading("Imp.dep",text="Importe Depreciacion")
        TablaSuma.heading("Dep_Acumulada",text="Depreciacion Acumulada")
        TablaSuma.heading("V_librosS",text="Valor Libros")

        TablaSuma.column("Anos", width=40)
        TablaSuma.column("Valor_his", width=90)
        TablaSuma.column("Costo_D", width=110)
        TablaSuma.column("S.D.A",width=60)
        TablaSuma.column("Imp.dep",width=150)
        TablaSuma.column("Dep_Acumulada",width=150)
        TablaSuma.column("V_librosS",width=110)
        global sum
        sum=0
        for i in range(int(VU_entry.get()) + 1):
            sum=sum+i
        
        for i in range(int(VU_entry.get()) + 1): 
            if i == 0: 
                Des=0
                Valor_h=int(Vh_entry.get())
                Costo_Dep = 0
                SDA = 0
                Imp_dep=0
                Dep_Acu =0 
                VL = int(Vh_entry.get() )
            else:
                if Des==0:
                    Des=int(VU_entry.get())+1
                Des= Des - 1
                Valor_h=int(Vh_entry.get())
                Costo_Dep = int(Vh_entry.get())-int(Vhr_entry.get()) 
                SDA =Des / sum
                Imp_dep=SDA*Costo_Dep
                Dep_Acu=Imp_dep+Dep_Acu
                VL = Valor_h - Dep_Acu
            Act_S={"Suma anos":sum,"Ano": i ,"Valor_historico": Valor_h ,"Costo_depreciable":Costo_Dep, "SDA":SDA,"Importe_Depreciable": Imp_dep,"Depreciacion_Acumulada":Dep_Acu,"Valor_libros":VL}      
            print( Des ,sum)
             
             
            TablaSuma.insert("", tk.END, values=( i,Valor_h,Costo_Dep if i != 0 else '', SDA if i > 0 else '',Imp_dep if i > 0 else '',Dep_Acu if i > 0 else '', VL))
            ListaAct_S["Activos_S"].extend([Act_S])
        Sum_entry.insert(0,sum)
        Sum_entry.config(state='readonly')
        TablaSuma.place(x=530,y=270) 
        print( ListaAct_S["Activos_S"])  

    def ConsultarDepreciaciones():
      Activos.eliminar_todos_los_widgets() 
      global Activo_depC_entry,Metodo_Dep_entry
      Depreciacion_A=tk.Label(app,text="CONSULTAR DEPRECIACION DE ACTIVOS", font=("Arial",28))
      Depreciacion_A.place(x=260,y=50) 
      Activo_depC=tk.Label(app, text="Identificador del activo",font=("Arial",12))
      Activo_depC.place(x=50,y=150,height=30,width=200)
      Activo_depC_entry=tk.Entry(app,validate="key", validatecommand=(app.register(lambda char: char.isalnum()), '%S'))
      Activo_depC_entry.place(x=250,y=150,height=30,width=190)
      Metodo_Dep_lab=tk.Label(app, text="Metodo depreciacion",font=("Arial",12))
      Metodo_Dep_lab.place(x=500,y=150,height=30,width=200)
      Op_met=["Linea recta","Suma de los digitos"]
      Metodo_Dep_entry=ttk.Combobox(app,values=Op_met,font=("Arial",12))
      Metodo_Dep_entry.place(x=680,y=150,height=30,width=170) 

      Bt_Consultar=tk.Button(app,text="Consultar",font=("Arial",15),command=Activos.Mostrar_depreciacion)
      Bt_Consultar.place(x=750,y=560,height=50,width=150)
      Bt_Eli=tk.Button(app,text="Borrar datos",font=("Arial",15),command=Activos.limpiar_tabla)
      Bt_Eli.place(x=900,y=560,height=50,width=150)
      Bt_Regresar=tk.Button(app,text="Regresar",font=("Arial",15),command=Activos.Menu)
      Bt_Regresar.place(x=1050,y=560,height=50,width=150) 
    
    def llenardicc(arc):
        with open(arc,"r")as file:
            datosJSON=json.load(file)["Activos"] 
            ListaActivos["Activos"].extend(datosJSON)  
            print(ListaActivos)
 
    def Menu():  
        if os.path.exists("Activos_CR.json"):
            print(ListaActivos["Activos"])
            if(ListaActivos["Activos"]==[]):
                Activos.llenardicc("Activos_CR.json")
                
        Activos.eliminar_todos_los_widgets() 
        Menu_Lab=tk.Label(app,text="MENU WENSOFT",font=("Arial",28) )
        Menu_Lab.place(x=470,y=100,height=80,width=300)
        Bt_Activos=tk.Button(app, text="Activos",font=("Arial",18),command=Activos.Pantalla_Activos) 
        Bt_Activos.place(x=100,y=300, height=60,width=170)
        Bt_Dep=tk.Button(app, text="Calcular depreciacion ",font=("Arial",18),command=Activos.Pantalla_Depreciacion) 
        Bt_Dep.place(x=300,y=300, height=60,width=260) 
        Bt_hist=tk.Button(app,text="Historial depreciaciones",font=("Arial",18),command=Activos.ConsultarDepreciaciones) 
        Bt_hist.place(x=600,y=300, height=60,width=280) 
        Bt_ManejoArc=tk.Button(app,text="Manejo Archivos",font=("Arial",18),command=Activos.GenerarArchivos)
        Bt_ManejoArc.place(x=900,y=300, height=60,width=280)
        Bt_Salir=tk.Button(app,text="Salir",font=("Arial",15),command=app.destroy)
        Bt_Salir.place(x=1100,y=560,height=50,width=150)
       
    def GenerarArchivos():  
        Activos.eliminar_todos_los_widgets() 
        MAN_lab=tk.Label(app,text="Manejo archivos",font=("Arial",28) )
        MAN_lab.place(x=470,y=100,height=80,width=300)
        bt_JSON_lab=tk.Button(app,text="Generar JSON",command=lambda:Activos.escribir_JSON(ListaActivos))
        bt_JSON_lab.place(x=180,y=300,height=70,width=280)
        bt_verificacionJSON=tk.Button(app,text="Verificar JSON",command=Activos.VerificarJSON)
        bt_verificacionJSON.place(x=480,y=300,height=70,width=280)
        bt_XML_lab=tk.Button(app,text="Generar Backup",command=Activos.GenerarXML)
        bt_XML_lab.place(x=780,y=300,height=70,width=280)
        
        Bt_Regresar=tk.Button(app,text="Regresar",font=("Arial",15),command=Activos.Menu)
        Bt_Regresar.place(x=1100,y=560,height=50,width=150)
        
        

    def InsertarActivos():
    
        if not Identificador_entry.get() or not Nombre_entry.get() or not Responsable_entry.get() or not VMonetario_entry.get() or not VMonetarioR_entry.get() or not VidaUtil_entry.get():
            Activos.mensaje("Todos los campos deben tener datos")
            return
    
        if int(VMonetario_entry.get()) <= 0 or int(VMonetarioR_entry.get()) <= 0 or int(VidaUtil_entry.get()) <= 0 or int(VidaUtil_entry.get()) >= 7:
            Activos.mensaje("Valores monetarios deben ser mayores a 0 y vida útil debe ser mayor a 0 y menor a 7")
            return

        identificador_ya_existe=False
        for activo in ListaActivos["Activos"]:
            if activo["ID"] == Identificador_entry.get():
                identificador_ya_existe = True
            
                
        if identificador_ya_existe:
            Activos.mensaje("El identificador del activo ya existe")
        else:
            Activo={"ID":Identificador_entry.get(),"Nombre": Nombre_entry.get(),"Responsable": Responsable_entry.get(),"Vmonetario": VMonetario_entry.get(), "VmonetarioR":VMonetarioR_entry.get(),"VvidaU": VidaUtil_entry.get(),"Depreciacion_Lineal":[ListaAct_L["Activos_L"]],"Suma de los anos":sum,"Depreciacion_Suma_Digitos":[ListaAct_S["Activos_S"]]}
            ListaActivos["Activos"].extend([Activo])
            print(ListaActivos)
            Activos.limpiarentry()
            Activos.mensaje("Activo insertado correctamente")
            identificador_ya_existe = False 
  
    def EditarActivos():
        if not Identificador_entry.get() or not Nombre_entry.get() or not Responsable_entry.get() or not VMonetario_entry.get() or not VMonetarioR_entry.get() or not VidaUtil_entry.get():
            Activos.mensaje("Todos los campos deben tener datos")
            return
        
        if int(VMonetario_entry.get()) <= 0 or int(VMonetarioR_entry.get()) <= 0 or int(VidaUtil_entry.get() )<= 0 or int(VidaUtil_entry.get()) >= 7:
            Activos.mensaje("Valores monetarios deben ser mayores a 0 y vida útil debe ser mayor a 0 y menor a 7")
            return
        
        for activo in ListaActivos["Activos"]:
            if Identificador_entry.get()==activo["ID"]: 
                activo["Nombre"]=Nombre_entry.get()
                activo["Responsable"]=Responsable_entry.get()
                activo["Vmonetario"]=VMonetario_entry.get()
                activo["VmonetarioR"]=VMonetarioR_entry.get()
                activo["VvidaU"]=VidaUtil_entry.get() 
                print(ListaActivos["Activos"])
                Activos.limpiarentry()
                break
    
   

    def EliminarActivos():
        if not Identificador_entry.get():
            return Activos.mensaje("Debe ingresar un identificador para eliminar")
        
        for activo in ListaActivos["Activos"]:
            if Identificador_entry.get()==activo["ID"]: 
                return Activos.mensaje("El identificador no existe")

        for activo in ListaActivos["Activos"]:
            if Identificador_entry.get()==activo["ID"]:
                ListaActivos["Activos"].remove(activo)
                Activos.limpiarentry()
                print(ListaActivos)
                break        
              

    def ConsultarActivos():
       for activo in ListaActivos["Activos"]:
            if Identificador_entry.get()==activo["ID"]:
                Nombre_entry.insert(0,activo["Nombre"])
                Responsable_entry.insert(0,activo["Responsable"])
                VMonetario_entry.insert(0,activo["Vmonetario"])
                VMonetarioR_entry.insert(0,activo["VmonetarioR"])
                VidaUtil_entry.insert(0,activo["VvidaU"]) 
                    
    def limpiarentry():    
        Identificador_entry.delete(0,tk.END),Nombre_entry.delete(0,tk.END),Responsable_entry.delete(0,tk.END),VMonetario_entry.delete(0,tk.END), VMonetarioR_entry.delete(0,tk.END), VidaUtil_entry.delete(0,tk.END)

    def Sel_Met():
       if Seleccion=="Linea recta":
           Activos.Pantalla_linea_recta()
       elif Seleccion=="Suma de los digitos":
           Activos.Pantalla_suma_digitos()
    
    def Calculodepreciaciones():

        if not activo_dep_entry.get():
            Activos.mensaje("Debe ingresar el identificador del activo a calcular")
            return

        if not Metodo_Dep_combo.get():
            Activos.mensaje("Seleccione el metodo a calcular")
            return

        global Seleccion
        Seleccion = Metodo_Dep_combo.get() 
        print(ListaActivos["Activos"])
        for activo in ListaActivos["Activos"]:
            if activo_dep_entry.get()==activo["ID"]:   
                Vh_entry.insert(0,activo["Vmonetario"])
                Vhr_entry.insert(0,activo["VmonetarioR"])
                VU_entry.insert(0,activo["VvidaU"]) 
                Vh_entry.config(state='readonly'),Vhr_entry.config(state='readonly'),VU_entry.config(state='readonly') 
        Activos.Sel_Met()
            
    def guardardepreciacion ():
        for activo in ListaActivos["Activos"]:
            if activo_dep_entry.get()==activo["ID"]: 
                if Seleccion=="Linea recta":
                    activo["Depreciacion_Lineal"]=ListaAct_L
                elif Seleccion=="Suma de los digitos": 
                    activo["Suma de los anos"]=Sum_entry.get()
                    activo["Depreciacion_Suma_Digitos"]=ListaAct_S 
                  
            print(ListaActivos )
                    
            
            Activos.Borrar_d_Calc() 
            break

    def Borrar_d_Calc(): 
        Seleccion = Metodo_Dep_combo.get() 
        if Seleccion=="Linea recta":
            Vh_entry.config(state='normal'),Vhr_entry.config(state='normal'),VU_entry.config(state='normal'),VU_entry.config(state='normal')
            activo_dep_entry.delete(0,tk.END),Metodo_Dep_combo.delete(0,tk.END),Vh_entry.delete(0,tk.END),Vhr_entry.delete(0,tk.END),VU_entry.delete(0,tk.END)
            Linea_R_Lab.destroy()
            TablaLinea.destroy()
        elif Seleccion=="Suma de los digitos":
            Sum_entry.config(state='normal'),Vh_entry.config(state='normal'),Vhr_entry.config(state='normal'),VU_entry.config(state='normal'),VU_entry.config(state='normal')
            activo_dep_entry.delete(0,tk.END),Metodo_Dep_combo.delete(0,tk.END),Vh_entry.delete(0,tk.END),Vhr_entry.delete(0,tk.END),VU_entry.delete(0,tk.END),Sum_entry.delete(0,tk.END)
            Sum_entry.destroy()
            sum_LAB.destroy()
            TablaSuma.destroy()
            Sum_Lab.destroy()
            
        
    def GenerarXML():
        Activos.leer_JSON()
        Activos.escribir_XML(datosJSON)
    
    def escribir_JSON( ListaActivos):
        with open ("Activos_CR.json","w") as file:
            json.dump(ListaActivos,file) 

    def leer_JSON():
        global datosJSON
        with open ("Activos_CR.json","r") as file:
             datosJSON= json.load(file) 
         
    def escribir_XML(datosJSON):
        # Recorrer cada activo en los datos JSON
        for activo in datosJSON["Activos"]:

            # Crear un subelemento para cada activo
            activo_element = ET.SubElement(root, "Activo")
        
            # Añadir los atributos del activo
            for key, value in activo.items():
                if isinstance(value, dict):
                    # Si el valor es un diccionario (como Depreciacion_Lineal), agregar sus elementos
                    subelement = ET.SubElement(activo_element, key)
                    for subkey, subvalue in value.items():
                        if isinstance(subvalue, list):
                            for item in subvalue:
                                item_element = ET.SubElement(subelement, subkey[:-1])
                                for item_key, item_value in item.items():
                                    item_sub_element = ET.SubElement(item_element, item_key)
                                    item_sub_element.text = str(item_value)
                        else:
                            subelement_sub = ET.SubElement(subelement, subkey)
                            subelement_sub.text = str(subvalue)
                elif isinstance(value, list):
                    subelement = ET.SubElement(activo_element, key)
                    for item in value:
                        item_element = ET.SubElement(subelement, "Item")
                        for item_key, item_value in item.items():
                            item_sub_element = ET.SubElement(item_element, item_key)
                            item_sub_element.text = str(item_value)
                else:
                    # Añadir subelemento para cada atributo del activo
                    subelement = ET.SubElement(activo_element, key)
                    subelement.text = str(value)
    
        # Crear un objeto ElementTree
        tree = ET.ElementTree(root)

        # Escribir el árbol en un archivo
        with open("Activos_CR.xml", "wb") as file:
         tree.write(file, encoding="utf-8", xml_declaration=True)

    def VerificarJSON():
        pass    
   
    def limpiar_tabla():
        Metodo_Dep_entry.config(state="normal"), Activo_depC_entry.config(state="normal")
        Seleccion=Metodo_Dep_entry.get() 
        Activo_depC_entry.delete(0,tk.END),Metodo_Dep_entry.delete(0,tk.END)
        if Seleccion=="Linea recta":
                Linea_R_Lab.destroy()
                TablaLinea.destroy()
        elif Seleccion=="Suma de los digitos":
                sum_LAB_Lab.destroy(),sum_LAB.destroy(),Sum_entry.destroy()
                TablaSuma.destroy()

    def Mostrar_depreciacion():
        global Linea_R_Lab,TablaLinea,sum_LAB,sum_LAB_Lab,TablaSuma,Sum_entry,sum_LAB_Lab

        if not Activo_depC_entry.get():
            Activos.mensaje("Debe ingresar el identificador del activo a calcular")
            return

        if not Metodo_Dep_entry.get():
            Activos.mensaje("Seleccione el metodo a calcular")
            return

        for activo in ListaActivos["Activos"]:
            if Activo_depC_entry.get()==activo["ID"]:
                Seleccion=Metodo_Dep_entry.get() 
                if Seleccion=="Linea recta":
                    Linea_R_Lab=tk.Label(app,text="CALCULO LINEA RECTA", font=("Arial",18))
                    Linea_R_Lab.place(x=440,y=250)

                    TablaLinea=ttk.Treeview(app,columns=("V_Act", "Anos", "Dep_Anual","Dep_Acumulada", "V_libros"),show="headings")
                    TablaLinea.heading("V_Act",text="Valor_Activo")
                    TablaLinea.heading("Anos",text="Ano")
                    TablaLinea.heading("Dep_Anual",text="Depreciacion Anual")
                    TablaLinea.heading("Dep_Acumulada",text="Depreciacion Acumulada")
                    TablaLinea.heading("V_libros",text="Valor en libros")
                    
                    TablaLinea.column("V_Act", width=150)
                    TablaLinea.column("Anos", width=60)
                    TablaLinea.column("Dep_Anual", width=150)
                    TablaLinea.column("Dep_Acumulada", width=150)
                    TablaLinea.column("V_libros", width=150) 
                    for activo in ListaActivos["Activos"] :  
                        if(activo["Depreciacion_Lineal"]!=[[]]):
                            for datos in activo["Depreciacion_Lineal"]["Activos_L"]:  
                                print(datos["Valor_historico"])
                                TablaLinea.insert("", tk.END, values=(datos["Valor_historico"] ,datos["Ano"],datos["Depreciacion_Anual"], datos["Depreciacion_Acumulada"], datos["Valor_libros"]))
                    

                    TablaLinea.place(x=300,y=290)

                elif Seleccion=="Suma de los digitos":
                    sum_LAB_Lab=tk.Label(app,text="CALCULO SUMA DE DIGITOS", font=("Arial",18))
                    sum_LAB_Lab.place(x=550,y=250)

                    sum_LAB=tk.Label(app,text="Suma de los años",font=("Arial",9))
                    sum_LAB.place(x=70,y=250)
                    Sum_entry=tk.Entry(app )
                    Sum_entry.place(x=190,y=250,height=20,width=100)
                    Sum_entry.insert(0,activo["Suma de los anos"])

                    TablaSuma=ttk.Treeview(app,columns=( "Anos","Valor_his" ,"Costo_D","S.D.A", "Imp.dep","Dep_Acumulada","V_librosS"),show="headings")
                    TablaSuma.heading("Anos",text="Anos")
                    TablaSuma.heading("Valor_his",text="Valor historico")
                    TablaSuma.heading("Costo_D",text="Costo_Depreciable")
                    TablaSuma.heading("S.D.A",text="s.d.a")
                    TablaSuma.heading("Imp.dep",text="Importe Depreciacion")
                    TablaSuma.heading("Dep_Acumulada",text="Depreciacion Acumulada")
                    TablaSuma.heading("V_librosS",text="Valor Libros")

                    TablaSuma.column("Anos", width=40)
                    TablaSuma.column("Valor_his", width=90)
                    TablaSuma.column("Costo_D", width=110)
                    TablaSuma.column("S.D.A",width=60)
                    TablaSuma.column("Imp.dep",width=150)
                    TablaSuma.column("Dep_Acumulada",width=150)
                    TablaSuma.column("V_librosS",width=110)
                    for activo in ListaActivos["Activos"]:  
                        if(activo["Depreciacion_Suma_Digitos"]!=[[]]):
                            for datos in activo["Depreciacion_Suma_Digitos"]["Activos_S"]:      
                                TablaSuma.insert("", tk.END, values=(datos["Ano"],datos["Valor_historico"],datos["Costo_depreciable"], datos["SDA"], datos["Importe_Depreciable"],datos["Depreciacion_Acumulada"],datos["Valor_libros"]))
                
                    TablaSuma.place(x=400,y=290)
            print(ListaActivos )
            Metodo_Dep_entry.config(state="readonly"), Activo_depC_entry.config(state="readonly")
            break

        
        
        
        

Activos.Menu()  

app.mainloop()
