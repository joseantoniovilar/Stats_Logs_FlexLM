


## Prerequisitos

* pyhton 3.9.16

## Proyecto organización
```
-Stats_Logs_FlexLM
    |   LICENSE
    |   readme.md			<- Fichero que describe el proyecto.
    |   requirements.txt	<- El fichero de requerimientos
    |
    +---csv				<- fichero csv depuesto de tratar los loogs con flexlm_log.py
    |       autodesk.csv
    |       flexlm_log.csv
    |
    +---data_raw			<- El fichero logs que crea FlexLM
    |       autodesk.log
    |       maple.log
    |       matlab.log
    |
    +---notebook			<- Estudio exploratorio de los logs depues de leer los logs
    |       flex_log_upm.ipynb
    |
    \---python
        |   flexlm_log.py	<- Permite leer y tratar los logs. Retorna un dataframe.
```

## Uso

1. Para recrear el poroyecto se puede utilizar  pip install -r requirements.txt

2. Con la funcion `flexlm_log_leer` del fichero `flexlm_log.py`  se trata de leer los log que genera el software felxlm estrayendo en un dataframe la informacion relevante: Fecha, licencia concedidad, licencuas retornadas, modulos utilizados, equipos que se conectan.


