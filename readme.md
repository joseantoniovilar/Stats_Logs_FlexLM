


## Prerequisitos

* pyhton 3.9.16

## Proyecto organización
```
-Stats_Logs_FlexLM
    |   LICENSE
    |   readme.md			    <- Fichero que describe el proyecto.
    |   requirements.txt	    <- El fichero de requerimientos
    |
    +---csv			    	    <- fichero csv generado despeus de leer los logs de flexlm con flexlm_log.py
    |       autodesk.csv
    |       flexlm_log.csv
    |
    +---data_raw			    <- El fichero logs que crea FlexLM
    |       autodesk.log
    |       maple.log
    |       matlab.log
    |
    +---notebook			    <- Estudio exploratorio de los logs depues de tratados los logs
    |       flex_log_upm.ipynb
    |
    \---python
            flexlm_log.py	    <- Permite leer la informacion relevante de los logs de felxlm. Retorna un dataframe.
```

## Uso

1. Para recrear el poroyecto se puede utilizar  pip install -r requirements.txt

2. Con la funcion `flexlm_log_leer` del fichero `flexlm_log.py`  se leer el log que genera el software flexlm estrayendo  informacion relevante: Fecha, licencia concedidad, licencuas retornadas, modulos utilizados, equipos que se conectan en un dataframe.


