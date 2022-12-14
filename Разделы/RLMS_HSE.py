#Задействованные модули
import pandas as pd
import os
import numpy as np
# import matplotlib.pyplot as plt
# import statsmodels.formula.api as smf

#==========================================================================================
waves_dict={1994:[5,'A'],
           1995:[6,'B'],
           1996:[7,'C'],
           1998:[8,'D'],
           2000:[9,'E'],
           2001:[10,'F'],
           2002:[11,'G'],
           2003:[12,'H'],
           2004:[13,'I'],
           2005:[14,'J'],
           2006:[15,'K'],
           2007:[16,'L'],
           2008:[17,'M'],
           2009:[18,'N'],
           2010:[19,'O'],
           2011:[20,'P'],
           2012:[21,'Q'],
           2013:[22,'R'],
           2014:[23,'S'],
           2015:[24,'T'],
           2016:[25,'U'],
           2017:[26,'V'],
           2018:[27,'W'],
           2019:[28,'X'],
           2020:[29,'Y'],
           2021:[30,'Z'] 
           }

#==========================================================================================
def download_wave_ind(year,path=r'C:\Users\user\Desktop\Saved\Репрезентативная выборка 06.09.2022'):
    """
    Загрузка выбранной волны инидвидуальных данных из выбранной директории на диске.
    
    Параметры
    ---------
    year : integer
        Год волны исследования.
    path : string
        Директория волн исследования.
    """
    if (year<1994) or (year==1997) or (year==1999):
        print('Волны {0} года не существует.'.format(year))
    else:
        filename=os.listdir(r'{0}\{1}-я волна\ИНДИВИДЫ'.format(path,waves_dict[year][0]))[0]
        return pd.read_spss(r'{0}\{1}-я волна\ИНДИВИДЫ\{2}'.format(path,waves_dict[year][0],filename))
    
#==========================================================================================
 # Загрузка в словарь нескольких волн исследования
def download_period_ind(period,path):
    """
    Загрузка списка с выбранными волнами данных индивидов из выбранной директории на диске.
    
    Параметры
    ---------
    period : list
        Список волн. 
    path : string
        Директория волн исследования.
    """
    dict_ind_period={}
    for i in period:
        if (i<1994) or (i==1997) or (i==1999):
            print('Волны {0} года не существует.'.format(i))
            continue
        dict_ind_period[i]=download_wave_ind(i,path)
        print('Загружен ',i)
    return dict_ind_period

#==========================================================================================
# Загрузка данных для работы FAST-функций
def FAST_variable_ind(path):
    """
    Функция, загружающая в среду словарь всех волн исследования индивидов, и сохраняющая его как глобальную переменную.
    
    Параметры
    ---------
    path : string
        Директория волн исследования.
    
    Notes
    -----
    #Написать про FAST-функции
    """
    global FAST_INDS_DFS
    FAST_INDS_DFS=download_period_ind(list(range(1993,2022)),path=path)
#==========================================================================================
















#==========================================================================================
#==Аналогично для ДХ=======================================================================
#=Загрузка фрейма данных волны выбранного года из папки
def download_wave_hh(year,path=r'C:\Users\user\Desktop\Saved\Репрезентативная выборка 06.09.2022'):
    """
    Загрузка выбранной волны (года) данных домашних хозяйств из выбранной директории на диске.
    
    Параметры
    ---------
    year : integer
        Год волны исследования.
    path : string
        Директория волн исследования.
    
    Notes
    -----
    #Написать про FAST-функции
    """
    if (year<1994) or (year==1997) or (year==1999):
        print('Волны {0} года не существует.'.format(year))
    else:
        filename=os.listdir(r'{0}\{1}-я волна\ДОМОХОЗЯЙСТВА'.format(path,waves_dict[year][0]))[0]
        return pd.read_spss(r'{0}\{1}-я волна\ДОМОХОЗЯЙСТВА\{2}'.format(path,waves_dict[year][0],filename))
#==========================================================================================
# Загрузка в словарь нескольких волн исследования
def download_period_hh(period,path):
    """
    Загрузка списка с выбранными волнами данных домашних хозяйств из выбранной директории на диске.
    
    Параметры
    ---------
    period : list
        Список волн. 
    path : string
        Директория волн исследования.
    """
    dict_hh_period={}
    for i in period:
        if (i<1994) or (i==1997) or (i==1999):
            print('Волны {0} года не существует.'.format(i))
            continue
        dict_hh_period[i]=download_wave_hh(i,path)
        print('Загружен ',i)
    return dict_hh_period
#==========================================================================================
def FAST_variable_hh(path):
    """
    Функция, загружающая в среду словарь всех волн исследования домашних хозяйств, и сохраняющий как глобальную переменную.
    
    Параметры
    ---------
    path : string
        Директория волн исследования.
    
    Notes
    -----
    #Написать про FAST-функции
    """
    global FAST_HH_DFS
    FAST_HH_DFS=download_period_hh(list(range(1993,2022)),path=path)
