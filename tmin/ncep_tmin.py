import xarray as xr
import pandas as pd
import glob
import os
from pathlib import Path
from colorama import Fore

# Define o caminho do diretório que você deseja criar
diretorio = Path("files")

# Cria o diretório, incluindo diretórios pai, se necessário
diretorio.mkdir(parents=True, exist_ok=True)

# Mude o diretório de trabalho para a pasta desejada
os.chdir("files")

# Verifique se a mudança foi bem-sucedida
print("Diretório de trabalho atual:", os.getcwd())

# Agora você pode executar operações de arquivo na pasta desejada
# Por exemplo, listar arquivos na pasta
for arquivo in os.listdir():
    print({Fore.LIGHTGREEN} arquivo {Fore.RESET})

date_ranges = [
    ("1982-06-01", "1983-08-01"),
    ("1986-11-01", "1988-04-01"),
    ("1991-07-01", "1992-08-01"),
    ("1994-11-01", "1995-05-01"),
    ("1997-07-01", "1998-07-01"),
    ("2002-08-01", "2003-04-01"),
    ("2004-09-01", "2005-04-01"),
    ("2006-11-01", "2007-03-01"),
    ("2009-08-01", "2010-05-01"),
    ("2014-12-01", "2016-04-01"),
    ("2018-09-01", "2019-06-01"),
    ("2023-07-01", "2024-06-01")
]

for (start_date, end_date) in date_ranges:
    # Carregar o arquivo netCDF
    nc_ndvi = xr.open_dataset('http://apdrc.soest.hawaii.edu:80/dods/public_data/Reanalysis_Data/NCEP/NCEP2/monthly/gaussian_grid/tmin2m')
    var1 = nc_ndvi['tmin']
    data = var1.sel(lat=slice(-60, 15), lon=slice(270, 330), time=slice(start_date, end_date)) 
    print(f"{Fore.LIGHTGREEN} data {Fore.RESET})
    data.to_netcdf(f"{start_date}.nc", mode='w')
