# Exportar transacciones de WalletApp by BudgetBakers
[![en](https://img.shields.io/badge/language-en-blue.svg)](README.md)

Debido a que **increíblemente** la app WalletApp de BudgetBakers no dispone de la función para exportar los registros que tenemos en la aplicación, este script es un *workaround* para poder exportar a `.csv` de la mejor forma posible a partir del `.htnl` de la web.

## Requisitos

El script se ha desarrollado y probado en la versión de **Python 3.12**. Para instalar las librerías necesarias ejecuta el comando `pip install -r requirements.txt`.

## Uso

1. Accede a tu cuenta desde la [versión web](https://web.budgetbakers.com/) y ve al apartado "Registros".

2. Selecciona el periodo de los registros que quieres exportar. Después, haz scroll hasta abajo del todo para cargar el `.html` de todos los registros del periodo seleccionado. Si son muchos, se recomienda hacerlo, por ejemplo, año a año. De hecho, también es recomendable para hacer exportaciones periódicas y no exportar todo cada vez.

3. Guarda la página con un nombre como `registros` en el directorio donde tengas este repositorio. Se te debe guardar el `.html` de la página y otra carpeta así:

```
├── README.md
├── registros_files
├── registros.html
├── requirements.txt
├── script.py
└── venv
```

4. Asegúrate que el nombre usado coincide con la variable correspondiente en el script (`html_path = "registros.html"`) y ejecuta el script `python3 script.py`.

5. Las transacciones se exportarán a un dataset `transacciones_exportadas.csv` con las columnas:

    - Fecha
    - Cantidad
    - Descripción
    - Categoría
    - Pagador/Cobrador
    - Etiquetas
    - Cuenta

## Limitaciones

El script extrae todo lo que puede del `.html`, pero éste no contiene toda la información de los registros. No podemos exportar:

- La hora de los registros
- La descripción completa (si contiene más de 40 caracteres)
- Forma de pago (efectivo, tarjeta de débito...)
- Tipo de pago (ingreso, transferencia...) aunque según si la cantidad es positiva o negativa, se puede deducir.
- Estado del pago
- Lugar