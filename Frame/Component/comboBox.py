def cargarDatos(opcion):
    if(opcion=="e-Flow"):return ["Instalador de servicio","Creador de site","Creador de aplicacion","Modificador de puerto","Emission.config","Consola","RHI", "NME","Nodo.xml"]
    if(opcion=="Citas"):return ["Instalador de servicio","Creador de site","Creador de aplicacion","Modificador de puerto","NME Citas","Configurador de citas"]
    if(opcion=="Encuestas"):return ["Instalador de servicio","Creador de site","Creador de aplicacion","Modificador de puerto","Configurador de Encuesta"]
    if(opcion=="Reportes"):return ["Basico","e-Flow","Citas","Encuesta","Virtual Queue"]
    if(opcion=="Automatizador"):return ["Basico"]
    if(opcion=="Client"):return ["SSPrinter","SSVoice","Internet Option"]
    