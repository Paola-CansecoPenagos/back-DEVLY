from reportlab.pdfgen import canvas
import matplotlib.pyplot as plt
import os
from reportlab.lib.pagesizes import letter
import  tempfile
from flask import current_app
def generar_graficaHumedad(arr_sorted):
    # Crear la gráfica utilizando Matplotlib
    x_labels = range(0, len(arr_sorted), 5)  # Etiquetas del eje x
    plt.plot(arr_sorted)
    plt.xlabel('Tiempo')
    plt.ylabel('Humedad')
    plt.title('Gráfica de Humedad')
    plt.xticks(x_labels)  # Establecer las etiquetas del eje x
    plt.grid(True)

    temp_filename = tempfile.NamedTemporaryFile(suffix='.png', delete=False).name
    plt.savefig(temp_filename)
    plt.close()

    return temp_filename

def generar_graficaTemperature(arr_sorted):
    # Crear la gráfica utilizando Matplotlib
    x_labels = range(0, len(arr_sorted), 5)  # Etiquetas del eje x
    plt.plot(arr_sorted)
    plt.xlabel('Tiempo')
    plt.ylabel('Temperatura ambiental')
    plt.title('Gráfica de Temperatura ambiental')
    plt.xticks(x_labels)  # Establecer las etiquetas del eje x
    plt.grid(True)

    temp_filename = tempfile.NamedTemporaryFile(suffix='.png', delete=False).name
    plt.savefig(temp_filename)
    plt.close()

    return temp_filename

def generar_graficaPressure(arr_sorted):
    # Crear la gráfica utilizando Matplotlib
    x_labels = range(0, len(arr_sorted), 5)  # Etiquetas del eje x
    plt.plot(arr_sorted)
    plt.xlabel('Tiempo')
    plt.ylabel('Temperatura de agua')
    plt.title('Gráfica de temperatura de agua')
    plt.xticks(x_labels)  # Establecer las etiquetas del eje x
    plt.grid(True)

    temp_filename = tempfile.NamedTemporaryFile(suffix='.png', delete=False).name
    plt.savefig(temp_filename)
    plt.close()

    return temp_filename

def generar_graficaCO2(arr_sorted):
    # Crear la gráfica utilizando Matplotlib
    x_labels = range(0, len(arr_sorted), 5)  # Etiquetas del eje x
    plt.plot(arr_sorted)
    plt.xlabel('Tiempo')
    plt.ylabel('Intensidad de luz')
    plt.title('Gráfica de intensidad de luz')
    plt.xticks(x_labels)  # Establecer las etiquetas del eje x
    plt.grid(True)

    temp_filename = tempfile.NamedTemporaryFile(suffix='.png', delete=False).name
    plt.savefig(temp_filename)
    plt.close()

    return temp_filename

def generar_graficaAltitude(arr_sorted):
    # Crear la gráfica utilizando Matplotlib
    x_labels = range(0, len(arr_sorted), 5)  # Etiquetas del eje x
    plt.plot(arr_sorted)
    plt.xlabel('Tiempo')
    plt.ylabel('pH')
    plt.title('Gráfica de pH')
    plt.xticks(x_labels)  # Establecer las etiquetas del eje x
    plt.grid(True)

    temp_filename = tempfile.NamedTemporaryFile(suffix='.png', delete=False).name
    plt.savefig(temp_filename)
    plt.close()

    return temp_filename

def generar_graficaConduct(arr_sorted):
    # Crear la gráfica utilizando Matplotlib
    x_labels = range(0, len(arr_sorted), 5)  # Etiquetas del eje x
    plt.plot(arr_sorted)
    plt.xlabel('Tiempo')
    plt.ylabel('Conductividad')
    plt.title('Gráfica de Conductividad')
    plt.xticks(x_labels)  # Establecer las etiquetas del eje x
    plt.grid(True)

    temp_filename = tempfile.NamedTemporaryFile(suffix='.png', delete=False).name
    plt.savefig(temp_filename)
    plt.close()

    return temp_filename

