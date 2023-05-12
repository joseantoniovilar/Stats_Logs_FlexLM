__author__ = "Jose Antonio Vilar"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Jose Antonio Vilar"
__email__ = "joseantonio.vilar@upm.es"
__status__ = "Production"

#Código para tratar el fichero log del software FlexLM.
#Extraemos la informacion (fecha, hora, servidor flexlm, producto, accion, complemento, usuario, host) y retorna un dataframe

def flexlm_log_leer(fichero, producto): 
    #Argumento producto admite los siguientes productos: autodesk, maple, matlab
    #Argumento fichero es la ruta del fichero flexlm.log que se quiere leer
    import pandas as pd
    from datetime import datetime
    import re

    
    datos=[]
    df_datos = pd.DataFrame()


    #Arranque o reinicio del servidor
    #linea ejemplo: 7:40:19 (lmgrd) FlexNet Licensing (v11.16.2.1 build 245043 x64_n6) started on flexlm01 (IBM PC) (4/6/2022)
    lmgrd_on = re.compile('(?P<hora>[ ]*\d{1,2}:\d{1,2}:\d{1,2}) \(lmgrd\) .* (?P<server>flexlm\w+) .* \((?P<fecha>\d+/\d+/\d+)\)')
    
    #Marcas en los logs
    #Ejemplo: 3:40:38 (lmgrd) TIMESTAMP 4/8/2022
    timestamp = re.compile(r'(?P<hora>[ ]*\d{1,2}:\d{1,2}:\d{1,2}) \(\w+\) TIMESTAMP (?P<fecha>\d+/\d+/\d+)')

    #adskflex
    #Ejemplo: 14:02:17 (MLM) IN: "MATLAB_5G_Toolbox" u697815@login1.hpc.lan 
    #flexlm_patron = re.compile('[ ]*(?P<hora>\d{1,2}:\d{1,2}:\d{2}) \(adskflex\) (?P<accion>\w+): \"(?P<complemento>\S+)\" (?P<usuario>\w+)@(?P<host>\S+)\s+\(*(?P<num_licencias>[0-9]*)\)*')
    
    if producto == "autodesk":
         #adskflex
        #Ejemplo: 14:02:17 (MLM) IN: "MATLAB_5G_Toolbox" u697815@login1.hpc.lan 
        #flexlm_patron = re.compile('[ ]*(?P<hora>\d{1,2}:\d{1,2}:\d{2}) \(adskflex\) (?P<accion>\w+): \"(?P<complemento>\S+)\" (?P<usuario>\w+)@(?P<host>\S+)\s+\(*(?P<num_licencias>[0-9]*)\)*')
        fabricante = "autodesk"
        flexlm_patron = re.compile('[ ]*(?P<hora>\d{1,2}:\d{1,2}:\d{2}) \(adskflex\) (?P<accion>\w+): \"(?P<complemento>\S+)\" (?P<usuario>\w+)@(?P<host>\S+)\s+\(*(?P<num_licencias>[0-9]*)\)*')
    elif producto  == "maple":
        fabricante = "maple"
        flexlm_patron = re.compile('[ ]*(?P<hora>\d{1,2}:\d{1,2}:\d{2}) \(maplelmg\) (?P<accion>\w+): \"(?P<complemento>\S+)\" (?P<usuario>\w+)@(?P<host>\S+)\s+\(*(?P<num_licencias>[0-9]*)\)*')
    elif producto  == "matlab":
        fabricante = "matlab"
        flexlm_patron = re.compile('[ ]*(?P<hora>\d{1,2}:\d{1,2}:\d{2}) \(MLM\) (?P<accion>\w+): \"(?P<complemento>\S+)\" (?P<usuario>\w+)@(?P<host>\S+)\s+\(*(?P<num_licencias>[0-9]*)\)*')
    elif producto  == "arcgis":
        fabricante = "arcgis"
        flexlm_patron = re.compile('[ ]*(?P<hora>\d{1,2}:\d{1,2}:\d{2}) \(ARCGIS\) (?P<accion>\w+): \"(?P<complemento>\S+)\" (?P<usuario>\w+)@(?P<host>\S+)\s+\(*(?P<num_licencias>[0-9]*)\)*')
    else:
        fabricante = ''
        flexlm_patron = ''
        

    with open(fichero) as f:
        for linea in f:
            linea.strip()
            #Fecha y hora de  arranque del servidor
            if lmgrd_on.match(linea):
                patron = lmgrd_on.match(linea)
                hora = patron.group('hora')
                fecha = patron.group('fecha')
                m,d,a = map(int,fecha.split("/"))
                fecha = datetime(a,m,d).strftime('%d/%m/%Y')
                #print("lmgrd: %s %s\n" % (fecha, hora))
                #Servidor del que se lee el log
                server = patron.group('server')
            
            
            #Marcas de tiempo en el Logs 
            #Ejemplo: 3:40:38 (lmgrd) TIMESTAMP 4/8/2022
            if timestamp.match(linea):
                patron = timestamp.match(linea)
                hora = patron.group('hora')
                fecha = patron.group('fecha')
                m,d,a = map(int,fecha.split("/"))
                fecha = datetime(a,m,d).strftime('%d/%m/%Y')
                #print("TIMESTAMP: %s %s\n" % (fecha, hora))
            
            #Los datos para para estadisticas: hora, producto, acción, complmento, usuario, host
            #Ejemplo: 14:02:17 (MLM) IN: "MATLAB_5G_Toolbox" u697815@login1.hpc.lan  
            if flexlm_patron.match(linea):
                patron = flexlm_patron.match(linea)
                hora = patron.group('hora')
                #Asigna la varible producto del argumento
                producto = fabricante
                accion = patron.group('accion')
                complemento = patron.group('complemento')
                usuario = patron.group('usuario')
                host = patron.group('host')
                #print("Datos: {} {} {} {} {} {} {}".format(fecha, hora, producto, accion, complemento, usuario, host))
                datos.append([fecha, hora, server, producto, accion, complemento, usuario, host]) 
                #datos.append([fecha, hora, producto, accion, complemento, usuario, host])
                #print(datos)

    #Creamos el dataframe
    pddatos = pd.DataFrame(datos, columns=['Fecha', 'Hora', 'Server', 'Producto', 'Accion', 'Modulo', 'Usuario', 'Host'])
    #pddatos = pd.DataFrame(datos, columns=['Fecha', 'Hora', 'Producto', 'Accion', 'Modulo', 'Usuario', 'Host'])
    f.close()
    return pddatos