#==========================================================================================   

    
      
    
    
    
    
    
    
    
    
    
    
    
# Далее реализовано лишь для индивидов и без FAST-префикса
#==========================================================================================
def good_namer(year, var='ind'):
    # Она должна быть FAST
    # Должно быть уточнение, что это только для индивидов
    """
    Возвращает фрейм данных, с переименованными атрибутами (убран префикс волны).
    
    Параметры
    ---------
    year : ineger
        Год волны исследования.
    var: string
        Если значение 'ind' ...
        Если значение 'hh' ...
    
    Notes
    -----
    # Написать про FAST-функции
    """
    if var=='ind':
        save=FAST_INDS_DFS[year].copy(deep=1)
    if var=='hh':
        save=FAST_HH_DFS[year].copy(deep=1)
        
    for i in save.columns:
        bad=waves_dict[year][1].lower()
        if 'id' in i:
            pass
        elif str(bad+'_') in i:
            save=save.rename(columns={i: i[2:]})
        elif bad==i[0]:
            save=save.rename(columns={i: i[1:]})
    return save

#==========================================================================================
def namer_period(period, var='ind'):
    """
    Возвращает словарь фреймов данных, с переименованными атрибутами (убран префикс волны).
    
    Параметры
    ---------
    period : list
        Список волн.
    
    Notes
    -----
    # Написать про FAST-функции
    """
    dict_ind_period={}
    for i in period:
        if (i<1994) or (i==1997) or (i==1999):
            print('Волны {0} года не существует.'.format(i))
            continue
        dict_ind_period[i]=good_namer(i,var)
        print('Исправлен ',i)
    return dict_ind_period
#==========================================================================================













#==========================================================================================
def corrector(year, var='ind'):
    """
    Возвращает словарь фреймов данных, с переименованными атрибутами (убран префикс волны).
    
    Параметры
    ---------
    period : list
        Список волн.
    
    Notes
    -----
    # Написать про FAST-функции
    """
    save=good_namer(year,var)
    if var=='ind':
        save.loc[:,'marst']=save.loc[:,'marst'].cat.rename_categories({'Bдовец (вдова)':'Вдовец (вдова)'})
    if var=='hh':
        pass
    return save
#==========================================================================================
def corrector_period(period,var='ind'):
    """
    Возвращает словарь фреймов данных, с переименованными атрибутами (убран префикс волны).
    
    Параметры
    ---------
    period : list
        Список волн.
    
    Notes
    -----
    # Написать про FAST-функции
    """
    dict_ind_period={}
    for i in period:
        if (i<1994) or (i==1997) or (i==1999):
            print('Волны {0} года не существует.'.format(i))
            continue
        dict_ind_period[i]=corrector(i,var)
        print('Исправлен ',i)
    return dict_ind_period
#==========================================================================================
def FAST_corrector_ind():
    """
    Возвращает словарь фреймов данных, с переименованными атрибутами (убран префикс волны).
    
    Параметры
    ---------
    period : list
        Список волн.
    
    Notes
    -----
    # Написать про FAST-функции
    """
    global FAST_CORRECTED_INDS_DFS
    FAST_CORRECTED_INDS_DFS=corrector_period(waves_dict.keys(),var='ind')
#==========================================================================================
def FAST_corrector_hh():
    """
    Возвращает словарь фреймов данных, с переименованными атрибутами (убран префикс волны).
    
    Параметры
    ---------
    period : list
        Список волн.
    
    Notes
    -----
    # Написать про FAST-функции
    """
    global FAST_CORRECTED_HH_DFS
    FAST_CORRECTED_HH_DFS=corrector_period(waves_dict.keys(),var='hh')














#==========================================================================================
def wave_scanner(codes,reverse=False):
    """
    Возвращает словарь волн исследования, в которых есть данные атрибуты.
    
    Параметры
    ---------
    codes : list, dictionary
        Список стандартизированных (без префиксов) атрибутов.
        Может получить словарь с атрибутами, то в таком случае выдает итоговый словарь в ключами данного словаря атрибутов. 
    reverse : bool, optional
        Если False, то возвращает словарь, где ключи - годы волн, а значения - это найденные атрибуты.
        Если True, то возвращает словарь, где ключи - выбранные коды атрибутов, а значения - годы, в котором есть эти артибуты.
        
    Notes
    -----

    """
    # Не написано reverse
    year_book={}
    nnn=FAST_CORRECTED_INDS_DFS
    if reverse:
        pass
    
    if reverse==False and type(codes)==list:
        for j in list(waves_dict.keys()):
            year_book[j]=list()
            
            for i in nnn[j].columns:
                for s in codes:
                    if s in i.lower():
                        year_book[j].append(s)
    
    if reverse==False and type(codes)==dict:
        reverse_dict={l[i]:k for k, l in codes.items() for i in range(len(l))}
        
    # Написать позже вариант для словаря
    
    new_dict = {a:list(set(b)) for a, b in year_book.items()}
    return new_dict
#==========================================================================================

#==========================================================================================

#==========================================================================================

#==========================================================================================