def generar_pdf(table_frecuency_campo2,table_frecuency_campo1,table_frecuency_campo3,
        table_frecuency_campo4,table_frecuency_campo5,arr_sorted_campo2, desviacion_media_campo2, varianza_campo2, media_campo2,
        desviacion_estandar_campo2,arr_sorted_campo1, arr_ordenate_campo2, arr_ordenate_campo1,
        desviacion_media_campo1, media_campo1, varianza_campo1, desviacion_estandar_campo1,pdf_filename,
        desviacion_media_campo3, media_campo3, varianza_campo3, desviacion_estandar_campo3, arr_ordenate_campo3,
        arr_sorted_campo3,desviacion_media_campo4, media_campo4, varianza_campo4, desviacion_estandar_campo4, arr_ordenate_campo4,
        arr_sorted_campo4,desviacion_media_campo5, media_campo5, varianza_campo5, desviacion_estandar_campo5,arr_ordenate_campo5,arr_sorted_campo5,moda_campo1,moda_campo2
                ,moda_campo3,moda_campo4,moda_campo5,desviacion_media_campo6, media_campo6, varianza_campo6, desviacion_estandar_campo6, arr_ordenate_campo6, table_frecuency_campo6,moda_campo6,arr_sorted_campo6):

    table_frecuency_campo1.to_string(index=False)
    table_frecuency_campo2.to_string(index=False)
    table_frecuency_campo3.to_string(index=False)
    table_frecuency_campo4.to_string(index=False)
    table_frecuency_campo5.to_string(index=False)
    table_frecuency_campo6.to_string(index=False)

    public_folder = current_app.static_folder
    # Generar la ruta completa del archivo PDF en la carpeta 'Public'
    pdf_filename = 'ReporteSensores.pdf'
    pdf_path = os.path.join(public_folder, pdf_filename)
    c = canvas.Canvas(pdf_path, pagesize=letter)
    c.setFont("Helvetica", 12)
    c.drawString(70, 700, "Datos de Humedad:")
    # Ajustar la posición de los datos de humedad en forma horizontal con salto de línea
    x_pos = 70
    y_pos = 680
    max_width = 550  # Ancho máximo disponible para los datos
    for dato in arr_sorted_campo2:
        text_width = c.stringWidth(str(dato), "Helvetica", 12)
        if x_pos + text_width > max_width:
            x_pos = 70  # Volver al inicio de la línea
            y_pos -= 20  # Saltar a la siguiente línea
        c.drawString(x_pos, y_pos, str(dato))
        x_pos += text_width + 20  # Dejar un espacio entre los datos
        # Espacio adicional antes de la desviación media
    x_pos = 70
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, 560, "Datos ordenados de Humedad:")
    for dato in arr_ordenate_campo2:
        text_width = c.stringWidth(str(dato), "Helvetica", 12)
        if x_pos + text_width > max_width:
            x_pos = 70  # Volver al inicio de la línea
            y_pos -= 20  # Saltar a la siguiente línea
        c.drawString(x_pos, y_pos, str(dato))
        x_pos += text_width + 20  # Dejar un espacio entre los datos

    # Ajustar la posición vertical después de mostrar los datos de humedad
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Desviación Media de Humedad:")
    c.drawString(70, y_pos - 20, str(desviacion_media_campo2))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Varianza de Humedad:")
    c.drawString(70, y_pos - 20, str(varianza_campo2))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Media de Humedad:")
    c.drawString(70, y_pos - 20, str(media_campo2))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Desviacion estandar humedad:")
    c.drawString(70, y_pos - 20, str(round(desviacion_estandar_campo2,2)))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Moda Humedad:")
    c.drawString(70, y_pos - 20, str(moda_campo2))
    c.showPage()
    temp_filename = generar_graficaHumedad(arr_sorted_campo2)
    c.drawImage(temp_filename, 80, 400, width=500, height=400)
    width, height = letter

    # Configurar la posición de la tabla en el PDF
    x_start = 50
    y_start = height - 450
    line_height = 20

    # Ajustar el espacio entre columnas
    x_offset = 80

    # Ajustar el tamaño de la letra para que quepa la tabla en una página
    font_size = 10

    # Agregar el título de la tabla
    c.setFont("Helvetica-Bold", 14)
    c.drawString(x_start, y_start, "Tabla de frecuencias")
    y_start -= line_height

    column_headers = table_frecuency_campo2.columns.tolist()
    c.setFont("Helvetica-Bold", font_size)
    x = x_start
    for header in column_headers:
        c.drawString(x, y_start, header)
        x += x_offset  # Ajustar el espacio entre columnas
    y_start -= line_height
    # Agregar los datos de la tabla
    c.setFont("Helvetica", font_size)
    for _, row in table_frecuency_campo2.iterrows():
        x = x_start
        for header in column_headers:
            value = str(row[header])
            if header == "Marca de clase":
                # Alinear a la izquierda y ajustar la longitud a 10 caracteres
                c.drawString(x, y_start, value.ljust(10))
            else:
                c.drawString(x, y_start, value)
            x += x_offset  # Ajustar el espacio entre columnas
        y_start -= line_height

    c.showPage()
    #Temperatura
    c.drawString(70, 700, "Datos de Temperatura:")
    # Ajustar la posición de los datos de humedad en forma horizontal con salto de línea
    x_pos = 70
    y_pos = 680
    max_width = 550  # Ancho máximo disponible para los datos
    for dato in arr_sorted_campo1:
        text_width = c.stringWidth(str(dato), "Helvetica", 12)
        if x_pos + text_width > max_width:
            x_pos = 70  # Volver al inicio de la línea
            y_pos -= 20  # Saltar a la siguiente línea
        c.drawString(x_pos, y_pos, str(dato))
        x_pos += text_width + 20  # Dejar un espacio entre los datos
    x_pos = 70
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, 550, "Datos ordenados de Temperatura:")
    for dato in arr_ordenate_campo1:
        text_width = c.stringWidth(str(dato), "Helvetica", 12)
        if x_pos + text_width > max_width:
            x_pos = 70  # Volver al inicio de la línea
            y_pos -= 20  # Saltar a la siguiente línea
        c.drawString(x_pos, y_pos, str(dato))
        x_pos += text_width + 20  # Dejar un espacio entre los datos
    # Ajustar la posición vertical después de mostrar los datos de humedad
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Desviación Media de Temperatura:")
    c.drawString(70, y_pos - 20, str(desviacion_media_campo1))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Varianza de Temperatura:")
    c.drawString(70, y_pos - 20, str(varianza_campo1))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Media de Temperatura:")
    c.drawString(70, y_pos - 20, str(media_campo1))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Desviacion estandar Temperatura:")
    c.drawString(70, y_pos - 20, str(round(desviacion_estandar_campo1, 2)))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Moda Temperatura:")
    c.drawString(70, y_pos - 20, str(moda_campo1))
    c.showPage()
    temp_filename = generar_graficaTemperature(arr_sorted_campo1)
    c.drawImage(temp_filename, 80, 400, width=500, height=400)
    os.remove(temp_filename)
    #Tabla
    width, height = letter

    # Configurar la posición de la tabla en el PDF
    x_start = 50
    y_start = height - 450
    line_height = 20

    # Ajustar el espacio entre columnas
    x_offset = 80

    # Ajustar el tamaño de la letra para que quepa la tabla en una página
    font_size = 10

    # Agregar el título de la tabla
    c.setFont("Helvetica-Bold", 14)
    c.drawString(x_start, y_start, "Tabla de frecuencias Temperatura")
    y_start -= line_height

    column_headers = table_frecuency_campo1.columns.tolist()
    c.setFont("Helvetica-Bold", font_size)
    x = x_start
    for header in column_headers:
        c.drawString(x, y_start, header)
        x += x_offset  # Ajustar el espacio entre columnas
    y_start -= line_height
    # Agregar los datos de la tabla
    c.setFont("Helvetica", font_size)
    for _, row in table_frecuency_campo1.iterrows():
        x = x_start
        for header in column_headers:
            value = str(row[header])
            if header == "Marca de clase":
                # Alinear a la izquierda y ajustar la longitud a 10 caracteres
                c.drawString(x, y_start, value.ljust(10))
            else:
                c.drawString(x, y_start, value)
            x += x_offset  # Ajustar el espacio entre columnas
        y_start -= line_height

    c.showPage()

    c.drawString(70, 700, "Datos de Temperatura del agua:")
    # Ajustar la posición de los datos de humedad en forma horizontal con salto de línea
    x_pos = 70
    y_pos = 680
    max_width = 550  # Ancho máximo disponible para los datos
    for dato in arr_sorted_campo3:
        text_width = c.stringWidth(str(dato), "Helvetica", 12)
        if x_pos + text_width > max_width:
            x_pos = 70  # Volver al inicio de la líneaq
            y_pos -= 20  # Saltar a la siguiente línea
        c.drawString(x_pos, y_pos, str(dato))
        x_pos += text_width + 20  # Dejar un espacio entre los datos
    x_pos = 70
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, 550, "Datos ordenados de Temperatura del agua:")
    for dato in arr_ordenate_campo3:
        text_width = c.stringWidth(str(dato), "Helvetica", 12)
        if x_pos + text_width > max_width:
            x_pos = 70  # Volver al inicio de la línea
            y_pos -= 20  # Saltar a la siguiente línea
        c.drawString(x_pos, y_pos, str(dato))
        x_pos += text_width + 20  # Dejar un espacio entre los datos
    # Ajustar la posición vertical después de mostrar los datos de humedad
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Desviación Media de Temperatura del agua:")
    c.drawString(70, y_pos - 20, str(desviacion_media_campo3))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Varianza de Temperatura del agua:")
    c.drawString(70, y_pos - 20, str(varianza_campo3))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Media de Temperatura del agua:")
    c.drawString(70, y_pos - 20, str(media_campo3))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Desviacion estandar Temperatura del agua:")
    c.drawString(70, y_pos - 20, str(round(desviacion_estandar_campo3, 2)))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Moda Temperatura del agua:")
    c.drawString(70, y_pos - 20, str(moda_campo3))
    c.showPage()
    temp_filename = generar_graficaPressure(arr_sorted_campo3)
    c.drawImage(temp_filename, 90, 400, width=400, height=300)
    os.remove(temp_filename)
    # Tabla
    width, height = letter

    # Configurar la posición de la tabla en el PDF
    x_start = 50
    y_start = height - 450
    line_height = 20

    # Ajustar el espacio entre columnas
    x_offset = 80

    # Ajustar el tamaño de la letra para que quepa la tabla en una página
    font_size = 10

    # Agregar el título de la tabla
    c.setFont("Helvetica-Bold", 14)
    c.drawString(x_start, y_start, "Tabla de frecuencias Temperatura del agua")
    y_start -= line_height

    column_headers = table_frecuency_campo3.columns.tolist()
    c.setFont("Helvetica-Bold", font_size)
    x = x_start
    for header in column_headers:
        c.drawString(x, y_start, header)
        x += x_offset  # Ajustar el espacio entre columnas
    y_start -= line_height
    # Agregar los datos de la tabla
    c.setFont("Helvetica", font_size)
    for _, row in table_frecuency_campo3.iterrows():
        x = x_start
        for header in column_headers:
            value = str(row[header])
            if header == "Marca de clase":
                # Alinear a la izquierda y ajustar la longitud a 10 caracteres
                c.drawString(x, y_start, value.ljust(10))
            else:
                c.drawString(x, y_start, value)
            x += x_offset  # Ajustar el espacio entre columnas
        y_start -= line_height

    c.showPage()

    # CO2
    c.drawString(70, 700, "Datos de Intensidad de luz:")
    # Ajustar la posición de los datos de humedad en forma horizontal con salto de línea
    x_pos = 70
    y_pos = 680
    max_width = 550  # Ancho máximo disponible para los datos
    for dato in arr_sorted_campo4:
        text_width = c.stringWidth(str(dato), "Helvetica", 12)
        if x_pos + text_width > max_width:
            x_pos = 70  # Volver al inicio de la línea
            y_pos -= 20  # Saltar a la siguiente línea
        c.drawString(x_pos, y_pos, str(dato))
        x_pos += text_width + 20  # Dejar un espacio entre los datos
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, 560, "Datos ordenados de Intensidad de luz:")
    for dato in arr_ordenate_campo4:
        text_width = c.stringWidth(str(dato), "Helvetica", 12)
        if x_pos + text_width > max_width:
            x_pos = 70  # Volver al inicio de la línea
            y_pos -= 20  # Saltar a la siguiente línea
        c.drawString(x_pos, y_pos, str(dato))
        x_pos += text_width + 20  # Dejar un espacio entre los datos
    # Ajustar la posición vertical después de mostrar los datos de humedad
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Desviación Media de Intensidad de luz:")
    c.drawString(70, y_pos - 20, str(desviacion_media_campo4))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Varianza de Intensidad de luz:")
    c.drawString(70, y_pos - 20, str(varianza_campo4))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Media de Intensidad de luz:")
    c.drawString(70, y_pos - 20, str(media_campo4))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Desviacion estandar Intensidad de luz:")
    c.drawString(70, y_pos - 20, str(round(desviacion_estandar_campo4, 2)))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Moda Intensidad de luz:")
    c.drawString(70, y_pos - 20, str(moda_campo4))
    c.showPage()
    temp_filename = generar_graficaCO2(arr_sorted_campo4)
    c.drawImage(temp_filename, 90, 400, width=400, height=300)
    os.remove(temp_filename)
    # Tabla
    width, height = letter

    # Configurar la posición de la tabla en el PDF
    x_start = 50
    y_start = height - 450
    line_height = 20

    # Ajustar el espacio entre columnas
    x_offset = 80

    # Ajustar el tamaño de la letra para que quepa la tabla en una página
    font_size = 10

    # Agregar el título de la tabla
    c.setFont("Helvetica-Bold", 14)
    c.drawString(x_start, y_start, "Tabla de frecuencias Intensidad de luz")
    y_start -= line_height

    column_headers = table_frecuency_campo4.columns.tolist()
    c.setFont("Helvetica-Bold", font_size)
    x = x_start
    for header in column_headers:
        c.drawString(x, y_start, header)
        x += x_offset  # Ajustar el espacio entre columnas
    y_start -= line_height
    # Agregar los datos de la tabla
    c.setFont("Helvetica", font_size)
    for _, row in table_frecuency_campo4.iterrows():
        x = x_start
        for header in column_headers:
            value = str(row[header])
            if header == "Marca de clase":
                # Alinear a la izquierda y ajustar la longitud a 10 caracteres
                c.drawString(x, y_start, value.ljust(10))
            else:
                c.drawString(x, y_start, value)
            x += x_offset  # Ajustar el espacio entre columnas
        y_start -= line_height

    c.showPage()
    #Altitude
    c.drawString(70, 700, "Datos de pH:")
    # Ajustar la posición de los datos de humedad en forma horizontal con salto de línea
    x_pos = 70
    y_pos = 680
    max_width = 550  # Ancho máximo disponible para los datos
    for dato in arr_sorted_campo5:
        text_width = c.stringWidth(str(dato), "Helvetica", 12)
        if x_pos + text_width > max_width:
            x_pos = 70  # Volver al inicio de la línea
            y_pos -= 20  # Saltar a la siguiente línea
        c.drawString(x_pos, y_pos, str(dato))
        x_pos += text_width + 20  # Dejar un espacio entre los datos
    y_pos -= 40  # Espacio adicional antes de la desviación media
    y_pos = 560  # Ajustar la posición vertical para comenzar la tabla de datos ordenados de Altitud
    max_width = 500
    line_height = 30  # Aumentar el espacio vertical entre líneas
    font_size = 12  # Aumentar el tamaño de la fuente

    c.setFont("Helvetica", font_size)  # Configurar el tamaño de la fuente
    arr_sorted_campo5.sort()
    c.drawString(70, 560, "Datos ordenados de pH:")
    for dato in arr_sorted_campo5:
        dato_redondeado = round(dato, 2)  # Redondear el dato a dos decimales
        text_width = c.stringWidth(str(dato_redondeado), "Helvetica", font_size)
        if x_pos + text_width > max_width:
            x_pos = 70  # Volver al inicio de la línea
            y_pos -= line_height  # Saltar a la siguiente línea con el nuevo espacio vertical
        c.drawString(x_pos, y_pos, str(dato_redondeado))
        x_pos += text_width + 10  # Reducir el espaciado horizontal entre datos
    # Ajustar la posición vertical después de mostrar los datos de humedad
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Desviación Media de pH:")
    c.drawString(70, y_pos - 20, str(desviacion_media_campo5))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Varianza de pH:")
    c.drawString(70, y_pos - 20, str(varianza_campo5))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Media de pH:")
    c.drawString(70, y_pos - 20, str(media_campo5))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Desviacion estandar pH:")
    c.drawString(70, y_pos - 20, str(round(desviacion_estandar_campo5, 2)))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Moda pH:")
    c.drawString(70, y_pos - 20, str(moda_campo5))
    c.showPage()
    temp_filename = generar_graficaAltitude(arr_sorted_campo5)
    c.drawImage(temp_filename, 90, 400, width=400, height=300)
    os.remove(temp_filename)
    # Tabla
    width, height = letter

    # Configurar la posición de la tabla en el PDF
    x_start = 50
    y_start = height - 450
    line_height = 20

    # Ajustar el espacio entre columnas
    x_offset = 80

    # Ajustar el tamaño de la letra para que quepa la tabla en una página
    font_size = 10

    # Agregar el título de la tabla
    c.setFont("Helvetica-Bold", 14)
    c.drawString(x_start, y_start, "Tabla de frecuencias pH")
    y_start -= line_height

    column_headers = table_frecuency_campo5.columns.tolist()
    c.setFont("Helvetica-Bold", font_size)
    x = x_start
    for header in column_headers:
        c.drawString(x, y_start, header)
        x += x_offset  # Ajustar el espacio entre columnas
    y_start -= line_height
    # Agregar los datos de la tabla
    c.setFont("Helvetica", font_size)
    for _, row in table_frecuency_campo5.iterrows():
        x = x_start
        for header in column_headers:
            value = str(row[header])
            if header == "Marca de clase":
                # Alinear a la izquierda y ajustar la longitud a 10 caracteres
                c.drawString(x, y_start, value.ljust(10))
            else:
                c.drawString(x, y_start, value)
            x += x_offset  # Ajustar el espacio entre columnas
        y_start -= line_height
    
    c.showPage()
    #Temperatura
    c.drawString(70, 700, "Datos de Conductividad del agua:")
    # Ajustar la posición de los datos de humedad en forma horizontal con salto de línea
    x_pos = 70
    y_pos = 680
    max_width = 550  # Ancho máximo disponible para los datos
    for dato in arr_sorted_campo6:
        text_width = c.stringWidth(str(dato), "Helvetica", 12)
        if x_pos + text_width > max_width:
            x_pos = 70  # Volver al inicio de la línea
            y_pos -= 20  # Saltar a la siguiente línea
        c.drawString(x_pos, y_pos, str(dato))
        x_pos += text_width + 20  # Dejar un espacio entre los datos
    x_pos = 70
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, 550, "Datos ordenados de Conductividad del agua:")
    for dato in arr_ordenate_campo6:
        text_width = c.stringWidth(str(dato), "Helvetica", 12)
        if x_pos + text_width > max_width:
            x_pos = 70  # Volver al inicio de la línea
            y_pos -= 20  # Saltar a la siguiente línea
        c.drawString(x_pos, y_pos, str(dato))
        x_pos += text_width + 20  # Dejar un espacio entre los datos
    # Ajustar la posición vertical después de mostrar los datos de humedad
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Desviación Media de Conductividad del agua:")
    c.drawString(70, y_pos - 20, str(desviacion_media_campo6))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Varianza de Conductividad del agua:")
    c.drawString(70, y_pos - 20, str(varianza_campo6))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Media de Conductividad del agua:")
    c.drawString(70, y_pos - 20, str(media_campo6))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Desviacion estandar Conductividad del agua:")
    c.drawString(70, y_pos - 20, str(round(desviacion_estandar_campo6, 2)))
    y_pos -= 40  # Espacio adicional antes de la desviación media
    c.drawString(70, y_pos, "Moda Conductividad del agua:")
    c.drawString(70, y_pos - 20, str(moda_campo6))
    c.showPage()
    temp_filename = generar_graficaConduct(arr_sorted_campo6)
    c.drawImage(temp_filename, 80, 400, width=500, height=400)
    os.remove(temp_filename)
    #Tabla
    width, height = letter

    # Configurar la posición de la tabla en el PDF
    x_start = 50
    y_start = height - 450
    line_height = 20

    # Ajustar el espacio entre columnas
    x_offset = 80

    # Ajustar el tamaño de la letra para que quepa la tabla en una página
    font_size = 10

    # Agregar el título de la tabla
    c.setFont("Helvetica-Bold", 14)
    c.drawString(x_start, y_start, "Tabla de frecuencias Conductividad del agua")
    y_start -= line_height

    column_headers = table_frecuency_campo6.columns.tolist()
    c.setFont("Helvetica-Bold", font_size)
    x = x_start
    for header in column_headers:
        c.drawString(x, y_start, header)
        x += x_offset  # Ajustar el espacio entre columnas
    y_start -= line_height
    # Agregar los datos de la tabla
    c.setFont("Helvetica", font_size)
    for _, row in table_frecuency_campo6.iterrows():
        x = x_start
        for header in column_headers:
            value = str(row[header])
            if header == "Marca de clase":
                # Alinear a la izquierda y ajustar la longitud a 10 caracteres
                c.drawString(x, y_start, value.ljust(10))
            else:
                c.drawString(x, y_start, value)
            x += x_offset  # Ajustar el espacio entre columnas
        y_start -= line_height

    c.save()

    return pdf_path