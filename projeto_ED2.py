#!/usr/bin/env python
# coding: utf-8

import csv

with open('laptops.csv') as f:
    reader = csv.reader(f)
    rows = list(reader)
    header = rows[0]
    rows = rows[1:]
    
print(header)
for i in range(5):
    print(rows[i])



def row_price(row):
    return row[-1]

class Inventory():                    
    
    def __init__(self, csv_filename):
        with open(csv_filename) as f: 
            reader = csv.reader(f)
            rows = list(reader)
        self.header = rows[0]        
        self.rows = rows[1:]
        for row in self.rows:              
            row[-1] = int(row[-1])
        self.id_to_row = {}                        
        for row in self.rows:                       
            self.id_to_row[row[0]] = row
        self.prices = set()                          
        for row in self.rows:                        
            self.prices.add(row[-1])
        self.rows_by_price = sorted(self.rows, key=row_price) 
    
    def get_laptop_from_id(self, laptop_id):
        for row in self.rows:                 
            if row[0] == laptop_id:
                return row
        return None   
    
    def get_laptop_from_id_fast(self, laptop_id):  
        if laptop_id in self.id_to_row:           
            return self.id_to_row[laptop_id]
        return None

    def check_promotion_dollars(self, dollars):    
        for row in self.rows:                   
            if row[-1] == dollars:
                return True
        for row1 in self.rows:                  
            for row2 in self.rows:
                if row1[-1] + row2[-1] == dollars:
                    return True
        return False                        
    
    def check_promotion_dollars_fast(self, dollars):
        if dollars in self.prices:                   
            return True
        for price in self.prices:                    
            if dollars - price in self.prices:
                return True
        return False                                
    
    def find_laptop_with_price(self, target_price):
        range_start = 0                                   
        range_end = len(self.rows_by_price) - 1                       
        while range_start < range_end:
            range_middle = (range_end + range_start) // 2  
            value = self.rows_by_price[range_middle][-1]
            if value == target_price:                            
                return range_middle                        
            elif value < target_price:                           
                range_start = range_middle + 1             
            else:                                          
                range_end = range_middle - 1 
        if self.rows_by_price[range_start][-1] != target_price:                  
            return -1                                      
        return range_start
    
    def find_first_laptop_more_expensive(self, target_price): 
        range_start = 0                                   
        range_end = len(self.rows_by_price) - 1                   
        while range_start < range_end:
            range_middle = (range_end + range_start) // 2  
            price = self.rows_by_price[range_middle][-1]
            if price > target_price:
                range_end = range_middle
            else:
                range_start = range_middle + 1
        if self.rows_by_price[range_start][-1] <= target_price:                  
            return -1                                   
        return range_start
    
    def find_laptops_in_price_range(self, min_price, max_price):
        laptops_in_range = []        
        for row in self.rows:
            # Obtém o preço do laptop atual a partir da última coluna (índice -1).
            price = row[-1]            
            # Verifica se o preço do laptop está dentro do intervalo especificado.
            if min_price <= price <= max_price:
                # Se o preço estiver dentro do intervalo, adiciona o laptop à lista.
                laptops_in_range.append(row)        
        return laptops_in_range

    
    def find_cheapest_laptop_with_specifications(self, ram, storage):
        filtered_laptops = []
        for row in self.rows:
            row_ram = row[8]  # Assume que a coluna de RAM é a nona (índice 8).
            row_storage = row[10]  # Assume que a coluna de armazenamento é a décima primeira (índice 10).
            if row_ram == ram and row_storage == storage:
                filtered_laptops.append(row)
        
        if not filtered_laptops:
            return None
        
        # Encontre o laptop mais barato entre os que atendem aos requisitos.
        cheapest_laptop = min(filtered_laptops, key=lambda x: x[-1])
        return cheapest_laptop

inventory = Inventory('laptops.csv')                              
print(inventory.find_first_laptop_more_expensive(1000))  
print(inventory.find_first_laptop_more_expensive(10000)) 
print(inventory.find_laptops_in_price_range(1000, 1010))
print(inventory.find_cheapest_laptop_with_specifications('8GB', '256GB'))






