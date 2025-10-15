import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import os

class SistemaAsistencias:
    def __init__(self, archivo_tsv):
        self.archivo_tsv = archivo_tsv
        self.df_original = None
        self.df_asistencias = None
        self.personas_seleccionadas = set()
        
        self.cargar_datos()
        self.crear_interfaz()
    
    def cargar_datos(self):
        """Carga los datos del archivo TSV"""
        try:
            self.df_original = pd.read_csv(self.archivo_tsv, sep='\t')
            print("Datos cargados correctamente")
            print(f"Columnas disponibles: {self.df_original.columns.tolist()}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el archivo: {e}")
            return
    
    def obtener_nombres(self):
        """Extrae los nombres de las personas de la base de datos"""
        nombres = []
        
        # Buscar columnas que puedan contener nombres
        columnas_posibles = ['name', 'nombre', 'first_name', 'last_name', 'full_name', 'person']
        
        for columna in columnas_posibles:
            if columna in self.df_original.columns:
                nombres = self.df_original[columna].dropna().unique().tolist()
                print(f"Usando columna: {columna}")
                break
        
        # Si no encuentra columnas típicas, usar la primera columna que parezca contener texto
        if not nombres:
            for columna in self.df_original.columns:
                if self.df_original[columna].dtype == 'object':  # Columnas de texto
                    sample_value = str(self.df_original[columna].iloc[0])
                    if len(sample_value) > 2 and any(c.isalpha() for c in sample_value):
                        nombres = self.df_original[columna].dropna().unique().tolist()
                        print(f"Usando columna por defecto: {columna}")
                        break
        
        return nombres
    
    def crear_interfaz(self):
        """Crea la interfaz gráfica del sistema"""
        self.ventana = tk.Tk()
        self.ventana.title("Sistema de Control de Asistencias")
        self.ventana.geometry("600x700")
        self.ventana.configure(bg='#f0f0f0')
        
        # Título
        titulo = tk.Label(self.ventana, 
                         text="Sistema de Asistencias", 
                         font=('Arial', 16, 'bold'),
                         bg='#f0f0f0',
                         fg='#333333')
        titulo.pack(pady=10)
        
        # Frame para controles
        frame_controles = tk.Frame(self.ventana, bg='#f0f0f0')
        frame_controles.pack(pady=10)
        
        # Botón seleccionar/deseleccionar todos
        btn_todos = tk.Button(frame_controles,
                             text="Seleccionar Todos",
                             command=self.seleccionar_todos,
                             bg='#4CAF50',
                             fg='white',
                             font=('Arial', 10))
        btn_todos.pack(side=tk.LEFT, padx=5)
        
        btn_ninguno = tk.Button(frame_controles,
                               text="Deseleccionar Todos",
                               command=self.deseleccionar_todos,
                               bg='#f44336',
                               fg='white',
                               font=('Arial', 10))
        btn_ninguno.pack(side=tk.LEFT, padx=5)
        
        # Botón guardar asistencias
        btn_guardar = tk.Button(frame_controles,
                               text="Guardar Asistencias",
                               command=self.guardar_asistencias,
                               bg='#2196F3',
                               fg='white',
                               font=('Arial', 10, 'bold'))
        btn_guardar.pack(side=tk.LEFT, padx=5)
        
        # Frame para la lista con scrollbar
        frame_lista = tk.Frame(self.ventana)
        frame_lista.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Scrollbar
        scrollbar = tk.Scrollbar(frame_lista)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Lista de personas con checkboxes
        self.lista_personas = tk.Listbox(frame_lista, 
                                        yscrollcommand=scrollbar.set,
                                        selectmode=tk.MULTIPLE,
                                        font=('Arial', 11),
                                        bg='white')
        self.lista_personas.pack(fill=tk.BOTH, expand=True)
        
        scrollbar.config(command=self.lista_personas.yview)
        
        # Contador
        self.contador = tk.Label(self.ventana,
                                text="Personas seleccionadas: 0",
                                font=('Arial', 12),
                                bg='#f0f0f0',
                                fg='#333333')
        self.contador.pack(pady=10)
        
        # Cargar nombres en la lista
        self.cargar_lista_personas()
        
        # Bind events
        self.lista_personas.bind('<<ListboxSelect>>', self.actualizar_contador)
    
    def cargar_lista_personas(self):
        """Carga los nombres en la lista"""
        nombres = self.obtener_nombres()
        
        if not nombres:
            messagebox.showwarning("Advertencia", 
                                 "No se encontraron nombres en la base de datos.\n"
                                 "Columnas disponibles:\n" + 
                                 "\n".join(self.df_original.columns.tolist()))
            return
        
        for nombre in sorted(nombres):
            self.lista_personas.insert(tk.END, nombre)
    
    def seleccionar_todos(self):
        """Selecciona todas las personas"""
        self.lista_personas.selection_set(0, tk.END)
        self.actualizar_contador()
    
    def deseleccionar_todos(self):
        """Deselecciona todas las personas"""
        self.lista_personas.selection_clear(0, tk.END)
        self.actualizar_contador()
    
    def actualizar_contador(self, event=None):
        """Actualiza el contador de personas seleccionadas"""
        seleccionados = self.lista_personas.curselection()
        self.contador.config(text=f"Personas seleccionadas: {len(seleccionados)}")
    
    def obtener_personas_seleccionadas(self):
        """Obtiene la lista de personas seleccionadas"""
        seleccionados = self.lista_personas.curselection()
        personas = [self.lista_personas.get(i) for i in seleccionados]
        return personas
    
    def guardar_asistencias(self):
        """Guarda las asistencias en un archivo CSV"""
        personas_presentes = self.obtener_personas_seleccionadas()
        
        if not personas_presentes:
            messagebox.showwarning("Advertencia", "No hay personas seleccionadas")
            return
        
        # Crear DataFrame de asistencias
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        datos_asistencias = {
            'Nombre': personas_presentes,
            'Asistencia': ['Presente'] * len(personas_presentes),
            'Fecha_Registro': [fecha_actual] * len(personas_presentes),
            'Timestamp': [datetime.now()] * len(personas_presentes)
        }
        
        self.df_asistencias = pd.DataFrame(datos_asistencias)
        
        # Guardar archivo
        nombre_archivo = f"asistencias_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        
        try:
            self.df_asistencias.to_csv(nombre_archivo, index=False, encoding='utf-8')
            
            # Mostrar resumen
            resumen = f"Asistencias guardadas exitosamente!\n\n"
            resumen += f"Archivo: {nombre_archivo}\n"
            resumen += f"Total de presentes: {len(personas_presentes)}\n"
            resumen += f"Fecha: {fecha_actual}\n\n"
            resumen += "Personas presentes:\n" + "\n".join(f"• {nombre}" for nombre in personas_presentes)
            
            messagebox.showinfo("Éxito", resumen)
            print(f"Asistencias guardadas en: {nombre_archivo}")
            print(f"Total de personas presentes: {len(personas_presentes)}")
            
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")
    
    def ejecutar(self):
        """Ejecuta la aplicación"""
        self.ventana.mainloop()

# Función principal
def main():
    # Especifica la ruta de tu archivo TSV
    archivo_tsv = r'D:\Code_\Workflow\python\Base de datos\archive\dobs.tsv'
    
    # Verificar que el archivo existe
    if not os.path.exists(archivo_tsv):
        print(f"Error: El archivo {archivo_tsv} no existe")
        # Buscar archivos TSV en el directorio
        directorio = os.path.dirname(archivo_tsv)
        if os.path.exists(directorio):
            archivos_tsv = [f for f in os.listdir(directorio) if f.endswith('.tsv')]
            if archivos_tsv:
                print(f"Archivos TSV encontrados: {archivos_tsv}")
        return
    
    # Crear y ejecutar el sistema
    sistema = SistemaAsistencias(archivo_tsv)
    sistema.ejecutar()

if __name__ == "__main__":
    main()